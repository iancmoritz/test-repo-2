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


from typing import List
from pydantic import BaseModel, Field, StrictInt, conlist
from astronomerregistry.models.label import Label

class LabelsPaginated(BaseModel):
    """
    LabelsPaginated
    """
    labels: conlist(Label) = Field(...)
    limit: StrictInt = Field(...)
    offset: StrictInt = Field(...)
    total_count: StrictInt = Field(..., alias="totalCount")
    __properties = ["labels", "limit", "offset", "totalCount"]

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
    def from_json(cls, json_str: str) -> LabelsPaginated:
        """Create an instance of LabelsPaginated from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item in self.labels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['labels'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LabelsPaginated:
        """Create an instance of LabelsPaginated from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LabelsPaginated.parse_obj(obj)

        _obj = LabelsPaginated.parse_obj({
            "labels": [Label.from_dict(_item) for _item in obj.get("labels")] if obj.get("labels") is not None else None,
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "total_count": obj.get("totalCount")
        })
        return _obj
