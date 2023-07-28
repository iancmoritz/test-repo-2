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


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class TestConnectionRequest(BaseModel):
    """
    TestConnectionRequest
    """
    extra: Optional[Dict[str, StrictStr]] = None
    host: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    login: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    port: Optional[StrictInt] = None
    var_schema: Optional[StrictStr] = Field(None, alias="schema")
    type: Optional[StrictStr] = None
    __properties = ["extra", "host", "id", "login", "password", "port", "schema", "type"]

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
    def from_json(cls, json_str: str) -> TestConnectionRequest:
        """Create an instance of TestConnectionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TestConnectionRequest:
        """Create an instance of TestConnectionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TestConnectionRequest.parse_obj(obj)

        _obj = TestConnectionRequest.parse_obj({
            "extra": obj.get("extra"),
            "host": obj.get("host"),
            "id": obj.get("id"),
            "login": obj.get("login"),
            "password": obj.get("password"),
            "port": obj.get("port"),
            "var_schema": obj.get("schema"),
            "type": obj.get("type")
        })
        return _obj

