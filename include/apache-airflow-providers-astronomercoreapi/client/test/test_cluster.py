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
from astronomercoreapi.models.cluster import Cluster  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestCluster(unittest.TestCase):
    """Cluster unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Cluster
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Cluster`
        """
        model = astronomercoreapi.models.cluster.Cluster()  # noqa: E501
        if include_optional :
            return Cluster(
                applied_template_version = '', 
                cloud_provider = 'aws', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                db_instance_type = '', 
                deleted_at = '', 
                id = '', 
                is_cordoned = True, 
                is_dry_run = True, 
                is_limited = True, 
                k8s_tags = [
                    astronomercoreapi.models.cluster_tag.ClusterTag(
                        key = '', 
                        value = '', )
                    ], 
                metadata = astronomercoreapi.models.cluster_metadata.ClusterMetadata(
                    external_ips = [
                        ''
                        ], ), 
                name = '', 
                node_pools = [
                    astronomercoreapi.models.node_pool.NodePool(
                        cloud_provider = '', 
                        cluster_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        is_default = True, 
                        max_node_count = 56, 
                        name = '', 
                        node_instance_type = '', 
                        supported_astro_machines = [
                            ''
                            ], 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ], 
                organization_id = '', 
                pod_subnet_range = '', 
                provider_account = '', 
                region = '', 
                service_peering_range = '', 
                service_subnet_range = '', 
                status = 'CREATING', 
                template_url = '', 
                template_version = '', 
                temporal_run_id = '', 
                tenant_id = '', 
                type = 'HOSTED', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                vpc_subnet_range = '', 
                workspaces = [
                    ''
                    ]
            )
        else :
            return Cluster(
                applied_template_version = '',
                cloud_provider = 'aws',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                db_instance_type = '',
                id = '',
                is_dry_run = True,
                is_limited = True,
                k8s_tags = [
                    astronomercoreapi.models.cluster_tag.ClusterTag(
                        key = '', 
                        value = '', )
                    ],
                metadata = astronomercoreapi.models.cluster_metadata.ClusterMetadata(
                    external_ips = [
                        ''
                        ], ),
                name = '',
                node_pools = [
                    astronomercoreapi.models.node_pool.NodePool(
                        cloud_provider = '', 
                        cluster_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        is_default = True, 
                        max_node_count = 56, 
                        name = '', 
                        node_instance_type = '', 
                        supported_astro_machines = [
                            ''
                            ], 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                organization_id = '',
                pod_subnet_range = '',
                provider_account = '',
                region = '',
                service_peering_range = '',
                service_subnet_range = '',
                status = 'CREATING',
                template_url = '',
                template_version = '',
                temporal_run_id = '',
                tenant_id = '',
                type = 'HOSTED',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                vpc_subnet_range = '',
                workspaces = [
                    ''
                    ],
        )
        """

    def testCluster(self):
        """Test Cluster"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
