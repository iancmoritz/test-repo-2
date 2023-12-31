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
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from astronomer_core_api.sdk.models.dag_run import DagRun
from astronomer_core_api.sdk.models.run_group import RunGroup


class RunsWithGroups(BaseModel):
    """
    RunsWithGroups
    """

    dag_runs: Optional[conlist(DagRun)] = Field(None, alias="dagRuns")
    groups: RunGroup = Field(...)
    ordering: conlist(StrictStr) = Field(...)
    __properties = ["dagRuns", "groups", "ordering"]

    @validator("ordering")
    def ordering_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in ("dataIntervalStart", "executionDate", "dataIntervalEnd"):
                raise ValueError(
                    "each list item must be one of ('dataIntervalStart', 'executionDate', 'dataIntervalEnd')"
                )
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
    def from_json(cls, json_str: str) -> RunsWithGroups:
        """Create an instance of RunsWithGroups from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in dag_runs (list)
        _items = []
        if self.dag_runs:
            for _item in self.dag_runs:
                if _item:
                    _items.append(_item.to_dict())
            _dict["dagRuns"] = _items
        # override the default output from pydantic by calling `to_dict()` of groups
        if self.groups:
            _dict["groups"] = self.groups.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RunsWithGroups:
        """Create an instance of RunsWithGroups from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RunsWithGroups.parse_obj(obj)

        _obj = RunsWithGroups.parse_obj(
            {
                "dag_runs": [DagRun.from_dict(_item) for _item in obj.get("dagRuns")]
                if obj.get("dagRuns") is not None
                else None,
                "groups": RunGroup.from_dict(obj.get("groups"))
                if obj.get("groups") is not None
                else None,
                "ordering": obj.get("ordering"),
            }
        )
        return _obj
