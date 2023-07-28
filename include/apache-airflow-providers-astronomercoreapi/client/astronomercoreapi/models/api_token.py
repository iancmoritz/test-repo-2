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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from astronomercoreapi.models.api_token_role import ApiTokenRole
from astronomercoreapi.models.basic_subject_profile import BasicSubjectProfile

class ApiToken(BaseModel):
    """
    ApiToken
    """
    created_at: datetime = Field(..., alias="createdAt")
    created_by: Optional[BasicSubjectProfile] = Field(None, alias="createdBy")
    created_by_id: StrictStr = Field(..., alias="createdById")
    deleted_at: Optional[datetime] = Field(None, alias="deletedAt")
    description: StrictStr = Field(...)
    end_at: Optional[datetime] = Field(None, alias="endAt")
    expiry_period_in_days: StrictInt = Field(..., alias="expiryPeriodInDays")
    id: StrictStr = Field(...)
    last_used_at: Optional[datetime] = Field(None, alias="lastUsedAt")
    name: StrictStr = Field(...)
    roles: conlist(ApiTokenRole) = Field(...)
    short_token: StrictStr = Field(..., alias="shortToken")
    start_at: datetime = Field(..., alias="startAt")
    token: Optional[StrictStr] = None
    type: StrictStr = Field(...)
    updated_at: datetime = Field(..., alias="updatedAt")
    updated_by: Optional[BasicSubjectProfile] = Field(None, alias="updatedBy")
    updated_by_id: StrictStr = Field(..., alias="updatedById")
    __properties = ["createdAt", "createdBy", "createdById", "deletedAt", "description", "endAt", "expiryPeriodInDays", "id", "lastUsedAt", "name", "roles", "shortToken", "startAt", "token", "type", "updatedAt", "updatedBy", "updatedById"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('WORKSPACE', 'ORGANIZATION'):
            raise ValueError("must be one of enum values ('WORKSPACE', 'ORGANIZATION')")
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
    def from_json(cls, json_str: str) -> ApiToken:
        """Create an instance of ApiToken from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roles'] = _items
        # override the default output from pydantic by calling `to_dict()` of updated_by
        if self.updated_by:
            _dict['updatedBy'] = self.updated_by.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiToken:
        """Create an instance of ApiToken from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiToken.parse_obj(obj)

        _obj = ApiToken.parse_obj({
            "created_at": obj.get("createdAt"),
            "created_by": BasicSubjectProfile.from_dict(obj.get("createdBy")) if obj.get("createdBy") is not None else None,
            "created_by_id": obj.get("createdById"),
            "deleted_at": obj.get("deletedAt"),
            "description": obj.get("description"),
            "end_at": obj.get("endAt"),
            "expiry_period_in_days": obj.get("expiryPeriodInDays"),
            "id": obj.get("id"),
            "last_used_at": obj.get("lastUsedAt"),
            "name": obj.get("name"),
            "roles": [ApiTokenRole.from_dict(_item) for _item in obj.get("roles")] if obj.get("roles") is not None else None,
            "short_token": obj.get("shortToken"),
            "start_at": obj.get("startAt"),
            "token": obj.get("token"),
            "type": obj.get("type"),
            "updated_at": obj.get("updatedAt"),
            "updated_by": BasicSubjectProfile.from_dict(obj.get("updatedBy")) if obj.get("updatedBy") is not None else None,
            "updated_by_id": obj.get("updatedById")
        })
        return _obj

