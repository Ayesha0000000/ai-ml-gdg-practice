from fastapi import FastAPI, Header, HTTPException
from git_day_practice.settings import get_settings

settings = get_settings()

app = FastAPI(title=settings.app_name)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/config")
def config():
    s = get_settings()
    return {
        "app_name": s.app_name,
        "environment": s.environment,
        "debug": s.debug,
        "port": s.port,
        "allowed_origins": s.allowed_origins,
    }


@app.get("/secure-data")
def secure(x_api_key: str = Header(None)):
    if x_api_key != settings.api_key:
        raise HTTPException(status_code=401, detail="Invalid key")
    return {"secret": "approved"}
