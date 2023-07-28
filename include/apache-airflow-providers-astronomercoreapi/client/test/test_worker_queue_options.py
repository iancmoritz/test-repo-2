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
from astronomercoreapi.models.worker_queue_options import WorkerQueueOptions  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestWorkerQueueOptions(unittest.TestCase):
    """WorkerQueueOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WorkerQueueOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkerQueueOptions`
        """
        model = astronomercoreapi.models.worker_queue_options.WorkerQueueOptions()  # noqa: E501
        if include_optional :
            return WorkerQueueOptions(
                max_workers = astronomercoreapi.models.resource_range.ResourceRange(
                    ceiling = 56, 
                    default = 56, 
                    floor = 56, ), 
                min_workers = astronomercoreapi.models.resource_range.ResourceRange(
                    ceiling = 56, 
                    default = 56, 
                    floor = 56, )
            )
        else :
            return WorkerQueueOptions(
        )
        """

    def testWorkerQueueOptions(self):
        """Test WorkerQueueOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()