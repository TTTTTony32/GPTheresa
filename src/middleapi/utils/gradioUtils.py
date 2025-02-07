#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 2025-MiddleAPI
# @File : gradioUtils.py
# @IDE : PyCharm
# @Author : DeckDes (deckdes@outlook.com)
# @Co-Author : Ashley Lee (nekokecore@emtips.net)
# @Date : 2025/2/4 13:37

# Copyright 2025 DeckDes (deckdes@outlook.com)
# Copyright 2025 Ashley Lee (nekokecore@emtips.net)

from gradio_client import Client, file
from utils.textUtils import cleantext
import os

def isdocker():
    return os.path.exists('/.dockerenv')

def posttosovits(voice, input):
    """
    
    Args:
        voice: Specify the language of the output speech.
        input: Specify the content of the text to be reasoned about.

    Returns: audio files.

    """
    if isdocker():
        client = Client("http://host.docker.internal:9872/")
    else:
        client = Client("http://localhost:9872/")

    result = client.predict(
        ref_wav_path=file('wavs/xiaote.wav'),
        prompt_text="我还记得这间会议室。这是专门为特蕾西娅空着的位置吗？不......我并不需要。",
        prompt_language=voice,
        text=cleantext(input),
        text_language=voice,
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

    return result