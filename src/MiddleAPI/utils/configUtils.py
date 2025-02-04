#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 2025-MiddleAPI
# @File : configUtils.py
# @IDE : PyCharm
# @Author : Ashley Lee (nekokecore@emtips.net)
# @Date : 2025/2/4 13:45
import configparser

# Copyright 2025 Ashley Lee (nekokecore@emtips.net)

def getconfig(section,key):
    """
    
    Args:
        section: Config section.
        key: Config key in section.

    Returns: Settings Value.

    """
    cf = configparser.ConfigParser()
    cf.read('config/config.ini')
    value = cf.get(section,key)
    return value

def setconfig(section,key,value):
    """
    
    Args:
        section: Config section.
        key: Config key in section.
        value: New value based what key you chosen.

    Returns: None.

    """
    cf = configparser.ConfigParser()
    cf.read('config/config.ini')
    cf.set(section,key,value)
    with open('config/config.ini', 'w', encoding='utf-8') as configfile:
        cf.write(configfile)