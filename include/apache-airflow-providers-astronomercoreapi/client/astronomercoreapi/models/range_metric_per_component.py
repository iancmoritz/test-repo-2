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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from astronomercoreapi.models.metric_value import MetricValue

class RangeMetricPerComponent(BaseModel):
    """
    RangeMetricPerComponent
    """
    component: StrictStr = Field(...)
    deployment_id: StrictStr = Field(..., alias="deploymentId")
    end: StrictInt = Field(...)
    release_name: StrictStr = Field(..., alias="releaseName")
    start: StrictInt = Field(...)
    step: StrictInt = Field(...)
    values: conlist(MetricValue) = Field(...)
    workspace_id: StrictStr = Field(..., alias="workspaceId")
    __properties = ["component", "deploymentId", "end", "releaseName", "start", "step", "values", "workspaceId"]

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
    def from_json(cls, json_str: str) -> RangeMetricPerComponent:
        """Create an instance of RangeMetricPerComponent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in values (list)
        _items = []
        if self.values:
            for _item in self.values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['values'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RangeMetricPerComponent:
        """Create an instance of RangeMetricPerComponent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RangeMetricPerComponent.parse_obj(obj)

        _obj = RangeMetricPerComponent.parse_obj({
            "component": obj.get("component"),
            "deployment_id": obj.get("deploymentId"),
            "end": obj.get("end"),
            "release_name": obj.get("releaseName"),
            "start": obj.get("start"),
            "step": obj.get("step"),
            "values": [MetricValue.from_dict(_item) for _item in obj.get("values")] if obj.get("values") is not None else None,
            "workspace_id": obj.get("workspaceId")
        })
        return _obj

