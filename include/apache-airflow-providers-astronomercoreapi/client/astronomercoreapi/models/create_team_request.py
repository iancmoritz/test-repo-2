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

class CreateTeamRequest(BaseModel):
    """
    CreateTeamRequest
    """
    description: Optional[StrictStr] = None
    member_ids: Optional[conlist(StrictStr)] = Field(None, alias="memberIds")
    name: StrictStr = Field(...)
    organization_role: Optional[StrictStr] = Field(None, alias="organizationRole")
    __properties = ["description", "memberIds", "name", "organizationRole"]

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
    def from_json(cls, json_str: str) -> CreateTeamRequest:
        """Create an instance of CreateTeamRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateTeamRequest:
        """Create an instance of CreateTeamRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateTeamRequest.parse_obj(obj)

        _obj = CreateTeamRequest.parse_obj({
            "description": obj.get("description"),
            "member_ids": obj.get("memberIds"),
            "name": obj.get("name"),
            "organization_role": obj.get("organizationRole")
        })
        return _obj

