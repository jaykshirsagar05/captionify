from fastapi import FastAPI, File
from starlette.responses import Response
import io
from PIL import Image
import caption as cp

tokenizer = cp.get_tokenizer()
cp_model = cp.get_model()

app = FastAPI(title="Image Captioning Project",
              description='''Obtain a brief caption from a image using "Show and tell architecture"''',
              version="0.1.0",
              )

@app.post("/caption")
async def get_caption(file: bytes = File(...)):
      '''Get caption from image file'''
      print('process started')
      # print(file)
      image = Image.open(io.BytesIO(file)).convert("RGB").resize((224,224))
      image = cp.extract_features(image)
      print('feature')
      caption = cp.generate_desc(cp_model,tokenizer,image,34)
      caption = caption[8:-6]
      print(caption)
      response = Response(caption, media_type='text/plain')
      print(response)
      return response

