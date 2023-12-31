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



from pydantic import BaseModel, Field, StrictStr, validator

class ApiTokenRole(BaseModel):
    """
    ApiTokenRole
    """
    entity_id: StrictStr = Field(..., alias="entityId")
    entity_type: StrictStr = Field(..., alias="entityType")
    role: StrictStr = Field(...)
    __properties = ["entityId", "entityType", "role"]

    @validator('entity_type')
    def entity_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('WORKSPACE', 'ORGANIZATION'):
            raise ValueError("must be one of enum values ('WORKSPACE', 'ORGANIZATION')")
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
    def from_json(cls, json_str: str) -> ApiTokenRole:
        """Create an instance of ApiTokenRole from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiTokenRole:
        """Create an instance of ApiTokenRole from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiTokenRole.parse_obj(obj)

        _obj = ApiTokenRole.parse_obj({
            "entity_id": obj.get("entityId"),
            "entity_type": obj.get("entityType"),
            "role": obj.get("role")
        })
        return _obj

