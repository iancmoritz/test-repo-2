# coding: utf-8

"""
    Astro Core API

    Astro Core API  # noqa: E501

    The version of the OpenAPI document: v1alpha1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import astronomercoreapi
from astronomercoreapi.api.invite_api import InviteApi  # noqa: E501
from astronomercoreapi.rest import ApiException


class TestInviteApi(unittest.TestCase):
    """InviteApi unit test stubs"""

    def setUp(self):
        self.api = astronomercoreapi.api.invite_api.InviteApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user_invite(self):
        """Test case for create_user_invite

        Create a user invitation  # noqa: E501
        """
        pass

    def test_delete_user_invite(self):
        """Test case for delete_user_invite

        Delete user invite  # noqa: E501
        """
        pass

    def test_get_user_invite(self):
        """Test case for get_user_invite

        Get user invite  # noqa: E501
        """
        pass

    def test_update_self_user_invite(self):
        """Test case for update_self_user_invite

        Update user invitation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
