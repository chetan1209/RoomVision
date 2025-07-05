from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from diffusers import StableDiffusionPipeline
import torch
import os
import uuid

app = FastAPI()

# Load your model with the Hugging Face token for private access
hf_token = os.environ.get("HF_TOKEN")
pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2",
    use_auth_token=hf_token,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

@app.post("/infer")
async def infer(prompt: str = Form(...)):
    image = pipe(prompt).images[0]
    output_filename = f"output_{uuid.uuid4().hex}.png"
    image.save(output_filename)
    return JSONResponse({"image_url": f"/file={output_filename}"})
