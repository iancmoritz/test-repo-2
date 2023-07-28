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
from astronomercoreapi.api.cloud_ide_project_api import CloudIDEProjectApi  # noqa: E501
from astronomercoreapi.rest import ApiException


class TestCloudIDEProjectApi(unittest.TestCase):
    """CloudIDEProjectApi unit test stubs"""

    def setUp(self):
        self.api = astronomercoreapi.api.cloud_ide_project_api.CloudIDEProjectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_project(self):
        """Test case for create_project

        Create a new project  # noqa: E501
        """
        pass

    def test_create_project_git_branch(self):
        """Test case for create_project_git_branch

        Create a new Git branch for the project repository  # noqa: E501
        """
        pass

    def test_create_project_git_commit(self):
        """Test case for create_project_git_commit

        Create a new Git commit for the project  # noqa: E501
        """
        pass

    def test_delete_project(self):
        """Test case for delete_project

        Delete a project  # noqa: E501
        """
        pass

    def test_get_project(self):
        """Test case for get_project

        Get project  # noqa: E501
        """
        pass

    def test_get_project_git_comparison(self):
        """Test case for get_project_git_comparison

        Get project Git comparison  # noqa: E501
        """
        pass

    def test_list_project_git_branches(self):
        """Test case for list_project_git_branches

        List project Git branches  # noqa: E501
        """
        pass

    def test_list_project_git_commits(self):
        """Test case for list_project_git_commits

        List project Git commits  # noqa: E501
        """
        pass

    def test_list_projects(self):
        """Test case for list_projects

        List projects  # noqa: E501
        """
        pass

    def test_sync_project_include(self):
        """Test case for sync_project_include

        Synchronize an include of a project  # noqa: E501
        """
        pass

    def test_test_connection(self):
        """Test case for test_connection

        Test a connection against a project  # noqa: E501
        """
        pass

    def test_test_project_connection(self):
        """Test case for test_project_connection

        Test an existing project connection  # noqa: E501
        """
        pass

    def test_update_project(self):
        """Test case for update_project

        Update a project  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()