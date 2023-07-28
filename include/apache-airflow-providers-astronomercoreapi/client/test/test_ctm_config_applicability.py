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
from astronomercoreapi.models.ctm_config_applicability import CtmConfigApplicability  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestCtmConfigApplicability(unittest.TestCase):
    """CtmConfigApplicability unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CtmConfigApplicability
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CtmConfigApplicability`
        """
        model = astronomercoreapi.models.ctm_config_applicability.CtmConfigApplicability()  # noqa: E501
        if include_optional :
            return CtmConfigApplicability(
                when_siblings = [
                    astronomercoreapi.models.ctm_clause.CtmClause(
                        key = '', 
                        operator = 'eq', 
                        value = astronomercoreapi.models.ctm_value.CtmValue(
                            boolean = True, 
                            duration = astronomercoreapi.models.ctm_value_duration.CtmValueDuration(
                                length = 56, 
                                unit = 'microseconds', ), 
                            file = astronomercoreapi.models.ctm_value_file.CtmValueFile(
                                conn_id = '', 
                                file_type = '', 
                                path = '', ), 
                            float = 1.337, 
                            integer = 56, 
                            string = '', 
                            string_list = [
                                ''
                                ], 
                            string_list_map = {
                                'key' : [
                                    ''
                                    ]
                                }, 
                            string_map = {
                                'key' : ''
                                }, 
                            string_map_list = [
                                {
                                    'key' : ''
                                    }
                                ], 
                            string_set = {
                                'key' : True
                                }, 
                            table = astronomercoreapi.models.ctm_value_table.CtmValueTable(
                                conn_id = '', 
                                database = '', 
                                name = '', 
                                schema = '', ), ), )
                    ]
            )
        else :
            return CtmConfigApplicability(
        )
        """

    def testCtmConfigApplicability(self):
        """Test CtmConfigApplicability"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
