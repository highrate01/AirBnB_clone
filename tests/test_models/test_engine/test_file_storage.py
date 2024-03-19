import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestfilestorageInstantiation(unittest.TestCase):
    """
    Testing the instatiation of file storage
    """

    def test_filestorage_instatiation_no_args(self):
        """Test creating a file storage instance with no args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_filestorage_instance_with_args(self):
        """
        test creating file storage with argument
        it should reaise TypeError.
        """
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_init(self):
        """
        Test if storage vaiable in model is an instance
        of filestorage.
        """
        self.assertEqual(type(models.storage), FileStorage)


class Testfilestorage(unittest.TestCase):

    def setUp(self):
        """
        create a tempoary test file for saving data
        """
        self.test_file = "test_file.json"

    def tearDown(self):
        """
        Remove tempoary test file after the test
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_storage_return_dict(self):
        """
        Test if all() method returns a dictionary.
        """
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """
        Test the new method by crreating and storing object
        """
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), models.storage.all())

    def test_new_with_args(self):
        """
        Test if new method contain additional argument. TypeError should be
        raised if it does
        """

        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """
        Test creating a new object with none. If true,
        An attribute error should be raised.
        """
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_and_reload(self):
        """
        Test saving object to a file and reload
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save()

        """creating a new storage instance to simulate reloading"""

        new_storage = FileStorage()
        new_storage.reload()

        """check if reloaded objects match the original object"""

        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj1.id))
                        is not None)
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj2.id))
                        is not None)

    def test_save_to_file(self):
        """
        Test saving object to a file and check if the file is created
        """
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reload_empty_file(self):
        """
        Test reloading when the file is empty or
        doest not exist
        """
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()


if __name__ == "__main__":
    unittest.main()
