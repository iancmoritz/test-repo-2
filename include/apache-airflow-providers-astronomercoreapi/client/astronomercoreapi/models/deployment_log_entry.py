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


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator

class DeploymentLogEntry(BaseModel):
    """
    DeploymentLogEntry
    """
    raw: StrictStr = Field(...)
    source: StrictStr = Field(...)
    timestamp: Union[StrictFloat, StrictInt] = Field(...)
    __properties = ["raw", "source", "timestamp"]

    @validator('source')
    def source_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('scheduler', 'webserver', 'triggerer', 'worker'):
            raise ValueError("must be one of enum values ('scheduler', 'webserver', 'triggerer', 'worker')")
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
    def from_json(cls, json_str: str) -> DeploymentLogEntry:
        """Create an instance of DeploymentLogEntry from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeploymentLogEntry:
        """Create an instance of DeploymentLogEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeploymentLogEntry.parse_obj(obj)

        _obj = DeploymentLogEntry.parse_obj({
            "raw": obj.get("raw"),
            "source": obj.get("source"),
            "timestamp": obj.get("timestamp")
        })
        return _obj
