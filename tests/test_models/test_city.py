#!usr/bin/python3
"""
defines unittest for user class
"""
import unittest
import os
import models
from models.city import City
from models.base_model import BaseModel
import uuid


class TestCity(unittest.TestCase):
    """
    Test class
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
        deletes the created test file
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_city_attr(self):
        """
        Test if City attributes are initialized properly
        """
        test_city = City()
        self.assertEqual(test_city.name, "")
        self.assertEqual(test_city.state_id, "")

    def test_city_inheritance(self):
        """
        test if the new city inherit from base model
        """
        test_city = City()
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_str_rep(self):
        """
        test if string representation is valid
        """
        state_id = str(uuid.uuid4())
        test_city = City(name="Lagos", state_id=state_id)
        city_str = str(test_city)
        self.assertIn(state_id, city_str)

    def test_city_to_dict(self):
        """
        tests conversion to dict
        """
        test_city = City()
        test_city.name = "Lagos"
        test_city.state_id = str(uuid.uuid4())
        test_city.save()
        city_dict = test_city.to_dict()
        self.assertEqual(city_dict['name'], 'Lagos')
        self.assertEqual(city_dict['state_id'], test_city.state_id)

    def test_city_instance(self):
        """
        test for new instance
        """
        state_id = str(uuid.uuid4())
        test_city = City(name="Lagos", state_id=state_id)
        self.assertEqual(test_city.state_id, state_id)

    def test_city_id(self):
        """
        test for created id
        """
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)


if __name__ == "__main__":
    unittest.main()
