"""
---
name: file.py
description: File package
copyright: 2018-2019 Marcio Pessoa
people:
  developers:
  - name: Marcio Pessoa
    email: marcio.pessoa@gmail.com
change-log: Check README.md file.
"""

import sys
import json
import yaml


class File:
    """
    description:
    """

    __version__ = 0.04

    def __init__(self):
        self.data = None

    def load(self, file, kind):
        """
        description:
        """
        # debugln('File: ' + str(file), 1)
        # Open file
        if not file:
            # File definition missing
            sys.exit(True)
        try:
            file_obj = open(file, 'r')
        except IOError as err:
            print(err)
            sys.exit(True)
        # Set file type and format
        if kind == 'json':
            data = file_obj.read()
            self.json_load(data)
            self.json_info()
        elif kind == 'gcode':
            data = file_obj.readlines()
            self.gcode_load(data)
            self.gcode_info()
        elif kind == 'yaml':
            data = file_obj.read()
            self.yaml_load(data)
            self.yaml_info()
        file_obj.close()

    def get(self):
        """
        description:
        """
        return self.data

    def yaml_load(self, data):
        """
        description:
        """
        # self.reset()
        # debugln('Parsing YAML...', 1)
        try:
            self.data = yaml.load(data)
        except ValueError as err:
            print(err)
            # erroln(str(err))
            sys.exit(True)

    def yaml_info(self):
        """
        description:
        """
        items = len(self.data)
        return {'items': items}

    def gcode_load(self, data):
        """
        description:
        """
        # self.reset()
        # debugln('Parsing G-code...', 1)
        self.data = data

    def gcode_info(self):
        """
        description:
        """
        line_total = len(self.data)
        char_total = len(''.join(self.data))
        return {'lines': line_total, 'chars': char_total}

    def json_load(self, data):
        """
        description:
        """
        # self.reset()
        # debugln('Parsing JSON...', 1)
        try:
            self.data = json.loads(data)
        except ValueError as err:
            print(err)
            # erroln(str(err))
            sys.exit(True)

    def json_info(self):
        """
        description:
        """
        hosts = 0
        devices = 0
        try:
            hosts = len(self.data["host"])
        except BaseException:
            pass
        try:
            devices = len(self.data["device"])
        except BaseException:
            pass
        return {'devices': devices, 'hosts': hosts}
