import chat_router
import text2image_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(chat_router.router)
app.include_router(text2image_router.router)
