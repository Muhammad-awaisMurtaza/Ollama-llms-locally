import base64
from io import BytesIO
from PIL import Image
from decouple import config
from langchain_community.llms.edenai import EdenAI

def generate_image(query: str):
  text2image = EdenAI(
    edenai_api_key = config('EDEN_AI_API_KEY'),
    feature="image",
    provider="openai",
    resolution="256x256"
  )
  image_string = text2image.invoke(query)
  print_image(image_string) 
  return "Done"

def print_image(base64_string):
  decded_string = base64.decode(base64_string)
  image_stream = BytesIO(decded_string) 
  img = Image.open(image_stream)
  img.show()
