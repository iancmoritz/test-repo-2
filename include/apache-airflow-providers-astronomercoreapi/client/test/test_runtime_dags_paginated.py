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
from astronomercoreapi.models.runtime_dags_paginated import RuntimeDagsPaginated  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestRuntimeDagsPaginated(unittest.TestCase):
    """RuntimeDagsPaginated unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RuntimeDagsPaginated
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RuntimeDagsPaginated`
        """
        model = astronomercoreapi.models.runtime_dags_paginated.RuntimeDagsPaginated()  # noqa: E501
        if include_optional :
            return RuntimeDagsPaginated(
                dags = [
                    astronomercoreapi.models.runtime_dag.RuntimeDag(
                        dag_id = '', 
                        default_view = '', 
                        description = '', 
                        file_token = '', 
                        fileloc = '', 
                        has_import_errors = True, 
                        has_task_concurrency_limits = True, 
                        is_active = True, 
                        is_paused = True, 
                        is_subdag = True, 
                        last_expired = '', 
                        last_parsed_time = '', 
                        last_pickled = '', 
                        max_active_runs = 56, 
                        max_active_tasks = 56, 
                        next_dagrun = '', 
                        next_dagrun_create_after = '', 
                        next_dagrun_data_interval_end = '', 
                        next_dagrun_data_interval_start = '', 
                        owners = [
                            ''
                            ], 
                        pickle_id = '', 
                        root_dag_id = '', 
                        schedule_interval = astronomercoreapi.models.schedule_interval.scheduleInterval(), 
                        scheduler_lock = True, 
                        tags = [
                            astronomercoreapi.models.dag_tag.DagTag(
                                name = '', )
                            ], 
                        timetable_description = '', )
                    ], 
                limit = 56, 
                offset = 56, 
                total_count = 56
            )
        else :
            return RuntimeDagsPaginated(
                dags = [
                    astronomercoreapi.models.runtime_dag.RuntimeDag(
                        dag_id = '', 
                        default_view = '', 
                        description = '', 
                        file_token = '', 
                        fileloc = '', 
                        has_import_errors = True, 
                        has_task_concurrency_limits = True, 
                        is_active = True, 
                        is_paused = True, 
                        is_subdag = True, 
                        last_expired = '', 
                        last_parsed_time = '', 
                        last_pickled = '', 
                        max_active_runs = 56, 
                        max_active_tasks = 56, 
                        next_dagrun = '', 
                        next_dagrun_create_after = '', 
                        next_dagrun_data_interval_end = '', 
                        next_dagrun_data_interval_start = '', 
                        owners = [
                            ''
                            ], 
                        pickle_id = '', 
                        root_dag_id = '', 
                        schedule_interval = astronomercoreapi.models.schedule_interval.scheduleInterval(), 
                        scheduler_lock = True, 
                        tags = [
                            astronomercoreapi.models.dag_tag.DagTag(
                                name = '', )
                            ], 
                        timetable_description = '', )
                    ],
                limit = 56,
                offset = 56,
                total_count = 56,
        )
        """

    def testRuntimeDagsPaginated(self):
        """Test RuntimeDagsPaginated"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
