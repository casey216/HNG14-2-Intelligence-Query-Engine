from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.settings import settings
from app.db.database import init_db
from app.models.profile import Profile


@asynccontextmanager
async def lifespan(app: FastAPI):
    if not settings.TESTING:
        init_db()

    yield


app = FastAPI(lifespan=lifespan)

reload = False
if settings.ENV == "development":
    reload = True

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app="app.server:app", reload=reload)