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


from pydantic import BaseModel, Field
from astronomer_core_api.sdk.models.permission_request import PermissionRequest
from astronomer_core_api.sdk.models.scope_request import ScopeRequest


class PermissionCheckRequest(BaseModel):
    """
    PermissionCheckRequest
    """

    permission: PermissionRequest = Field(...)
    scope: ScopeRequest = Field(...)
    __properties = ["permission", "scope"]

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
    def from_json(cls, json_str: str) -> PermissionCheckRequest:
        """Create an instance of PermissionCheckRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of permission
        if self.permission:
            _dict["permission"] = self.permission.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scope
        if self.scope:
            _dict["scope"] = self.scope.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PermissionCheckRequest:
        """Create an instance of PermissionCheckRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PermissionCheckRequest.parse_obj(obj)

        _obj = PermissionCheckRequest.parse_obj(
            {
                "permission": PermissionRequest.from_dict(obj.get("permission"))
                if obj.get("permission") is not None
                else None,
                "scope": ScopeRequest.from_dict(obj.get("scope"))
                if obj.get("scope") is not None
                else None,
            }
        )
        return _obj
