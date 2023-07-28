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
from astronomercoreapi.models.create_sso_connection_request import CreateSsoConnectionRequest  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestCreateSsoConnectionRequest(unittest.TestCase):
    """CreateSsoConnectionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateSsoConnectionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSsoConnectionRequest`
        """
        model = astronomercoreapi.models.create_sso_connection_request.CreateSsoConnectionRequest()  # noqa: E501
        if include_optional :
            return CreateSsoConnectionRequest(
                auth0_connection_name = '012', 
                configuration = astronomercoreapi.models.sso_connection_config.SsoConnectionConfig(
                    azure_client_id = '', 
                    azure_client_secret = '', 
                    azure_domain_name = '', 
                    saml_sign_in_url = '', 
                    saml_sign_out_url = '', 
                    saml_signing_cert = '', 
                    strategy = 'samlp', ), 
                idp_initiated_login_enabled = True, 
                jit_policy = astronomercoreapi.models.jit_policy.JitPolicy(
                    default_org_role = '', 
                    default_workspace_roles = [
                        astronomercoreapi.models.workspace_role.WorkspaceRole(
                            workspace_id = '', 
                            workspace_role = '', )
                        ], ), 
                managed_domains = [
                    astronomercoreapi.models.sso_connection_managed_domain.SsoConnectionManagedDomain(
                        id = '', 
                        name = '', )
                    ]
            )
        else :
            return CreateSsoConnectionRequest(
                auth0_connection_name = '012',
                configuration = astronomercoreapi.models.sso_connection_config.SsoConnectionConfig(
                    azure_client_id = '', 
                    azure_client_secret = '', 
                    azure_domain_name = '', 
                    saml_sign_in_url = '', 
                    saml_sign_out_url = '', 
                    saml_signing_cert = '', 
                    strategy = 'samlp', ),
                managed_domains = [
                    astronomercoreapi.models.sso_connection_managed_domain.SsoConnectionManagedDomain(
                        id = '', 
                        name = '', )
                    ],
        )
        """

    def testCreateSsoConnectionRequest(self):
        """Test CreateSsoConnectionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()