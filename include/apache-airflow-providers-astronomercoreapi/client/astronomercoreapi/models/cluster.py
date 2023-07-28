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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, validator
from astronomercoreapi.models.cluster_metadata import ClusterMetadata
from astronomercoreapi.models.cluster_tag import ClusterTag
from astronomercoreapi.models.node_pool import NodePool

class Cluster(BaseModel):
    """
    Cluster
    """
    applied_template_version: StrictStr = Field(..., alias="appliedTemplateVersion")
    cloud_provider: StrictStr = Field(..., alias="cloudProvider")
    created_at: datetime = Field(..., alias="createdAt")
    db_instance_type: StrictStr = Field(..., alias="dbInstanceType")
    deleted_at: Optional[StrictStr] = Field(None, alias="deletedAt")
    id: StrictStr = Field(...)
    is_cordoned: Optional[StrictBool] = Field(None, alias="isCordoned")
    is_dry_run: StrictBool = Field(..., alias="isDryRun")
    is_limited: StrictBool = Field(..., alias="isLimited")
    k8s_tags: conlist(ClusterTag) = Field(..., alias="k8sTags")
    metadata: ClusterMetadata = Field(...)
    name: StrictStr = Field(...)
    node_pools: conlist(NodePool) = Field(..., alias="nodePools")
    organization_id: StrictStr = Field(..., alias="organizationId")
    pod_subnet_range: StrictStr = Field(..., alias="podSubnetRange")
    provider_account: StrictStr = Field(..., alias="providerAccount")
    region: StrictStr = Field(...)
    service_peering_range: StrictStr = Field(..., alias="servicePeeringRange")
    service_subnet_range: StrictStr = Field(..., alias="serviceSubnetRange")
    status: StrictStr = Field(...)
    template_url: StrictStr = Field(..., alias="templateUrl")
    template_version: StrictStr = Field(..., alias="templateVersion")
    temporal_run_id: StrictStr = Field(..., alias="temporalRunId")
    tenant_id: StrictStr = Field(..., alias="tenantId")
    type: StrictStr = Field(...)
    updated_at: datetime = Field(..., alias="updatedAt")
    vpc_subnet_range: StrictStr = Field(..., alias="vpcSubnetRange")
    workspaces: conlist(StrictStr) = Field(...)
    __properties = ["appliedTemplateVersion", "cloudProvider", "createdAt", "dbInstanceType", "deletedAt", "id", "isCordoned", "isDryRun", "isLimited", "k8sTags", "metadata", "name", "nodePools", "organizationId", "podSubnetRange", "providerAccount", "region", "servicePeeringRange", "serviceSubnetRange", "status", "templateUrl", "templateVersion", "temporalRunId", "tenantId", "type", "updatedAt", "vpcSubnetRange", "workspaces"]

    @validator('cloud_provider')
    def cloud_provider_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('aws', 'gcp', 'azure'):
            raise ValueError("must be one of enum values ('aws', 'gcp', 'azure')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CREATING', 'CREATED', 'CREATE_FAILED', 'UPDATING', 'DELETING', 'DELETED', 'DELETE_FAILED', 'FORCE_DELETED'):
            raise ValueError("must be one of enum values ('CREATING', 'CREATED', 'CREATE_FAILED', 'UPDATING', 'DELETING', 'DELETED', 'DELETE_FAILED', 'FORCE_DELETED')")
        return value

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('HOSTED', 'BRING_YOUR_OWN_CLOUD', 'VIRTUAL_RUNTIMES', 'SHARED'):
            raise ValueError("must be one of enum values ('HOSTED', 'BRING_YOUR_OWN_CLOUD', 'VIRTUAL_RUNTIMES', 'SHARED')")
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
    def from_json(cls, json_str: str) -> Cluster:
        """Create an instance of Cluster from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in k8s_tags (list)
        _items = []
        if self.k8s_tags:
            for _item in self.k8s_tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['k8sTags'] = _items
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in node_pools (list)
        _items = []
        if self.node_pools:
            for _item in self.node_pools:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nodePools'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Cluster:
        """Create an instance of Cluster from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Cluster.parse_obj(obj)

        _obj = Cluster.parse_obj({
            "applied_template_version": obj.get("appliedTemplateVersion"),
            "cloud_provider": obj.get("cloudProvider"),
            "created_at": obj.get("createdAt"),
            "db_instance_type": obj.get("dbInstanceType"),
            "deleted_at": obj.get("deletedAt"),
            "id": obj.get("id"),
            "is_cordoned": obj.get("isCordoned"),
            "is_dry_run": obj.get("isDryRun"),
            "is_limited": obj.get("isLimited"),
            "k8s_tags": [ClusterTag.from_dict(_item) for _item in obj.get("k8sTags")] if obj.get("k8sTags") is not None else None,
            "metadata": ClusterMetadata.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "name": obj.get("name"),
            "node_pools": [NodePool.from_dict(_item) for _item in obj.get("nodePools")] if obj.get("nodePools") is not None else None,
            "organization_id": obj.get("organizationId"),
            "pod_subnet_range": obj.get("podSubnetRange"),
            "provider_account": obj.get("providerAccount"),
            "region": obj.get("region"),
            "service_peering_range": obj.get("servicePeeringRange"),
            "service_subnet_range": obj.get("serviceSubnetRange"),
            "status": obj.get("status"),
            "template_url": obj.get("templateUrl"),
            "template_version": obj.get("templateVersion"),
            "temporal_run_id": obj.get("temporalRunId"),
            "tenant_id": obj.get("tenantId"),
            "type": obj.get("type"),
            "updated_at": obj.get("updatedAt"),
            "vpc_subnet_range": obj.get("vpcSubnetRange"),
            "workspaces": obj.get("workspaces")
        })
        return _obj

