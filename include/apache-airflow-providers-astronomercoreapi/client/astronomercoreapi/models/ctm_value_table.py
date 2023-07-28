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
from pydantic import BaseModel, Field, StrictStr

class CtmValueTable(BaseModel):
    """
    CtmValueTable
    """
    conn_id: StrictStr = Field(..., alias="connId")
    database: Optional[StrictStr] = None
    name: StrictStr = Field(...)
    var_schema: Optional[StrictStr] = Field(None, alias="schema")
    __properties = ["connId", "database", "name", "schema"]

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
    def from_json(cls, json_str: str) -> CtmValueTable:
        """Create an instance of CtmValueTable from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CtmValueTable:
        """Create an instance of CtmValueTable from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CtmValueTable.parse_obj(obj)

        _obj = CtmValueTable.parse_obj({
            "conn_id": obj.get("connId"),
            "database": obj.get("database"),
            "name": obj.get("name"),
            "var_schema": obj.get("schema")
        })
        return _obj
