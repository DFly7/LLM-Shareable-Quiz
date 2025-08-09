## FastAPI backend

### Prerequisites

- Python 3.12+

### Setup (first time)

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

If you don't have `requirements.txt` yet, install directly:

```bash
pip install "fastapi>=0.111,<1" "uvicorn[standard]>=0.30,<1"
pip freeze > requirements.txt
```

### Activate Venv

source backend/.venv/bin/activate

### Run the server (dev)

From the repository root or the `backend` directory:

```bash
# Using the venv directly (no need to activate)
../backend/.venv/bin/uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

# Or, if you activated the venv
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

- API root: `http://localhost:8000`
- OpenAPI docs (Swagger UI): `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- OpenAPI schema JSON: `http://localhost:8000/openapi.json`

### CORS configuration

If your frontend (e.g., Next.js) runs on a different origin (like `http://localhost:3000`), you need CORS enabled. This project enables CORS via middleware and reads allowed origins from the `ALLOWED_ORIGINS` environment variable (comma-separated).

Examples:

```bash
# Allow Next.js dev server
export ALLOWED_ORIGINS="http://localhost:3000"

# Allow multiple origins
export ALLOWED_ORIGINS="http://localhost:3000,https://your-prod-domain.com"

# Optional: use an .env file (loaded automatically)
echo 'ALLOWED_ORIGINS="http://localhost:3000"' > .env
```

Restart the server after changing env vars.

### Production notes

- Bind to an internal interface and use a reverse proxy (e.g., Nginx) for TLS.
- Set `ALLOWED_ORIGINS` to your real domains only.
- Run with workers, e.g.: `uvicorn backend.main:app --host 0.0.0.0 --port 8000 --workers 2`
