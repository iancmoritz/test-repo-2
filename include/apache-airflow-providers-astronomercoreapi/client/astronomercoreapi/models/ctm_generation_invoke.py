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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist

class CtmGenerationInvoke(BaseModel):
    """
    CtmGenerationInvoke
    """
    exclude_task_id_arg: Optional[StrictBool] = Field(None, alias="excludeTaskIdArg")
    function_name: StrictStr = Field(..., alias="functionName")
    imports: Optional[conlist(StrictStr)] = None
    __properties = ["excludeTaskIdArg", "functionName", "imports"]

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
    def from_json(cls, json_str: str) -> CtmGenerationInvoke:
        """Create an instance of CtmGenerationInvoke from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CtmGenerationInvoke:
        """Create an instance of CtmGenerationInvoke from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CtmGenerationInvoke.parse_obj(obj)

        _obj = CtmGenerationInvoke.parse_obj({
            "exclude_task_id_arg": obj.get("excludeTaskIdArg"),
            "function_name": obj.get("functionName"),
            "imports": obj.get("imports")
        })
        return _obj

