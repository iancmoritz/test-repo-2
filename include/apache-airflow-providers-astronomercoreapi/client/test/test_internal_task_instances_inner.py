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
from astronomercoreapi.models.internal_task_instances_inner import InternalTaskInstancesInner  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestInternalTaskInstancesInner(unittest.TestCase):
    """InternalTaskInstancesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InternalTaskInstancesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InternalTaskInstancesInner`
        """
        model = astronomercoreapi.models.internal_task_instances_inner.InternalTaskInstancesInner()  # noqa: E501
        if include_optional :
            return InternalTaskInstancesInner(
                mapped_task_instance_summary = astronomercoreapi.models.internal_mapped_task_instance_summary.internal_MappedTaskInstanceSummary(
                    end_date = '', 
                    overall_state = '', 
                    start_date = '', 
                    states = {
                        'key' : 56
                        }, 
                    task_id = '', 
                    try_number = 56, ), 
                unmapped_task_instance = astronomercoreapi.models.internal_unmapped_task_instance.internal_UnmappedTaskInstance(
                    end_date = '', 
                    start_date = '', 
                    state = '', 
                    task_id = '', 
                    try_number = 56, )
            )
        else :
            return InternalTaskInstancesInner(
        )
        """

    def testInternalTaskInstancesInner(self):
        """Test InternalTaskInstancesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
