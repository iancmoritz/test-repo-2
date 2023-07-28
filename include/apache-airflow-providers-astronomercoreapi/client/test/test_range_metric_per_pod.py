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
from astronomercoreapi.models.range_metric_per_pod import RangeMetricPerPod  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestRangeMetricPerPod(unittest.TestCase):
    """RangeMetricPerPod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RangeMetricPerPod
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RangeMetricPerPod`
        """
        model = astronomercoreapi.models.range_metric_per_pod.RangeMetricPerPod()  # noqa: E501
        if include_optional :
            return RangeMetricPerPod(
                component = '', 
                deployment_id = '', 
                end = 56, 
                pod = '', 
                release_name = '', 
                start = 56, 
                step = 56, 
                values = [
                    astronomercoreapi.models.metric_value.MetricValue(
                        timestamp = 1.337, 
                        value = 1.337, )
                    ], 
                workspace_id = ''
            )
        else :
            return RangeMetricPerPod(
                component = '',
                deployment_id = '',
                end = 56,
                pod = '',
                release_name = '',
                start = 56,
                step = 56,
                values = [
                    astronomercoreapi.models.metric_value.MetricValue(
                        timestamp = 1.337, 
                        value = 1.337, )
                    ],
                workspace_id = '',
        )
        """

    def testRangeMetricPerPod(self):
        """Test RangeMetricPerPod"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()