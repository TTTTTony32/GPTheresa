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
from fastapi.responses import HTMLResponse

from utils.GradioUtils import GradioClient
from utils.PydanticUtils import OpenWebUIObj, SetConfigObj, GetConfigObj
from utils.ConfigUtils import ConfigTools

app = FastAPI()

@app.get("/",response_class=HTMLResponse)
async def root(html = "index.html"):
    """
    
    Args:
        html: Page name.

    Returns: HTMLResponse

    """
    if html == "index.html":
        with open('www/index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    if html == "settings.html":
        with open('www/settings.html', 'r', encoding='utf-8') as f:
            html = f.read()
    return html

@app.post("/audio/speech")
async def tts(openjson: OpenWebUIObj):
    """
    
    Args:
        openjson: Request body.

    Returns: Audio file.

    """
    with open(GradioClient.inference(openjson.voice,openjson.input), "rb") as f:
        file_bytes = f.read()
    return Response(content=file_bytes, media_type="audio/wav")

@app.post("/app/setconfig")
async def sc(sc: SetConfigObj):
    """
    
    Args:
        sc: Request body.

    Returns: Json response.

    """
    cm = ConfigTools("config/config.yaml")
    config = cm.read_config()
    config[sc.section][sc.key] = sc.value
    cm.write_config(config)
    return {"msg":"OK","code":0}

@app.post("/app/getconfig")
async def gc(gc: GetConfigObj):
    """
    
    Args:
        gc: Request body.

    Returns: Json response.

    """
    cm = ConfigTools("config/config.yaml")
    config = cm.get_value(gc.section)[gc.key]
    if config is None:
        return {"msg":"FAILED","code":1}
    return {"msg":"OK","code":0,"section":gc.section,"key":gc.key,"value":config}
