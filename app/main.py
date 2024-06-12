from fastapi import FastAPI
from fastapi_pagination import add_pagination

from memes.routers import (
    router as memes_router
)

app = FastAPI(
    title="Meme's API",
    root_path="/api"
)

app.include_router(memes_router)

add_pagination(app)
