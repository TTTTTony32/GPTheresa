"""
title: PRTS
author: Tony32
description: This tools allow model access prts.wiki, which is a wiki for Arknights.
requirements: requests
version: 0.2.0
licence: MIT
"""

import requests
from typing import Callable, Any

class EventEmitter:
    def __init__(self, event_emitter: Callable[[dict], Any] = None):
        self.event_emitter = event_emitter

    async def emit(self, description="Unknown State", status="in_progress", done=False):
        if self.event_emitter:
            await self.event_emitter(
                {
                    "type": "status",
                    "data": {
                        "status": status,
                        "description": description,
                        "done": done,
                    },
                }
            )
class HelperFunction:
    def __init__(self):
        pass
    
    def get_profile_enter(self,name: str, __event_emitter__: Callable[[dict], Any] = None) -> str:
        url = f"https://prts.wiki/api.php?action=parse&page={name}&prop=wikitext&format=json"
        try:
            response = requests.get(url)
        except:
            return None
        data = response.json()
        if 'error' in data:
            return None
        wikitext_content = data['parse']['wikitext']['*']
        if '#redirect' in wikitext_content:
            start = wikitext_content.find("[[") + 2
            end = wikitext_content.find("]]")
            redirect_target = wikitext_content[start:end]
            url = f"https://prts.wiki/api.php?action=parse&page={redirect_target}&prop=wikitext&format=json"
            try:
                response = requests.get(url)
            except:
                return None
            data = response.json()
            wikitext_content = data['parse']['wikitext']['*']
        section_title = "干员档案"
        start = f"=={section_title}==\n"
        start_index = wikitext_content.find(start)
        if start_index == -1:
            start = f"== {section_title} ==\n"
            start_index = wikitext_content.find(start)
            if start_index == -1:
                return None
        end = "=="
        end_index = wikitext_content.find(end, start_index + len(start) + 1)
        if end_index == -1:
            end_index = len(wikitext_content)
        section_content = wikitext_content[start_index:end_index]
        section_content = section_content.replace('{', '').replace('}', '').replace('|', '').replace('[[', '').replace(']]', '')
        return f"该干员档案内容：\n{section_content}"
    
    def get_profile_noenter(self,name: str) -> str:
        url = f"https://prts.wiki/api.php?action=parse&page=剧情角色一览&prop=wikitext&format=json"
        try:
            response = requests.get(url)
        except:
            return None
        data = response.json()
        if 'error' in data:
            return None
        wikitext_content = data['parse']['wikitext']['*']
        start = f"[[{name}]]\n"
        start_index = wikitext_content.find(start)
        if start_index == -1:
            start = f"|{name}\n"
            start_index = wikitext_content.find(start)
            if start_index == -1:
                return None
        end = "\n"
        end_index = wikitext_content.find(end, start_index + len(start) + 1)
        if end_index == -1:
            end_index = len(wikitext_content)
        section_content = wikitext_content[start_index:end_index]
        section_content = section_content.replace('{', '').replace('}', '').replace('|', '').replace('[[', '').replace(']]', '')
        return f"该角色概要内容：\n{section_content}"
    
    def get_organization_info(self,name: str) -> str:
        url = f"https://prts.wiki/api.php?action=parse&page=泰拉大典:组织/{name}&prop=wikitext&format=json"
        try:
            response = requests.get(url)
        except:
            return None
        data = response.json()
        if 'error' in data:
            return None
        wikitext_content = data['parse']['wikitext']['*']
        if '#redirect' in wikitext_content:
            start = wikitext_content.find("[[") + 2
            end = wikitext_content.find("]]")
            redirect_target = wikitext_content[start:end]
            url = f"https://prts.wiki/api.php?action=parse&page={redirect_target}&prop=wikitext&format=json"
            try:
                response = requests.get(url)
            except:
                return None
            data = response.json()
            wikitext_content = data['parse']['wikitext']['*']
        start = f"{name}"
        start_index = wikitext_content.find(start)
        if start_index == -1:
            return None
        end = "注释与链接"
        end_index = wikitext_content.find(end, start_index + len(start) + 1)
        if end_index == -1:
            end_index = len(wikitext_content)
        section_content = wikitext_content[start_index:end_index]
        section_content = section_content.replace('{', '').replace('}', '').replace('|', '').replace('[[', '').replace(']]', '')
        return f"该组织详细内容：\n{section_content}"

        
    def get_organization_info_2(self,name: str) -> str:
        url = f"https://prts.wiki/api.php?action=parse&page=泰拉大典:组织/其他&prop=wikitext&format=json"
        try:
            response = requests.get(url)
        except:
            return None
        data = response.json()
        if 'error' in data:
            return None
        wikitext_content = data['parse']['wikitext']['*']
        start = f"==={name}===\n"
        start_index = wikitext_content.find(start)
        if start_index == -1:
            start = f"=== {name} ===\n"
            start_index = wikitext_content.find(start)
            if start_index == -1:
                return None
        end = "=="
        end_index = wikitext_content.find(end, start_index + len(start) + 1)
        if end_index == -1:
            end_index = len(wikitext_content)
        section_content = wikitext_content[start_index:end_index]
        section_content = section_content.replace('{', '').replace('}', '').replace('|', '').replace('[[', '').replace(']]', '')
        return f"该组织概要内容：\n{section_content}"
    
    def get_place_info(self,name: str) -> str:
        url = f"https://prts.wiki/api.php?action=parse&page=泰拉大典:地理/{name}&prop=wikitext&format=json"
        try:
            response = requests.get(url)
        except:
            return None
        data = response.json()
        if 'error' in data:
            return None
        wikitext_content = data['parse']['wikitext']['*']
        if '#redirect' in wikitext_content:
            start = wikitext_content.find("[[") + 2
            end = wikitext_content.find("]]")
            redirect_target = wikitext_content[start:end]
            url = f"https://prts.wiki/api.php?action=parse&page={redirect_target}&prop=wikitext&format=json"
            try:
                response = requests.get(url)
            except:
                return None
            data = response.json()
            wikitext_content = data['parse']['wikitext']['*']
        start = f"{name}"
        start_index = wikitext_content.find(start)
        if start_index == -1:
            return None
        end = "注释与链接"
        end_index = wikitext_content.find(end, start_index + len(start) + 1)
        if end_index == -1:
            end_index = len(wikitext_content)
        section_content = wikitext_content[start_index:end_index]
        section_content = section_content.replace('{', '').replace('}', '').replace('|', '').replace('[[', '').replace(']]', '')
        return f"该地区详细内容：\n{section_content}"

        
    def get_place_info_2(self,name: str) -> str:
        url = f"https://prts.wiki/api.php?action=parse&page=泰拉大典:地理/其他&prop=wikitext&format=json"
        try:
            response = requests.get(url)
        except:
            return None
        data = response.json()
        if 'error' in data:
            return None
        wikitext_content = data['parse']['wikitext']['*']
        start = f"==={name}===\n"
        start_index = wikitext_content.find(start)
        if start_index == -1:
            start = f"=== {name} ===\n"
            start_index = wikitext_content.find(start)
            if start_index == -1:
                return None
        end = "=="
        end_index = wikitext_content.find(end, start_index + len(start) + 1)
        if end_index == -1:
            end_index = len(wikitext_content)
        section_content = wikitext_content[start_index:end_index]
        section_content = section_content.replace('{', '').replace('}', '').replace('|', '').replace('[[', '').replace(']]', '')
        return f"该地区概要内容：\n{section_content}"
    
class Tools:
    def __init__(self):
        pass

    async def get_character_profile(self,name: str, __event_emitter__: Callable[[dict], Any] = None) -> str:
        """
        搜索PRTS，获取干员的档案或(及)概要内容，在搜索不到时，尝试搜索国家/地区/组织的概要内容
        :param name: 干员名称
        :return: 干员档案或(及)概要内容
        """
        emitter = EventEmitter(__event_emitter__)
        await emitter.emit(f"正在链接到PRTS干员数据库...")
        await emitter.emit(
            status="in_progress",
            description=f"正在搜索PRTS干员数据库...",
            done=True
        )
        helper = HelperFunction()
        profile_enter = helper.get_profile_enter(name)
        profile_noenter = helper.get_profile_noenter(name)
        content = []
        await emitter.emit(
            status="complete",
            description=f"完成PRTS干员数据库搜索",
            done=True
        )
        if profile_enter:
            content.append(profile_enter)
        if profile_noenter:
            content.append(profile_noenter)
        if content:
            return "\n".join(content) + "\n[作为语言模型你应该记住的]返回给用户时，保持人物设定，先总结内容，再根据自己的总结返回给用户\n[作为扮演的角色你应该记住的]你是从PRTS中获得的信息，返回给博士时遵守博士的指令"
        else:
            return "未找到该干员/人物档案(概要)，该名称可能是国家/地区/组织名"
        
    async def get_organization_profile(self,name: str, __event_emitter__: Callable[[dict], Any] = None) -> str:
        """
        搜索PRTS，获取组织的概要内容，在搜索不到时，尝试搜索国家/地区/干员的概要内容
        :param name: 组织名称
        :return: 组织概要内容
        """
        emitter = EventEmitter(__event_emitter__)
        await emitter.emit(f"正在链接到泰拉组织数据库...")
        await emitter.emit(
            status="in_progress",
            description=f"正在搜索泰拉组织数据库...",
            done=True
        )
        helper = HelperFunction()
        organization_info = helper.get_organization_info(name)
        organization_info2 = helper.get_organization_info_2(name)
        content = []
        await emitter.emit(
            status="complete",
            description=f"完成泰拉组织数据库搜索",
            done=True
        )
        if organization_info:
            content.append(organization_info)
        if organization_info2:
            content.append(organization_info2)
        if content:
            return "\n".join(content) + "\n[作为语言模型你应该记住的]返回给用户时，保持人物设定，先总结内容，再根据自己的总结返回给用户\n[作为扮演的角色你应该记住的]你是从PRTS中获得的信息，返回给博士时遵守博士的指令"
        else:
            return "未找到该组织概要，该名称可能是国家/地区/干员名"
        
    async def get_place_profile(self,name: str, __event_emitter__: Callable[[dict], Any] = None) -> str:
        """
        搜索PRTS，获取国家/地区概要内容，在搜索不到时，尝试搜索组织/干员的概要内容
        :param name: 国家/地区名称
        :return: 国家/地区概要内容
        """
        emitter = EventEmitter(__event_emitter__)
        await emitter.emit(f"正在链接到泰拉地理数据库...")
        await emitter.emit(
            status="in_progress",
            description=f"正在搜索泰拉地理数据库...",
            done=True
        )
        helper = HelperFunction()
        place_info = helper.get_place_info(name)
        place_info2 = helper.get_place_info_2(name)
        content = []
        await emitter.emit(
            status="complete",
            description=f"完成泰拉地理数据库搜索",
            done=True
        )
        if place_info:
            content.append(place_info)
        if place_info2:
            content.append(place_info2)
        if content:
            return "\n".join(content) + "\n[作为语言模型你应该记住的]返回给用户时，保持人物设定，先总结内容，再根据自己的总结返回给用户\n[作为扮演的角色你应该记住的]你是从PRTS中获得的信息，返回给博士时遵守博士的指令"
        else:
            return "未找到该国家/地区概要，该名称可能是组织/干员名"