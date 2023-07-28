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
from astronomercoreapi.models.update_project_request import UpdateProjectRequest  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestUpdateProjectRequest(unittest.TestCase):
    """UpdateProjectRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateProjectRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateProjectRequest`
        """
        model = astronomercoreapi.models.update_project_request.UpdateProjectRequest()  # noqa: E501
        if include_optional :
            return UpdateProjectRequest(
                connections = [
                    astronomercoreapi.models.update_project_connection_request.UpdateProjectConnectionRequest(
                        extra = {
                            'key' : ''
                            }, 
                        host = '', 
                        id = '', 
                        login = '', 
                        password = '', 
                        port = 56, 
                        schema = '', 
                        type = '', )
                    ], 
                description = '', 
                git = astronomercoreapi.models.update_project_git_request.UpdateProjectGitRequest(
                    branch = '', 
                    dags_path = '', 
                    git_vendor_attributes = astronomercoreapi.models.update_project_git_vendor_attributes_request.UpdateProjectGitVendorAttributesRequest(
                        azure_dev_ops_organization = '', 
                        azure_dev_ops_project_id = '', ), 
                    repo = '', 
                    token = '', 
                    vendor = 'github', ), 
                includes = [
                    astronomercoreapi.models.update_project_include_request.UpdateProjectIncludeRequest(
                        auto_sync_disabled = True, 
                        name = '', 
                        type = 'project-git', )
                    ], 
                name = '', 
                requirements = [
                    ''
                    ], 
                variables = [
                    astronomercoreapi.models.update_project_variable_request.UpdateProjectVariableRequest(
                        is_secret = True, 
                        key = '', 
                        type = 'airflow', 
                        value = '', )
                    ]
            )
        else :
            return UpdateProjectRequest(
                name = '',
        )
        """

    def testUpdateProjectRequest(self):
        """Test UpdateProjectRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()