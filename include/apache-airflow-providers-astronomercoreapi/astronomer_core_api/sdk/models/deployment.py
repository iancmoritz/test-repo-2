# coding: utf-8

"""
    Astro Core API

    Astro Core API  # noqa: E501

    The version of the OpenAPI document: v1alpha1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import (
    BaseModel,
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
    conlist,
    validator,
)
from astronomer_core_api.sdk.models.deployment_env_var import DeploymentEnvVar
from astronomer_core_api.sdk.models.deployment_worker_queue import DeploymentWorkerQueue


class Deployment(BaseModel):
    """
    Deployment
    """

    alert_emails: Optional[conlist(StrictStr)] = Field(None, alias="alertEmails")
    api_key_only_deployments: StrictBool = Field(..., alias="apiKeyOnlyDeployments")
    cluster_id: StrictStr = Field(..., alias="clusterId")
    created_at: datetime = Field(..., alias="createdAt")
    current_dag_tarball_version: Optional[StrictStr] = Field(
        None, alias="currentDagTarballVersion"
    )
    current_image_version: Optional[StrictStr] = Field(
        None, alias="currentImageVersion"
    )
    dag_deploy_enabled: StrictBool = Field(..., alias="dagDeployEnabled")
    description: Optional[StrictStr] = None
    desired_dag_tarball_version: Optional[StrictStr] = Field(
        None, alias="desiredDagTarballVersion"
    )
    environment_variables: Optional[conlist(DeploymentEnvVar)] = Field(
        None, alias="environmentVariables"
    )
    executor: Optional[StrictStr] = None
    external_ips: Optional[conlist(StrictStr)] = Field(None, alias="externalIPs")
    id: StrictStr = Field(...)
    image_id: StrictStr = Field(..., alias="imageId")
    image_repository: StrictStr = Field(..., alias="imageRepository")
    image_tag: StrictStr = Field(..., alias="imageTag")
    is_high_availability: StrictBool = Field(..., alias="isHighAvailability")
    name: StrictStr = Field(...)
    org_short_name: Optional[StrictStr] = Field(
        None,
        alias="orgShortName",
        description="Deprecated: orgShortName has been replaced with organizationShortName",
    )
    organization_id: StrictStr = Field(..., alias="organizationId")
    organization_name: StrictStr = Field(..., alias="organizationName")
    organization_short_name: StrictStr = Field(..., alias="organizationShortName")
    release_name: StrictStr = Field(..., alias="releaseName")
    runtime_version: StrictStr = Field(..., alias="runtimeVersion")
    scheduler_au: StrictInt = Field(..., alias="schedulerAu")
    scheduler_cpu: StrictStr = Field(..., alias="schedulerCpu")
    scheduler_memory: StrictStr = Field(..., alias="schedulerMemory")
    scheduler_replicas: StrictInt = Field(..., alias="schedulerReplicas")
    scheduler_size: Optional[StrictStr] = Field(None, alias="schedulerSize")
    spec_created_at: datetime = Field(..., alias="specCreatedAt")
    spec_updated_at: datetime = Field(..., alias="specUpdatedAt")
    status: StrictStr = Field(...)
    status_reason: Optional[StrictStr] = Field(None, alias="statusReason")
    type: Optional[StrictStr] = None
    updated_at: datetime = Field(..., alias="updatedAt")
    web_server_cpu: StrictStr = Field(..., alias="webServerCpu")
    web_server_ingress_hostname: StrictStr = Field(
        ..., alias="webServerIngressHostname"
    )
    web_server_memory: StrictStr = Field(..., alias="webServerMemory")
    web_server_replicas: Optional[StrictInt] = Field(None, alias="webServerReplicas")
    web_server_url: StrictStr = Field(..., alias="webServerUrl")
    worker_cpu: StrictStr = Field(..., alias="workerCpu")
    worker_memory: StrictStr = Field(..., alias="workerMemory")
    worker_queues: Optional[conlist(DeploymentWorkerQueue)] = Field(
        None, alias="workerQueues"
    )
    workers_au: StrictInt = Field(..., alias="workersAu")
    workers_replicas: Optional[StrictInt] = Field(None, alias="workersReplicas")
    workload_identity: Optional[StrictStr] = Field(None, alias="workloadIdentity")
    workspace_id: StrictStr = Field(..., alias="workspaceId")
    __properties = [
        "alertEmails",
        "apiKeyOnlyDeployments",
        "clusterId",
        "createdAt",
        "currentDagTarballVersion",
        "currentImageVersion",
        "dagDeployEnabled",
        "description",
        "desiredDagTarballVersion",
        "environmentVariables",
        "executor",
        "externalIPs",
        "id",
        "imageId",
        "imageRepository",
        "imageTag",
        "isHighAvailability",
        "name",
        "orgShortName",
        "organizationId",
        "organizationName",
        "organizationShortName",
        "releaseName",
        "runtimeVersion",
        "schedulerAu",
        "schedulerCpu",
        "schedulerMemory",
        "schedulerReplicas",
        "schedulerSize",
        "specCreatedAt",
        "specUpdatedAt",
        "status",
        "statusReason",
        "type",
        "updatedAt",
        "webServerCpu",
        "webServerIngressHostname",
        "webServerMemory",
        "webServerReplicas",
        "webServerUrl",
        "workerCpu",
        "workerMemory",
        "workerQueues",
        "workersAu",
        "workersReplicas",
        "workloadIdentity",
        "workspaceId",
    ]

    @validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ("HEALTHY", "UNHEALTHY", "UNKNOWN", "CREATING", "DEPLOYING"):
            raise ValueError(
                "must be one of enum values ('HEALTHY', 'UNHEALTHY', 'UNKNOWN', 'CREATING', 'DEPLOYING')"
            )
        return value

    @validator("type")
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("HYBRID", "HOSTED_DEDICATED", "HOSTED_SHARED"):
            raise ValueError(
                "must be one of enum values ('HYBRID', 'HOSTED_DEDICATED', 'HOSTED_SHARED')"
            )
        return value

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Deployment:
        """Create an instance of Deployment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in environment_variables (list)
        _items = []
        if self.environment_variables:
            for _item in self.environment_variables:
                if _item:
                    _items.append(_item.to_dict())
            _dict["environmentVariables"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in worker_queues (list)
        _items = []
        if self.worker_queues:
            for _item in self.worker_queues:
                if _item:
                    _items.append(_item.to_dict())
            _dict["workerQueues"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Deployment:
        """Create an instance of Deployment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Deployment.parse_obj(obj)

        _obj = Deployment.parse_obj(
            {
                "alert_emails": obj.get("alertEmails"),
                "api_key_only_deployments": obj.get("apiKeyOnlyDeployments"),
                "cluster_id": obj.get("clusterId"),
                "created_at": obj.get("createdAt"),
                "current_dag_tarball_version": obj.get("currentDagTarballVersion"),
                "current_image_version": obj.get("currentImageVersion"),
                "dag_deploy_enabled": obj.get("dagDeployEnabled"),
                "description": obj.get("description"),
                "desired_dag_tarball_version": obj.get("desiredDagTarballVersion"),
                "environment_variables": [
                    DeploymentEnvVar.from_dict(_item)
                    for _item in obj.get("environmentVariables")
                ]
                if obj.get("environmentVariables") is not None
                else None,
                "executor": obj.get("executor"),
                "external_ips": obj.get("externalIPs"),
                "id": obj.get("id"),
                "image_id": obj.get("imageId"),
                "image_repository": obj.get("imageRepository"),
                "image_tag": obj.get("imageTag"),
                "is_high_availability": obj.get("isHighAvailability"),
                "name": obj.get("name"),
                "org_short_name": obj.get("orgShortName"),
                "organization_id": obj.get("organizationId"),
                "organization_name": obj.get("organizationName"),
                "organization_short_name": obj.get("organizationShortName"),
                "release_name": obj.get("releaseName"),
                "runtime_version": obj.get("runtimeVersion"),
                "scheduler_au": obj.get("schedulerAu"),
                "scheduler_cpu": obj.get("schedulerCpu"),
                "scheduler_memory": obj.get("schedulerMemory"),
                "scheduler_replicas": obj.get("schedulerReplicas"),
                "scheduler_size": obj.get("schedulerSize"),
                "spec_created_at": obj.get("specCreatedAt"),
                "spec_updated_at": obj.get("specUpdatedAt"),
                "status": obj.get("status"),
                "status_reason": obj.get("statusReason"),
                "type": obj.get("type"),
                "updated_at": obj.get("updatedAt"),
                "web_server_cpu": obj.get("webServerCpu"),
                "web_server_ingress_hostname": obj.get("webServerIngressHostname"),
                "web_server_memory": obj.get("webServerMemory"),
                "web_server_replicas": obj.get("webServerReplicas"),
                "web_server_url": obj.get("webServerUrl"),
                "worker_cpu": obj.get("workerCpu"),
                "worker_memory": obj.get("workerMemory"),
                "worker_queues": [
                    DeploymentWorkerQueue.from_dict(_item)
                    for _item in obj.get("workerQueues")
                ]
                if obj.get("workerQueues") is not None
                else None,
                "workers_au": obj.get("workersAu"),
                "workers_replicas": obj.get("workersReplicas"),
                "workload_identity": obj.get("workloadIdentity"),
                "workspace_id": obj.get("workspaceId"),
            }
        )
        return _obj
