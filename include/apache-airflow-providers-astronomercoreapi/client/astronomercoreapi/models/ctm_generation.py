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
from pydantic import BaseModel, Field, StrictStr, validator
from astronomercoreapi.models.ctm_generation_decorator import CtmGenerationDecorator
from astronomercoreapi.models.ctm_generation_invoke import CtmGenerationInvoke

class CtmGeneration(BaseModel):
    """
    CtmGeneration
    """
    decorator: Optional[CtmGenerationDecorator] = None
    invoke: Optional[CtmGenerationInvoke] = None
    type: StrictStr = Field(...)
    __properties = ["decorator", "invoke", "type"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('invoke', 'decorator'):
            raise ValueError("must be one of enum values ('invoke', 'decorator')")
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
    def from_json(cls, json_str: str) -> CtmGeneration:
        """Create an instance of CtmGeneration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of decorator
        if self.decorator:
            _dict['decorator'] = self.decorator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of invoke
        if self.invoke:
            _dict['invoke'] = self.invoke.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CtmGeneration:
        """Create an instance of CtmGeneration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CtmGeneration.parse_obj(obj)

        _obj = CtmGeneration.parse_obj({
            "decorator": CtmGenerationDecorator.from_dict(obj.get("decorator")) if obj.get("decorator") is not None else None,
            "invoke": CtmGenerationInvoke.from_dict(obj.get("invoke")) if obj.get("invoke") is not None else None,
            "type": obj.get("type")
        })
        return _obj
