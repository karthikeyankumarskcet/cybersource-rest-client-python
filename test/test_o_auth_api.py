# coding: utf-8

"""
    OAuth2 API

    OAuth2 Token Service (OAuth2)

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import CyberSource
from CyberSource.rest import ApiException
from CyberSource.apis.o_auth_api import OAuthApi


class TestOAuthApi(unittest.TestCase):
    """ OAuthApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.o_auth_api.OAuthApi()

    def tearDown(self):
        pass

    def test_create_access_token(self):
        """
        Test case for create_access_token

        Create access token and refresh token
        """
        pass


if __name__ == '__main__':
    unittest.main()
