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
from pydantic import BaseModel, Field, StrictStr, validator
from astronomercoreapi.models.ctm_definition import CtmDefinition

class CellTypeMetadata(BaseModel):
    """
    CellTypeMetadata
    """
    created_at: Optional[StrictStr] = Field(None, alias="createdAt")
    created_by: Optional[StrictStr] = Field(None, alias="createdBy")
    definition: Optional[CtmDefinition] = None
    name: StrictStr = Field(...)
    organization_id: Optional[StrictStr] = Field(None, alias="organizationId")
    project_id: Optional[StrictStr] = Field(None, alias="projectId")
    source: StrictStr = Field(...)
    updated_at: Optional[StrictStr] = Field(None, alias="updatedAt")
    updated_by: Optional[StrictStr] = Field(None, alias="updatedBy")
    workspace_id: Optional[StrictStr] = Field(None, alias="workspaceId")
    __properties = ["createdAt", "createdBy", "definition", "name", "organizationId", "projectId", "source", "updatedAt", "updatedBy", "workspaceId"]

    @validator('source')
    def source_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('provided', 'project', 'validation'):
            raise ValueError("must be one of enum values ('provided', 'project', 'validation')")
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
    def from_json(cls, json_str: str) -> CellTypeMetadata:
        """Create an instance of CellTypeMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of definition
        if self.definition:
            _dict['definition'] = self.definition.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CellTypeMetadata:
        """Create an instance of CellTypeMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CellTypeMetadata.parse_obj(obj)

        _obj = CellTypeMetadata.parse_obj({
            "created_at": obj.get("createdAt"),
            "created_by": obj.get("createdBy"),
            "definition": CtmDefinition.from_dict(obj.get("definition")) if obj.get("definition") is not None else None,
            "name": obj.get("name"),
            "organization_id": obj.get("organizationId"),
            "project_id": obj.get("projectId"),
            "source": obj.get("source"),
            "updated_at": obj.get("updatedAt"),
            "updated_by": obj.get("updatedBy"),
            "workspace_id": obj.get("workspaceId")
        })
        return _obj

