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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr, conlist

class EventUser(BaseModel):
    """
    EventUser
    """
    app_metadata: Optional[Dict[str, Any]] = None
    created_at: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    email_verified: Optional[StrictBool] = None
    family_name: Optional[StrictStr] = None
    given_name: Optional[StrictStr] = None
    identities: Optional[conlist(Dict[str, Any])] = None
    last_password_reset: Optional[StrictStr] = None
    multifactor: Optional[conlist(StrictStr)] = None
    name: Optional[StrictStr] = None
    nickname: Optional[StrictStr] = None
    phone_number: Optional[StrictStr] = None
    phone_verified: Optional[StrictBool] = None
    picture: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    user_id: Optional[StrictStr] = None
    user_metadata: Optional[Dict[str, Any]] = None
    username: Optional[StrictStr] = None
    __properties = ["app_metadata", "created_at", "email", "email_verified", "family_name", "given_name", "identities", "last_password_reset", "multifactor", "name", "nickname", "phone_number", "phone_verified", "picture", "updated_at", "user_id", "user_metadata", "username"]

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
    def from_json(cls, json_str: str) -> EventUser:
        """Create an instance of EventUser from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventUser:
        """Create an instance of EventUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventUser.parse_obj(obj)

        _obj = EventUser.parse_obj({
            "app_metadata": obj.get("app_metadata"),
            "created_at": obj.get("created_at"),
            "email": obj.get("email"),
            "email_verified": obj.get("email_verified"),
            "family_name": obj.get("family_name"),
            "given_name": obj.get("given_name"),
            "identities": obj.get("identities"),
            "last_password_reset": obj.get("last_password_reset"),
            "multifactor": obj.get("multifactor"),
            "name": obj.get("name"),
            "nickname": obj.get("nickname"),
            "phone_number": obj.get("phone_number"),
            "phone_verified": obj.get("phone_verified"),
            "picture": obj.get("picture"),
            "updated_at": obj.get("updated_at"),
            "user_id": obj.get("user_id"),
            "user_metadata": obj.get("user_metadata"),
            "username": obj.get("username")
        })
        return _obj
