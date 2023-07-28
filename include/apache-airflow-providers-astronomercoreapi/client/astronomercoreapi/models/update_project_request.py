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
from astronomercoreapi.models.update_project_connection_request import UpdateProjectConnectionRequest
from astronomercoreapi.models.update_project_git_request import UpdateProjectGitRequest
from astronomercoreapi.models.update_project_include_request import UpdateProjectIncludeRequest
from astronomercoreapi.models.update_project_variable_request import UpdateProjectVariableRequest

class UpdateProjectRequest(BaseModel):
    """
    UpdateProjectRequest
    """
    connections: Optional[conlist(UpdateProjectConnectionRequest)] = None
    description: Optional[StrictStr] = None
    git: Optional[UpdateProjectGitRequest] = None
    includes: Optional[conlist(UpdateProjectIncludeRequest, max_items=1)] = None
    name: StrictStr = Field(...)
    requirements: Optional[conlist(StrictStr)] = None
    variables: Optional[conlist(UpdateProjectVariableRequest)] = None
    __properties = ["connections", "description", "git", "includes", "name", "requirements", "variables"]

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
    def from_json(cls, json_str: str) -> UpdateProjectRequest:
        """Create an instance of UpdateProjectRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in connections (list)
        _items = []
        if self.connections:
            for _item in self.connections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['connections'] = _items
        # override the default output from pydantic by calling `to_dict()` of git
        if self.git:
            _dict['git'] = self.git.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in includes (list)
        _items = []
        if self.includes:
            for _item in self.includes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['includes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in variables (list)
        _items = []
        if self.variables:
            for _item in self.variables:
                if _item:
                    _items.append(_item.to_dict())
            _dict['variables'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateProjectRequest:
        """Create an instance of UpdateProjectRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateProjectRequest.parse_obj(obj)

        _obj = UpdateProjectRequest.parse_obj({
            "connections": [UpdateProjectConnectionRequest.from_dict(_item) for _item in obj.get("connections")] if obj.get("connections") is not None else None,
            "description": obj.get("description"),
            "git": UpdateProjectGitRequest.from_dict(obj.get("git")) if obj.get("git") is not None else None,
            "includes": [UpdateProjectIncludeRequest.from_dict(_item) for _item in obj.get("includes")] if obj.get("includes") is not None else None,
            "name": obj.get("name"),
            "requirements": obj.get("requirements"),
            "variables": [UpdateProjectVariableRequest.from_dict(_item) for _item in obj.get("variables")] if obj.get("variables") is not None else None
        })
        return _obj
