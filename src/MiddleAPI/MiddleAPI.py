#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 2025-MiddleAPI
# @File : MiddleAPI.py
# @IDE : PyCharm
# @Author : DeckDes (deckdes@outlook.com)
# @Co-Author : Ashley Lee (nekokecore@emtips.net)
# @Date : 2025/2/4 13:37

# Copyright 2025 DeckDes (deckdes@outlook.com)
# Copyright 2025 Ashley Lee (nekokecore@emtips.net)

from fastapi import FastAPI, Response
from utils.gradioUtils import posttosovits
from utils.pydanticUtils import OpenWebUI, SetConfig
from utils.configUtils import setconfig, getconfig

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "MiddleAPI"}

@app.post("/audio/speech")
async def tts(openjson: OpenWebUI):
    """
    
    Args:
        openjson: Request body.

    Returns: Audio file.

    """
    with open(posttosovits(openjson.voice,openjson.input), "rb") as f:
        file_bytes = f.read()
    return Response(content=file_bytes, media_type="audio/wav")

@app.post("/app/setconfig")
async def sc(sc: SetConfig):
    setconfig(sc.section, sc.key, sc.value)
    return {"msg":"OK","code":0}

