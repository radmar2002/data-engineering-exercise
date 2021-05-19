"""
Use Python unittest for nest.py script
"""
import json
import unittest
import pandas as pd

from nest import list_nester


def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    shared_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o: (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
    same = set(o for o in shared_keys if d1[o] == d2[o])
    return added, removed, modified, same


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.inputfile = pd.read_json('test_input.json')
        self.input = pd.read_json('input.json')
        self.expected = pd.read_json('expected_output.json')

        # inp = self.input.to_json()
        # exp = self.expected.to_json()
        # print(inp)
        # print(exp)

    def test_good_result(self):
        """
        check if expected VS. delivered jsons are:
            added, removed, modified, same
        """
        added, removed, modified, same = dict_compare(
            self.input.to_dict(), self.expected.to_dict())
        self.assertEqual(len(modified), 0)

    def test_list_nester_type(self):
        # should raise an exception if list nester return_type is not string
        resnl = list_nester(self.inputfile, ["country", "city"])
        self.assertIs(type(resnl), str)

    def test_four_columns_mock(self):

        # should raise an exception for if there are no
        self.assertEqual(len(self.inputfile.columns), 4)

    def test_amount(self):
        """ test amount column presence """
        element = "amount"
        self.assertTrue(element in list(self.inputfile.columns))

        """ test ammounts column presence """
        element = "ammounts"
        self.assertFalse(element in list(self.inputfile.columns))


if __name__ == '__main__':
    unittest.main()
