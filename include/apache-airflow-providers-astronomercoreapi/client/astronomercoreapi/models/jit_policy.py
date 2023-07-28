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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from astronomercoreapi.models.workspace_role import WorkspaceRole

class JitPolicy(BaseModel):
    """
    JitPolicy
    """
    default_org_role: StrictStr = Field(..., alias="defaultOrgRole")
    default_workspace_roles: Optional[conlist(WorkspaceRole)] = Field(None, alias="defaultWorkspaceRoles")
    __properties = ["defaultOrgRole", "defaultWorkspaceRoles"]

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
    def from_json(cls, json_str: str) -> JitPolicy:
        """Create an instance of JitPolicy from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in default_workspace_roles (list)
        _items = []
        if self.default_workspace_roles:
            for _item in self.default_workspace_roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['defaultWorkspaceRoles'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JitPolicy:
        """Create an instance of JitPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JitPolicy.parse_obj(obj)

        _obj = JitPolicy.parse_obj({
            "default_org_role": obj.get("defaultOrgRole"),
            "default_workspace_roles": [WorkspaceRole.from_dict(_item) for _item in obj.get("defaultWorkspaceRoles")] if obj.get("defaultWorkspaceRoles") is not None else None
        })
        return _obj
