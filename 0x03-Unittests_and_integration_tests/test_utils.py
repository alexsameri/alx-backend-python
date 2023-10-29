"""
module for test
"""
import unittest
from parameterized import parameterized

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    testing the method to return an expected value
    """
    @parameterized.expand([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        {"a": {"b": 2}}, ("a", "b"), 2,
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """use assertEqual"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == "__main__":
    unittest.main()