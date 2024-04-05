#!/usr/bin/env python3
""" BaseModel TestClass
"""
import unittest
from models.baseModel import BaseModel
from datetime import datetime
import time
import models
from unittest import mock


class TestBaseModel(unittest.TestCase):
    """ Test BaseModel class
    """
    def testInstantiation(self):
        """ Test that baseModel object is correctly created
        """
        obj = BaseModel()
        self.assertIs(type(obj), BaseModel)
        obj.max = 100
        obj.name = 'upbeat'
        self.assertEqual(obj.name, "upbeat")
        self.assertEqual(obj.max, 100)
        obj_attr_type = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "max": int
        }
        for attr, typ in obj_attr_type.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, obj.__dict__)
                self.assertIs(type(obj.__dict__[attr]), typ)

    def test_uuid(self):
        """ Test that a valid uuid is created
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)
        uuid_regex = '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
        for obj in [obj1, obj2]:
            uuid = obj.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid, uuid_regex)

    def test_datetime_attributes(self):
        """ Test created at and updated attribures
        """
        t1 = datetime.now()
        obj1 = BaseModel()
        t2 = datetime.now()
        self.assertTrue(t1 <= obj1.created_at)
        self.assertTrue(t2 >= obj1.created_at)
        time.sleep(0.5)
        t1 = datetime.now()
        obj2 = BaseModel()
        t2 = datetime.now()
        self.assertTrue(t1 <= obj2.created_at)
        self.assertTrue(t2 >= obj2.created_at)

        self.assertNotEqual(obj1.created_at, obj2.created_at)
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)

        self.assertEqual(obj1.created_at, obj1.updated_at)
        self.assertEqual(obj2.created_at, obj2.updated_at)

    def test_to_dict_conversion(self):
        """ Test to_dict for correct conversion of obj to dict
        """
        obj = BaseModel()
        obj.max = 100
        obj.name = 'upbeat'
        obj_dict = obj.to_dict()
        correct_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "max",
                          "__class__"]
        self.assertCountEqual(obj_dict.keys(), correct_attrs)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['name'], "upbeat")
        self.assertEqual(obj_dict['max'], 100)

    def test_to_dict_values(self):
        """ Test the valus of to_dict method conversion
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(type(obj_dict["created_at"]), str)
        self.assertEqual(type(obj_dict["updated_at"]), str)
        self.assertEqual(obj_dict["created_at"], obj.created_at.strftime(time_format))
        self.assertEqual(obj_dict["updated_at"], obj.updated_at.strftime(time_format))

    def test_str(self):
        """ Test str representation of baseModel obj
        """
        obj = BaseModel()
        str_rep = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str_rep, str(obj))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """ Test the save method of basemodel
        """
        obj = BaseModel()
        initial_created_at = obj.created_at
        initial_updated_at = obj.updated_at
        time.sleep(0.5)
        obj.save()
        new_created_at = obj.created_at
        new_updated_at =obj.updated_at
        self.assertNotEqual(initial_updated_at, new_updated_at)
        self.assertEqual(initial_created_at, new_created_at)
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)

    @mock.patch('models.storage')
    def test_delete(self, mock_storage):
        """ Test the delete method of baseModel
        """
        obj = BaseModel()
        obj.delete()
        self.assertTrue(mock_storage.delete.called)

    @mock.patch('models.storage')
    def test_update(self, mock_storage):
        """ Test the delete method of baseModel
        """
        obj = BaseModel()
        obj.name = 'upbeat'
        obj.max = 100
        initial_created_at = obj.created_at
        initial_updated_at = obj.updated_at
        updated_val = {
            'name': 'upbeat_updated',
            'max': 200,
            'new_attr': 'test_added'
        }
        obj.update(**updated_val)
        self.assertEqual(obj.name, 'upbeat_updated')
        self.assertEqual(obj.max, 200)
        self.assertEqual(obj.new_attr, 'test_added')
        self.assertTrue(mock_storage.save.called)
