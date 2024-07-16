from fastapi import APIRouter
from text2image_interactor import generate_image

router = APIRouter()

@router.get('/image')
def image(query: str):
  return generate_image(query)
