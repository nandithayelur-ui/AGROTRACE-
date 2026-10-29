import importlib
import importlib.metadata as metadata
import inspect
import pkgutil
import re
import sys
from pathlib import Path


def find_qpiai_distributions():
    print("=" * 80)
    print("1. INSTALLED DISTRIBUTIONS MATCHING 'qpiai' / 'qcloud' / 'opt'")
    print("=" * 80)
    matched_dists = []
    for dist in metadata.distributions():
        name = dist.metadata["Name"] or ""
        if any(k in name.lower() for k in ("qpiai", "qcloud", "qpi")):
            matched_dists.append(dist)
            print(f"- {name} == {dist.version}")
            top_level = dist.read_text("top_level.txt")
            if top_level:
                print(f"  top_level.txt: {top_level.strip().splitlines()}")
            files = dist.files or []
            py_files = [str(f) for f in files if str(f).endswith(".py") and not str(f).startswith("..")]
            print(f"  py files ({len(py_files)}): {py_files[:25]}")
    if not matched_dists:
        print("WARNING: No installed distributions matching 'qpiai' found in current Python environment!")
        print(f"Python executable: {sys.executable}")
    return matched_dists


def discover_root_modules(dists):
    roots = set()
    for dist in dists:
        top_level = dist.read_text("top_level.txt")
        if top_level:
            for line in top_level.strip().splitlines():
                if line.strip():
                    roots.add(line.strip())
        for f in dist.files or []:
            parts = Path(str(f)).parts
            if parts and not parts[0].startswith("..") and not parts[0].endswith(".dist-info"):
                if parts[0].endswith(".py"):
                    roots.add(parts[0][:-3])
                else:
                    roots.add(parts[0])
    for candidate in ("qpiai", "qpiai_opt", "qpiai_quantum", "qcloud", "qpi_opt", "qpi_quantum"):
        try:
            importlib.import_module(candidate)
            roots.add(candidate)
        except Exception:
            pass
    return sorted(roots)


def inspect_module_tree(root_name: str):
    print("\n" + "=" * 80)
    print(f"2. INTROSPECTING MODULE TREE: {root_name}")
    print("=" * 80)
    try:
        root_mod = importlib.import_module(root_name)
    except Exception as e:
        print(f"Failed to import {root_name}: {type(e).__name__}: {e}")
        return

    modules_to_visit = [root_name]
    if hasattr(root_mod, "__path__"):
        for _, modname, _ in pkgutil.walk_packages(root_mod.__path__, prefix=root_name + "."):
            modules_to_visit.append(modname)

    env_vars_found = set()

    for modname in modules_to_visit:
        print(f"\n--- Module: {modname} ---")
        try:
            mod = importlib.import_module(modname)
        except Exception as e:
            print(f"  [Import Error] {type(e).__name__}: {e}")
            continue

        doc = inspect.getdoc(mod)
        if doc:
            first_lines = " | ".join(doc.splitlines()[:3])
            print(f"  Doc: {first_lines}")

        try:
            src = inspect.getsource(mod)
            for match in re.findall(r"(?:getenv|environ\.get|environ\[)\(\s*['\"]([A-Za-z0-9_]+)['\"]", src):
                env_vars_found.add(match)
        except Exception:
            pass

        for attr_name in dir(mod):
            if attr_name.startswith("_"):
                continue
            try:
                obj = getattr(mod, attr_name)
            except Exception:
                continue

            obj_mod = getattr(obj, "__module__", None)
            if obj_mod and not obj_mod.startswith(root_name):
                continue

            if inspect.isclass(obj):
                try:
                    init_sig = str(inspect.signature(obj.__init__))
                except Exception:
                    init_sig = "(?)"
                print(f"  [Class] {attr_name}{init_sig}")
                for m_name, m_obj in inspect.getmembers(obj, predicate=lambda x: inspect.isfunction(x) or inspect.ismethod(x)):
                    if m_name.startswith("_") and m_name != "__init__":
                        continue
                    try:
                        msig = str(inspect.signature(m_obj))
                    except Exception:
                        msig = "(?)"
                    print(f"      .{m_name}{msig}")
            elif inspect.isfunction(obj):
                try:
                    fsig = str(inspect.signature(obj))
                except Exception:
                    fsig = "(?)"
                print(f"  [Func]  {attr_name}{fsig}")

    if env_vars_found:
        print(f"\n[Environment variables referenced inside {root_name}]: {sorted(env_vars_found)}")


def main():
    # Windows terminals commonly default to cp1252, while SDK docs and
    # annotations may include Unicode. Keep this diagnostic usable everywhere.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print(f"Python Version: {sys.version}")
    dists = find_qpiai_distributions()
    roots = discover_root_modules(dists)
    print(f"\nDiscovered Root Modules: {roots}")
    for r in roots:
        inspect_module_tree(r)
    print("\n" + "=" * 80)
    print("PROBE COMPLETE.")
    print("=" * 80)


if __name__ == "__main__":
    main()
