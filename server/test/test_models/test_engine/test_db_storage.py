#!/usr/bin/python3
""" Module for testing db storage"""
import psycopg2
import os
import unittest
from datetime import datetime

from models import storage
from models.exp_tokens import ExpToken

class TestDBStorage(unittest.TestCase):
    """ Class to test the database storage method
    """
    def test_storage_var_created(self):
        """ DBStorage object storage created """
        from models.engine.db_storage import DBStorage
        self.assertEqual(type(storage), DBStorage)

    def test_new(self):
        """ New object is correctly added to database
        """
        data = {
            'jti': '55e294cd-e1f4-4996-ad65-a4b61d9aa7e8'
        }
        new = ExpToken(**data)
        self.assertFalse(new in storage.all().values())
        new.save()
        self.assertTrue(new in storage.all().values())
        conn = psycopg2.connect(database=os.environ['DB_NAME'],
                        user=os.environ['DB_USERNAME'],
                        password=os.environ['DB_PASSWORD'],
                        host=os.environ['DB_HOST'],
                        port=5432)
        cur = conn.cursor()
        cur.execute("SELECT * FROM exptoken WHERE id='{}'".format(new.id))
        row = cur.fetchone()
        self.assertTrue(row is not None)
        self.assertIn('55e294cd-e1f4-4996-ad65-a4b61d9aa7e8', row)
        cur.close()
        conn.close()

    def test_delete(self):
        """ Test the delete methos of storage class
        """
        data = {
            'jti': '55e294cd-e1f4-4996-ad65-a4b61d9aa7ey'
        }
        new = ExpToken(**data)
        new.save()
        self.assertTrue(new in storage.all().values())
        conn = psycopg2.connect(database=os.environ['DB_NAME'],
                user=os.environ['DB_USERNAME'],
                password=os.environ['DB_PASSWORD'],
                host=os.environ['DB_HOST'],
                port=5432)
        cur = conn.cursor()
        cur.execute("SELECT * FROM exptoken WHERE id='{}'".format(new.id))
        row = cur.fetchone()
        self.assertTrue(row is not None)
        self.assertIn('55e294cd-e1f4-4996-ad65-a4b61d9aa7ey', row)
        new.delete()
        self.assertFalse(new in storage.all().values())
        cur.close()
        conn.close()

    def test_new_and_save(self):
        """ testing to be sure new and save methods works properly in sync
        """
        data = {
            'jti': '55e294cd-e1f4-4996-ad65-a4b61d9aa7e23'
        }
        new = ExpToken(**data)
        new.save()
        conn = psycopg2.connect(database=os.environ['DB_NAME'],
                user=os.environ['DB_USERNAME'],
                password=os.environ['DB_PASSWORD'],
                host=os.environ['DB_HOST'],
                port=5432)
        cur = conn.cursor()
        cur.execute("SELECT * FROM exptoken".format(new.id))
        row = cur.fetchall()
        cur.close()
        conn.close()

        data = {
            'jti': '55e294cd-e1f4-4996-ad65-a4b61d9aa7e2'
        }
        new = ExpToken(**data)
        new.save()
        conn = psycopg2.connect(database=os.environ['DB_NAME'],
                user=os.environ['DB_USERNAME'],
                password=os.environ['DB_PASSWORD'],
                host=os.environ['DB_HOST'],
                port=5432)
        cur = conn.cursor()
        cur.execute("SELECT * FROM exptoken".format(new.id))
        row2 = cur.fetchall()
        self.assertEqual(len(row), len(row2) - 1)

        cur.close()
        conn.close()

    def test_get(self):
        """ Test the get method by id storage class 
        """
        data = {
            'jti': '55e294cd-e1f4-4996-ad65-a4b61d9aa7e34'
        }
        new = ExpToken(**data)
        new.save()
        db_data = storage.get(ExpToken, new.id)
        self.assertEqual(db_data.id, new.id)
        self.assertEqual(db_data.jti, new.jti)

    def test_get_none(self):
        """ Test the get method by id storage class for None value
        """
        id = 'invalid id'
        db_data = storage.get(ExpToken, id)
        self.assertIsNone(db_data)





