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


from typing import List
from pydantic import BaseModel, Field, StrictInt, conlist
from astronomer_core_api.sdk.models.runtime import Runtime


class RuntimesPaginated(BaseModel):
    """
    RuntimesPaginated
    """

    limit: StrictInt = Field(...)
    offset: StrictInt = Field(...)
    runtimes: conlist(Runtime) = Field(...)
    total_count: StrictInt = Field(..., alias="totalCount")
    __properties = ["limit", "offset", "runtimes", "totalCount"]

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
    def from_json(cls, json_str: str) -> RuntimesPaginated:
        """Create an instance of RuntimesPaginated from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in runtimes (list)
        _items = []
        if self.runtimes:
            for _item in self.runtimes:
                if _item:
                    _items.append(_item.to_dict())
            _dict["runtimes"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RuntimesPaginated:
        """Create an instance of RuntimesPaginated from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RuntimesPaginated.parse_obj(obj)

        _obj = RuntimesPaginated.parse_obj(
            {
                "limit": obj.get("limit"),
                "offset": obj.get("offset"),
                "runtimes": [Runtime.from_dict(_item) for _item in obj.get("runtimes")]
                if obj.get("runtimes") is not None
                else None,
                "total_count": obj.get("totalCount"),
            }
        )
        return _obj