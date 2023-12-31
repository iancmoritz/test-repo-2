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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator
from astronomer_core_api.sdk.models.ctm_value import CtmValue


class CtmConfigDisplay(BaseModel):
    """
    CtmConfigDisplay
    """

    default: Optional[CtmValue] = None
    description: Optional[StrictStr] = None
    example: Optional[CtmValue] = None
    fixed_width_font: Optional[StrictBool] = Field(None, alias="fixedWidthFont")
    highlight_language: Optional[StrictStr] = Field(None, alias="highlightLanguage")
    label: Optional[StrictStr] = None
    num_lines: Optional[StrictInt] = Field(None, alias="numLines")
    raw_type: Optional[StrictStr] = Field(None, alias="rawType")
    __properties = [
        "default",
        "description",
        "example",
        "fixedWidthFont",
        "highlightLanguage",
        "label",
        "numLines",
        "rawType",
    ]

    @validator("highlight_language")
    def highlight_language_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("python", "sql", "js"):
            raise ValueError("must be one of enum values ('python', 'sql', 'js')")
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
    def from_json(cls, json_str: str) -> CtmConfigDisplay:
        """Create an instance of CtmConfigDisplay from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of default
        if self.default:
            _dict["default"] = self.default.to_dict()
        # override the default output from pydantic by calling `to_dict()` of example
        if self.example:
            _dict["example"] = self.example.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CtmConfigDisplay:
        """Create an instance of CtmConfigDisplay from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CtmConfigDisplay.parse_obj(obj)

        _obj = CtmConfigDisplay.parse_obj(
            {
                "default": CtmValue.from_dict(obj.get("default"))
                if obj.get("default") is not None
                else None,
                "description": obj.get("description"),
                "example": CtmValue.from_dict(obj.get("example"))
                if obj.get("example") is not None
                else None,
                "fixed_width_font": obj.get("fixedWidthFont"),
                "highlight_language": obj.get("highlightLanguage"),
                "label": obj.get("label"),
                "num_lines": obj.get("numLines"),
                "raw_type": obj.get("rawType"),
            }
        )
        return _obj
