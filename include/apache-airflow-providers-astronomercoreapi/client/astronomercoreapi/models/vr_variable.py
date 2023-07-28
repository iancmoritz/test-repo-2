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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from astronomercoreapi.models.basic_subject_profile import BasicSubjectProfile

class VRVariable(BaseModel):
    """
    VRVariable
    """
    created_at: datetime = Field(..., alias="createdAt")
    created_by_user: BasicSubjectProfile = Field(..., alias="createdByUser")
    is_secret: StrictBool = Field(..., alias="isSecret")
    key: StrictStr = Field(...)
    updated_at: datetime = Field(..., alias="updatedAt")
    updated_by_user: BasicSubjectProfile = Field(..., alias="updatedByUser")
    value: Optional[StrictStr] = None
    __properties = ["createdAt", "createdByUser", "isSecret", "key", "updatedAt", "updatedByUser", "value"]

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
    def from_json(cls, json_str: str) -> VRVariable:
        """Create an instance of VRVariable from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of created_by_user
        if self.created_by_user:
            _dict['createdByUser'] = self.created_by_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_by_user
        if self.updated_by_user:
            _dict['updatedByUser'] = self.updated_by_user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VRVariable:
        """Create an instance of VRVariable from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VRVariable.parse_obj(obj)

        _obj = VRVariable.parse_obj({
            "created_at": obj.get("createdAt"),
            "created_by_user": BasicSubjectProfile.from_dict(obj.get("createdByUser")) if obj.get("createdByUser") is not None else None,
            "is_secret": obj.get("isSecret"),
            "key": obj.get("key"),
            "updated_at": obj.get("updatedAt"),
            "updated_by_user": BasicSubjectProfile.from_dict(obj.get("updatedByUser")) if obj.get("updatedByUser") is not None else None,
            "value": obj.get("value")
        })
        return _obj

