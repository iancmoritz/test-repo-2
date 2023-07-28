# coding: utf-8

"""
    Astro Registry API

    Astro Registry API  # noqa: E501

    The version of the OpenAPI document: v1alpha1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class TaskDependency(BaseModel):
    """
    TaskDependency
    """
    operator: StrictStr = Field(...)
    provider: Optional[StrictStr] = Field(None, description="May not exist in DB")
    version: Optional[StrictStr] = Field(None, description="May not exist in DB")
    __properties = ["operator", "provider", "version"]

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
    def from_json(cls, json_str: str) -> TaskDependency:
        """Create an instance of TaskDependency from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaskDependency:
        """Create an instance of TaskDependency from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaskDependency.parse_obj(obj)

        _obj = TaskDependency.parse_obj({
            "operator": obj.get("operator"),
            "provider": obj.get("provider"),
            "version": obj.get("version")
        })
        return _obj

