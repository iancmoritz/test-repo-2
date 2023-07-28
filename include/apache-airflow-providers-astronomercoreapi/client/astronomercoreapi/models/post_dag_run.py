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
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class PostDagRun(BaseModel):
    """
    PostDagRun
    """
    conf: Optional[Dict[str, Any]] = None
    dag_id: Optional[StrictStr] = Field(None, alias="dagId")
    dag_run_id: Optional[StrictStr] = Field(None, alias="dagRunId")
    end_date: Optional[datetime] = Field(None, alias="endDate")
    external_trigger: Optional[StrictBool] = Field(None, alias="externalTrigger")
    logical_date: Optional[datetime] = Field(None, alias="logicalDate")
    start_date: Optional[datetime] = Field(None, alias="startDate")
    state: Optional[StrictStr] = None
    __properties = ["conf", "dagId", "dagRunId", "endDate", "externalTrigger", "logicalDate", "startDate", "state"]

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
    def from_json(cls, json_str: str) -> PostDagRun:
        """Create an instance of PostDagRun from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PostDagRun:
        """Create an instance of PostDagRun from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostDagRun.parse_obj(obj)

        _obj = PostDagRun.parse_obj({
            "conf": obj.get("conf"),
            "dag_id": obj.get("dagId"),
            "dag_run_id": obj.get("dagRunId"),
            "end_date": obj.get("endDate"),
            "external_trigger": obj.get("externalTrigger"),
            "logical_date": obj.get("logicalDate"),
            "start_date": obj.get("startDate"),
            "state": obj.get("state")
        })
        return _obj

