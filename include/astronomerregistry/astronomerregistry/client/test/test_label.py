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
from astronomerregistry.models.label import Label  # noqa: E501
from astronomerregistry.rest import ApiException

class TestLabel(unittest.TestCase):
    """Label unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Label
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Label`
        """
        model = astronomerregistry.models.label.Label()  # noqa: E501
        if include_optional :
            return Label(
                created_at = '', 
                created_by = '', 
                description = '', 
                graphics = astronomerregistry.models.label_graphics.LabelGraphics(
                    banner = '', 
                    icon = '', ), 
                id = '', 
                name = '', 
                organization_id = '', 
                updated_at = '', 
                updated_by = ''
            )
        else :
            return Label(
                created_at = '',
                created_by = '',
                id = '',
                name = '',
                updated_at = '',
                updated_by = '',
        )
        """

    def testLabel(self):
        """Test Label"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
