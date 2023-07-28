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
from astronomercoreapi.models.user import User  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test User
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `User`
        """
        model = astronomercoreapi.models.user.User()  # noqa: E501
        if include_optional :
            return User(
                avatar_url = '', 
                color_mode_preference = '', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                full_name = '', 
                id = '', 
                invites = [
                    astronomercoreapi.models.invite.Invite(
                        expires_at = '', 
                        invite_id = '', 
                        invitee = astronomercoreapi.models.basic_subject_profile.BasicSubjectProfile(
                            api_token_name = '', 
                            avatar_url = '', 
                            full_name = '', 
                            id = '', 
                            subject_type = 'USER', 
                            username = '', ), 
                        inviter = astronomercoreapi.models.basic_subject_profile.BasicSubjectProfile(
                            api_token_name = '', 
                            avatar_url = '', 
                            full_name = '', 
                            id = '', 
                            subject_type = 'USER', 
                            username = '', ), 
                        o_auth_invite_id = '', 
                        org_name = '', 
                        org_short_name = '', 
                        organization_id = '', 
                        organization_name = '', 
                        organization_short_name = '', 
                        ticket_id = '', 
                        user_id = '', )
                    ], 
                last_login = '', 
                last_login_connection_name = '', 
                last_login_connection_type = '', 
                org_count = 56, 
                org_role = '', 
                org_user_relation_is_idp_managed = True, 
                roles = [
                    astronomercoreapi.models.user_role.UserRole(
                        role = '', 
                        scope = astronomercoreapi.models.scope.Scope(
                            entity_id = '', 
                            type = '', ), 
                        subject = astronomercoreapi.models.subject.Subject(
                            entity_id = '', 
                            type = '', ), )
                    ], 
                status = '', 
                system_role = '', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                username = '', 
                workspace_count = 56, 
                workspace_role = ''
            )
        else :
            return User(
                avatar_url = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                full_name = '',
                id = '',
                status = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                username = '',
        )
        """

    def testUser(self):
        """Test User"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
