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
from astronomercoreapi.models.run_group import RunGroup  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestRunGroup(unittest.TestCase):
    """RunGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RunGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RunGroup`
        """
        model = astronomercoreapi.models.run_group.RunGroup()  # noqa: E501
        if include_optional :
            return RunGroup(
                children = [
                    astronomercoreapi.models.run_group.RunGroup(
                        children = [
                            astronomercoreapi.models.run_group.RunGroup(
                                extra_links = [
                                    ''
                                    ], 
                                has_outlet_datasets = True, 
                                id = '', 
                                is_mapped = True, 
                                label = '', 
                                operator = '', 
                                task_instances = [
                                    astronomercoreapi.models.task_instance.TaskInstance(
                                        dag_id = '', 
                                        dag_run_id = '', 
                                        duration = 1.337, 
                                        end_date = '', 
                                        execution_date = '', 
                                        executor_config = '', 
                                        hostname = '', 
                                        map_index = 56, 
                                        max_tries = 56, 
                                        note = '', 
                                        operator = '', 
                                        pid = 56, 
                                        pool = '', 
                                        pool_slots = 56, 
                                        priority_weight = 56, 
                                        queue = '', 
                                        queued_when = '', 
                                        rendered_fields = { }, 
                                        start_date = '', 
                                        state = 'success', 
                                        task_id = '', 
                                        try_number = 56, 
                                        unixname = '', )
                                    ], )
                            ], 
                        extra_links = [
                            ''
                            ], 
                        has_outlet_datasets = True, 
                        id = '', 
                        is_mapped = True, 
                        label = '', 
                        operator = '', 
                        task_instances = [
                            astronomercoreapi.models.task_instance.TaskInstance(
                                dag_id = '', 
                                dag_run_id = '', 
                                duration = 1.337, 
                                end_date = '', 
                                execution_date = '', 
                                executor_config = '', 
                                hostname = '', 
                                map_index = 56, 
                                max_tries = 56, 
                                note = '', 
                                operator = '', 
                                pid = 56, 
                                pool = '', 
                                pool_slots = 56, 
                                priority_weight = 56, 
                                queue = '', 
                                queued_when = '', 
                                start_date = '', 
                                state = 'success', 
                                task_id = '', 
                                try_number = 56, 
                                unixname = '', )
                            ], )
                    ], 
                extra_links = [
                    ''
                    ], 
                has_outlet_datasets = True, 
                id = '', 
                is_mapped = True, 
                label = '', 
                operator = '', 
                task_instances = [
                    astronomercoreapi.models.task_instance.TaskInstance(
                        dag_id = '', 
                        dag_run_id = '', 
                        duration = 1.337, 
                        end_date = '', 
                        execution_date = '', 
                        executor_config = '', 
                        hostname = '', 
                        map_index = 56, 
                        max_tries = 56, 
                        note = '', 
                        operator = '', 
                        pid = 56, 
                        pool = '', 
                        pool_slots = 56, 
                        priority_weight = 56, 
                        queue = '', 
                        queued_when = '', 
                        rendered_fields = { }, 
                        start_date = '', 
                        state = 'success', 
                        task_id = '', 
                        try_number = 56, 
                        unixname = '', )
                    ]
            )
        else :
            return RunGroup(
        )
        """

    def testRunGroup(self):
        """Test RunGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
