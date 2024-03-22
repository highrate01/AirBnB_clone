#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""
import os
import models
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing
    instantiation of the State class.
    """
    def setUp(self):
        """
        creates a temp file for saving data
        """
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        """
        deletes the created test file after used
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_inheritance(self):
        """
        test if state class inherit from base_model
        """
        test_state = State()
        self.assertTrue(issubclass(State, BaseModel))

    def test_no_args_instantiates(self):
        """
        test with no args
        """
        self.assertEqual(State, type(State()))

    def test_id_is_public_str(self):
        """
        test if id is public string
        """
        self.assertEqual(str, type(State().id))

    def test_name_is_public_class_attribute(self):
        """
        test if class is public attribute
        """
        st = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(st))
        self.assertNotIn("name", st.__dict__)

    def test_two_states_unique_ids(self):
        """
        test for unique ids
        """
        st1 = State()
        st2 = State()
        self.assertNotEqual(st1.id, st2.id)


if __name__ == "__main__":
    unittest.main()
