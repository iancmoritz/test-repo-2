from __future__ import annotations

from functools import cached_property

from client.astronomerregistry import ApiClient
import client.astronomerregistry.api as api_group

from client.astronomerregistry.models import (
    CreateDagRequest,
    CreateLabelRequest,
    CreateModuleRequest,
    CreateProviderRequest,
    Dag,
    DagsPaginated,
    Label,
    LabelsPaginated,
    Module,
    ModulesPaginated,
    Provider,
    ProvidersPaginated,
    RegistrySearch,
    RegistrySearchRequest,
    UpdateDagRequest,
    UpdateLabelRequest,
    UpdateModuleRequest,
    UpdateProviderRequest,
)

from client.astronomerregistry.configuration import Configuration
from airflow.models import Connection

from airflow.hooks.base import BaseHook
from typing import Optional
from typing_extensions import Annotated
from pydantic import Field, StrictBool, StrictStr, conint, conlist


class AstronomerRegistryHook(BaseHook):
    def __init__(self, conn_id: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.connection = self.get_connection(conn_id)

    @cached_property
    def connection(self) -> Connection:
        return self.get_connection(self.conn_id)

    @cached_property
    def client(self) -> ApiClient:
        conn = self.connection

        if not conn.host:
            raise ValueError("Cannot properly build API configuration.")

        configuration = Configuration(host=conn.host)
        # A token is not required for get/list, but it is required for all other actions.
        if conn.password:
            configuration.api_key["JWT"] = conn.password
            configuration.api_key_prefix["JWT"] = "Bearer"

        return ApiClient(configuration)

    def create_dag(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        body: Annotated[
            CreateDagRequest,
            Field(..., description="request body for creating a registry dag"),
        ],
    ) -> Dag:
        api = api_group.DagApi(self.client)
        response = api.create_dag(
            org_short_name_id=org_short_name_id,
            body=body,
        )
        return response

    def delete_dag(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        dag_name: Annotated[StrictStr, Field(..., description="The name of the dag")],
        version: Annotated[StrictStr, Field(..., description="The version of the dag")],
    ) -> Dag:
        api = api_group.DagApi(self.client)
        response = api.delete_dag(
            org_short_name_id=org_short_name_id,
            dag_name=dag_name,
            version=version,
        )
        return response

    def get_dag(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        dag_name: Annotated[
            StrictStr, Field(..., description="The name or display name of the dag")
        ],
        version: Annotated[
            StrictStr,
            Field(
                ...,
                description="The version of the dag, or keyword 'latest' for latest version",
            ),
        ],
    ) -> Dag:
        api = api_group.DagApi(self.client)
        response = api.get_dag(
            org_short_name_id=org_short_name_id,
            dag_name=dag_name,
            version=version,
        )
        return response

    def list_dags(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        is_certified: Annotated[
            Optional[StrictBool], Field(description="return only certified dags")
        ],
        is_featured: Annotated[
            Optional[StrictBool], Field(description="return only featured dags")
        ],
        is_global: Annotated[
            Optional[StrictBool], Field(description="return only global dags")
        ],
        is_private: Annotated[
            Optional[StrictBool], Field(description="return only private dags")
        ],
        is_cloud_ide_compatible: Annotated[
            Optional[StrictBool],
            Field(description="return only cloud ide compatible dags"),
        ],
        type_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one type in input filter list"),
        ],
        tier_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one tier in input filter list"),
        ],
        category_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one category in input filter list"),
        ],
        badge_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one badge in input filter list"),
        ],
        dag_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has one id in input filter list"),
        ],
        module_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has one module in input filter list"),
        ],
        provider_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has one dag in input filter list"),
        ],
        tier_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one tier name in input filter list"),
        ],
        category_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one category name in input filter list"),
        ],
        badge_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one badge name in input filter list"),
        ],
        module_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has one module name in input filter list"),
        ],
        provider_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has one provider name in input filter list"),
        ],
        query: Annotated[
            Optional[StrictStr], Field(description="Search query for dag")
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for pagination"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
    ) -> DagsPaginated:
        api = api_group.DagApi(self.client)
        response = api.list_dags(
            org_short_name_id=org_short_name_id,
            is_certified=is_certified,
            is_featured=is_featured,
            is_global=is_global,
            is_private=is_private,
            is_cloud_ide_compatible=is_cloud_ide_compatible,
            type_name=type_name,
            tier_id=tier_id,
            category_id=category_id,
            badge_id=badge_id,
            dag_id=dag_id,
            module_id=module_id,
            provider_id=provider_id,
            tier_name=tier_name,
            category_name=category_name,
            badge_name=badge_name,
            module_name=module_name,
            provider_name=provider_name,
            query=query,
            offset=offset,
            limit=limit,
            sorts=sorts,
        )
        return response

    def update_dag(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        dag_name: Annotated[StrictStr, Field(..., description="The name of the dag")],
        version: Annotated[StrictStr, Field(..., description="The version of the dag")],
        body: Annotated[
            UpdateDagRequest,
            Field(..., description="request body for updating a registry dag"),
        ],
    ) -> Dag:
        api = api_group.DagApi(self.client)
        response = api.update_dag(
            org_short_name_id=org_short_name_id,
            dag_name=dag_name,
            version=version,
            body=body,
        )
        return response

    def create_label(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        label_group: Annotated[
            StrictStr, Field(..., description="Group name of the label")
        ],
        body: Annotated[
            CreateLabelRequest,
            Field(..., description="request body for creating a registry label"),
        ],
    ) -> Label:
        api = api_group.LabelApi(self.client)
        response = api.create_label(
            org_short_name_id=org_short_name_id,
            label_group=label_group,
            body=body,
        )
        return response

    def delete_label(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        label_group: Annotated[
            StrictStr, Field(..., description="Group name of the label")
        ],
        label_name: Annotated[
            StrictStr, Field(..., description="The name of the label")
        ],
    ) -> Label:
        api = api_group.LabelApi(self.client)
        response = api.delete_label(
            org_short_name_id=org_short_name_id,
            label_group=label_group,
            label_name=label_name,
        )
        return response

    def get_label(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        label_group: Annotated[
            StrictStr, Field(..., description="Group name of the label")
        ],
        label_name: Annotated[
            StrictStr, Field(..., description="The name of the label")
        ],
    ) -> Label:
        api = api_group.LabelApi(self.client)
        response = api.get_label(
            org_short_name_id=org_short_name_id,
            label_group=label_group,
            label_name=label_name,
        )
        return response

    def list_labels(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        label_group: Annotated[
            StrictStr, Field(..., description="Group name of the labels")
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for pagination"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
    ) -> LabelsPaginated:
        api = api_group.LabelApi(self.client)
        response = api.list_labels(
            org_short_name_id=org_short_name_id,
            label_group=label_group,
            offset=offset,
            limit=limit,
            sorts=sorts,
        )
        return response

    def update_label(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        label_group: Annotated[
            StrictStr, Field(..., description="Group name of the label")
        ],
        label_name: Annotated[
            StrictStr, Field(..., description="The name of the label")
        ],
        body: Annotated[
            UpdateLabelRequest,
            Field(..., description="request body for updating a registry label"),
        ],
    ) -> Label:
        api = api_group.LabelApi(self.client)
        response = api.update_label(
            org_short_name_id=org_short_name_id,
            label_group=label_group,
            label_name=label_name,
            body=body,
        )
        return response

    def create_module(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        provider_name: Annotated[
            StrictStr,
            Field(..., description="The name or display name of the provider"),
        ],
        version: Annotated[
            StrictStr,
            Field(
                ...,
                description="The version of the module, or keyword 'latest' for latest version",
            ),
        ],
        body: Annotated[
            CreateModuleRequest,
            Field(..., description="request body for creating a registry module"),
        ],
    ) -> Module:
        api = api_group.ModuleApi(self.client)
        response = api.create_module(
            org_short_name_id=org_short_name_id,
            provider_name=provider_name,
            version=version,
            body=body,
        )
        return response

    def delete_module(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        provider_name: Annotated[
            StrictStr,
            Field(..., description="The name or display name of the provider"),
        ],
        version: Annotated[
            StrictStr,
            Field(
                ...,
                description="The version of the module, or keyword 'latest' for latest version",
            ),
        ],
        module_name: Annotated[
            StrictStr, Field(..., description="The name of the module")
        ],
    ) -> Module:
        api = api_group.ModuleApi(self.client)
        response = api.delete_module(
            org_short_name_id=org_short_name_id,
            provider_name=provider_name,
            version=version,
            module_name=module_name,
        )
        return response

    def get_module(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        provider_name: Annotated[
            StrictStr,
            Field(..., description="The name or display name of the provider"),
        ],
        version: Annotated[
            StrictStr,
            Field(
                ...,
                description="The version of the module, or keyword 'latest' for latest version",
            ),
        ],
        module_name: Annotated[
            StrictStr, Field(..., description="The name or display name of the module")
        ],
    ) -> Module:
        api = api_group.ModuleApi(self.client)
        response = api.get_module(
            org_short_name_id=org_short_name_id,
            provider_name=provider_name,
            version=version,
            module_name=module_name,
        )
        return response

    def list_modules(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        is_certified: Annotated[
            Optional[StrictBool], Field(description="return only certified modules")
        ],
        is_featured: Annotated[
            Optional[StrictBool], Field(description="return only featured modules")
        ],
        is_global: Annotated[
            Optional[StrictBool], Field(description="return only global modules")
        ],
        is_private: Annotated[
            Optional[StrictBool], Field(description="return only private modules")
        ],
        is_cloud_ide_compatible: Annotated[
            Optional[StrictBool],
            Field(description="return only cloud ide compatible modules"),
        ],
        type_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one type in input filter list"),
        ],
        tier_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one tier in input filter list"),
        ],
        category_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one category in input filter list"),
        ],
        badge_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one badge in input filter list"),
        ],
        dag_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has one id in input filter list"),
        ],
        module_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has one module in input filter list"),
        ],
        provider_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has one provider in input filter list"),
        ],
        tier_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one tier name in input filter list"),
        ],
        category_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one category name in input filter list"),
        ],
        badge_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one badge name in input filter list"),
        ],
        provider_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has one provider name in input filter list"),
        ],
        query: Annotated[
            Optional[StrictStr], Field(description="Search query for module")
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for pagination"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
    ) -> ModulesPaginated:
        api = api_group.ModuleApi(self.client)
        response = api.list_modules(
            org_short_name_id=org_short_name_id,
            is_certified=is_certified,
            is_featured=is_featured,
            is_global=is_global,
            is_private=is_private,
            is_cloud_ide_compatible=is_cloud_ide_compatible,
            type_name=type_name,
            tier_id=tier_id,
            category_id=category_id,
            badge_id=badge_id,
            dag_id=dag_id,
            module_id=module_id,
            provider_id=provider_id,
            tier_name=tier_name,
            category_name=category_name,
            badge_name=badge_name,
            provider_name=provider_name,
            query=query,
            offset=offset,
            limit=limit,
            sorts=sorts,
        )
        return response

    def list_modules_internal(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        module_name: Annotated[
            StrictStr, Field(..., description="The name or display name of the module")
        ],
    ) -> ModulesPaginated:
        api = api_group.ModuleApi(self.client)
        response = api.list_modules_internal(
            org_short_name_id=org_short_name_id,
            module_name=module_name,
        )
        return response

    def update_module(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        provider_name: Annotated[
            StrictStr, Field(..., description="The name of the provider")
        ],
        version: Annotated[
            StrictStr, Field(..., description="The version of the module")
        ],
        module_name: Annotated[
            StrictStr, Field(..., description="The name of the module")
        ],
        body: Annotated[
            UpdateModuleRequest,
            Field(..., description="request body for updating a registry module"),
        ],
    ) -> Module:
        api = api_group.ModuleApi(self.client)
        response = api.update_module(
            org_short_name_id=org_short_name_id,
            provider_name=provider_name,
            version=version,
            module_name=module_name,
            body=body,
        )
        return response

    def create_provider(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        body: Annotated[
            CreateProviderRequest,
            Field(..., description="request body for creating a registry provider"),
        ],
    ) -> Provider:
        api = api_group.ProviderApi(self.client)
        response = api.create_provider(
            org_short_name_id=org_short_name_id,
            body=body,
        )
        return response

    def delete_provider(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        provider_name: Annotated[
            StrictStr, Field(..., description="The name of the provider")
        ],
        version: Annotated[
            StrictStr, Field(..., description="The version of the provider")
        ],
    ) -> Provider:
        api = api_group.ProviderApi(self.client)
        response = api.delete_provider(
            org_short_name_id=org_short_name_id,
            provider_name=provider_name,
            version=version,
        )
        return response

    def get_provider(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        provider_name: Annotated[
            StrictStr,
            Field(..., description="The name or display name of the provider"),
        ],
        version: Annotated[
            StrictStr,
            Field(
                ...,
                description="The version of the provider, or keyword 'latest' for latest version",
            ),
        ],
    ) -> Provider:
        api = api_group.ProviderApi(self.client)
        response = api.get_provider(
            org_short_name_id=org_short_name_id,
            provider_name=provider_name,
            version=version,
        )
        return response

    def list_providers(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        is_certified: Annotated[
            Optional[StrictBool], Field(description="return only certified providers")
        ],
        is_featured: Annotated[
            Optional[StrictBool], Field(description="return only featured providers")
        ],
        is_global: Annotated[
            Optional[StrictBool], Field(description="return only global providers")
        ],
        is_private: Annotated[
            Optional[StrictBool], Field(description="return only private providers")
        ],
        is_cloud_ide_compatible: Annotated[
            Optional[StrictBool],
            Field(description="return only cloud ide compatible providers"),
        ],
        type_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one type in input filter list"),
        ],
        tier_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one tier in input filter list"),
        ],
        category_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one category in input filter list"),
        ],
        badge_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one badge in input filter list"),
        ],
        provider_id: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has one id in input filter list"),
        ],
        tier_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one tier name in input filter list"),
        ],
        category_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one category name in input filter list"),
        ],
        badge_name: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Has at least one badge name in input filter list"),
        ],
        query: Annotated[
            Optional[StrictStr], Field(description="Search query for provider")
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for pagination"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
    ) -> ProvidersPaginated:
        api = api_group.ProviderApi(self.client)
        response = api.list_providers(
            org_short_name_id=org_short_name_id,
            is_certified=is_certified,
            is_featured=is_featured,
            is_global=is_global,
            is_private=is_private,
            is_cloud_ide_compatible=is_cloud_ide_compatible,
            type_name=type_name,
            tier_id=tier_id,
            category_id=category_id,
            badge_id=badge_id,
            provider_id=provider_id,
            tier_name=tier_name,
            category_name=category_name,
            badge_name=badge_name,
            query=query,
            offset=offset,
            limit=limit,
            sorts=sorts,
        )
        return response

    def update_provider(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        provider_name: Annotated[
            StrictStr, Field(..., description="The name of the provider")
        ],
        version: Annotated[
            StrictStr, Field(..., description="The version of the provider")
        ],
        body: Annotated[
            UpdateProviderRequest,
            Field(..., description="request body for updating a registry provider"),
        ],
    ) -> Provider:
        api = api_group.ProviderApi(self.client)
        response = api.update_provider(
            org_short_name_id=org_short_name_id,
            provider_name=provider_name,
            version=version,
            body=body,
        )
        return response

    def search(
        self,
        org_short_name_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        body: Annotated[
            RegistrySearchRequest,
            Field(..., description="request body for a registry search"),
        ],
        is_certified: Annotated[
            Optional[StrictBool], Field(description="return only certified providers")
        ],
        is_featured: Annotated[
            Optional[StrictBool], Field(description="return only featured providers")
        ],
        is_global: Annotated[
            Optional[StrictBool], Field(description="return only global providers")
        ],
        is_private: Annotated[
            Optional[StrictBool], Field(description="return only private providers")
        ],
        is_cloud_ide_compatible: Annotated[
            Optional[StrictBool],
            Field(description="return only cloud ide compatible providers"),
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for pagination"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'. Default to searchRank:asc"
            ),
        ],
    ) -> RegistrySearch:
        api = api_group.SearchApi(self.client)
        response = api.search(
            org_short_name_id=org_short_name_id,
            body=body,
            is_certified=is_certified,
            is_featured=is_featured,
            is_global=is_global,
            is_private=is_private,
            is_cloud_ide_compatible=is_cloud_ide_compatible,
            offset=offset,
            limit=limit,
            sorts=sorts,
        )
        return response

