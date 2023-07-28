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
from astronomer_core_api.sdk.models.team import Team


class TeamsPaginated(BaseModel):
    """
    TeamsPaginated
    """

    limit: StrictInt = Field(...)
    offset: StrictInt = Field(...)
    teams: conlist(Team) = Field(...)
    total_count: StrictInt = Field(..., alias="totalCount")
    __properties = ["limit", "offset", "teams", "totalCount"]

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
    def from_json(cls, json_str: str) -> TeamsPaginated:
        """Create an instance of TeamsPaginated from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in teams (list)
        _items = []
        if self.teams:
            for _item in self.teams:
                if _item:
                    _items.append(_item.to_dict())
            _dict["teams"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamsPaginated:
        """Create an instance of TeamsPaginated from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamsPaginated.parse_obj(obj)

        _obj = TeamsPaginated.parse_obj(
            {
                "limit": obj.get("limit"),
                "offset": obj.get("offset"),
                "teams": [Team.from_dict(_item) for _item in obj.get("teams")]
                if obj.get("teams") is not None
                else None,
                "total_count": obj.get("totalCount"),
            }
        )
        return _obj