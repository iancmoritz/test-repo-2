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


from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator

class TaskInstance(BaseModel):
    """
    TaskInstance
    """
    dag_id: StrictStr = Field(..., alias="dagId")
    dag_run_id: StrictStr = Field(..., alias="dagRunId")
    duration: Optional[Union[StrictFloat, StrictInt]] = None
    end_date: Optional[StrictStr] = Field(None, alias="endDate")
    execution_date: Optional[StrictStr] = Field(None, alias="executionDate")
    executor_config: Optional[StrictStr] = Field(None, alias="executorConfig")
    hostname: Optional[StrictStr] = None
    map_index: Optional[StrictInt] = Field(None, alias="mapIndex")
    max_tries: Optional[StrictInt] = Field(None, alias="maxTries")
    note: Optional[StrictStr] = None
    operator: Optional[StrictStr] = None
    pid: Optional[StrictInt] = None
    pool: Optional[StrictStr] = None
    pool_slots: Optional[StrictInt] = Field(None, alias="poolSlots")
    priority_weight: Optional[StrictInt] = Field(None, alias="priorityWeight")
    queue: Optional[StrictStr] = None
    queued_when: Optional[StrictStr] = Field(None, alias="queuedWhen")
    rendered_fields: Optional[Dict[str, Any]] = Field(None, alias="renderedFields")
    start_date: Optional[StrictStr] = Field(None, alias="startDate")
    state: Optional[StrictStr] = None
    task_id: StrictStr = Field(..., alias="taskId")
    try_number: Optional[StrictInt] = Field(None, alias="tryNumber")
    unixname: Optional[StrictStr] = None
    __properties = ["dagId", "dagRunId", "duration", "endDate", "executionDate", "executorConfig", "hostname", "mapIndex", "maxTries", "note", "operator", "pid", "pool", "poolSlots", "priorityWeight", "queue", "queuedWhen", "renderedFields", "startDate", "state", "taskId", "tryNumber", "unixname"]

    @validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('success', 'running', 'failed', 'upstreamFailed', 'skipped', 'upForRetry', 'upForReschedule', 'queued', 'none', 'scheduled', 'deferred', 'removed', 'restarting'):
            raise ValueError("must be one of enum values ('success', 'running', 'failed', 'upstreamFailed', 'skipped', 'upForRetry', 'upForReschedule', 'queued', 'none', 'scheduled', 'deferred', 'removed', 'restarting')")
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
    def from_json(cls, json_str: str) -> TaskInstance:
        """Create an instance of TaskInstance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaskInstance:
        """Create an instance of TaskInstance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaskInstance.parse_obj(obj)

        _obj = TaskInstance.parse_obj({
            "dag_id": obj.get("dagId"),
            "dag_run_id": obj.get("dagRunId"),
            "duration": obj.get("duration"),
            "end_date": obj.get("endDate"),
            "execution_date": obj.get("executionDate"),
            "executor_config": obj.get("executorConfig"),
            "hostname": obj.get("hostname"),
            "map_index": obj.get("mapIndex"),
            "max_tries": obj.get("maxTries"),
            "note": obj.get("note"),
            "operator": obj.get("operator"),
            "pid": obj.get("pid"),
            "pool": obj.get("pool"),
            "pool_slots": obj.get("poolSlots"),
            "priority_weight": obj.get("priorityWeight"),
            "queue": obj.get("queue"),
            "queued_when": obj.get("queuedWhen"),
            "rendered_fields": obj.get("renderedFields"),
            "start_date": obj.get("startDate"),
            "state": obj.get("state"),
            "task_id": obj.get("taskId"),
            "try_number": obj.get("tryNumber"),
            "unixname": obj.get("unixname")
        })
        return _obj

