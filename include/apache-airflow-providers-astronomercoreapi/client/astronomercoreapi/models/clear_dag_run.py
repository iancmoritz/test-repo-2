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
from pydantic import BaseModel, Field, conlist
from astronomercoreapi.models.dag_run import DagRun
from astronomercoreapi.models.task_instance import TaskInstance

class ClearDagRun(BaseModel):
    """
    ClearDagRun
    """
    dag_run: Optional[DagRun] = Field(None, alias="dagRun")
    task_instances: Optional[conlist(TaskInstance)] = Field(None, alias="taskInstances")
    __properties = ["dagRun", "taskInstances"]

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
    def from_json(cls, json_str: str) -> ClearDagRun:
        """Create an instance of ClearDagRun from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of dag_run
        if self.dag_run:
            _dict['dagRun'] = self.dag_run.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in task_instances (list)
        _items = []
        if self.task_instances:
            for _item in self.task_instances:
                if _item:
                    _items.append(_item.to_dict())
            _dict['taskInstances'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClearDagRun:
        """Create an instance of ClearDagRun from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClearDagRun.parse_obj(obj)

        _obj = ClearDagRun.parse_obj({
            "dag_run": DagRun.from_dict(obj.get("dagRun")) if obj.get("dagRun") is not None else None,
            "task_instances": [TaskInstance.from_dict(_item) for _item in obj.get("taskInstances")] if obj.get("taskInstances") is not None else None
        })
        return _obj
