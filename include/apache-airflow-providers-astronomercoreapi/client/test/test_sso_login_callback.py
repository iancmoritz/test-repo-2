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
from astronomercoreapi.models.sso_login_callback import SsoLoginCallback  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestSsoLoginCallback(unittest.TestCase):
    """SsoLoginCallback unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SsoLoginCallback
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SsoLoginCallback`
        """
        model = astronomercoreapi.models.sso_login_callback.SsoLoginCallback()  # noqa: E501
        if include_optional :
            return SsoLoginCallback(
                access_token_claims = {
                    'key' : ''
                    }, 
                deny = astronomercoreapi.models.sso_login_deny.SsoLoginDeny(
                    connections = [
                        ''
                        ], 
                    message = '', 
                    reason = '', ), 
                id_token_claims = {
                    'key' : ''
                    }, 
                user_meta_data = None
            )
        else :
            return SsoLoginCallback(
        )
        """

    def testSsoLoginCallback(self):
        """Test SsoLoginCallback"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
