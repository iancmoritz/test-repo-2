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
from astronomerregistry.models.related_module_request import RelatedModuleRequest  # noqa: E501
from astronomerregistry.rest import ApiException

class TestRelatedModuleRequest(unittest.TestCase):
    """RelatedModuleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RelatedModuleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RelatedModuleRequest`
        """
        model = astronomerregistry.models.related_module_request.RelatedModuleRequest()  # noqa: E501
        if include_optional :
            return RelatedModuleRequest(
                module_name = '', 
                provider_name = '', 
                version = ''
            )
        else :
            return RelatedModuleRequest(
                module_name = '',
                provider_name = '',
                version = '',
        )
        """

    def testRelatedModuleRequest(self):
        """Test RelatedModuleRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
