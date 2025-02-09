#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 2025-MiddleAPI
# @File : TextUtils.py
# @IDE : PyCharm
# @Author : DeckDes (deckdes@outlook.com)
# @Co-Author : Ashley Lee (nekokecore@emtips.net)
# @Date : 2025/2/4 13:37

# Copyright 2025 DeckDes (deckdes@outlook.com)
# Copyright 2025 Ashley Lee (nekokecore@emtips.net)
import re

class CleanText:
    @staticmethod
    def text(input_text):
        """

        Returns: Deleted [***] text.

        """
        return re.sub(r"\[.*?]", "", input_text)

class OldAPI:
    @staticmethod
    def old_api(use_new_api,input_text):
        mapping = {
            "中文": "Chinese",
            "英文": "English",
            "日文": "Japanese",
            "不切": "No slice",
            "凑四句一切": "Slice once every 4 sentences",
            "凑50字一切": "Cut per 50 characters",
            "按中文句号。切": "Slice by Chinese punct",
            "按英文句号.切": "Slice by English punct",
            "按标点符号切": "Slice by every punct",
        }
        reverse_mapping = {v: k for k, v in mapping.items()}
        return mapping.get(input_text, input_text) if use_new_api else reverse_mapping.get(input_text, input_text)