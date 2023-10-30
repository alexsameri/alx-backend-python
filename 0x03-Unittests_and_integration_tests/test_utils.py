"""
module for test
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
# import requests


class TestAccessNestedMap(unittest.TestCase):
    """
    testing the method to return an expected value
    """
    @parameterized.expand([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2,)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """use assertEqual"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a", ), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_result):
        """
        Use assertRaises to test that an exception is raised when the method is called.
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected_result}')", repr(e.exception))


if __name__ == "__main__":
    unittest.main()
