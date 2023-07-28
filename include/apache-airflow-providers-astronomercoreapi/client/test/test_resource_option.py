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
from astronomercoreapi.models.resource_option import ResourceOption  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestResourceOption(unittest.TestCase):
    """ResourceOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ResourceOption
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceOption`
        """
        model = astronomercoreapi.models.resource_option.ResourceOption()  # noqa: E501
        if include_optional :
            return ResourceOption(
                cpu = astronomercoreapi.models.resource_range.ResourceRange(
                    ceiling = 56, 
                    default = 56, 
                    floor = 56, ), 
                memory = astronomercoreapi.models.resource_range.ResourceRange(
                    ceiling = 56, 
                    default = 56, 
                    floor = 56, )
            )
        else :
            return ResourceOption(
                cpu = astronomercoreapi.models.resource_range.ResourceRange(
                    ceiling = 56, 
                    default = 56, 
                    floor = 56, ),
                memory = astronomercoreapi.models.resource_range.ResourceRange(
                    ceiling = 56, 
                    default = 56, 
                    floor = 56, ),
        )
        """

    def testResourceOption(self):
        """Test ResourceOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()