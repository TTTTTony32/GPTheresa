"""
title: PRTS
author: Tony32
author_url: 
git_url: 
description: This tools allow model access prts.wiki, which is a wiki for Arknights.
required_open_webui_version: 0.1.0
requirements: requests
version: 0.1.0
licence: MIT
"""

import requests

class Tools:
    def __init__(self):
        pass

    def get_info(self,name: str) -> str:
        """
        从PRTS获取干员/人物/组织/国家/地区的档案或(及)概要内容
        :param name: 干员/人物/组织/国家/地区名称
        :return: 档案或(及)概要内容
        """
        profile_enter = self.get_profile_enter(name)
        profile_noenter = self.get_profile_noenter(name)
        organization_info = self.get_organization_info(name)
        place_info = self.get_place_info(name)
        content = []
        if profile_enter:
            content.append(profile_enter)
        if profile_noenter:
            content.append(profile_noenter)
        if organization_info:
            content.append(organization_info)
        if place_info:
            content.append(place_info)
        if content:
            return "\n".join(content) + "\n[作为语言模型你应该记住的]返回给用户时，保持人物设定，先总结内容，再根据自己的总结返回给用户\n[作为扮演的角色你应该记住的]你是从PRTS中获得的信息，返回给博士时遵守博士的指令"
        else:
            return "未找到该干员/人物档案(概要)"

    def get_profile_enter(self,name: str) -> str:
        url = f"https://prts.wiki/api.php?action=parse&page={name}&prop=wikitext&format=json"
        response = requests.get(url)
        data = response.json()
        if 'error' in data:
            return None
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
        response = requests.get(url)
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
        response = requests.get(url)
        data = response.json()
        if 'error' in data:
            return self.get_organization_info_2(name)
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
        response = requests.get(url)
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
        response = requests.get(url)
        data = response.json()
        if 'error' in data:
            return self.get_place_info_2(name)
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
        response = requests.get(url)
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