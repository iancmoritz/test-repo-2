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
from astronomerregistry.models.module_inherits_from import ModuleInheritsFrom  # noqa: E501
from astronomerregistry.rest import ApiException

class TestModuleInheritsFrom(unittest.TestCase):
    """ModuleInheritsFrom unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ModuleInheritsFrom
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModuleInheritsFrom`
        """
        model = astronomerregistry.models.module_inherits_from.ModuleInheritsFrom()  # noqa: E501
        if include_optional :
            return ModuleInheritsFrom(
                module_name = '', 
                organization_id = '', 
                provider_name = '', 
                version = ''
            )
        else :
            return ModuleInheritsFrom(
        )
        """

    def testModuleInheritsFrom(self):
        """Test ModuleInheritsFrom"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()