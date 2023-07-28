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
from pydantic import BaseModel, StrictStr, conlist
from astronomercoreapi.models.internal_dag_structure_group import InternalDagStructureGroup
from astronomercoreapi.models.internal_edge import InternalEdge

class InternalDagStructure(BaseModel):
    """
    InternalDagStructure
    """
    edges: Optional[conlist(InternalEdge)] = None
    group: Optional[InternalDagStructureGroup] = None
    ordering: Optional[conlist(StrictStr)] = None
    __properties = ["edges", "group", "ordering"]

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
    def from_json(cls, json_str: str) -> InternalDagStructure:
        """Create an instance of InternalDagStructure from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in edges (list)
        _items = []
        if self.edges:
            for _item in self.edges:
                if _item:
                    _items.append(_item.to_dict())
            _dict['edges'] = _items
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InternalDagStructure:
        """Create an instance of InternalDagStructure from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InternalDagStructure.parse_obj(obj)

        _obj = InternalDagStructure.parse_obj({
            "edges": [InternalEdge.from_dict(_item) for _item in obj.get("edges")] if obj.get("edges") is not None else None,
            "group": InternalDagStructureGroup.from_dict(obj.get("group")) if obj.get("group") is not None else None,
            "ordering": obj.get("ordering")
        })
        return _obj
