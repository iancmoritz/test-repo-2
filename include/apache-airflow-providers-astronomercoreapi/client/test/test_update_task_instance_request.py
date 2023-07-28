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
from astronomercoreapi.models.update_task_instance_request import UpdateTaskInstanceRequest  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestUpdateTaskInstanceRequest(unittest.TestCase):
    """UpdateTaskInstanceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateTaskInstanceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateTaskInstanceRequest`
        """
        model = astronomercoreapi.models.update_task_instance_request.UpdateTaskInstanceRequest()  # noqa: E501
        if include_optional :
            return UpdateTaskInstanceRequest(
                is_dry_run = True, 
                state = ''
            )
        else :
            return UpdateTaskInstanceRequest(
                state = '',
        )
        """

    def testUpdateTaskInstanceRequest(self):
        """Test UpdateTaskInstanceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()