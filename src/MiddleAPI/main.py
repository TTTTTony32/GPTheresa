import re
from gradio_client import Client, file
from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "MiddleAPI"}

GPT_SOVITS_API_URL = "http://localhost:9872/api/v1/audio/speech"

class Openjson(BaseModel):
    input:str
    voice:str

@app.post("/audio/speech")
async def tts(openjson: Openjson):

    def clean_text(input_text):
        return re.sub(r"\[.*?\]", "", input_text)
    
    # 转发请求到 GPT-SoVITS
    client = Client("http://localhost:9872/")
    result = client.predict(
        ref_wav_path=file('D:/AI/GPT-SoVITS/v2/GPT-SoVITS-v2-240821/GPT-SoVITS-v2-240821/wavs/xiaote.wav'),
        prompt_text="我还记得这间会议室。这是专门为特蕾西娅空着的位置吗？不......我并不需要。",
        prompt_language=openjson.voice,
        text=clean_text(openjson.input),
        text_language=openjson.voice,
        how_to_cut="凑四句一切",
        top_k=15,
        top_p=1,
        temperature=1,
        ref_free=False,
        speed=1,
        if_freeze=False,
        inp_refs=[],
        api_name="/get_tts_wav"
    )

    with open(result, "rb") as f:
        file_bytes = f.read()
    return Response(content=file_bytes, media_type="audio/wav")
