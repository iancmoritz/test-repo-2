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
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from astronomercoreapi.models.basic_subject_profile import BasicSubjectProfile

class Workspace(BaseModel):
    """
    Workspace
    """
    api_key_only_deployments_default: StrictBool = Field(..., alias="apiKeyOnlyDeploymentsDefault")
    created_at: datetime = Field(..., alias="createdAt")
    created_by: Optional[BasicSubjectProfile] = Field(None, alias="createdBy")
    deployment_count: Optional[StrictInt] = Field(None, alias="deploymentCount")
    description: Optional[StrictStr] = None
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    org_short_name: Optional[StrictStr] = Field(None, alias="orgShortName", description="Deprecated: orgShortName has been replaced with organizationShortName")
    organization_id: StrictStr = Field(..., alias="organizationId")
    organization_name: Optional[StrictStr] = Field(None, alias="organizationName")
    organization_short_name: Optional[StrictStr] = Field(None, alias="organizationShortName")
    serverless_runtime_count: Optional[StrictInt] = Field(None, alias="serverlessRuntimeCount")
    updated_at: datetime = Field(..., alias="updatedAt")
    updated_by: Optional[BasicSubjectProfile] = Field(None, alias="updatedBy")
    user_count: Optional[StrictInt] = Field(None, alias="userCount")
    __properties = ["apiKeyOnlyDeploymentsDefault", "createdAt", "createdBy", "deploymentCount", "description", "id", "name", "orgShortName", "organizationId", "organizationName", "organizationShortName", "serverlessRuntimeCount", "updatedAt", "updatedBy", "userCount"]

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
    def from_json(cls, json_str: str) -> Workspace:
        """Create an instance of Workspace from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_by
        if self.updated_by:
            _dict['updatedBy'] = self.updated_by.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Workspace:
        """Create an instance of Workspace from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Workspace.parse_obj(obj)

        _obj = Workspace.parse_obj({
            "api_key_only_deployments_default": obj.get("apiKeyOnlyDeploymentsDefault"),
            "created_at": obj.get("createdAt"),
            "created_by": BasicSubjectProfile.from_dict(obj.get("createdBy")) if obj.get("createdBy") is not None else None,
            "deployment_count": obj.get("deploymentCount"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "org_short_name": obj.get("orgShortName"),
            "organization_id": obj.get("organizationId"),
            "organization_name": obj.get("organizationName"),
            "organization_short_name": obj.get("organizationShortName"),
            "serverless_runtime_count": obj.get("serverlessRuntimeCount"),
            "updated_at": obj.get("updatedAt"),
            "updated_by": BasicSubjectProfile.from_dict(obj.get("updatedBy")) if obj.get("updatedBy") is not None else None,
            "user_count": obj.get("userCount")
        })
        return _obj

