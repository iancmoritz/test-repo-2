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
from astronomercoreapi.models.update_azure_cluster_request import UpdateAzureClusterRequest  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestUpdateAzureClusterRequest(unittest.TestCase):
    """UpdateAzureClusterRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateAzureClusterRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateAzureClusterRequest`
        """
        model = astronomercoreapi.models.update_azure_cluster_request.UpdateAzureClusterRequest()  # noqa: E501
        if include_optional :
            return UpdateAzureClusterRequest(
                db_instance_type = '', 
                k8s_tags = [
                    astronomercoreapi.models.cluster_tag.ClusterTag(
                        key = '', 
                        value = '', )
                    ], 
                name = '', 
                node_pools = [
                    astronomercoreapi.models.update_node_pool_request.UpdateNodePoolRequest(
                        id = '', 
                        is_default = True, 
                        max_node_count = 56, 
                        name = '', 
                        node_instance_type = '', )
                    ], 
                template_version = ''
            )
        else :
            return UpdateAzureClusterRequest(
                db_instance_type = '',
                k8s_tags = [
                    astronomercoreapi.models.cluster_tag.ClusterTag(
                        key = '', 
                        value = '', )
                    ],
                name = '',
                node_pools = [
                    astronomercoreapi.models.update_node_pool_request.UpdateNodePoolRequest(
                        id = '', 
                        is_default = True, 
                        max_node_count = 56, 
                        name = '', 
                        node_instance_type = '', )
                    ],
                template_version = '',
        )
        """

    def testUpdateAzureClusterRequest(self):
        """Test UpdateAzureClusterRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
