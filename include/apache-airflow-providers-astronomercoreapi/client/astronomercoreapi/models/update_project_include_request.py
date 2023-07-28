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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class UpdateProjectIncludeRequest(BaseModel):
    """
    UpdateProjectIncludeRequest
    """
    auto_sync_disabled: Optional[StrictBool] = Field(None, alias="autoSyncDisabled")
    name: StrictStr = Field(...)
    type: StrictStr = Field(...)
    __properties = ["autoSyncDisabled", "name", "type"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('project-git'):
            raise ValueError("must be one of enum values ('project-git')")
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
    def from_json(cls, json_str: str) -> UpdateProjectIncludeRequest:
        """Create an instance of UpdateProjectIncludeRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateProjectIncludeRequest:
        """Create an instance of UpdateProjectIncludeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateProjectIncludeRequest.parse_obj(obj)

        _obj = UpdateProjectIncludeRequest.parse_obj({
            "auto_sync_disabled": obj.get("autoSyncDisabled"),
            "name": obj.get("name"),
            "type": obj.get("type")
        })
        return _obj

