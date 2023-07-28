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

from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, validator
from astronomercoreapi.models.basic_subject_profile import BasicSubjectProfile
from astronomercoreapi.models.entitlement import Entitlement
from astronomercoreapi.models.managed_domain import ManagedDomain

class Organization(BaseModel):
    """
    Organization
    """
    auth_service_id: StrictStr = Field(..., alias="authServiceId")
    billing_email: Optional[StrictStr] = Field(None, alias="billingEmail")
    created_at: datetime = Field(..., alias="createdAt")
    created_by: Optional[StrictStr] = Field(None, alias="createdBy")
    created_by_subject: Optional[BasicSubjectProfile] = Field(None, alias="createdBySubject")
    domains: Optional[conlist(StrictStr)] = None
    entitlements: Optional[Dict[str, Entitlement]] = None
    id: StrictStr = Field(...)
    is_azure_managed: Optional[StrictBool] = Field(None, alias="isAzureManaged")
    is_scim_enabled: StrictBool = Field(..., alias="isScimEnabled")
    managed_domains: Optional[conlist(ManagedDomain)] = Field(None, alias="managedDomains")
    metronome_id: Optional[StrictStr] = Field(None, alias="metronomeId")
    metronome_plan_id: Optional[StrictStr] = Field(None, alias="metronomePlanId")
    name: StrictStr = Field(...)
    payment_method: Optional[StrictStr] = Field(None, alias="paymentMethod")
    product: Optional[StrictStr] = None
    salesforce_id: Optional[StrictStr] = Field(None, alias="salesforceId")
    short_name: StrictStr = Field(..., alias="shortName")
    status: Optional[StrictStr] = None
    stripe_id: Optional[StrictStr] = Field(None, alias="stripeId")
    stripe_payment_method_id: Optional[StrictStr] = Field(None, alias="stripePaymentMethodId")
    support_plan: StrictStr = Field(..., alias="supportPlan")
    trial_expires_at: Optional[datetime] = Field(None, alias="trialExpiresAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    updated_by: Optional[StrictStr] = Field(None, alias="updatedBy")
    updated_by_subject: Optional[BasicSubjectProfile] = Field(None, alias="updatedBySubject")
    uses_custom_metronome_plan: Optional[StrictBool] = Field(None, alias="usesCustomMetronomePlan")
    __properties = ["authServiceId", "billingEmail", "createdAt", "createdBy", "createdBySubject", "domains", "entitlements", "id", "isAzureManaged", "isScimEnabled", "managedDomains", "metronomeId", "metronomePlanId", "name", "paymentMethod", "product", "salesforceId", "shortName", "status", "stripeId", "stripePaymentMethodId", "supportPlan", "trialExpiresAt", "updatedAt", "updatedBy", "updatedBySubject", "usesCustomMetronomePlan"]

    @validator('payment_method')
    def payment_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CREDIT_CARD', 'INVOICE', 'AWS_MARKETPLACE', 'AZURE_MARKETPLACE', 'GCP_MARKETPLACE'):
            raise ValueError("must be one of enum values ('CREDIT_CARD', 'INVOICE', 'AWS_MARKETPLACE', 'AZURE_MARKETPLACE', 'GCP_MARKETPLACE')")
        return value

    @validator('product')
    def product_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('HOSTED', 'HYBRID'):
            raise ValueError("must be one of enum values ('HOSTED', 'HYBRID')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ACTIVE', 'INACTIVE', 'SUSPENDED'):
            raise ValueError("must be one of enum values ('ACTIVE', 'INACTIVE', 'SUSPENDED')")
        return value

    @validator('support_plan')
    def support_plan_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('INTERNAL', 'POV', 'TRIAL', 'BASIC', 'STANDARD', 'PREMIUM', 'BUSINESS_CRITICAL'):
            raise ValueError("must be one of enum values ('INTERNAL', 'POV', 'TRIAL', 'BASIC', 'STANDARD', 'PREMIUM', 'BUSINESS_CRITICAL')")
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
    def from_json(cls, json_str: str) -> Organization:
        """Create an instance of Organization from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of created_by_subject
        if self.created_by_subject:
            _dict['createdBySubject'] = self.created_by_subject.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in entitlements (dict)
        _field_dict = {}
        if self.entitlements:
            for _key in self.entitlements:
                if self.entitlements[_key]:
                    _field_dict[_key] = self.entitlements[_key].to_dict()
            _dict['entitlements'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in managed_domains (list)
        _items = []
        if self.managed_domains:
            for _item in self.managed_domains:
                if _item:
                    _items.append(_item.to_dict())
            _dict['managedDomains'] = _items
        # override the default output from pydantic by calling `to_dict()` of updated_by_subject
        if self.updated_by_subject:
            _dict['updatedBySubject'] = self.updated_by_subject.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Organization:
        """Create an instance of Organization from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Organization.parse_obj(obj)

        _obj = Organization.parse_obj({
            "auth_service_id": obj.get("authServiceId"),
            "billing_email": obj.get("billingEmail"),
            "created_at": obj.get("createdAt"),
            "created_by": obj.get("createdBy"),
            "created_by_subject": BasicSubjectProfile.from_dict(obj.get("createdBySubject")) if obj.get("createdBySubject") is not None else None,
            "domains": obj.get("domains"),
            "entitlements": dict(
                (_k, Entitlement.from_dict(_v))
                for _k, _v in obj.get("entitlements").items()
            )
            if obj.get("entitlements") is not None
            else None,
            "id": obj.get("id"),
            "is_azure_managed": obj.get("isAzureManaged"),
            "is_scim_enabled": obj.get("isScimEnabled"),
            "managed_domains": [ManagedDomain.from_dict(_item) for _item in obj.get("managedDomains")] if obj.get("managedDomains") is not None else None,
            "metronome_id": obj.get("metronomeId"),
            "metronome_plan_id": obj.get("metronomePlanId"),
            "name": obj.get("name"),
            "payment_method": obj.get("paymentMethod"),
            "product": obj.get("product"),
            "salesforce_id": obj.get("salesforceId"),
            "short_name": obj.get("shortName"),
            "status": obj.get("status"),
            "stripe_id": obj.get("stripeId"),
            "stripe_payment_method_id": obj.get("stripePaymentMethodId"),
            "support_plan": obj.get("supportPlan"),
            "trial_expires_at": obj.get("trialExpiresAt"),
            "updated_at": obj.get("updatedAt"),
            "updated_by": obj.get("updatedBy"),
            "updated_by_subject": BasicSubjectProfile.from_dict(obj.get("updatedBySubject")) if obj.get("updatedBySubject") is not None else None,
            "uses_custom_metronome_plan": obj.get("usesCustomMetronomePlan")
        })
        return _obj

