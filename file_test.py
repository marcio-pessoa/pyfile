#!/usr/bin/env python3
"""
---
name: file_test.py
description: Test File package
copyright: 2018-2019 Marcio Pessoa
people:
  developers:
  - name: Marcio Pessoa
    email: marcio.pessoa@gmail.com
"""

import unittest
from file import File


class TestFileMethods(unittest.TestCase):
    """
    description:
    """

    def test_load(self):
        """
        description: Load some file.
        """
        path = 'file.py'
        content = File()
        content.load(path, 'gcode')
        self.assertNotEqual(content.get(), '')


if __name__ == '__main__':
    unittest.main()
