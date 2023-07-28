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
from astronomercoreapi.api.api_token_api import ApiTokenApi  # noqa: E501
from astronomercoreapi.rest import ApiException


class TestApiTokenApi(unittest.TestCase):
    """ApiTokenApi unit test stubs"""

    def setUp(self):
        self.api = astronomercoreapi.api.api_token_api.ApiTokenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_organization_api_token(self):
        """Test case for create_organization_api_token

        Create Organization API token  # noqa: E501
        """
        pass

    def test_create_workspace_api_token(self):
        """Test case for create_workspace_api_token

        Create Workspace API token  # noqa: E501
        """
        pass

    def test_delete_organization_api_token(self):
        """Test case for delete_organization_api_token

        Delete organization API token  # noqa: E501
        """
        pass

    def test_delete_workspace_api_token(self):
        """Test case for delete_workspace_api_token

        Delete Workspace API token  # noqa: E501
        """
        pass

    def test_get_organization_api_token(self):
        """Test case for get_organization_api_token

        Get Organization API token  # noqa: E501
        """
        pass

    def test_get_workspace_api_token(self):
        """Test case for get_workspace_api_token

        Get Workspace API token  # noqa: E501
        """
        pass

    def test_list_organization_api_tokens(self):
        """Test case for list_organization_api_tokens

        List Organization API tokens  # noqa: E501
        """
        pass

    def test_list_workspace_api_tokens(self):
        """Test case for list_workspace_api_tokens

        List Workspace API tokens  # noqa: E501
        """
        pass

    def test_rotate_organization_api_token(self):
        """Test case for rotate_organization_api_token

        Rotate organization API token  # noqa: E501
        """
        pass

    def test_rotate_workspace_api_token(self):
        """Test case for rotate_workspace_api_token

        Rotate Workspace API token  # noqa: E501
        """
        pass

    def test_update_organization_api_token(self):
        """Test case for update_organization_api_token

        Update Organization API token  # noqa: E501
        """
        pass

    def test_update_workspace_api_token(self):
        """Test case for update_workspace_api_token

        Update Workspace API token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()