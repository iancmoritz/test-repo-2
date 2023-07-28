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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from astronomercoreapi.models.sso_login_deny import SsoLoginDeny

class SsoLoginCallback(BaseModel):
    """
    SsoLoginCallback
    """
    access_token_claims: Optional[Dict[str, StrictStr]] = Field(None, alias="accessTokenClaims")
    deny: Optional[SsoLoginDeny] = None
    id_token_claims: Optional[Dict[str, StrictStr]] = Field(None, alias="idTokenClaims")
    user_meta_data: Optional[Dict[str, Any]] = Field(None, alias="userMetaData")
    __properties = ["accessTokenClaims", "deny", "idTokenClaims", "userMetaData"]

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
    def from_json(cls, json_str: str) -> SsoLoginCallback:
        """Create an instance of SsoLoginCallback from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of deny
        if self.deny:
            _dict['deny'] = self.deny.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SsoLoginCallback:
        """Create an instance of SsoLoginCallback from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SsoLoginCallback.parse_obj(obj)

        _obj = SsoLoginCallback.parse_obj({
            "access_token_claims": obj.get("accessTokenClaims"),
            "deny": SsoLoginDeny.from_dict(obj.get("deny")) if obj.get("deny") is not None else None,
            "id_token_claims": obj.get("idTokenClaims"),
            "user_meta_data": obj.get("userMetaData")
        })
        return _obj

