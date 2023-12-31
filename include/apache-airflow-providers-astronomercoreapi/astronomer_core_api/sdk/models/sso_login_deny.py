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

class SsoLoginDeny(BaseModel):
    """
    SsoLoginDeny
    """
    connections: Optional[conlist(StrictStr)] = None
    message: StrictStr = Field(...)
    reason: StrictStr = Field(...)
    __properties = ["connections", "message", "reason"]

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
    def from_json(cls, json_str: str) -> SsoLoginDeny:
        """Create an instance of SsoLoginDeny from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SsoLoginDeny:
        """Create an instance of SsoLoginDeny from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SsoLoginDeny.parse_obj(obj)

        _obj = SsoLoginDeny.parse_obj({
            "connections": obj.get("connections"),
            "message": obj.get("message"),
            "reason": obj.get("reason")
        })
        return _obj

