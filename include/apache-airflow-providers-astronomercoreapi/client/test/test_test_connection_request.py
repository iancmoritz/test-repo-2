# coding: utf-8

"""
    Astro Core API

    Astro Core API  # noqa: E501

    The version of the OpenAPI document: v1alpha1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import astronomercoreapi
from astronomercoreapi.models.test_connection_request import TestConnectionRequest  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestTestConnectionRequest(unittest.TestCase):
    """TestConnectionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TestConnectionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TestConnectionRequest`
        """
        model = astronomercoreapi.models.test_connection_request.TestConnectionRequest()  # noqa: E501
        if include_optional :
            return TestConnectionRequest(
                extra = {
                    'key' : ''
                    }, 
                host = '', 
                id = '', 
                login = '', 
                password = '', 
                port = 56, 
                var_schema = '', 
                type = ''
            )
        else :
            return TestConnectionRequest(
        )
        """

    def testTestConnectionRequest(self):
        """Test TestConnectionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
