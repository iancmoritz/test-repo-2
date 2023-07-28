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
from astronomercoreapi.models.runtime_api_capabilities import RuntimeApiCapabilities  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestRuntimeApiCapabilities(unittest.TestCase):
    """RuntimeApiCapabilities unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RuntimeApiCapabilities
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RuntimeApiCapabilities`
        """
        model = astronomercoreapi.models.runtime_api_capabilities.RuntimeApiCapabilities()  # noqa: E501
        if include_optional :
            return RuntimeApiCapabilities(
                can_clear_dag_run = True, 
                can_update_task_instance = True
            )
        else :
            return RuntimeApiCapabilities(
                can_clear_dag_run = True,
                can_update_task_instance = True,
        )
        """

    def testRuntimeApiCapabilities(self):
        """Test RuntimeApiCapabilities"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
