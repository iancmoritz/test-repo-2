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
from astronomercoreapi.models.update_project_git_request import UpdateProjectGitRequest  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestUpdateProjectGitRequest(unittest.TestCase):
    """UpdateProjectGitRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateProjectGitRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateProjectGitRequest`
        """
        model = astronomercoreapi.models.update_project_git_request.UpdateProjectGitRequest()  # noqa: E501
        if include_optional :
            return UpdateProjectGitRequest(
                branch = '', 
                dags_path = '', 
                git_vendor_attributes = astronomercoreapi.models.update_project_git_vendor_attributes_request.UpdateProjectGitVendorAttributesRequest(
                    azure_dev_ops_organization = '', 
                    azure_dev_ops_project_id = '', ), 
                repo = '', 
                token = '', 
                vendor = 'github'
            )
        else :
            return UpdateProjectGitRequest(
        )
        """

    def testUpdateProjectGitRequest(self):
        """Test UpdateProjectGitRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()