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
from pydantic import BaseModel, Field
from astronomercoreapi.models.internal_schedule_interval_cron_expression import InternalScheduleIntervalCronExpression
from astronomercoreapi.models.internal_schedule_interval_relative_delta import InternalScheduleIntervalRelativeDelta
from astronomercoreapi.models.internal_schedule_interval_time_delta import InternalScheduleIntervalTimeDelta

class DagSchedule(BaseModel):
    """
    DagSchedule
    """
    cron_expression: Optional[InternalScheduleIntervalCronExpression] = Field(None, alias="CronExpression")
    relative_delta: Optional[InternalScheduleIntervalRelativeDelta] = Field(None, alias="RelativeDelta")
    time_delta: Optional[InternalScheduleIntervalTimeDelta] = Field(None, alias="TimeDelta")
    __properties = ["CronExpression", "RelativeDelta", "TimeDelta"]

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
    def from_json(cls, json_str: str) -> DagSchedule:
        """Create an instance of DagSchedule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of cron_expression
        if self.cron_expression:
            _dict['CronExpression'] = self.cron_expression.to_dict()
        # override the default output from pydantic by calling `to_dict()` of relative_delta
        if self.relative_delta:
            _dict['RelativeDelta'] = self.relative_delta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_delta
        if self.time_delta:
            _dict['TimeDelta'] = self.time_delta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DagSchedule:
        """Create an instance of DagSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DagSchedule.parse_obj(obj)

        _obj = DagSchedule.parse_obj({
            "cron_expression": InternalScheduleIntervalCronExpression.from_dict(obj.get("CronExpression")) if obj.get("CronExpression") is not None else None,
            "relative_delta": InternalScheduleIntervalRelativeDelta.from_dict(obj.get("RelativeDelta")) if obj.get("RelativeDelta") is not None else None,
            "time_delta": InternalScheduleIntervalTimeDelta.from_dict(obj.get("TimeDelta")) if obj.get("TimeDelta") is not None else None
        })
        return _obj

