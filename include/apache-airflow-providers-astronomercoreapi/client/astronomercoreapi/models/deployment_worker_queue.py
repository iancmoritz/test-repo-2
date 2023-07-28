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



from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class DeploymentWorkerQueue(BaseModel):
    """
    DeploymentWorkerQueue
    """
    id: StrictStr = Field(...)
    is_default: StrictBool = Field(..., alias="isDefault")
    max_worker_count: StrictInt = Field(..., alias="maxWorkerCount")
    min_worker_count: StrictInt = Field(..., alias="minWorkerCount")
    name: StrictStr = Field(...)
    node_pool_id: StrictStr = Field(..., alias="nodePoolId")
    pod_cpu: StrictStr = Field(..., alias="podCpu")
    pod_ram: StrictStr = Field(..., alias="podRam")
    pod_size: StrictStr = Field(..., alias="podSize")
    worker_concurrency: StrictInt = Field(..., alias="workerConcurrency")
    __properties = ["id", "isDefault", "maxWorkerCount", "minWorkerCount", "name", "nodePoolId", "podCpu", "podRam", "podSize", "workerConcurrency"]

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
    def from_json(cls, json_str: str) -> DeploymentWorkerQueue:
        """Create an instance of DeploymentWorkerQueue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeploymentWorkerQueue:
        """Create an instance of DeploymentWorkerQueue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeploymentWorkerQueue.parse_obj(obj)

        _obj = DeploymentWorkerQueue.parse_obj({
            "id": obj.get("id"),
            "is_default": obj.get("isDefault"),
            "max_worker_count": obj.get("maxWorkerCount"),
            "min_worker_count": obj.get("minWorkerCount"),
            "name": obj.get("name"),
            "node_pool_id": obj.get("nodePoolId"),
            "pod_cpu": obj.get("podCpu"),
            "pod_ram": obj.get("podRam"),
            "pod_size": obj.get("podSize"),
            "worker_concurrency": obj.get("workerConcurrency")
        })
        return _obj

