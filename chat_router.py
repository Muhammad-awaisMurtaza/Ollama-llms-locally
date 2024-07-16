import chat_interactor
from fastapi import APIRouter

router = APIRouter()

@router.get('/chat')
def chat(question: str):
  return chat_interactor.chat(question)
