#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 2025-MiddleAPI
# @File : PydanticUtils.py
# @IDE : PyCharm
# @Author : Ashley Lee (nekokecore@emtips.net)
# @Date : 2025/2/4 14:05

# Copyright 2025 Ashley Lee (nekokecore@emtips.net)
from pydantic import BaseModel
from typing import Union

class OpenWebUIObj(BaseModel):
    input:str
    voice:str

class SetConfigObj(BaseModel):
    section:str
    key:str
    value:Union[str, int, float, bool]

class GetConfigObj(BaseModel):
    section:str
    key:str
