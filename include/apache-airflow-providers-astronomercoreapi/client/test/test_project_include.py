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
from astronomercoreapi.models.project_include import ProjectInclude  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestProjectInclude(unittest.TestCase):
    """ProjectInclude unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectInclude
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectInclude`
        """
        model = astronomercoreapi.models.project_include.ProjectInclude()  # noqa: E501
        if include_optional :
            return ProjectInclude(
                auto_sync_disabled = True, 
                git = astronomercoreapi.models.project_includes_git.ProjectIncludesGit(
                    sha = '', ), 
                name = '', 
                type = 'project-git'
            )
        else :
            return ProjectInclude(
                name = '',
                type = 'project-git',
        )
        """

    def testProjectInclude(self):
        """Test ProjectInclude"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
