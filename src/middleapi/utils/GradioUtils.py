#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 2025-MiddleAPI
# @File : GradioUtils.py
# @IDE : PyCharm
# @Author : DeckDes (deckdes@outlook.com)
# @Co-Author : Ashley Lee (nekokecore@emtips.net)
# @Date : 2025/2/4 13:37

# Copyright 2025 DeckDes (deckdes@outlook.com)
# Copyright 2025 Ashley Lee (nekokecore@emtips.net)

from gradio_client import Client, file
from utils.ConfigUtils import ConfigTools
from utils.TextUtils import CleanText, OldAPI
import os

def isdocker():
    return os.path.exists('/.dockerenv')

class GradioClient:
    @staticmethod
    def inference(language,text):
        """

        Returns: audio files.

        """
        cm = ConfigTools("config/config.yaml")
        
        use_new_api=cm.get_value("global")["use_new_api"]

        reference_audio = cm.get_value("reference")["reference_audio"]
        reference_audio_text = cm.get_value("reference")["reference_audio_text"]
        reference_audio_language = OldAPI.old_api(use_new_api,cm.get_value("reference")["reference_audio_language"])
        no_reference_mode = cm.get_value("reference")["no_reference_mode"]
        inp_refs = cm.get_value("reference")["inp_refs"]

        inference_text = CleanText.text(text)
        inference_text_language = OldAPI.old_api(use_new_api,language)

        radio_component = OldAPI.old_api(use_new_api,cm.get_value("cutting")["radio_component"])

        top_k = cm.get_value("gpt")["top_k"]
        top_p = cm.get_value("gpt")["top_p"]
        temperature = cm.get_value("gpt")["temperature"]
        speed = cm.get_value("gpt")["speed"]
        if_freeze = cm.get_value("gpt")["if_freeze"]

        if isdocker():
            client = Client("http://host.docker.internal:9872/")
        else:
            client = Client("http://localhost:9872/")
            
        if cm.get_value("global")["use_new_api"]:
            result = client.predict(reference_audio, reference_audio_text, reference_audio_language, inference_text,
                                    inference_text_language, radio_component, top_k, top_p, temperature,
                                    no_reference_mode,
                                    fn_index=3)
        else:
            result = client.predict(
                ref_wav_path=file(reference_audio), 
                prompt_text=reference_audio_text, 
                prompt_language=reference_audio_language,
                text=inference_text,
                text_language=inference_text_language,
                how_to_cut=radio_component,
                top_k=top_k,
                top_p=top_p,
                temperature=temperature,
                ref_free=no_reference_mode,
                speed=speed,
                if_freeze=if_freeze,
                inp_refs=inp_refs,
                api_name="/get_tts_wav"
            )

        return result