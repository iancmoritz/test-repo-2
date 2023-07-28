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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class MutateVirtualRuntimeRequest(BaseModel):
    """
    MutateVirtualRuntimeRequest
    """
    description: Optional[StrictStr] = None
    name: StrictStr = Field(...)
    task_mem_gib: Union[StrictFloat, StrictInt] = Field(..., alias="taskMemGib")
    __properties = ["description", "name", "taskMemGib"]

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
    def from_json(cls, json_str: str) -> MutateVirtualRuntimeRequest:
        """Create an instance of MutateVirtualRuntimeRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MutateVirtualRuntimeRequest:
        """Create an instance of MutateVirtualRuntimeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MutateVirtualRuntimeRequest.parse_obj(obj)

        _obj = MutateVirtualRuntimeRequest.parse_obj({
            "description": obj.get("description"),
            "name": obj.get("name"),
            "task_mem_gib": obj.get("taskMemGib")
        })
        return _obj

