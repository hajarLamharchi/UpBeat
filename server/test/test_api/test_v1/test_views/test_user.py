#!/usr/bin/python3
""" Module for user api"""
import unittest
from unittest.mock import patch
import requests
from flask import Flask
from flask_jwt_extended import JWTManager, create_access_token

class UserAPITestCase(unittest.TestCase):
    """ Test user/auth endpoints
    """
    @patch('requests.post')
    def test_login_with_json(self, mock):
        """ Test login endpoint with valid Json
        """
        mock_response = {
                'message': 'user loggedin successfully',
                'tokens': {
                    'access_token': 'token',
                    'refresh_token': 'token'
                }
            }
        mock.return_value.json.return_value = mock_response
        mock.return_value.status_code = 200

        credentials = {'email': 'example_user', 'password': 'example_password'}

        response = requests.post('http://127.0.0.1:5000/api/user/login', json=credentials)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), mock_response)

    @patch('requests.post')
    def test_login_with_wrong_content_type(self, mock):
        """ Login details that is not json
        """
        mock_res = {'error': 'invalid content type, please use json'}
        mock.return_value.json.return_value = mock_res
        mock.return_value.status_code = 415

        response = requests.post('http://127.0.0.1:5000/api/user/login')
        self.assertEqual(response.status_code, 415)
        self.assertEqual(response.json(), mock_res)

    @patch('requests.post')
    def test_login_with_with_incomplete_details(self, mock):
        """ Either username or password not passed
        """
        mock_res = {'error': 'email and password is required'}
        mock.return_value.json.return_value = mock_res
        mock.return_value.status_code = 400

        creden1 = {'email': 'example_user'}
        creden2 = {'password': 'example_password'}
        creden3 = {}

        response1 = requests.post('http://127.0.0.1:5000/api/user/login', json=creden1)
        response2 = requests.post('http://127.0.0.1:5000/api/user/login', json=creden2)
        response3 = requests.post('http://127.0.0.1:5000/api/user/login', json=creden3)

        self.assertEqual(response1.status_code, 400)
        self.assertEqual(response1.json(), mock_res)
        self.assertEqual(response2.status_code, 400)
        self.assertEqual(response2.json(), mock_res)
        self.assertEqual(response3.status_code, 400)
        self.assertEqual(response3.json(), mock_res)

    @patch('requests.post')
    def test_login_with_invalid_details(self, mock):
        """ Either username or password are invalid
        """
        mock_res = {'error': 'invalid email or password'}
        mock.return_value.json.return_value = mock_res
        mock.return_value.status_code = 400
        
        credentials1 = {'email': 'invalid_user', 'password': 'invalid_paswword'}
        credentials2 = {'email': 'valid_user', 'password': 'invalid_paswword'}
        credentials3 = {'email': 'invalid_user', 'password': 'valid_paswword'}

        response1 = requests.post('http://127.0.0.1:5000/api/user/login', json=credentials1)
        response2 = requests.post('http://127.0.0.1:5000/api/user/login', json=credentials2)
        response3 = requests.post('http://127.0.0.1:5000/api/user/login', json=credentials3)

        self.assertEqual(response1.status_code, 400)
        self.assertEqual(response1.json(), mock_res)
        self.assertEqual(response2.status_code, 400)
        self.assertEqual(response2.json(), mock_res)
        self.assertEqual(response3.status_code, 400)
        self.assertEqual(response3.json(), mock_res)