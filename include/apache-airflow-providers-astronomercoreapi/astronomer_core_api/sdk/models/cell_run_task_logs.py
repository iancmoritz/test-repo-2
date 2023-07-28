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


from typing import List
from pydantic import BaseModel, Field, StrictInt, conlist
from astronomer_core_api.sdk.models.cell_run_task_log import CellRunTaskLog


class CellRunTaskLogs(BaseModel):
    """
    CellRunTaskLogs
    """

    last: StrictInt = Field(...)
    logs: conlist(CellRunTaskLog) = Field(...)
    __properties = ["last", "logs"]

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
    def from_json(cls, json_str: str) -> CellRunTaskLogs:
        """Create an instance of CellRunTaskLogs from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in logs (list)
        _items = []
        if self.logs:
            for _item in self.logs:
                if _item:
                    _items.append(_item.to_dict())
            _dict["logs"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CellRunTaskLogs:
        """Create an instance of CellRunTaskLogs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CellRunTaskLogs.parse_obj(obj)

        _obj = CellRunTaskLogs.parse_obj(
            {
                "last": obj.get("last"),
                "logs": [CellRunTaskLog.from_dict(_item) for _item in obj.get("logs")]
                if obj.get("logs") is not None
                else None,
            }
        )
        return _obj