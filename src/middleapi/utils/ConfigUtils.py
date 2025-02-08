#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : 2025-MiddleAPI
# @File : ConfigUtils.py
# @IDE : PyCharm
# @Author : Ashley Lee (nekokecore@emtips.net)
# @Date : 2025/2/4 13:45

# Copyright 2025 Ashley Lee (nekokecore@emtips.net)
import yaml
import os

class ConfigTools:
    def __init__(self, file_path):
        """
        
        Args:
            file_path: Config file path.
            
        """
        self.file_path = file_path
        if not os.path.exists(file_path):
            self._create_empty_config()

    def _create_empty_config(self):
        """
        
        Returns: None

        """
        with open(self.file_path, 'w', encoding='utf-8') as f:
            yaml.dump({}, f, default_flow_style=False, allow_unicode=True)

    def read_config(self):
        """
        
        Returns: Config context.

        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except yaml.YAMLError:
            return 1

    def write_config(self, config_data):
        """
        
        Args:
            config_data: new config data.

        Returns: status.

        """
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                yaml.dump(config_data, f, default_flow_style=False, allow_unicode=True)
            return 0
        except yaml.YAMLError:
            return 1

    def update_config(self, key, value):
        """
        
        Args:
            key: Config key.
            value: Config value.

        Returns:

        """
        config = self.read_config()
        config[key] = value
        self.write_config(config)
        return 0

    def get_value(self, key, default=None):
        """
            
        Args:
            key: Config key.
            default: If no value use this value.

        Returns:

        """
        config = self.read_config()
        return config.get(key, default)

    def delete_key(self, key):
        """
        
        Args:
            key: Config key.

        Returns: status.

        """
        config = self.read_config()
        if key in config:
            del config[key]
            self.write_config(config)
        return 0