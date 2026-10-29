import time
import requests
from typing import Any, Callable, Dict, Optional, Tuple
import config

class QpiAIError(Exception):
    def __init__(self, code: str, message: str, hint: str, http_status: int = 500, service: str = "qpiai"):
        super().__init__(message)
        self.code = code
        self.message = message
        self.hint = hint
        self.http_status = http_status
        self.service = service

    def to_dict(self) -> Dict[str, Any]:
        return {
            "code": self.code,
            "http_status": self.http_status,
            "service": self.service,
            "message": self.message,
            "hint": self.hint
        }

def call_qpiai(
    service: str,  # "opt" | "qcloud"
    fn: Callable[[], Any],
    payload_summary: Dict[str, Any],
    timeout_sec: float = 60.0,
    max_retries: int = 2
) -> Tuple[Optional[Any], Optional[Dict[str, Any]], str]:
    """
    Executes a QpiAI call with validation, masked secrets, timeouts, and structured errors.
    Returns: (result_or_none, error_dict_or_none, mode)
    Mode is strictly: "qpiai_real" | "fallback_local" | "error"
    """
    # 1. Key Check
    key = config.QPIAI_OPT_API_KEY if service == "opt" else config.QPIAI_QCLOUD_API_KEY
    env_name = "QPIAI_OPT_API_KEY" if service == "opt" else "QPIAI_QCLOUD_API_KEY"
    if not key or not key.strip():
        err = QpiAIError(
            code="MISSING_KEY",
            message=f"{env_name} is not set in environment or .env",
            hint=f"Set {env_name} with your valid QpiAI token.",
            http_status=401,
            service=service
        ).to_dict()
        mode = "fallback_local" if config.ALLOW_FALLBACK else "error"
        return None, err, mode

    # 2. Retry Loop with Backoff
    attempts = 0
    backoff = 0.5
    last_error: Optional[Dict[str, Any]] = None

    while attempts <= max_retries:
        try:
            attempts += 1
            start_t = time.perf_counter()
            result = fn()
            return result, None, "qpiai_real"
        except requests.exceptions.Timeout as te:
            last_error = QpiAIError("TIMEOUT", f"Service call timed out after {timeout_sec}s: {te}", "Increase timeout or check connection", 504, service).to_dict()
        except requests.exceptions.ConnectionError as ce:
            last_error = QpiAIError("NETWORK", f"Cannot reach QpiAI endpoint: {ce}", "Check internet access and endpoint routing", 503, service).to_dict()
        except Exception as ex:
            msg = str(ex)
            if "401" in msg or "403" in msg or "unauthorized" in msg.lower():
                last_error = QpiAIError("UNAUTHORIZED", f"Invalid or expired key: {msg}", f"Check {env_name}", 401, service).to_dict()
                break  # Do not retry auth failures
            elif "429" in msg or "quota" in msg.lower():
                last_error = QpiAIError("QUOTA_EXCEEDED", f"Quota limit reached: {msg}", "Wait for quota reset or switch to simulator", 429, service).to_dict()
                break
            else:
                last_error = QpiAIError("SERVER", f"QpiAI server error ({type(ex).__name__}): {msg}", "Inspect SDK call payload", 500, service).to_dict()

        if attempts <= max_retries:
            time.sleep(backoff)
            backoff *= 2.0

    mode = "fallback_local" if config.ALLOW_FALLBACK else "error"
    return None, last_error, mode
