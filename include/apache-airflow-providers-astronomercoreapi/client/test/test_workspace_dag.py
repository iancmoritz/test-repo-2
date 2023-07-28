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
from astronomercoreapi.models.workspace_dag import WorkspaceDag  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestWorkspaceDag(unittest.TestCase):
    """WorkspaceDag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WorkspaceDag
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkspaceDag`
        """
        model = astronomercoreapi.models.workspace_dag.WorkspaceDag()  # noqa: E501
        if include_optional :
            return WorkspaceDag(
                dag_id = '', 
                deployment_id = '', 
                is_active = True, 
                is_paused = True, 
                next_run_at = '', 
                owners = [
                    ''
                    ], 
                runs = [
                    astronomercoreapi.models.workspace_dag_run.WorkspaceDagRun(
                        data_interval_end = '', 
                        data_interval_start = '', 
                        end_date = '', 
                        logical_date = '', 
                        run_id = '', 
                        run_type = '', 
                        start_date = '', 
                        state = '', )
                    ], 
                schedule = astronomercoreapi.models.dag_schedule.DagSchedule(
                    cron_expression = astronomercoreapi.models.internal_schedule_interval_cron_expression.internal_ScheduleIntervalCronExpression(
                        value = '', ), 
                    relative_delta = astronomercoreapi.models.internal_schedule_interval_relative_delta.internal_ScheduleIntervalRelativeDelta(
                        day = 56, 
                        days = 56, 
                        hour = 56, 
                        hours = 56, 
                        leapdays = 56, 
                        microsecond = 56, 
                        microseconds = 56, 
                        minute = 56, 
                        minutes = 56, 
                        month = 56, 
                        months = 56, 
                        second = 56, 
                        seconds = 56, 
                        week = 56, 
                        weeks = 56, 
                        year = 56, 
                        years = 56, ), 
                    time_delta = astronomercoreapi.models.internal_schedule_interval_time_delta.internal_ScheduleIntervalTimeDelta(
                        days = 56, 
                        microseconds = 56, 
                        seconds = 56, ), ), 
                tags = [
                    ''
                    ], 
                timetable_description = ''
            )
        else :
            return WorkspaceDag(
                dag_id = '',
                deployment_id = '',
                is_paused = True,
        )
        """

    def testWorkspaceDag(self):
        """Test WorkspaceDag"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
