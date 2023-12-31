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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class CellCache(BaseModel):
    """
    CellCache
    """
    applicable: StrictBool = Field(...)
    available: Optional[StrictBool] = None
    dirty: Optional[StrictBool] = None
    dirty_reason: Optional[StrictStr] = Field(None, alias="dirtyReason")
    updated_at: Optional[StrictStr] = Field(None, alias="updatedAt")
    __properties = ["applicable", "available", "dirty", "dirtyReason", "updatedAt"]

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
    def from_json(cls, json_str: str) -> CellCache:
        """Create an instance of CellCache from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CellCache:
        """Create an instance of CellCache from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CellCache.parse_obj(obj)

        _obj = CellCache.parse_obj({
            "applicable": obj.get("applicable"),
            "available": obj.get("available"),
            "dirty": obj.get("dirty"),
            "dirty_reason": obj.get("dirtyReason"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj

