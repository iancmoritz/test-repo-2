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
from astronomercoreapi.models.connections_paginated import ConnectionsPaginated  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestConnectionsPaginated(unittest.TestCase):
    """ConnectionsPaginated unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ConnectionsPaginated
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectionsPaginated`
        """
        model = astronomercoreapi.models.connections_paginated.ConnectionsPaginated()  # noqa: E501
        if include_optional :
            return ConnectionsPaginated(
                connections = [
                    astronomercoreapi.models.connection.Connection(
                        connection_name = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_by_user = astronomercoreapi.models.basic_subject_profile.BasicSubjectProfile(
                            api_token_name = '', 
                            avatar_url = '', 
                            full_name = '', 
                            id = '', 
                            subject_type = 'USER', 
                            username = '', ), 
                        extra = {
                            'key' : ''
                            }, 
                        host = '', 
                        id = '', 
                        login = '', 
                        password = '', 
                        port = 56, 
                        schema = '', 
                        type = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_by_user = astronomercoreapi.models.basic_subject_profile.BasicSubjectProfile(
                            api_token_name = '', 
                            avatar_url = '', 
                            full_name = '', 
                            id = '', 
                            subject_type = 'USER', 
                            username = '', ), )
                    ], 
                limit = 56, 
                offset = 56, 
                total_count = 56
            )
        else :
            return ConnectionsPaginated(
                connections = [
                    astronomercoreapi.models.connection.Connection(
                        connection_name = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_by_user = astronomercoreapi.models.basic_subject_profile.BasicSubjectProfile(
                            api_token_name = '', 
                            avatar_url = '', 
                            full_name = '', 
                            id = '', 
                            subject_type = 'USER', 
                            username = '', ), 
                        extra = {
                            'key' : ''
                            }, 
                        host = '', 
                        id = '', 
                        login = '', 
                        password = '', 
                        port = 56, 
                        schema = '', 
                        type = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_by_user = astronomercoreapi.models.basic_subject_profile.BasicSubjectProfile(
                            api_token_name = '', 
                            avatar_url = '', 
                            full_name = '', 
                            id = '', 
                            subject_type = 'USER', 
                            username = '', ), )
                    ],
                limit = 56,
                offset = 56,
                total_count = 56,
        )
        """

    def testConnectionsPaginated(self):
        """Test ConnectionsPaginated"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()