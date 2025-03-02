from fastapi import FastAPI, File
from starlette.responses import Response
import io
from PIL import Image
from .fastapi.segmentation import get_segmentator, get_segments
from .fastapi import caption as cp

tokenizer = cp.get_tokenizer()
cp_model = cp.get_model()

model = get_segmentator()

app = FastAPI(title="DeepLabV3 image segmentation",
              description='''Obtain semantic segmentation maps of the image in input via DeepLabV3 implemented in PyTorch.
                           Visit this URL at port 8501 for the streamlit interface.''',
              version="0.1.0",
              )


@app.post("/segmentation")
def get_segmentation_map(file: bytes = File(...)):
    '''Get segmentation maps from image file'''
    segmented_image = get_segments(model, file)
    bytes_io = io.BytesIO()
    segmented_image.save(bytes_io, format='PNG')
    return Response(bytes_io.getvalue(), media_type="image/png")

@app.post("/caption")
async def get_caption(file: bytes = File(...)):
      '''Get caption from image file'''
      print('process started')
      # print(file)
      image = Image.open(io.BytesIO(file)).convert("RGB").resize((224,224))
      image = cp.extract_features(image)
      print('feature')
      caption = cp.generate_desc(cp_model,tokenizer,image,34)
      print(caption)
      response = Response(caption, media_type='text/plain')
      return response

