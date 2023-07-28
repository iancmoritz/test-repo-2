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
from pydantic import BaseModel, Field, StrictBool, StrictStr
from astronomerregistry.models.module_inherits_from import ModuleInheritsFrom
from astronomerregistry.models.type_def import TypeDef

class ModuleParameter(BaseModel):
    """
    ModuleParameter
    """
    default_value: Optional[StrictStr] = Field(None, alias="defaultValue")
    description: Optional[StrictStr] = None
    inherits_from: ModuleInheritsFrom = Field(..., alias="inheritsFrom")
    name: StrictStr = Field(...)
    required: StrictBool = Field(...)
    type: Optional[StrictStr] = None
    type_def: Optional[TypeDef] = Field(None, alias="typeDef")
    __properties = ["defaultValue", "description", "inheritsFrom", "name", "required", "type", "typeDef"]

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
    def from_json(cls, json_str: str) -> ModuleParameter:
        """Create an instance of ModuleParameter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of inherits_from
        if self.inherits_from:
            _dict['inheritsFrom'] = self.inherits_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type_def
        if self.type_def:
            _dict['typeDef'] = self.type_def.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModuleParameter:
        """Create an instance of ModuleParameter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ModuleParameter.parse_obj(obj)

        _obj = ModuleParameter.parse_obj({
            "default_value": obj.get("defaultValue"),
            "description": obj.get("description"),
            "inherits_from": ModuleInheritsFrom.from_dict(obj.get("inheritsFrom")) if obj.get("inheritsFrom") is not None else None,
            "name": obj.get("name"),
            "required": obj.get("required"),
            "type": obj.get("type"),
            "type_def": TypeDef.from_dict(obj.get("typeDef")) if obj.get("typeDef") is not None else None
        })
        return _obj

