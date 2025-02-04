#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 2025-MiddleAPI
# @File : pydanticUtils.py
# @IDE : PyCharm
# @Author : Ashley
# @Date : 2025/2/4 14:05
from pydantic import BaseModel

class OpenWebUI(BaseModel):
    input:str
    voice:str

class SetConfig(BaseModel):
    section:str
    key:str
    value:str
    
