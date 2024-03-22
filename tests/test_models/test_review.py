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
import model
from models.review import Review


class TestReview(unittest.TestCase):
    """
    class TestReview
    """
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
