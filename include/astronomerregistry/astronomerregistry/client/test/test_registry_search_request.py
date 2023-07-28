# coding: utf-8

"""
    Astro Registry API

    Astro Registry API  # noqa: E501

    The version of the OpenAPI document: v1alpha1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import astronomerregistry
from astronomerregistry.models.registry_search_request import RegistrySearchRequest  # noqa: E501
from astronomerregistry.rest import ApiException

class TestRegistrySearchRequest(unittest.TestCase):
    """RegistrySearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RegistrySearchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RegistrySearchRequest`
        """
        model = astronomerregistry.models.registry_search_request.RegistrySearchRequest()  # noqa: E501
        if include_optional :
            return RegistrySearchRequest(
                include_dags = True, 
                include_modules = True, 
                include_providers = True, 
                query = ''
            )
        else :
            return RegistrySearchRequest(
                query = '',
        )
        """

    def testRegistrySearchRequest(self):
        """Test RegistrySearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()