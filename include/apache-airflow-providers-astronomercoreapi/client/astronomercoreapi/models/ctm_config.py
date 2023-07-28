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
from astronomercoreapi.models.ctm_config_applicability import CtmConfigApplicability
from astronomercoreapi.models.ctm_config_display import CtmConfigDisplay
from astronomercoreapi.models.ctm_config_generation import CtmConfigGeneration
from astronomercoreapi.models.ctm_config_validity import CtmConfigValidity

class CtmConfig(BaseModel):
    """
    CtmConfig
    """
    applicability: Optional[CtmConfigApplicability] = None
    data_type: StrictStr = Field(..., alias="dataType")
    display: Optional[CtmConfigDisplay] = None
    generation: Optional[CtmConfigGeneration] = None
    key: StrictStr = Field(...)
    validity: Optional[CtmConfigValidity] = None
    __properties = ["applicability", "dataType", "display", "generation", "key", "validity"]

    @validator('data_type')
    def data_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('string', 'stringList', 'stringMap', 'stringListMap', 'stringMapList', 'stringSet', 'boolean', 'integer', 'float', 'duration', 'table', 'file', 'unsupported'):
            raise ValueError("must be one of enum values ('string', 'stringList', 'stringMap', 'stringListMap', 'stringMapList', 'stringSet', 'boolean', 'integer', 'float', 'duration', 'table', 'file', 'unsupported')")
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
    def from_json(cls, json_str: str) -> CtmConfig:
        """Create an instance of CtmConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of applicability
        if self.applicability:
            _dict['applicability'] = self.applicability.to_dict()
        # override the default output from pydantic by calling `to_dict()` of display
        if self.display:
            _dict['display'] = self.display.to_dict()
        # override the default output from pydantic by calling `to_dict()` of generation
        if self.generation:
            _dict['generation'] = self.generation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity
        if self.validity:
            _dict['validity'] = self.validity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CtmConfig:
        """Create an instance of CtmConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CtmConfig.parse_obj(obj)

        _obj = CtmConfig.parse_obj({
            "applicability": CtmConfigApplicability.from_dict(obj.get("applicability")) if obj.get("applicability") is not None else None,
            "data_type": obj.get("dataType"),
            "display": CtmConfigDisplay.from_dict(obj.get("display")) if obj.get("display") is not None else None,
            "generation": CtmConfigGeneration.from_dict(obj.get("generation")) if obj.get("generation") is not None else None,
            "key": obj.get("key"),
            "validity": CtmConfigValidity.from_dict(obj.get("validity")) if obj.get("validity") is not None else None
        })
        return _obj
