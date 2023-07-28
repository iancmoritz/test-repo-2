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
from astronomercoreapi.models.api_token import ApiToken  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestApiToken(unittest.TestCase):
    """ApiToken unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiToken
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiToken`
        """
        model = astronomercoreapi.models.api_token.ApiToken()  # noqa: E501
        if include_optional :
            return ApiToken(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = astronomercoreapi.models.basic_subject_profile.BasicSubjectProfile(
                    api_token_name = '', 
                    avatar_url = '', 
                    full_name = '', 
                    id = '', 
                    subject_type = 'USER', 
                    username = '', ), 
                created_by_id = '', 
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                description = '', 
                end_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                expiry_period_in_days = 56, 
                id = '', 
                last_used_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                name = '', 
                roles = [
                    astronomercoreapi.models.api_token_role.ApiTokenRole(
                        entity_id = '', 
                        entity_type = 'WORKSPACE', 
                        role = '', )
                    ], 
                short_token = '', 
                start_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                token = '', 
                type = 'WORKSPACE', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_by = astronomercoreapi.models.basic_subject_profile.BasicSubjectProfile(
                    api_token_name = '', 
                    avatar_url = '', 
                    full_name = '', 
                    id = '', 
                    subject_type = 'USER', 
                    username = '', ), 
                updated_by_id = ''
            )
        else :
            return ApiToken(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by_id = '',
                description = '',
                expiry_period_in_days = 56,
                id = '',
                name = '',
                roles = [
                    astronomercoreapi.models.api_token_role.ApiTokenRole(
                        entity_id = '', 
                        entity_type = 'WORKSPACE', 
                        role = '', )
                    ],
                short_token = '',
                start_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                type = 'WORKSPACE',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_by_id = '',
        )
        """

    def testApiToken(self):
        """Test ApiToken"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
