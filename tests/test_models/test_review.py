#!/usr/bin/python3
"""Unittests for models/review.py

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_attribute values are set
    TestAmenity_attribute values can be asssigned
"""
import os
import unittest
from models.base_model import BaseModel
import models
from models.review import Review


class TestReview(unittest.TestCase):
    """
    class TestReview
    """
    def setUp(self):
        """
        creates a temp file to save data
        """
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        """
        deletes the created test file
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_review_inheritance(self):
        """
        test if state inheritance from parent class
        BaseModel
        """
        test_city = Review()
        self.assertTrue(issubclass(Review, BaseModel))

    def test_instance_creation(self):
        """Test if an instance of Review is
        created successfully.
        """
        review = Review()
        self.assertIsInstance(review, Review)

    def test_attribute_default_values(self):
        """ Test if default attribute
        values are set correctly.
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
