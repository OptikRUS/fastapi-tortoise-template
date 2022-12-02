from config import site_config
from config.app import get_fastapi_app

app = get_fastapi_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("run:app", **site_config)
