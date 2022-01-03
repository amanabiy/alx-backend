#!/usr/bin/env python3
"""
test access_nested_map
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized

class TestAccessNestedMap(unittest.Testcase):
    """
    Test the utils
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, answer):
        test_file = {"a": 1, "b": {"c": 3}}
        self.assertEqual(access_nested_map(nested_map, path), answer)