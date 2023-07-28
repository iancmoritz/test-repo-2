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
from pydantic import BaseModel, Field, StrictInt, StrictStr
from astronomercoreapi.models.cell_run_task_results_schema import CellRunTaskResultsSchema

class CellRunTaskResults(BaseModel):
    """
    CellRunTaskResults
    """
    data: StrictStr = Field(...)
    row_count: Optional[StrictInt] = Field(None, alias="rowCount")
    var_schema: CellRunTaskResultsSchema = Field(..., alias="schema")
    __properties = ["data", "rowCount", "schema"]

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
    def from_json(cls, json_str: str) -> CellRunTaskResults:
        """Create an instance of CellRunTaskResults from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CellRunTaskResults:
        """Create an instance of CellRunTaskResults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CellRunTaskResults.parse_obj(obj)

        _obj = CellRunTaskResults.parse_obj({
            "data": obj.get("data"),
            "row_count": obj.get("rowCount"),
            "var_schema": CellRunTaskResultsSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None
        })
        return _obj

