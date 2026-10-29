# Deploying AgroTrace AI on Vercel

This repository deploys as one Vercel project with two services:

- `frontend` is the public React/Vite interface at `/`.
- `app` is the FastAPI service, public only through `/api/*`.

The browser calls its own `/api` path, so no service binding is needed. Vercel bindings are only for server-to-server traffic, and this frontend runs in the browser.

## Project environment variables

Add these in the Vercel project settings for Preview and Production. Do not commit their values.

| Variable | Required | Purpose |
| --- | --- | --- |
| `CHAIN_RPC` | Yes | HTTPS/WSS RPC URL for the deployed blockchain; do not use `127.0.0.1`. |
| `CONTRACT_ADDRESS` | Yes | `AgroTrace` contract address on the same chain. |
| `IPFS_API` | Yes for evidence publishing | Hosted IPFS HTTP endpoint; do not use a local daemon URL. |
| `QPIAI_QCLOUD_API_KEY` | If QpiAI quantum runs are enabled | QpiAI QCloud credential. |
| `QPIAI_OPT_API_KEY` | If QpiAI optimization is enabled | QpiAI optimization credential. |
| `QPIAI_QCLOUD_URL` | Optional | Override for the QCloud API endpoint. |
| `QPIAI_OPT_URL` | Optional | Override for the optimization API endpoint. |
| `ALLOW_FALLBACK` | Optional | Set to `true` only when local fallback solvers are acceptable. |

## Local deployment check

Run `vercel dev -L` from the repository root to start both services together. The frontend is served at `/` and the API is at `/api/health`.

## Runtime persistence

Vercel functions have an ephemeral, writable `/tmp` directory. The API stores its SQLite index, runs, and local evidence cache there when deployed, which keeps the function writable but does **not** preserve state across cold starts. Connect a managed database and durable object store before treating production records as permanent.
