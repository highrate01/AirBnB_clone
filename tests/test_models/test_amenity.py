#!/usr/bin/python3
"""Unittests for models/amenity.py

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_attribute values are set
    TestAmenity_attribute values can be asssigned
"""
import os
import unittest
from models.base_model import BaseModel
import models
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    Test amneity class
    """
    def setUp(self):
        """
        creates a tempoary file to save data
        """
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        """
        deletes the temp file
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_instance_creation(self):
        """
        Test for instantiation of the amenity class
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_attribute_default_values(self):
        """
        Test to check if amenity attribute values are set
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_attribute_assignment(self):
        """
        Check if amenity attribut values
        can be assigned and not just an empty string
        """
        amenity = Amenity()
        amenity.name = "Gym"
        self.assertEqual(amenity.name, "Gym")

    def test_amenity_inheritance(self):
        """
        test if amenity class inherit from BaseModel
        """
        test_city = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_args_unused(self):
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """
        instantiation with kwargs
        """
        dt = datetime.utcnow()
        dt_iso = dt.isoformat()
        am = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(am.id, "345")
        self.assertEqual(am.created_at, dt)
        self.assertEqual(am.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """
        Instantiation with none kwargs
        """
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
