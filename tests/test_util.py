# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import namedtuple
import unittest
from datetime import date, time, datetime

from knack.util import todict, to_snake_case


class TestUtils(unittest.TestCase):

    def test_application_todict_none(self):
        the_input = None
        actual = todict(the_input)
        expected = None
        self.assertEqual(actual, expected)

    def test_application_todict_dict_empty(self):
        the_input = {}
        actual = todict(the_input)
        expected = {}
        self.assertEqual(actual, expected)

    def test_application_todict_dict(self):
        the_input = {'a': 'b'}
        actual = todict(the_input)
        expected = {'a': 'b'}
        self.assertEqual(actual, expected)

    def test_application_todict_list(self):
        the_input = [{'a': 'b'}]
        actual = todict(the_input)
        expected = [{'a': 'b'}]
        self.assertEqual(actual, expected)

    def test_application_todict_obj(self):
        MyObject = namedtuple('MyObject', 'a b')
        the_input = MyObject('x', 'y')
        actual = todict(the_input)
        expected = {'a': 'x', 'b': 'y'}
        self.assertEqual(actual, expected)

    def test_application_todict_dict_with_obj(self):
        MyObject = namedtuple('MyObject', 'a b')
        mo = MyObject('x', 'y')
        the_input = {'a': mo}
        actual = todict(the_input)
        expected = {'a': {'a': 'x', 'b': 'y'}}
        self.assertEqual(actual, expected)

    def test_application_todict_dict_with_date(self):
        the_input = date(2017, 10, 13)
        actual = todict(the_input)
        expected = the_input.isoformat()
        self.assertEqual(actual, expected)

    def test_application_todict_dict_with_datetime(self):
        the_input = datetime(2017, 10, 13, 1, 23, 45)
        actual = todict(the_input)
        expected = the_input.isoformat()
        self.assertEqual(actual, expected)

    def test_application_todict_dict_with_time(self):
        the_input = time(1, 23, 45)
        actual = todict(the_input)
        expected = the_input.isoformat()
        self.assertEqual(actual, expected)

    def test_to_snake_case_from_camel(self):
        the_input = 'thisIsCamelCase'
        expected = 'this_is_camel_case'
        actual = to_snake_case(the_input)
        self.assertEqual(expected, actual)

    def test_to_snake_case_empty(self):
        the_input = ''
        expected = ''
        actual = to_snake_case(the_input)
        self.assertEqual(expected, actual)

    def test_to_snake_case_already_snake(self):
        the_input = 'this_is_snake_cased'
        expected = 'this_is_snake_cased'
        actual = to_snake_case(the_input)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
