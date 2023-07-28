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
from astronomercoreapi.models.deployments_paginated import DeploymentsPaginated  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestDeploymentsPaginated(unittest.TestCase):
    """DeploymentsPaginated unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeploymentsPaginated
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeploymentsPaginated`
        """
        model = astronomercoreapi.models.deployments_paginated.DeploymentsPaginated()  # noqa: E501
        if include_optional :
            return DeploymentsPaginated(
                deployments = [
                    astronomercoreapi.models.deployment.Deployment(
                        alert_emails = [
                            ''
                            ], 
                        api_key_only_deployments = True, 
                        cluster_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        current_dag_tarball_version = '', 
                        current_image_version = '', 
                        dag_deploy_enabled = True, 
                        description = '', 
                        desired_dag_tarball_version = '', 
                        environment_variables = [
                            astronomercoreapi.models.deployment_env_var.DeploymentEnvVar(
                                is_secret = True, 
                                key = '', 
                                updated_at = '', 
                                value = '', )
                            ], 
                        executor = '', 
                        external_ips = [
                            ''
                            ], 
                        id = '', 
                        image_id = '', 
                        image_repository = '', 
                        image_tag = '', 
                        is_high_availability = True, 
                        name = '', 
                        org_short_name = '', 
                        organization_id = '', 
                        organization_name = '', 
                        organization_short_name = '', 
                        release_name = '', 
                        runtime_version = '', 
                        scheduler_au = 56, 
                        scheduler_cpu = '', 
                        scheduler_memory = '', 
                        scheduler_replicas = 56, 
                        scheduler_size = '', 
                        spec_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        spec_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = 'HEALTHY', 
                        status_reason = '', 
                        type = 'HYBRID', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        web_server_cpu = '', 
                        web_server_ingress_hostname = '', 
                        web_server_memory = '', 
                        web_server_replicas = 56, 
                        web_server_url = '', 
                        worker_cpu = '', 
                        worker_memory = '', 
                        worker_queues = [
                            astronomercoreapi.models.deployment_worker_queue.DeploymentWorkerQueue(
                                id = '', 
                                is_default = True, 
                                max_worker_count = 56, 
                                min_worker_count = 56, 
                                name = '', 
                                node_pool_id = '', 
                                pod_cpu = '', 
                                pod_ram = '', 
                                pod_size = '', 
                                worker_concurrency = 56, )
                            ], 
                        workers_au = 56, 
                        workers_replicas = 56, 
                        workload_identity = '', 
                        workspace_id = '', )
                    ], 
                limit = 56, 
                offset = 56, 
                total_count = 56
            )
        else :
            return DeploymentsPaginated(
                deployments = [
                    astronomercoreapi.models.deployment.Deployment(
                        alert_emails = [
                            ''
                            ], 
                        api_key_only_deployments = True, 
                        cluster_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        current_dag_tarball_version = '', 
                        current_image_version = '', 
                        dag_deploy_enabled = True, 
                        description = '', 
                        desired_dag_tarball_version = '', 
                        environment_variables = [
                            astronomercoreapi.models.deployment_env_var.DeploymentEnvVar(
                                is_secret = True, 
                                key = '', 
                                updated_at = '', 
                                value = '', )
                            ], 
                        executor = '', 
                        external_ips = [
                            ''
                            ], 
                        id = '', 
                        image_id = '', 
                        image_repository = '', 
                        image_tag = '', 
                        is_high_availability = True, 
                        name = '', 
                        org_short_name = '', 
                        organization_id = '', 
                        organization_name = '', 
                        organization_short_name = '', 
                        release_name = '', 
                        runtime_version = '', 
                        scheduler_au = 56, 
                        scheduler_cpu = '', 
                        scheduler_memory = '', 
                        scheduler_replicas = 56, 
                        scheduler_size = '', 
                        spec_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        spec_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = 'HEALTHY', 
                        status_reason = '', 
                        type = 'HYBRID', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        web_server_cpu = '', 
                        web_server_ingress_hostname = '', 
                        web_server_memory = '', 
                        web_server_replicas = 56, 
                        web_server_url = '', 
                        worker_cpu = '', 
                        worker_memory = '', 
                        worker_queues = [
                            astronomercoreapi.models.deployment_worker_queue.DeploymentWorkerQueue(
                                id = '', 
                                is_default = True, 
                                max_worker_count = 56, 
                                min_worker_count = 56, 
                                name = '', 
                                node_pool_id = '', 
                                pod_cpu = '', 
                                pod_ram = '', 
                                pod_size = '', 
                                worker_concurrency = 56, )
                            ], 
                        workers_au = 56, 
                        workers_replicas = 56, 
                        workload_identity = '', 
                        workspace_id = '', )
                    ],
                limit = 56,
                offset = 56,
                total_count = 56,
        )
        """

    def testDeploymentsPaginated(self):
        """Test DeploymentsPaginated"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()