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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class TypeDef(BaseModel):
    """
    TypeDef
    """
    annotation_type: Optional[StrictStr] = Field(None, alias="annotationType")
    raw_annotation: Optional[StrictStr] = Field(None, alias="rawAnnotation")
    type_variables: Optional[conlist(TypeDef)] = Field(None, alias="typeVariables")
    __properties = ["annotationType", "rawAnnotation", "typeVariables"]

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
    def from_json(cls, json_str: str) -> TypeDef:
        """Create an instance of TypeDef from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in type_variables (list)
        _items = []
        if self.type_variables:
            for _item in self.type_variables:
                if _item:
                    _items.append(_item.to_dict())
            _dict['typeVariables'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TypeDef:
        """Create an instance of TypeDef from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TypeDef.parse_obj(obj)

        _obj = TypeDef.parse_obj({
            "annotation_type": obj.get("annotationType"),
            "raw_annotation": obj.get("rawAnnotation"),
            "type_variables": [TypeDef.from_dict(_item) for _item in obj.get("typeVariables")] if obj.get("typeVariables") is not None else None
        })
        return _obj
