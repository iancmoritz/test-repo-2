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
from astronomercoreapi.models.create_project_git_branch_request import CreateProjectGitBranchRequest  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestCreateProjectGitBranchRequest(unittest.TestCase):
    """CreateProjectGitBranchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateProjectGitBranchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateProjectGitBranchRequest`
        """
        model = astronomercoreapi.models.create_project_git_branch_request.CreateProjectGitBranchRequest()  # noqa: E501
        if include_optional :
            return CreateProjectGitBranchRequest(
                var_from = '', 
                name = ''
            )
        else :
            return CreateProjectGitBranchRequest(
                name = '',
        )
        """

    def testCreateProjectGitBranchRequest(self):
        """Test CreateProjectGitBranchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
