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
from astronomercoreapi.models.internal_pagination_result_dag_run_with_task_instances import InternalPaginationResultDagRunWithTaskInstances  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestInternalPaginationResultDagRunWithTaskInstances(unittest.TestCase):
    """InternalPaginationResultDagRunWithTaskInstances unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InternalPaginationResultDagRunWithTaskInstances
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InternalPaginationResultDagRunWithTaskInstances`
        """
        model = astronomercoreapi.models.internal_pagination_result_dag_run_with_task_instances.InternalPaginationResultDagRunWithTaskInstances()  # noqa: E501
        if include_optional :
            return InternalPaginationResultDagRunWithTaskInstances(
                items = [
                    astronomercoreapi.models.internal_dag_run_with_task_instances.internal_DagRunWithTaskInstances(
                        data_interval_end = '', 
                        data_interval_start = '', 
                        end_date = '', 
                        logical_date = '', 
                        run_id = '', 
                        run_type = '', 
                        start_date = '', 
                        state = '', 
                        task_instances = [
                            astronomercoreapi.models.internal_task_instances_inner.internal_TaskInstancesInner(
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
                                    try_number = 56, ), )
                            ], )
                    ], 
                next_cursor = '', 
                prev_cursor = '', 
                total_count = 56
            )
        else :
            return InternalPaginationResultDagRunWithTaskInstances(
        )
        """

    def testInternalPaginationResultDagRunWithTaskInstances(self):
        """Test InternalPaginationResultDagRunWithTaskInstances"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()