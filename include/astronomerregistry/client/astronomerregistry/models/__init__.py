# coding: utf-8

# flake8: noqa
"""
    Astro Registry API

    Astro Registry API  # noqa: E501

    The version of the OpenAPI document: v1alpha1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


# import models into model package
from astronomerregistry.models.create_dag_request import CreateDagRequest
from astronomerregistry.models.create_label_request import CreateLabelRequest
from astronomerregistry.models.create_module_parameter_request import CreateModuleParameterRequest
from astronomerregistry.models.create_module_request import CreateModuleRequest
from astronomerregistry.models.create_provider_request import CreateProviderRequest
from astronomerregistry.models.dag import Dag
from astronomerregistry.models.dag_filters import DagFilters
from astronomerregistry.models.dags_paginated import DagsPaginated
from astronomerregistry.models.error import Error
from astronomerregistry.models.label import Label
from astronomerregistry.models.label_graphics import LabelGraphics
from astronomerregistry.models.labels_paginated import LabelsPaginated
from astronomerregistry.models.module import Module
from astronomerregistry.models.module_filters import ModuleFilters
from astronomerregistry.models.module_inherits_from import ModuleInheritsFrom
from astronomerregistry.models.module_parameter import ModuleParameter
from astronomerregistry.models.modules_paginated import ModulesPaginated
from astronomerregistry.models.provider import Provider
from astronomerregistry.models.provider_filters import ProviderFilters
from astronomerregistry.models.providers_paginated import ProvidersPaginated
from astronomerregistry.models.registry_search import RegistrySearch
from astronomerregistry.models.registry_search_hit import RegistrySearchHit
from astronomerregistry.models.registry_search_request import RegistrySearchRequest
from astronomerregistry.models.related_module_request import RelatedModuleRequest
from astronomerregistry.models.short_label import ShortLabel
from astronomerregistry.models.short_module import ShortModule
from astronomerregistry.models.short_provider import ShortProvider
from astronomerregistry.models.social_stats import SocialStats
from astronomerregistry.models.task_dependency import TaskDependency
from astronomerregistry.models.task_dependency_tree import TaskDependencyTree
from astronomerregistry.models.type_def import TypeDef
from astronomerregistry.models.update_dag_request import UpdateDagRequest
from astronomerregistry.models.update_label_request import UpdateLabelRequest
from astronomerregistry.models.update_module_parameter_request import UpdateModuleParameterRequest
from astronomerregistry.models.update_module_request import UpdateModuleRequest
from astronomerregistry.models.update_provider_request import UpdateProviderRequest