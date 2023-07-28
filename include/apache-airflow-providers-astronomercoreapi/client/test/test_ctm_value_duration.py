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
from astronomercoreapi.models.ctm_value_duration import CtmValueDuration  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestCtmValueDuration(unittest.TestCase):
    """CtmValueDuration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CtmValueDuration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CtmValueDuration`
        """
        model = astronomercoreapi.models.ctm_value_duration.CtmValueDuration()  # noqa: E501
        if include_optional :
            return CtmValueDuration(
                length = 56, 
                unit = 'microseconds'
            )
        else :
            return CtmValueDuration(
                length = 56,
                unit = 'microseconds',
        )
        """

    def testCtmValueDuration(self):
        """Test CtmValueDuration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()