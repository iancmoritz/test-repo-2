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
from astronomercoreapi.models.create_cell_request import CreateCellRequest  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestCreateCellRequest(unittest.TestCase):
    """CreateCellRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateCellRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCellRequest`
        """
        model = astronomercoreapi.models.create_cell_request.CreateCellRequest()  # noqa: E501
        if include_optional :
            return CreateCellRequest(
                dependencies_explicit = [
                    ''
                    ], 
                name = '', 
                type = '', 
                type_config_forms = {
                    'key' : ''
                    }, 
                type_configs = None
            )
        else :
            return CreateCellRequest(
                name = '',
                type = '',
        )
        """

    def testCreateCellRequest(self):
        """Test CreateCellRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
