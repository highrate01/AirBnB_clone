#!usr/bin/python3
"""
defines unittest for user class
"""
import unittest
import os
import models
from models.user import User
from models.base_model import BaseModel


class Test_user(unittest.TestCase):
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

    def test_user_attr(self):
        """
        creates user instance
        """
        test_user = User()
        self.assertEqual(test_user.first_name, "")
        self.assertEqual(test_user.last_name, "")
        self.assertEqual(test_user.email, "")
        self.assertEqual(test_user.password, "")

    def test_user_inheritance(self):
        """
        test if the new user inherit from base model
        """
        test_user = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str_rep(self):
        """
        test if string representation is valid
        """
        test_user = User()
        test_user.first_name = "Olufemi"
        test_user.last_name = "John"
        test_user.email = "johnolufemi@example.com"
        test_user.password = "password22"
        user_str = str(test_user)
        self.assertIn("User", user_str)
        self.assertIn("Olufemi", user_str)
        self.assertIn("John", user_str)
        self.assertIn("johnolufemi@example.com", user_str)

    def test_user_to_dict(self):
        """
        tests conersion to dict
        """
        test_user = User()
        test_user.first_name = "Olufemi"
        test_user.last_name = "John"
        test_user.email = "johnolufemi@example.com"
        test_user.save()
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['first_name'], "Olufemi")
        self.assertEqual(user_dict['last_name'], "John")
        self.assertEqual(user_dict['email'], "johnolufemi@example.com")

    def test_user_instance(self):
        """
        test for new instance
        """
        test_user = User(first_name="Olufemi", last_name="John",
                         email="johnolufemi@example.com",
                         password="password22")
        self.assertEqual(test_user.first_name, "Olufemi")
        self.assertEqual(test_user.last_name, "John")
        self.assertEqual(test_user.email, "johnolufemi@example.com")
        self.assertEqual(test_user.password, "password22")

    def test_user_id(self):
        """
        test for created id
        """
        test_user = User()
        user2 = User()
        self.assertNotEqual(test_user.id, user2.id)


if __name__ == "__main__":
    unittest.main()
