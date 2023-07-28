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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class VirtualRuntimeImportError(BaseModel):
    """
    VirtualRuntimeImportError
    """
    filename: Optional[StrictStr] = None
    import_error_id: StrictInt = Field(..., alias="importErrorId")
    stack_trace: Optional[StrictStr] = Field(None, alias="stackTrace")
    timestamp: Optional[StrictStr] = None
    __properties = ["filename", "importErrorId", "stackTrace", "timestamp"]

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
    def from_json(cls, json_str: str) -> VirtualRuntimeImportError:
        """Create an instance of VirtualRuntimeImportError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VirtualRuntimeImportError:
        """Create an instance of VirtualRuntimeImportError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VirtualRuntimeImportError.parse_obj(obj)

        _obj = VirtualRuntimeImportError.parse_obj({
            "filename": obj.get("filename"),
            "import_error_id": obj.get("importErrorId"),
            "stack_trace": obj.get("stackTrace"),
            "timestamp": obj.get("timestamp")
        })
        return _obj

