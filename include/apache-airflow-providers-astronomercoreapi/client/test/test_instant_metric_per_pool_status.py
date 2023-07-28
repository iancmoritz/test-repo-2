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
from astronomercoreapi.models.instant_metric_per_pool_status import InstantMetricPerPoolStatus  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestInstantMetricPerPoolStatus(unittest.TestCase):
    """InstantMetricPerPoolStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InstantMetricPerPoolStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstantMetricPerPoolStatus`
        """
        model = astronomercoreapi.models.instant_metric_per_pool_status.InstantMetricPerPoolStatus()  # noqa: E501
        if include_optional :
            return InstantMetricPerPoolStatus(
                deployment_id = '', 
                pool = '', 
                release_name = '', 
                status = '', 
                value = 1.337, 
                workspace_id = ''
            )
        else :
            return InstantMetricPerPoolStatus(
                deployment_id = '',
                pool = '',
                release_name = '',
                status = '',
                value = 1.337,
                workspace_id = '',
        )
        """

    def testInstantMetricPerPoolStatus(self):
        """Test InstantMetricPerPoolStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()