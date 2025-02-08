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

from gradio_client import Client
from utils.ConfigUtils import ConfigTools
from utils.TextUtils import CleanText
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

        reference_audio = cm.get_value("reference")["reference_audio"]
        reference_audio_text = cm.get_value("reference")["reference_audio_text"]
        reference_audio_language = cm.get_value("reference")["reference_audio_language"]
        no_reference_mode = cm.get_value("reference")["no_reference_mode"]

        inference_text = CleanText.text(text)
        inference_text_language = language

        radio_component = cm.get_value("cutting")["radio_component"]

        top_k = cm.get_value("gpt")["top_k"]
        top_p = cm.get_value("gpt")["top_p"]
        temperature = cm.get_value("gpt")["temperature"]

        if isdocker():
            client = Client("http://host.docker.internal:9872/")
        else:
            client = Client("http://localhost:9872/")

        result = client.predict(reference_audio, reference_audio_text, reference_audio_language, inference_text,
                                inference_text_language, radio_component, top_k, top_p, temperature, no_reference_mode,
                                fn_index=3)

        return result