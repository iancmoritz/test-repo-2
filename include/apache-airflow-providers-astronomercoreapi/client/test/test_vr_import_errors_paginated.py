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
from astronomercoreapi.models.vr_import_errors_paginated import VRImportErrorsPaginated  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestVRImportErrorsPaginated(unittest.TestCase):
    """VRImportErrorsPaginated unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VRImportErrorsPaginated
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VRImportErrorsPaginated`
        """
        model = astronomercoreapi.models.vr_import_errors_paginated.VRImportErrorsPaginated()  # noqa: E501
        if include_optional :
            return VRImportErrorsPaginated(
                import_errors = [
                    astronomercoreapi.models.virtual_runtime_import_error.VirtualRuntimeImportError(
                        filename = '', 
                        import_error_id = 56, 
                        stack_trace = '', 
                        timestamp = '', )
                    ], 
                limit = 56, 
                offset = 56, 
                total_count = 56
            )
        else :
            return VRImportErrorsPaginated(
                import_errors = [
                    astronomercoreapi.models.virtual_runtime_import_error.VirtualRuntimeImportError(
                        filename = '', 
                        import_error_id = 56, 
                        stack_trace = '', 
                        timestamp = '', )
                    ],
                limit = 56,
                offset = 56,
                total_count = 56,
        )
        """

    def testVRImportErrorsPaginated(self):
        """Test VRImportErrorsPaginated"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
