import uvicorn
from src.config import settings


if __name__=='__main__':
    if (settings.debug):
        uvicorn.run("src:create_app", port=5000, reload=True)
    else:
        uvicorn.run("src:create_app", port=5000)