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
from astronomercoreapi.models.create_aws_cluster_request import CreateAwsClusterRequest  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestCreateAwsClusterRequest(unittest.TestCase):
    """CreateAwsClusterRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateAwsClusterRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateAwsClusterRequest`
        """
        model = astronomercoreapi.models.create_aws_cluster_request.CreateAwsClusterRequest()  # noqa: E501
        if include_optional :
            return CreateAwsClusterRequest(
                db_instance_type = '', 
                is_dry_run = True, 
                k8s_tags = [
                    astronomercoreapi.models.cluster_tag.ClusterTag(
                        key = '', 
                        value = '', )
                    ], 
                name = '', 
                node_pools = [
                    astronomercoreapi.models.create_node_pool_request.CreateNodePoolRequest(
                        is_default = True, 
                        max_node_count = 56, 
                        name = '', 
                        node_instance_type = '', )
                    ], 
                provider_account = '', 
                region = '', 
                template_version = '', 
                type = 'HOSTED', 
                vpc_subnet_range = ''
            )
        else :
            return CreateAwsClusterRequest(
                db_instance_type = '',
                name = '',
                region = '',
                template_version = '',
                type = 'HOSTED',
                vpc_subnet_range = '',
        )
        """

    def testCreateAwsClusterRequest(self):
        """Test CreateAwsClusterRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
