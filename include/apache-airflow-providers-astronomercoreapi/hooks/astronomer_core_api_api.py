from __future__ import annotations

from functools import cached_property

from client.astronomercoreapi import ApiClient
import client.astronomercoreapi.api as api_group

from client.astronomercoreapi.models import (
    AddTeamMembersRequest,
    ApiToken,
    AstroRelease,
    Cell,
    CellRun,
    CellRunTaskFigures,
    CellRunTaskLogs,
    CellRunTaskResults,
    CellsPaginated,
    ClearDagRun,
    ClearDagRunRequest,
    ClearTaskInstancesRequest,
    Cluster,
    ClusterDetailed,
    ClusterOptions,
    ClustersPaginated,
    Code,
    Connection,
    ConnectionsPaginated,
    CreateAwsClusterRequest,
    CreateAzureClusterRequest,
    CreateCell,
    CreateCellRequest,
    CreateCellRun,
    CreateCellRunRequest,
    CreateCellType,
    CreateCellTypeRequest,
    CreateDagRun,
    CreateDagRunRequest,
    CreateDeploymentRequest,
    CreateGcpClusterRequest,
    CreateManagedDomainRequest,
    CreateOrganizationApiTokenRequest,
    CreateOrganizationRequest,
    CreatePipeline,
    CreatePipelineRequest,
    CreatePipelineSession,
    CreateProject,
    CreateProjectGitBranchRequest,
    CreateProjectGitCommitRequest,
    CreateProjectRequest,
    CreateSsoConnectionRequest,
    CreateTeamRequest,
    CreateUserInviteRequest,
    CreateWorkspaceApiTokenRequest,
    CreateWorkspaceRequest,
    DagFilters,
    DagRun,
    DagRunsPaginated,
    DagsPaginated,
    Deployment,
    DeploymentLog,
    DeploymentOptions,
    DeploymentsPaginated,
    DuplicateCell,
    DuplicateCellRequest,
    GetCellType,
    HasPermissions,
    HasPermissionsRequest,
    InstantMetricPerComponentStatus,
    InstantMetricPerPoolStatus,
    InstantMetricsPaginated,
    InternalDagStructure,
    InternalPaginationResultDagRunWithTaskInstances,
    Invite,
    ListApiTokensPaginated,
    ListCellTypes,
    ListWorkspaceDags,
    ManagedDomain,
    ModelSelf,
    MutateConnectionRequest,
    MutateOrgTeamRoleRequest,
    MutateOrgUserRoleRequest,
    MutateVRRequirementsRequest,
    MutateVRVariablesRequest,
    MutateVirtualRuntimeRequest,
    MutateWorkspaceTeamRoleRequest,
    MutateWorkspaceUserRoleRequest,
    Organization,
    Pipeline,
    PipelinesPaginated,
    PostDagRun,
    PostDagRunRequest,
    Project,
    ProjectGitBranch,
    ProjectGitBranchesPaginated,
    ProjectGitCommit,
    ProjectGitCommitsPaginated,
    ProjectGitComparison,
    ProjectsPaginated,
    RangeMetric,
    RangeMetricPerComponent,
    RangeMetricPerComponentAndQueueAndStatus,
    RangeMetricPerPod,
    RangeMetricPerStatus,
    RangeMetricsPaginated,
    RangeMetricsPerStatusPaginated,
    RunsWithGroups,
    Runtime,
    RuntimeDag,
    RuntimeDagsPaginated,
    RuntimeImportErrorsPaginated,
    RuntimeRelease,
    RuntimesPaginated,
    SharedCluster,
    SsoBypassKey,
    SsoConnection,
    SsoLoginCallback,
    TaskInstance,
    TaskInstanceLogs,
    TaskInstanceReference,
    TaskInstanceReferences,
    TaskInstancesPaginated,
    Team,
    TeamRole,
    TeamsPaginated,
    TestConnection,
    TestConnectionRequest,
    UpdateAwsClusterRequest,
    UpdateAzureClusterRequest,
    UpdateCellRequest,
    UpdateCellTypeRequest,
    UpdateDag,
    UpdateDagRunRequest,
    UpdateDeploymentRequest,
    UpdateGcpClusterRequest,
    UpdateInviteRequest,
    UpdateManagedDomainRequest,
    UpdateOrganizationApiTokenRequest,
    UpdateOrganizationRequest,
    UpdatePipelineRequest,
    UpdateProjectRequest,
    UpdateRuntimeDag,
    UpdateRuntimeDagRequest,
    UpdateSsoConnectionRequest,
    UpdateTaskInstanceRequest,
    UpdateTaskInstancesStateRequest,
    UpdateTeamRequest,
    UpdateWorkspaceApiTokenRequest,
    UpdateWorkspaceRequest,
    User,
    UserRole,
    UsersPaginated,
    VRDagRunTaskInstancesPaginated,
    VRDagRunsPaginated,
    VRDagsPaginated,
    VRImportErrorsPaginated,
    VRRequirements,
    VRVariables,
    ValidateCellType,
    ValidateCellTypeRequest,
    ValidateSsoLoginRequest,
    VirtualRuntime,
    VirtualRuntimesPaginated,
    Workspace,
    WorkspaceRangeMetricPerStatus,
    WorkspacesPaginated,
)

from client.astronomercoreapi.configuration import Configuration
from airflow.models import Connection

from airflow.hooks.base import BaseHook
from typing import Optional, Union, List, Dict
from typing_extensions import Annotated
from pydantic import Field, StrictBool, StrictInt, StrictStr, conint, conlist


class AstronomerCoreApiHook(BaseHook):
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

    def create_organization_api_token(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        body: Annotated[
            CreateOrganizationApiTokenRequest,
            Field(
                ..., description="request body for creating an organization API token"
            ),
        ],
    ) -> ApiToken:
        api = api_group.ApiTokenApi(self.client)
        response = api.create_organization_api_token(
            organization_id=organization_id,
            body=body,
        )
        return response

    def create_workspace_api_token(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        body: Annotated[
            CreateWorkspaceApiTokenRequest,
            Field(..., description="request body for creating a workspace API token"),
        ],
    ) -> ApiToken:
        api = api_group.ApiTokenApi(self.client)
        response = api.create_workspace_api_token(
            organization_id=organization_id,
            workspace_id=workspace_id,
            body=body,
        )
        return response

    def delete_organization_api_token(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        api_token_id: Annotated[StrictStr, Field(..., description="API token ID")],
    ) -> None:
        api = api_group.ApiTokenApi(self.client)
        response = api.delete_organization_api_token(
            organization_id=organization_id,
            api_token_id=api_token_id,
        )
        return response

    def delete_workspace_api_token(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        api_token_id: Annotated[
            StrictStr, Field(..., description="ID of the API token")
        ],
    ) -> None:
        api = api_group.ApiTokenApi(self.client)
        response = api.delete_workspace_api_token(
            organization_id=organization_id,
            workspace_id=workspace_id,
            api_token_id=api_token_id,
        )
        return response

    def get_organization_api_token(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        api_token_id: Annotated[StrictStr, Field(..., description="API token ID")],
    ) -> ApiToken:
        api = api_group.ApiTokenApi(self.client)
        response = api.get_organization_api_token(
            organization_id=organization_id,
            api_token_id=api_token_id,
        )
        return response

    def get_workspace_api_token(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        api_token_id: Annotated[StrictStr, Field(..., description="API token ID")],
    ) -> ApiToken:
        api = api_group.ApiTokenApi(self.client)
        response = api.get_workspace_api_token(
            organization_id=organization_id,
            workspace_id=workspace_id,
            api_token_id=api_token_id,
        )
        return response

    def list_organization_api_tokens(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="Offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="Limit for pagination"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="Sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
    ) -> ListApiTokensPaginated:
        api = api_group.ApiTokenApi(self.client)
        response = api.list_organization_api_tokens(
            organization_id=organization_id,
            offset=offset,
            limit=limit,
            sorts=sorts,
        )
        return response

    def list_workspace_api_tokens(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="Offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="Limit for pagination"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="Sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
    ) -> ListApiTokensPaginated:
        api = api_group.ApiTokenApi(self.client)
        response = api.list_workspace_api_tokens(
            organization_id=organization_id,
            workspace_id=workspace_id,
            offset=offset,
            limit=limit,
            sorts=sorts,
        )
        return response

    def rotate_organization_api_token(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        api_token_id: Annotated[StrictStr, Field(..., description="API token ID")],
    ) -> ApiToken:
        api = api_group.ApiTokenApi(self.client)
        response = api.rotate_organization_api_token(
            organization_id=organization_id,
            api_token_id=api_token_id,
        )
        return response

    def rotate_workspace_api_token(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        api_token_id: Annotated[StrictStr, Field(..., description="API token ID")],
    ) -> ApiToken:
        api = api_group.ApiTokenApi(self.client)
        response = api.rotate_workspace_api_token(
            organization_id=organization_id,
            workspace_id=workspace_id,
            api_token_id=api_token_id,
        )
        return response

    def update_organization_api_token(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        api_token_id: Annotated[StrictStr, Field(..., description="API token ID")],
        body: Annotated[
            UpdateOrganizationApiTokenRequest,
            Field(
                ..., description="request body for updating an organization API token"
            ),
        ],
    ) -> ApiToken:
        api = api_group.ApiTokenApi(self.client)
        response = api.update_organization_api_token(
            organization_id=organization_id,
            api_token_id=api_token_id,
            body=body,
        )
        return response

    def update_workspace_api_token(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        api_token_id: Annotated[StrictStr, Field(..., description="API token ID")],
        body: Annotated[
            UpdateWorkspaceApiTokenRequest,
            Field(..., description="request body for updating a workspace API token"),
        ],
    ) -> ApiToken:
        api = api_group.ApiTokenApi(self.client)
        response = api.update_workspace_api_token(
            organization_id=organization_id,
            workspace_id=workspace_id,
            api_token_id=api_token_id,
            body=body,
        )
        return response

    def get_user_invite(
        self,
        invite_id: Annotated[
            StrictStr, Field(..., description="invite ID or auth0 ticket ID")
        ],
    ) -> Invite:
        api = api_group.AuthApi(self.client)
        response = api.get_user_invite(
            invite_id=invite_id,
        )
        return response

    def validate_sso_bypass_key(
        self,
        sso_bypass_key: Annotated[
            StrictStr, Field(..., description="SSO bypass key for organization")
        ],
    ) -> SsoBypassKey:
        api = api_group.AuthApi(self.client)
        response = api.validate_sso_bypass_key(
            sso_bypass_key=sso_bypass_key,
        )
        return response

    def has_permissions(
        self,
        body: Annotated[
            HasPermissionsRequest,
            Field(..., description="request body for get permissions"),
        ],
    ) -> HasPermissions:
        api = api_group.AuthzApi(self.client)
        response = api.has_permissions(
            body=body,
        )
        return response

    def create_cell(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[StrictStr, Field(..., description="project ID")],
        pipeline_id: Annotated[StrictStr, Field(..., description="pipeline ID")],
        data: Annotated[
            CreateCellRequest,
            Field(..., description="request body for creating a new cell"),
        ],
    ) -> CreateCell:
        api = api_group.CloudIDECellApi(self.client)
        response = api.create_cell(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
            data=data,
        )
        return response

    def delete_cell(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        project_id: Annotated[StrictStr, Field(..., description="ID of the project")],
        pipeline_id: Annotated[StrictStr, Field(..., description="ID of the pipeline")],
        cell_id: Annotated[StrictStr, Field(..., description="ID of the cell")],
    ) -> None:
        api = api_group.CloudIDECellApi(self.client)
        response = api.delete_cell(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
            cell_id=cell_id,
        )
        return response

    def duplicate_cell(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        project_id: Annotated[StrictStr, Field(..., description="ID of the project")],
        pipeline_id: Annotated[StrictStr, Field(..., description="ID of the pipeline")],
        cell_id: Annotated[StrictStr, Field(..., description="ID of the cell")],
        data: Annotated[
            DuplicateCellRequest,
            Field(..., description="request body for duplicating a cell"),
        ],
    ) -> DuplicateCell:
        api = api_group.CloudIDECellApi(self.client)
        response = api.duplicate_cell(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
            cell_id=cell_id,
            data=data,
        )
        return response

    def get_cell(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        pipeline_id: Annotated[
            StrictStr, Field(..., description="The ID of the pipeline")
        ],
        cell_id: Annotated[StrictStr, Field(..., description="ID of the cell")],
    ) -> Cell:
        api = api_group.CloudIDECellApi(self.client)
        response = api.get_cell(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
            cell_id=cell_id,
        )
        return response

    def list_cells(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        pipeline_id: Annotated[
            StrictStr, Field(..., description="The ID of the pipeline")
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
        include_cell_types: Annotated[
            Optional[StrictBool], Field(description="include cell types in response")
        ],
        pipeline_session_id: Annotated[
            Optional[StrictStr], Field(description="pipeline session ID")
        ],
    ) -> CellsPaginated:
        api = api_group.CloudIDECellApi(self.client)
        response = api.list_cells(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
            offset=offset,
            limit=limit,
            sorts=sorts,
            include_cell_types=include_cell_types,
            pipeline_session_id=pipeline_session_id,
        )
        return response

    def update_cell(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        project_id: Annotated[StrictStr, Field(..., description="ID of the project")],
        pipeline_id: Annotated[StrictStr, Field(..., description="ID of the pipeline")],
        cell_id: Annotated[StrictStr, Field(..., description="ID of the cell")],
        data: Annotated[
            UpdateCellRequest,
            Field(..., description="request body for updating a cell"),
        ],
    ) -> None:
        api = api_group.CloudIDECellApi(self.client)
        response = api.update_cell(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
            cell_id=cell_id,
            data=data,
        )
        return response

    def create_cell_type(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[StrictStr, Field(..., description="project ID")],
        data: Annotated[
            CreateCellTypeRequest,
            Field(..., description="request body for creating a new cell type"),
        ],
    ) -> CreateCellType:
        api = api_group.CloudIDECellTypeApi(self.client)
        response = api.create_cell_type(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            data=data,
        )
        return response

    def delete_cell_type(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[StrictStr, Field(..., description="project ID")],
        cell_type_name: Annotated[StrictStr, Field(..., description="cell type name")],
    ) -> None:
        api = api_group.CloudIDECellTypeApi(self.client)
        response = api.delete_cell_type(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            cell_type_name=cell_type_name,
        )
        return response

    def get_cell_type(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[StrictStr, Field(..., description="project ID")],
        cell_type_name: Annotated[StrictStr, Field(..., description="cell type name")],
    ) -> GetCellType:
        api = api_group.CloudIDECellTypeApi(self.client)
        response = api.get_cell_type(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            cell_type_name=cell_type_name,
        )
        return response

    def list_cell_types(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[StrictStr, Field(..., description="project ID")],
        names: Annotated[
            Optional[StrictStr],
            Field(description="cell type names to filter by, comma-separated"),
        ],
    ) -> ListCellTypes:
        api = api_group.CloudIDECellTypeApi(self.client)
        response = api.list_cell_types(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            names=names,
        )
        return response

    def update_cell_type(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[StrictStr, Field(..., description="project ID")],
        cell_type_name: Annotated[StrictStr, Field(..., description="cell type name")],
        data: Annotated[
            UpdateCellTypeRequest,
            Field(..., description="request body for updating a cell type"),
        ],
    ) -> None:
        api = api_group.CloudIDECellTypeApi(self.client)
        response = api.update_cell_type(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            cell_type_name=cell_type_name,
            data=data,
        )
        return response

    def validate_cell_type(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[StrictStr, Field(..., description="project ID")],
        data: Annotated[
            ValidateCellTypeRequest,
            Field(..., description="request body for validating a cell type"),
        ],
    ) -> ValidateCellType:
        api = api_group.CloudIDECellTypeApi(self.client)
        response = api.validate_cell_type(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            data=data,
        )
        return response

    def create_pipeline(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[StrictStr, Field(..., description="project ID")],
        data: Annotated[
            CreatePipelineRequest,
            Field(..., description="request body for creating a new pipeline"),
        ],
    ) -> CreatePipeline:
        api = api_group.CloudIDEPipelineApi(self.client)
        response = api.create_pipeline(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            data=data,
        )
        return response

    def delete_pipeline(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        pipeline_id: Annotated[StrictStr, Field(..., description="ID of the pipeline")],
    ) -> None:
        api = api_group.CloudIDEPipelineApi(self.client)
        response = api.delete_pipeline(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
        )
        return response

    def get_pipeline(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        pipeline_id: Annotated[StrictStr, Field(..., description="ID of the pipeline")],
    ) -> Pipeline:
        api = api_group.CloudIDEPipelineApi(self.client)
        response = api.get_pipeline(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
        )
        return response

    def list_pipelines(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="workspace IDs the pipelines belong to"),
        ],
        project_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="project IDs the pipelines belong to"),
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for pagination"),
        ],
        search: Annotated[
            Optional[StrictStr],
            Field(description="search string across pipeline name and description"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
    ) -> PipelinesPaginated:
        api = api_group.CloudIDEPipelineApi(self.client)
        response = api.list_pipelines(
            organization_id=organization_id,
            workspace_ids=workspace_ids,
            project_ids=project_ids,
            offset=offset,
            limit=limit,
            search=search,
            sorts=sorts,
        )
        return response

    def update_pipeline(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        project_id: Annotated[StrictStr, Field(..., description="ID of the project")],
        pipeline_id: Annotated[StrictStr, Field(..., description="ID of the pipeline")],
        data: Annotated[
            UpdatePipelineRequest,
            Field(..., description="request body for updating a pipeline"),
        ],
    ) -> None:
        api = api_group.CloudIDEPipelineApi(self.client)
        response = api.update_pipeline(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
            data=data,
        )
        return response

    def create_project(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        data: Annotated[
            CreateProjectRequest,
            Field(..., description="request body for creating a new project"),
        ],
    ) -> CreateProject:
        api = api_group.CloudIDEProjectApi(self.client)
        response = api.create_project(
            organization_id=organization_id,
            workspace_id=workspace_id,
            data=data,
        )
        return response

    def create_project_git_branch(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        data: Annotated[
            CreateProjectGitBranchRequest,
            Field(..., description="request body for creating a new branch"),
        ],
    ) -> ProjectGitBranch:
        api = api_group.CloudIDEProjectApi(self.client)
        response = api.create_project_git_branch(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            data=data,
        )
        return response

    def create_project_git_commit(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        data: Annotated[
            CreateProjectGitCommitRequest,
            Field(..., description="request body for creating a new commit"),
        ],
    ) -> ProjectGitCommit:
        api = api_group.CloudIDEProjectApi(self.client)
        response = api.create_project_git_commit(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            data=data,
        )
        return response

    def delete_project(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
    ) -> None:
        api = api_group.CloudIDEProjectApi(self.client)
        response = api.delete_project(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
        )
        return response

    def get_project(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        include_pipeline_count: Annotated[
            Optional[StrictBool],
            Field(description="Include pipeline count for the project"),
        ],
    ) -> Project:
        api = api_group.CloudIDEProjectApi(self.client)
        response = api.get_project(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            include_pipeline_count=include_pipeline_count,
        )
        return response

    def get_project_git_comparison(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        branch: Annotated[
            Optional[StrictStr],
            Field(
                description="The branch to compare against, if different to the project's branch"
            ),
        ],
        exclude_config: Annotated[
            Optional[StrictBool],
            Field(description="Whether to exclude config files from the comparison"),
        ],
        pipeline_id: Annotated[
            Optional[StrictStr],
            Field(description="only include changes for this pipeline"),
        ],
    ) -> ProjectGitComparison:
        api = api_group.CloudIDEProjectApi(self.client)
        response = api.get_project_git_comparison(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            branch=branch,
            exclude_config=exclude_config,
            pipeline_id=pipeline_id,
        )
        return response

    def list_project_git_branches(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="Workspace ID that the project belong to")
        ],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        repo: Annotated[
            Optional[StrictStr],
            Field(description="a repo to override the project's repo"),
        ],
        vendor: Annotated[
            Optional[StrictStr],
            Field(description="a vendor to override the project's git vendor"),
        ],
        azure_dev_ops_organization: Annotated[
            Optional[StrictStr],
            Field(
                description="an Azure DevOps organization to override the project's git vendor attributes"
            ),
        ],
        azure_dev_ops_project_id: Annotated[
            Optional[StrictStr],
            Field(
                description="an Azure DevOps project ID to override the project's git vendor attributes"
            ),
        ],
        page: Annotated[
            Optional[conint(strict=True, ge=1)],
            Field(description="page number for pagination"),
        ],
        per_page: Annotated[
            Optional[conint(strict=True, ge=1)],
            Field(description="page size for pagination"),
        ],
        x_git_token: Annotated[
            Optional[StrictStr],
            Field(description="a token to override the project's token"),
        ],
    ) -> ProjectGitBranchesPaginated:
        api = api_group.CloudIDEProjectApi(self.client)
        response = api.list_project_git_branches(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            repo=repo,
            vendor=vendor,
            azure_dev_ops_organization=azure_dev_ops_organization,
            azure_dev_ops_project_id=azure_dev_ops_project_id,
            page=page,
            per_page=per_page,
            x_git_token=x_git_token,
        )
        return response

    def list_project_git_commits(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="Workspace ID that the project belong to")
        ],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        branch: Annotated[
            Optional[StrictStr],
            Field(
                description="The branch to list commits for, if different to the project's branch"
            ),
        ],
        page: Annotated[
            Optional[conint(strict=True, ge=1)],
            Field(description="page number for pagination"),
        ],
        per_page: Annotated[
            Optional[conint(strict=True, ge=1)],
            Field(description="page size for pagination"),
        ],
    ) -> ProjectGitCommitsPaginated:
        api = api_group.CloudIDEProjectApi(self.client)
        response = api.list_project_git_commits(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            branch=branch,
            page=page,
            per_page=per_page,
        )
        return response

    def list_projects(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="Workspace IDs that projects belong to"),
        ],
        include_pipeline_counts: Annotated[
            Optional[StrictBool],
            Field(description="Include pipeline counts for each project"),
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for pagination"),
        ],
        search: Annotated[
            Optional[StrictStr],
            Field(description="search string across name and description"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
    ) -> ProjectsPaginated:
        api = api_group.CloudIDEProjectApi(self.client)
        response = api.list_projects(
            organization_id=organization_id,
            workspace_ids=workspace_ids,
            include_pipeline_counts=include_pipeline_counts,
            offset=offset,
            limit=limit,
            search=search,
            sorts=sorts,
        )
        return response

    def sync_project_include(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        include_id: Annotated[
            StrictStr, Field(..., description="The name of the include")
        ],
    ) -> None:
        api = api_group.CloudIDEProjectApi(self.client)
        response = api.sync_project_include(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            include_id=include_id,
        )
        return response

    def test_connection(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        data: Annotated[
            TestConnectionRequest,
            Field(..., description="request body for testing a connection"),
        ],
    ) -> TestConnection:
        api = api_group.CloudIDEProjectApi(self.client)
        response = api.test_connection(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            data=data,
        )
        return response

    def test_project_connection(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        connection_id: Annotated[
            StrictStr, Field(..., description="The ID of the connection")
        ],
    ) -> TestConnection:
        api = api_group.CloudIDEProjectApi(self.client)
        response = api.test_project_connection(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            connection_id=connection_id,
        )
        return response

    def update_project(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        data: Annotated[
            UpdateProjectRequest,
            Field(..., description="request body for updating a project"),
        ],
    ) -> None:
        api = api_group.CloudIDEProjectApi(self.client)
        response = api.update_project(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            data=data,
        )
        return response

    def create_cell_run(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[StrictStr, Field(..., description="project ID")],
        pipeline_id: Annotated[StrictStr, Field(..., description="pipeline ID")],
        cell_id: Annotated[StrictStr, Field(..., description="cell ID")],
        data: Annotated[
            CreateCellRunRequest,
            Field(..., description="request body for creating a new cell run"),
        ],
    ) -> CreateCellRun:
        api = api_group.CloudIDERunApi(self.client)
        response = api.create_cell_run(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
            cell_id=cell_id,
            data=data,
        )
        return response

    def create_pipeline_session(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[StrictStr, Field(..., description="project ID")],
        pipeline_id: Annotated[StrictStr, Field(..., description="pipeline ID")],
    ) -> CreatePipelineSession:
        api = api_group.CloudIDERunApi(self.client)
        response = api.create_pipeline_session(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
        )
        return response

    def get_cell_run(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        pipeline_id: Annotated[
            StrictStr, Field(..., description="The ID of the pipeline")
        ],
        cell_id: Annotated[StrictStr, Field(..., description="ID of the cell")],
        cell_run_id: Annotated[StrictStr, Field(..., description="ID of the cell run")],
    ) -> CellRun:
        api = api_group.CloudIDERunApi(self.client)
        response = api.get_cell_run(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
            cell_id=cell_id,
            cell_run_id=cell_run_id,
        )
        return response

    def get_cell_run_task_figures(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        pipeline_id: Annotated[
            StrictStr, Field(..., description="The ID of the pipeline")
        ],
        cell_id: Annotated[StrictStr, Field(..., description="ID of the cell")],
        cell_run_id: Annotated[StrictStr, Field(..., description="ID of the cell run")],
        task_id: Annotated[StrictStr, Field(..., description="ID of the task")],
    ) -> CellRunTaskFigures:
        api = api_group.CloudIDERunApi(self.client)
        response = api.get_cell_run_task_figures(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
            cell_id=cell_id,
            cell_run_id=cell_run_id,
            task_id=task_id,
        )
        return response

    def get_cell_run_task_logs(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        pipeline_id: Annotated[
            StrictStr, Field(..., description="The ID of the pipeline")
        ],
        cell_id: Annotated[StrictStr, Field(..., description="ID of the cell")],
        cell_run_id: Annotated[StrictStr, Field(..., description="ID of the cell run")],
        task_id: Annotated[StrictStr, Field(..., description="ID of the task")],
        var_from: Annotated[
            Optional[StrictInt], Field(description="The line number to start from")
        ],
    ) -> CellRunTaskLogs:
        api = api_group.CloudIDERunApi(self.client)
        response = api.get_cell_run_task_logs(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
            cell_id=cell_id,
            cell_run_id=cell_run_id,
            task_id=task_id,
            var_from=var_from,
        )
        return response

    def get_cell_run_task_results(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        project_id: Annotated[
            StrictStr, Field(..., description="The ID of the project")
        ],
        pipeline_id: Annotated[
            StrictStr, Field(..., description="The ID of the pipeline")
        ],
        cell_id: Annotated[StrictStr, Field(..., description="ID of the cell")],
        cell_run_id: Annotated[StrictStr, Field(..., description="ID of the cell run")],
        task_id: Annotated[StrictStr, Field(..., description="ID of the task")],
    ) -> CellRunTaskResults:
        api = api_group.CloudIDERunApi(self.client)
        response = api.get_cell_run_task_results(
            organization_id=organization_id,
            workspace_id=workspace_id,
            project_id=project_id,
            pipeline_id=pipeline_id,
            cell_id=cell_id,
            cell_run_id=cell_run_id,
            task_id=task_id,
        )
        return response

    def create_aws_cluster(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        body: Annotated[
            CreateAwsClusterRequest,
            Field(..., description="request body for creating a new AWS cluster"),
        ],
    ) -> Cluster:
        api = api_group.ClusterApi(self.client)
        response = api.create_aws_cluster(
            organization_id=organization_id,
            body=body,
        )
        return response

    def create_azure_cluster(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        body: Annotated[
            CreateAzureClusterRequest,
            Field(..., description="request body for creating a new Azure cluster"),
        ],
    ) -> Cluster:
        api = api_group.ClusterApi(self.client)
        response = api.create_azure_cluster(
            organization_id=organization_id,
            body=body,
        )
        return response

    def create_gcp_cluster(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        body: Annotated[
            CreateGcpClusterRequest,
            Field(..., description="request body for creating a new GCP cluster"),
        ],
    ) -> Cluster:
        api = api_group.ClusterApi(self.client)
        response = api.create_gcp_cluster(
            organization_id=organization_id,
            body=body,
        )
        return response

    def delete_cluster(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        cluster_id: Annotated[StrictStr, Field(..., description="cluster ID")],
    ) -> None:
        api = api_group.ClusterApi(self.client)
        response = api.delete_cluster(
            organization_id=organization_id,
            cluster_id=cluster_id,
        )
        return response

    def get_cluster(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        cluster_id: Annotated[StrictStr, Field(..., description="cluster ID to fetch")],
    ) -> ClusterDetailed:
        api = api_group.ClusterApi(self.client)
        response = api.get_cluster(
            organization_id=organization_id,
            cluster_id=cluster_id,
        )
        return response

    def get_shared_cluster(
        self,
        region: Annotated[StrictStr, Field(..., description="region")],
        cloud_provider: Annotated[StrictStr, Field(..., description="cloud provider")],
    ) -> SharedCluster:
        api = api_group.ClusterApi(self.client)
        response = api.get_shared_cluster(
            region=region,
            cloud_provider=cloud_provider,
        )
        return response

    def list_clusters(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        provider: Annotated[
            Optional[StrictStr],
            Field(description="cloud provider to filter clusters on"),
        ],
        types: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="type to filter clusters on"),
        ],
        status: Annotated[
            Optional[StrictStr], Field(description="status to filter clusters on")
        ],
        search: Annotated[
            Optional[StrictStr],
            Field(description="string to search for when listing clusters"),
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
    ) -> ClustersPaginated:
        api = api_group.ClusterApi(self.client)
        response = api.list_clusters(
            organization_id=organization_id,
            provider=provider,
            types=types,
            status=status,
            search=search,
            offset=offset,
            limit=limit,
            sorts=sorts,
        )
        return response

    def update_aws_cluster(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        cluster_id: Annotated[StrictStr, Field(..., description="cluster ID")],
        body: Annotated[
            UpdateAwsClusterRequest,
            Field(..., description="request body for updating an AWS cluster"),
        ],
    ) -> Cluster:
        api = api_group.ClusterApi(self.client)
        response = api.update_aws_cluster(
            organization_id=organization_id,
            cluster_id=cluster_id,
            body=body,
        )
        return response

    def update_azure_cluster(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        cluster_id: Annotated[StrictStr, Field(..., description="cluster ID")],
        body: Annotated[
            UpdateAzureClusterRequest,
            Field(..., description="request body for updating an Azure cluster"),
        ],
    ) -> Cluster:
        api = api_group.ClusterApi(self.client)
        response = api.update_azure_cluster(
            organization_id=organization_id,
            cluster_id=cluster_id,
            body=body,
        )
        return response

    def update_gcp_cluster(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        cluster_id: Annotated[StrictStr, Field(..., description="cluster ID")],
        body: Annotated[
            UpdateGcpClusterRequest,
            Field(..., description="request body for updating a GCP cluster"),
        ],
    ) -> Cluster:
        api = api_group.ClusterApi(self.client)
        response = api.update_gcp_cluster(
            organization_id=organization_id,
            cluster_id=cluster_id,
            body=body,
        )
        return response

    def get_runs_with_groups(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        dag_id: Annotated[StrictStr, Field(..., description="ID of the dag")],
        root: Annotated[
            Optional[StrictStr],
            Field(description="name of parent task to get grid data for"),
        ],
        run_state: Annotated[
            Optional[StrictStr], Field(description="run state to filter on")
        ],
        run_type: Annotated[
            Optional[StrictStr], Field(description="run type to filter on")
        ],
        base_date: Annotated[Optional[datetime], Field(description="base date")],
        num_runs: Annotated[
            Optional[StrictStr],
            Field(description="number of runs to select grid data for"),
        ],
    ) -> RunsWithGroups:
        api = api_group.DagApi(self.client)
        response = api.get_runs_with_groups(
            organization_id=organization_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
            dag_id=dag_id,
            root=root,
            run_state=run_state,
            run_type=run_type,
            base_date=base_date,
            num_runs=num_runs,
        )
        return response

    def list_dags(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="ID that defines the workspaces where dags belong to"),
        ],
        deployment_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="ID that defines the deployments where dags belong to"),
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
            organization_id=organization_id,
            workspace_ids=workspace_ids,
            deployment_ids=deployment_ids,
            offset=offset,
            limit=limit,
            sorts=sorts,
        )
        return response

    def clear_dag_run(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        dag_id: Annotated[StrictStr, Field(..., description="dag ID")],
        dag_run_id: Annotated[StrictStr, Field(..., description="dag run ID")],
        data: Annotated[
            ClearDagRunRequest,
            Field(..., description="request body for clearing a dag run"),
        ],
    ) -> ClearDagRun:
        api = api_group.DagRunApi(self.client)
        response = api.clear_dag_run(
            organization_id=organization_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            data=data,
        )
        return response

    def update_dag_run(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        dag_id: Annotated[StrictStr, Field(..., description="dag ID")],
        dag_run_id: Annotated[StrictStr, Field(..., description="dag run ID")],
        data: Annotated[
            UpdateDagRunRequest,
            Field(..., description="request body for updating a dag run"),
        ],
    ) -> DagRun:
        api = api_group.DagRunApi(self.client)
        response = api.update_dag_run(
            organization_id=organization_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            data=data,
        )
        return response

    def create_deployment(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        body: Annotated[
            CreateDeploymentRequest,
            Field(..., description="request body for create a deployment"),
        ],
    ) -> Deployment:
        api = api_group.DeploymentApi(self.client)
        response = api.create_deployment(
            organization_id=organization_id,
            workspace_id=workspace_id,
            body=body,
        )
        return response

    def get_deployment_dag_runs(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(..., description="deployment ID to query for dags structure"),
        ],
        dag_id: Annotated[StrictStr, Field(..., description="dagId of the dags")],
        page_size: Annotated[
            Optional[conint(strict=True, le=100, ge=1)],
            Field(description="page size, default of 20"),
        ],
        cursor: Annotated[Optional[StrictStr], Field(description="pagination cursor")],
        run_id: Annotated[
            Optional[StrictStr], Field(description="filter by ID of the dags run")
        ],
        logical_date__lt: Annotated[
            Optional[datetime],
            Field(
                description="filter by logical date (aka execution date)  of  the  dags  run  less     than  (RFC3339 format)"
            ),
        ],
        logical_date__gt: Annotated[
            Optional[datetime],
            Field(
                description="filter by logical date (aka execution date)  of  the  dags  run  greater  than  (RFC3339 format)"
            ),
        ],
        start_date__lt: Annotated[
            Optional[datetime],
            Field(
                description="filter by start date of the dags run less than (RFC3339 format)"
            ),
        ],
        start_date__gt: Annotated[
            Optional[datetime],
            Field(
                description="filter by start date of the dags run greater than (RFC3339 format)"
            ),
        ],
        end_date__lt: Annotated[
            Optional[datetime],
            Field(
                description="filter by end date of the dags run less than (RFC3339 format)"
            ),
        ],
        end_date__gt: Annotated[
            Optional[datetime],
            Field(
                description="filter by end date of the dags run greater than (RFC3339 format)"
            ),
        ],
        state: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="filter by dags runs with any of these run states"),
        ],
        run_type__in: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="filter by dags runs with any of these run types"),
        ],
    ) -> InternalPaginationResultDagRunWithTaskInstances:
        api = api_group.DeploymentApi(self.client)
        response = api.get_deployment_dag_runs(
            organization_id=organization_id,
            deployment_id=deployment_id,
            dag_id=dag_id,
            page_size=page_size,
            cursor=cursor,
            run_id=run_id,
            logical_date__lt=logical_date__lt,
            logical_date__gt=logical_date__gt,
            start_date__lt=start_date__lt,
            start_date__gt=start_date__gt,
            end_date__lt=end_date__lt,
            end_date__gt=end_date__gt,
            state=state,
            run_type__in=run_type__in,
        )
        return response

    def get_deployment_dag_structure(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(..., description="deployment ID to query for dag structure"),
        ],
        dag_id: Annotated[StrictStr, Field(..., description="dagId of the dag")],
    ) -> InternalDagStructure:
        api = api_group.DeploymentApi(self.client)
        response = api.get_deployment_dag_structure(
            organization_id=organization_id,
            deployment_id=deployment_id,
            dag_id=dag_id,
        )
        return response

    def get_deployment_health(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(
                ..., description="deployment ID for which to return health information"
            ),
        ],
    ) -> Dict[str, object]:
        api = api_group.DeploymentApi(self.client)
        response = api.get_deployment_health(
            organization_id=organization_id,
            deployment_id=deployment_id,
        )
        return response

    def get_deployment_logs(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr, Field(..., description="deployment ID to get logs from")
        ],
        sources: Annotated[
            conlist(StrictStr),
            Field(..., description="log sources to select logs from"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=1)],
            Field(description="limit of the count of the logs"),
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset of the log entries"),
        ],
        range: Annotated[
            Optional[conint(strict=True, ge=60)],
            Field(description="range of the log search in seconds"),
        ],
        max_num_results: Annotated[
            Optional[conint(strict=True, ge=1)],
            Field(description="maximum number of results across all pages"),
        ],
        search_id: Annotated[
            Optional[StrictStr], Field(description="searchId to get logs from")
        ],
        search_text: Annotated[
            Optional[StrictStr],
            Field(description="an exact text search param used to filter the data on"),
        ],
    ) -> DeploymentLog:
        api = api_group.DeploymentApi(self.client)
        response = api.get_deployment_logs(
            organization_id=organization_id,
            deployment_id=deployment_id,
            sources=sources,
            limit=limit,
            offset=offset,
            range=range,
            max_num_results=max_num_results,
            search_id=search_id,
            search_text=search_text,
        )
        return response

    def list_deployments(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="IDs that define the deployments"),
        ],
        workspace_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="IDs that define the workspaces where deployments belong to"
            ),
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
    ) -> DeploymentsPaginated:
        api = api_group.DeploymentApi(self.client)
        response = api.list_deployments(
            organization_id=organization_id,
            deployment_ids=deployment_ids,
            workspace_ids=workspace_ids,
            offset=offset,
            limit=limit,
            sorts=sorts,
        )
        return response

    def update_deployment(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        deployment_id: Annotated[
            StrictStr, Field(..., description="ID of the deployment")
        ],
        body: Annotated[
            UpdateDeploymentRequest,
            Field(..., description="request body for updating a deployment"),
        ],
    ) -> Deployment:
        api = api_group.DeploymentApi(self.client)
        response = api.update_deployment(
            organization_id=organization_id,
            workspace_id=workspace_id,
            deployment_id=deployment_id,
            body=body,
        )
        return response

    def get_deployment_cpu_usage_limits(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(..., description="deployment ID corresponding to the metrics"),
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(..., description="range of the CPU usage limits metrics in seconds"),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(
                ...,
                description="step interval of the CPU usage limits metrics in seconds",
            ),
        ],
    ) -> List[RangeMetricPerComponent]:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.get_deployment_cpu_usage_limits(
            organization_id=organization_id,
            deployment_id=deployment_id,
            range=range,
            step=step,
        )
        return response

    def get_deployment_cpu_usages_per_pod(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(..., description="deployment ID corresponding to the metrics"),
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(..., description="range of the CPU usages metrics in seconds"),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(
                ..., description="step interval of the CPU usages metrics in seconds"
            ),
        ],
    ) -> List[RangeMetricPerPod]:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.get_deployment_cpu_usages_per_pod(
            organization_id=organization_id,
            deployment_id=deployment_id,
            range=range,
            step=step,
        )
        return response

    def get_deployment_memory_byte_limits(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(..., description="deployment ID corresponding to the metrics"),
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(
                ..., description="range of the memory byte limits metrics in seconds"
            ),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(
                ...,
                description="step interval of the memory byte limits metrics in seconds",
            ),
        ],
    ) -> List[RangeMetricPerComponent]:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.get_deployment_memory_byte_limits(
            organization_id=organization_id,
            deployment_id=deployment_id,
            range=range,
            step=step,
        )
        return response

    def get_deployment_memory_bytes_per_pod(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(..., description="deployment ID corresponding to the metrics"),
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(..., description="range of the memory bytes metrics in seconds"),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(
                ..., description="step interval of the memory bytes metrics in seconds"
            ),
        ],
    ) -> List[RangeMetricPerPod]:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.get_deployment_memory_bytes_per_pod(
            organization_id=organization_id,
            deployment_id=deployment_id,
            range=range,
            step=step,
        )
        return response

    def get_deployment_network_bytes_per_pod(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(..., description="deployment ID corresponding to the metrics"),
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(..., description="range of the network bytes metrics in seconds"),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(
                ..., description="step interval of the network bytes metrics in seconds"
            ),
        ],
    ) -> List[RangeMetricPerPod]:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.get_deployment_network_bytes_per_pod(
            organization_id=organization_id,
            deployment_id=deployment_id,
            range=range,
            step=step,
        )
        return response

    def get_deployment_scheduler_heartbeat(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(..., description="deployment ID corresponding to the metrics"),
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(
                ..., description="range of the scheduler heartbeats metrics in seconds"
            ),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(
                ...,
                description="step interval to find max per-minute scheduler heartbeats metrics in seconds",
            ),
        ],
    ) -> List[RangeMetric]:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.get_deployment_scheduler_heartbeat(
            organization_id=organization_id,
            deployment_id=deployment_id,
            range=range,
            step=step,
        )
        return response

    def get_deployments_dag_run_durations_per_status(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(..., description="deployment ID corresponding to the metrics"),
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(..., description="range of the DAG run durations metrics in seconds"),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(
                ...,
                description="step interval of the DAG run durations metrics in seconds",
            ),
        ],
        status: Annotated[Optional[StrictStr], Field(description="status of dag runs")],
    ) -> List[RangeMetricPerStatus]:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.get_deployments_dag_run_durations_per_status(
            organization_id=organization_id,
            deployment_id=deployment_id,
            range=range,
            step=step,
            status=status,
        )
        return response

    def get_deployments_dag_runs_per_status(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(..., description="deployment ID corresponding to the metrics"),
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(..., description="range of the DAG runs metrics in seconds"),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(..., description="step interval of the DAG runs metrics in seconds"),
        ],
        status: Annotated[Optional[StrictStr], Field(description="status of dag runs")],
    ) -> List[RangeMetricPerStatus]:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.get_deployments_dag_runs_per_status(
            organization_id=organization_id,
            deployment_id=deployment_id,
            range=range,
            step=step,
            status=status,
        )
        return response

    def get_deployments_task_run_durations_per_status(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(..., description="deployment ID corresponding to the metrics"),
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(
                ..., description="range of the task run durations metrics in seconds"
            ),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(
                ...,
                description="step interval of the task run durations metrics in seconds",
            ),
        ],
        status: Annotated[
            Optional[StrictStr], Field(description="status of task runs")
        ],
    ) -> List[RangeMetricPerStatus]:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.get_deployments_task_run_durations_per_status(
            organization_id=organization_id,
            deployment_id=deployment_id,
            range=range,
            step=step,
            status=status,
        )
        return response

    def get_deployments_task_runs_per_status(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(..., description="deployment ID corresponding to the metrics"),
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(..., description="range of the task runs metrics in seconds"),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(..., description="step interval of the task runs metrics in seconds"),
        ],
        status: Annotated[
            Optional[StrictStr], Field(description="status of task runs")
        ],
    ) -> List[RangeMetricPerStatus]:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.get_deployments_task_runs_per_status(
            organization_id=organization_id,
            deployment_id=deployment_id,
            range=range,
            step=step,
            status=status,
        )
        return response

    def get_pod_count_over_time(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(..., description="deployment ID corresponding to the metrics"),
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(..., description="range of pod count metrics in seconds"),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(..., description="step of pod count metrics in seconds"),
        ],
    ) -> List[RangeMetricPerComponentAndQueueAndStatus]:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.get_pod_count_over_time(
            organization_id=organization_id,
            deployment_id=deployment_id,
            range=range,
            step=step,
        )
        return response

    def list_deployments_cpu_usages(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(..., description="range of the CPU usages metrics in seconds"),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(
                ..., description="step interval of the CPU usages metrics in seconds"
            ),
        ],
        deployment_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="IDs that define the deployments"),
        ],
        workspace_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="IDs that define the workspaces where deployments belong to"
            ),
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for deployments pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for deployments pagination"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="sorting criteria for deployments, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
    ) -> RangeMetricsPaginated:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.list_deployments_cpu_usages(
            organization_id=organization_id,
            range=range,
            step=step,
            deployment_ids=deployment_ids,
            workspace_ids=workspace_ids,
            offset=offset,
            limit=limit,
            sorts=sorts,
        )
        return response

    def list_deployments_dag_runs(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(..., description="range of the DAG runs metrics in seconds"),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(..., description="step interval of the DAG runs metrics in seconds"),
        ],
        deployment_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="IDs that define the deployments"),
        ],
        workspace_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="IDs that define the workspaces where deployments belong to"
            ),
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for deployments pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for deployments pagination"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="sorting criteria for deployments, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
        status: Annotated[Optional[StrictStr], Field(description="status of dag runs")],
    ) -> RangeMetricsPerStatusPaginated:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.list_deployments_dag_runs(
            organization_id=organization_id,
            range=range,
            step=step,
            deployment_ids=deployment_ids,
            workspace_ids=workspace_ids,
            offset=offset,
            limit=limit,
            sorts=sorts,
            status=status,
        )
        return response

    def list_deployments_dagbag_sizes(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        deployment_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="IDs that define the deployments"),
        ],
        workspace_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="IDs that define the workspaces where deployments belong to"
            ),
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for deployments pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for deployments pagination"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="sorting criteria for deployments, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
    ) -> InstantMetricsPaginated:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.list_deployments_dagbag_sizes(
            organization_id=organization_id,
            deployment_ids=deployment_ids,
            workspace_ids=workspace_ids,
            offset=offset,
            limit=limit,
            sorts=sorts,
        )
        return response

    def list_deployments_memory_usages(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(..., description="range of the memory usages metrics in seconds"),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(
                ..., description="step interval of the memory usages metrics in seconds"
            ),
        ],
        deployment_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="IDs that define the deployments"),
        ],
        workspace_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="IDs that define the workspaces where deployments belong to"
            ),
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for deployments pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for deployments pagination"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="sorting criteria for deployments, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
    ) -> RangeMetricsPaginated:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.list_deployments_memory_usages(
            organization_id=organization_id,
            range=range,
            step=step,
            deployment_ids=deployment_ids,
            workspace_ids=workspace_ids,
            offset=offset,
            limit=limit,
            sorts=sorts,
        )
        return response

    def list_deployments_pod_count_per_status(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(..., description="deployment ID corresponding to the metrics"),
        ],
    ) -> List[InstantMetricPerComponentStatus]:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.list_deployments_pod_count_per_status(
            organization_id=organization_id,
            deployment_id=deployment_id,
        )
        return response

    def list_deployments_pool_count_per_status(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization FQN")
        ],
        deployment_id: Annotated[
            StrictStr,
            Field(..., description="deployment ID corresponding to the metrics"),
        ],
    ) -> List[InstantMetricPerPoolStatus]:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.list_deployments_pool_count_per_status(
            organization_id=organization_id,
            deployment_id=deployment_id,
        )
        return response

    def list_deployments_task_runs(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(..., description="range of the task runs metric in seconds"),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(..., description="step interval of task runs metric in seconds"),
        ],
        deployment_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="IDs that define the deployments"),
        ],
        workspace_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="IDs that define the workspaces where deployments belong to"
            ),
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for deployments pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for deployments pagination"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="sorting criteria for deployments, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
        status: Annotated[
            Optional[StrictStr], Field(description="status of task runs")
        ],
        include_deleted_deployments: Annotated[
            Optional[StrictBool],
            Field(
                description="results should include data from soft deleted deployments"
            ),
        ],
    ) -> RangeMetricsPerStatusPaginated:
        api = api_group.DeploymentMetricsApi(self.client)
        response = api.list_deployments_task_runs(
            organization_id=organization_id,
            range=range,
            step=step,
            deployment_ids=deployment_ids,
            workspace_ids=workspace_ids,
            offset=offset,
            limit=limit,
            sorts=sorts,
            status=status,
            include_deleted_deployments=include_deleted_deployments,
        )
        return response

    def create_user_invite(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        body: Annotated[
            CreateUserInviteRequest,
            Field(..., description="request body for create user invitation"),
        ],
    ) -> Invite:
        api = api_group.InviteApi(self.client)
        response = api.create_user_invite(
            organization_id=organization_id,
            body=body,
        )
        return response

    def delete_user_invite(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        invite_id: Annotated[StrictStr, Field(..., description="user invite ID")],
    ) -> None:
        api = api_group.InviteApi(self.client)
        response = api.delete_user_invite(
            organization_id=organization_id,
            invite_id=invite_id,
        )
        return response

    def get_user_invite(
        self,
        invite_id: Annotated[
            StrictStr, Field(..., description="invite ID or auth0 ticket ID")
        ],
    ) -> Invite:
        api = api_group.InviteApi(self.client)
        response = api.get_user_invite(
            invite_id=invite_id,
        )
        return response

    def update_self_user_invite(
        self,
        invite_id: Annotated[StrictStr, Field(..., description="invite ID")],
        body: Annotated[
            UpdateInviteRequest,
            Field(..., description="request body for update user self invitation"),
        ],
    ) -> Invite:
        api = api_group.InviteApi(self.client)
        response = api.update_self_user_invite(
            invite_id=invite_id,
            body=body,
        )
        return response

    def get_cluster_options(
        self,
        type: Annotated[StrictStr, Field(..., description="cluster type")],
        provider: Annotated[Optional[StrictStr], Field(description="cloud provider")],
    ) -> List[ClusterOptions]:
        api = api_group.OptionsApi(self.client)
        response = api.get_cluster_options(
            type=type,
            provider=provider,
        )
        return response

    def get_deployment_options(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
    ) -> DeploymentOptions:
        api = api_group.OptionsApi(self.client)
        response = api.get_deployment_options(
            organization_id=organization_id,
        )
        return response

    def create_managed_domain(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        body: Annotated[
            CreateManagedDomainRequest,
            Field(..., description="request body for creating a managed domain"),
        ],
    ) -> ManagedDomain:
        api = api_group.OrganizationApi(self.client)
        response = api.create_managed_domain(
            organization_id=organization_id,
            body=body,
        )
        return response

    def create_organization(
        self,
        body: Annotated[
            CreateOrganizationRequest,
            Field(..., description="request body for creating an organization"),
        ],
    ) -> Organization:
        api = api_group.OrganizationApi(self.client)
        response = api.create_organization(
            body=body,
        )
        return response

    def create_sso_connection(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        body: Annotated[
            CreateSsoConnectionRequest,
            Field(..., description="request body for creating a sso connection"),
        ],
    ) -> SsoConnection:
        api = api_group.OrganizationApi(self.client)
        response = api.create_sso_connection(
            organization_id=organization_id,
            body=body,
        )
        return response

    def delete_managed_domain(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        domain_id: Annotated[StrictStr, Field(..., description="managed domain ID")],
    ) -> None:
        api = api_group.OrganizationApi(self.client)
        response = api.delete_managed_domain(
            organization_id=organization_id,
            domain_id=domain_id,
        )
        return response

    def delete_sso_bypass_key(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
    ) -> None:
        api = api_group.OrganizationApi(self.client)
        response = api.delete_sso_bypass_key(
            organization_id=organization_id,
        )
        return response

    def delete_sso_connection(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        connection_id: Annotated[StrictStr, Field(..., description="connection ID")],
    ) -> None:
        api = api_group.OrganizationApi(self.client)
        response = api.delete_sso_connection(
            organization_id=organization_id,
            connection_id=connection_id,
        )
        return response

    def get_managed_domain(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        domain_id: Annotated[StrictStr, Field(..., description="managed domain ID")],
    ) -> ManagedDomain:
        api = api_group.OrganizationApi(self.client)
        response = api.get_managed_domain(
            organization_id=organization_id,
            domain_id=domain_id,
        )
        return response

    def get_organization(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        is_look_up_only: Annotated[
            Optional[StrictBool],
            Field(description="only look up organization metadata if true"),
        ],
    ) -> Organization:
        api = api_group.OrganizationApi(self.client)
        response = api.get_organization(
            organization_id=organization_id,
            is_look_up_only=is_look_up_only,
        )
        return response

    def get_organization_audit_logs(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        earliest: Annotated[
            Optional[StrictStr],
            Field(description="starting point in days for audit logs"),
        ],
    ) -> List[int]:
        api = api_group.OrganizationApi(self.client)
        response = api.get_organization_audit_logs(
            organization_id=organization_id,
            earliest=earliest,
        )
        return response

    def get_sso_bypass_key(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
    ) -> SsoBypassKey:
        api = api_group.OrganizationApi(self.client)
        response = api.get_sso_bypass_key(
            organization_id=organization_id,
        )
        return response

    def get_sso_connection(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        connection_id: Annotated[StrictStr, Field(..., description="connection ID")],
    ) -> SsoConnection:
        api = api_group.OrganizationApi(self.client)
        response = api.get_sso_connection(
            organization_id=organization_id,
            connection_id=connection_id,
        )
        return response

    def list_managed_domains(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
    ) -> List[ManagedDomain]:
        api = api_group.OrganizationApi(self.client)
        response = api.list_managed_domains(
            organization_id=organization_id,
        )
        return response

    def list_organization_auth_ids(
        self,
        email: Annotated[
            StrictStr,
            Field(..., description="User email to retrieve organization auth IDs for"),
        ],
    ) -> List[str]:
        api = api_group.OrganizationApi(self.client)
        response = api.list_organization_auth_ids(
            email=email,
        )
        return response

    def list_organizations(
        self,
        search: Annotated[
            Optional[StrictStr],
            Field(description="string to search for when listing users"),
        ],
        trial_status: Annotated[
            Optional[StrictStr],
            Field(description="filter by trial status, null for all orgs"),
        ],
        support_plan: Annotated[
            Optional[StrictStr],
            Field(
                description="filter by support plan, should be one of INTERNAL, POV, TRIAL, BASIC, STANDARD, PREMIUM, BUSINESS_CRITICAL, or null for all orgs"
            ),
        ],
        product: Annotated[
            Optional[StrictStr],
            Field(description="filter by product, null for all orgs"),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
    ) -> List[Organization]:
        api = api_group.OrganizationApi(self.client)
        response = api.list_organizations(
            search=search,
            trial_status=trial_status,
            support_plan=support_plan,
            product=product,
            sorts=sorts,
        )
        return response

    def list_sso_connections(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
    ) -> List[SsoConnection]:
        api = api_group.OrganizationApi(self.client)
        response = api.list_sso_connections(
            organization_id=organization_id,
        )
        return response

    def update_managed_domain(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        domain_id: Annotated[StrictStr, Field(..., description="managed domain ID")],
        body: Annotated[
            UpdateManagedDomainRequest,
            Field(..., description="request body for updating a managed domain"),
        ],
    ) -> ManagedDomain:
        api = api_group.OrganizationApi(self.client)
        response = api.update_managed_domain(
            organization_id=organization_id,
            domain_id=domain_id,
            body=body,
        )
        return response

    def update_organization(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        body: Annotated[
            UpdateOrganizationRequest,
            Field(..., description="request body for updating an organization"),
        ],
    ) -> Organization:
        api = api_group.OrganizationApi(self.client)
        response = api.update_organization(
            organization_id=organization_id,
            body=body,
        )
        return response

    def update_sso_connection(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        connection_id: Annotated[StrictStr, Field(..., description="connection ID")],
        body: Annotated[
            UpdateSsoConnectionRequest,
            Field(..., description="request body for updating a sso connection"),
        ],
    ) -> SsoConnection:
        api = api_group.OrganizationApi(self.client)
        response = api.update_sso_connection(
            organization_id=organization_id,
            connection_id=connection_id,
            body=body,
        )
        return response

    def upsert_sso_bypass_key(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
    ) -> SsoBypassKey:
        api = api_group.OrganizationApi(self.client)
        response = api.upsert_sso_bypass_key(
            organization_id=organization_id,
        )
        return response

    def validate_sso_login(
        self,
        body: Annotated[
            ValidateSsoLoginRequest,
            Field(..., description="event request body for sso login validation"),
        ],
    ) -> SsoLoginCallback:
        api = api_group.OrganizationApi(self.client)
        response = api.validate_sso_login(
            body=body,
        )
        return response

    def verify_managed_domain(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        domain_id: Annotated[StrictStr, Field(..., description="managed domain ID")],
    ) -> ManagedDomain:
        api = api_group.OrganizationApi(self.client)
        response = api.verify_managed_domain(
            organization_id=organization_id,
            domain_id=domain_id,
        )
        return response

    def list_astro_releases(
        self,
    ) -> List[AstroRelease]:
        api = api_group.ReleaseApi(self.client)
        response = api.list_astro_releases()
        return response

    def list_cli_releases(
        self,
    ) -> List[AstroRelease]:
        api = api_group.ReleaseApi(self.client)
        response = api.list_cli_releases()
        return response

    def list_runtime_releases(
        self,
    ) -> List[RuntimeRelease]:
        api = api_group.ReleaseApi(self.client)
        response = api.list_runtime_releases()
        return response

    def create_dag_run(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        dag_id: Annotated[StrictStr, Field(..., description="ID of the dag")],
        data: Annotated[
            CreateDagRunRequest,
            Field(..., description="request body for creating a dag run"),
        ],
    ) -> CreateDagRun:
        api = api_group.RuntimeApi(self.client)
        response = api.create_dag_run(
            organization_id=organization_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
            dag_id=dag_id,
            data=data,
        )
        return response

    def get_dag_code(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        file_token: Annotated[
            StrictStr, Field(..., description="Token for the code file")
        ],
    ) -> Code:
        api = api_group.RuntimeApi(self.client)
        response = api.get_dag_code(
            organization_id=organization_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
            file_token=file_token,
        )
        return response

    def get_runtime(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
    ) -> Runtime:
        api = api_group.RuntimeApi(self.client)
        response = api.get_runtime(
            organization_id=organization_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
        )
        return response

    def get_runtime_dag(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        dag_id: Annotated[StrictStr, Field(..., description="dag ID")],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
    ) -> RuntimeDag:
        api = api_group.RuntimeApi(self.client)
        response = api.get_runtime_dag(
            organization_id=organization_id,
            dag_id=dag_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
        )
        return response

    def get_task_instance_logs(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        dag_id: Annotated[StrictStr, Field(..., description="ID of the dag")],
        dag_run_id: Annotated[StrictStr, Field(..., description="ID of the dag run")],
        dag_task_id: Annotated[
            StrictStr, Field(..., description="ID of the dag run task")
        ],
        dag_task_try_number: Annotated[
            StrictInt, Field(..., description="ID of the dag run task try number")
        ],
        full_content: Annotated[
            Optional[StrictBool], Field(description="task log full content")
        ],
        map_index: Annotated[
            Optional[StrictInt], Field(description="task map index for mapped task")
        ],
        token: Annotated[
            Optional[StrictStr],
            Field(description="token that allows you to continue fetching logs"),
        ],
    ) -> TaskInstanceLogs:
        api = api_group.RuntimeApi(self.client)
        response = api.get_task_instance_logs(
            organization_id=organization_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            dag_task_id=dag_task_id,
            dag_task_try_number=dag_task_try_number,
            full_content=full_content,
            map_index=map_index,
            token=token,
        )
        return response

    def list_dag_runs(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        dag_id: Annotated[StrictStr, Field(..., description="ID of the dag")],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, le=100, ge=0)],
            Field(description="limit for pagination"),
        ],
        order_by: Annotated[
            Optional[StrictStr], Field(description="order list by the field name")
        ],
        state: Annotated[
            Optional[StrictStr],
            Field(
                description="list of state of dag runs, separated by comma (OR condition)"
            ),
        ],
        execution_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs executed on date greater than or equal to specified date"
            ),
        ],
        execution_date_lte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs executed on date less than or equal to specified date"
            ),
        ],
        start_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs started on date greater than or equal to specified date"
            ),
        ],
        start_date_lte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs started on date less than or equal to specified date"
            ),
        ],
        end_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs ended on date greater than or equal to specified date"
            ),
        ],
        end_date_lte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs ended on date less than or equal to specified date"
            ),
        ],
    ) -> DagRunsPaginated:
        api = api_group.RuntimeApi(self.client)
        response = api.list_dag_runs(
            organization_id=organization_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
            dag_id=dag_id,
            offset=offset,
            limit=limit,
            order_by=order_by,
            state=state,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
        )
        return response

    def list_runtime_dags(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, le=100, ge=1)],
            Field(description="limit for pagination"),
        ],
        order_by: Annotated[
            Optional[StrictStr], Field(description="order dags by the field name")
        ],
        tags: Annotated[Optional[StrictStr], Field(description="tags")],
        only_active: Annotated[
            Optional[StrictBool], Field(description="show only active dags")
        ],
        dag_id_pattern: Annotated[
            Optional[StrictStr], Field(description="show dags that match this pattern")
        ],
    ) -> RuntimeDagsPaginated:
        api = api_group.RuntimeApi(self.client)
        response = api.list_runtime_dags(
            organization_id=organization_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
            offset=offset,
            limit=limit,
            order_by=order_by,
            tags=tags,
            only_active=only_active,
            dag_id_pattern=dag_id_pattern,
        )
        return response

    def list_runtime_import_errors(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, le=100, ge=1)],
            Field(description="limit for pagination"),
        ],
        order_by: Annotated[
            Optional[StrictStr], Field(description="order list by the field name")
        ],
    ) -> RuntimeImportErrorsPaginated:
        api = api_group.RuntimeApi(self.client)
        response = api.list_runtime_import_errors(
            organization_id=organization_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
            offset=offset,
            limit=limit,
            order_by=order_by,
        )
        return response

    def list_runtimes(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="IDs that define the workspaces where runtimes belong to"
            ),
        ],
        runtime_type: Annotated[
            Optional[StrictStr],
            Field(description="runtimeType to filter runtimes with"),
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for pagination"),
        ],
        release_names: Annotated[
            Optional[StrictStr],
            Field(
                description="release names to filter runtimes with, separated by comma"
            ),
        ],
        sorts: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="sorting criteria, each criterion should conform to format 'fieldName:asc' or 'fieldName:desc'"
            ),
        ],
    ) -> RuntimesPaginated:
        api = api_group.RuntimeApi(self.client)
        response = api.list_runtimes(
            organization_id=organization_id,
            workspace_ids=workspace_ids,
            runtime_type=runtime_type,
            offset=offset,
            limit=limit,
            release_names=release_names,
            sorts=sorts,
        )
        return response

    def list_task_instances(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        dag_id: Annotated[StrictStr, Field(..., description="ID of the dag")],
        dag_run_id: Annotated[StrictStr, Field(..., description="ID of the dag run")],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, le=100, ge=0)],
            Field(description="limit for pagination"),
        ],
        execution_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="execution date is greater or equal to the specified date"
            ),
        ],
        execution_date_lte: Annotated[
            Optional[datetime],
            Field(
                description="execution date is less than or equal to the specified date"
            ),
        ],
        start_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="start date is greater than or equal to the specified date"
            ),
        ],
        start_date_lte: Annotated[
            Optional[datetime],
            Field(description="start date is less than or equal to the specified date"),
        ],
        end_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="end date is greater than or equal to the specified date"
            ),
        ],
        end_date_lte: Annotated[
            Optional[datetime],
            Field(description="end date is less than or equal to the specified date"),
        ],
        duration_sec_gte: Annotated[
            Optional[Union[StrictFloat, StrictInt]],
            Field(
                description="duration is greater than or equal to the specified in seconds"
            ),
        ],
        duration_sec_lte: Annotated[
            Optional[Union[StrictFloat, StrictInt]],
            Field(
                description="duration is less than or equal to the specified in seconds"
            ),
        ],
        states: Annotated[
            Optional[conlist(StrictStr)], Field(description="task states")
        ],
        pools: Annotated[Optional[conlist(StrictStr)], Field(description="task pools")],
        queues: Annotated[
            Optional[conlist(StrictStr)], Field(description="task queues")
        ],
    ) -> TaskInstancesPaginated:
        api = api_group.RuntimeApi(self.client)
        response = api.list_task_instances(
            organization_id=organization_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            offset=offset,
            limit=limit,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
            duration_sec_gte=duration_sec_gte,
            duration_sec_lte=duration_sec_lte,
            states=states,
            pools=pools,
            queues=queues,
        )
        return response

    def update_runtime_dag(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        dag_id: Annotated[StrictStr, Field(..., description="ID of the dag")],
        data: Annotated[
            UpdateRuntimeDagRequest,
            Field(..., description="request body for updating a dag"),
        ],
    ) -> UpdateRuntimeDag:
        api = api_group.RuntimeApi(self.client)
        response = api.update_runtime_dag(
            organization_id=organization_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
            dag_id=dag_id,
            data=data,
        )
        return response

    def clear_task_instances(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        dag_id: Annotated[StrictStr, Field(..., description="dag ID")],
        data: Annotated[
            ClearTaskInstancesRequest,
            Field(..., description="request body for clearing a dag run tasks"),
        ],
    ) -> TaskInstanceReferences:
        api = api_group.TaskApi(self.client)
        response = api.clear_task_instances(
            organization_id=organization_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
            dag_id=dag_id,
            data=data,
        )
        return response

    def get_mapped_task_instance(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        dag_id: Annotated[StrictStr, Field(..., description="dag ID")],
        dag_run_id: Annotated[StrictStr, Field(..., description="dag run ID")],
        task_id: Annotated[StrictStr, Field(..., description="task ID")],
        map_index: Annotated[StrictStr, Field(..., description="task map index")],
    ) -> TaskInstance:
        api = api_group.TaskApi(self.client)
        response = api.get_mapped_task_instance(
            organization_id=organization_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            map_index=map_index,
        )
        return response

    def list_mapped_task_instances(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        task_id: Annotated[StrictStr, Field(..., description="ID of the task")],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        dag_id: Annotated[StrictStr, Field(..., description="ID of the dag")],
        dag_run_id: Annotated[StrictStr, Field(..., description="ID of the dag run")],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, le=100, ge=0)],
            Field(description="limit for pagination"),
        ],
        execution_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="execution date is greater or equal to the specified date"
            ),
        ],
        execution_date_lte: Annotated[
            Optional[datetime],
            Field(
                description="execution date is less than or equal to the specified date"
            ),
        ],
        start_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="start date is greater than or equal to the specified date"
            ),
        ],
        start_date_lte: Annotated[
            Optional[datetime],
            Field(description="start date is less than or equal to the specified date"),
        ],
        end_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="end date is greater than or equal to the specified date"
            ),
        ],
        end_date_lte: Annotated[
            Optional[datetime],
            Field(description="end date is less than or equal to the specified date"),
        ],
        duration_gte: Annotated[
            Optional[Union[StrictFloat, StrictInt]],
            Field(
                description="duration is greater than or equal to the specified in seconds"
            ),
        ],
        duration_lte: Annotated[
            Optional[Union[StrictFloat, StrictInt]],
            Field(
                description="duration is less than or equal to the specified in seconds"
            ),
        ],
        states: Annotated[
            Optional[conlist(StrictStr)], Field(description="task states")
        ],
        pools: Annotated[Optional[conlist(StrictStr)], Field(description="task pools")],
        queues: Annotated[
            Optional[conlist(StrictStr)], Field(description="task queues")
        ],
        order_by: Annotated[
            Optional[StrictStr],
            Field(
                description="The name of the field to order the results by. Prefix a field name with - to reverse the sort order."
            ),
        ],
    ) -> TaskInstancesPaginated:
        api = api_group.TaskApi(self.client)
        response = api.list_mapped_task_instances(
            organization_id=organization_id,
            task_id=task_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            offset=offset,
            limit=limit,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
            duration_gte=duration_gte,
            duration_lte=duration_lte,
            states=states,
            pools=pools,
            queues=queues,
            order_by=order_by,
        )
        return response

    def update_task_instance(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        dag_id: Annotated[StrictStr, Field(..., description="dag ID")],
        dag_run_id: Annotated[StrictStr, Field(..., description="dag run ID")],
        task_id: Annotated[StrictStr, Field(..., description="task ID")],
        data: Annotated[
            UpdateTaskInstanceRequest,
            Field(..., description="request body for updating a task"),
        ],
    ) -> TaskInstanceReference:
        api = api_group.TaskApi(self.client)
        response = api.update_task_instance(
            organization_id=organization_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            data=data,
        )
        return response

    def update_task_instances_state(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        runtime_id: Annotated[StrictStr, Field(..., description="ID of the runtime")],
        dag_id: Annotated[StrictStr, Field(..., description="dag ID")],
        data: Annotated[
            UpdateTaskInstancesStateRequest,
            Field(..., description="request body for clearing a dag run tasks"),
        ],
    ) -> TaskInstanceReferences:
        api = api_group.TaskApi(self.client)
        response = api.update_task_instances_state(
            organization_id=organization_id,
            workspace_id=workspace_id,
            runtime_id=runtime_id,
            dag_id=dag_id,
            data=data,
        )
        return response

    def add_team_members(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        team_id: Annotated[StrictStr, Field(..., description="team ID")],
        body: Annotated[
            AddTeamMembersRequest,
            Field(..., description="request body for adding members to a team"),
        ],
    ) -> None:
        api = api_group.TeamApi(self.client)
        response = api.add_team_members(
            organization_id=organization_id,
            team_id=team_id,
            body=body,
        )
        return response

    def create_team(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        body: Annotated[
            CreateTeamRequest,
            Field(..., description="request body for creating a team"),
        ],
    ) -> Team:
        api = api_group.TeamApi(self.client)
        response = api.create_team(
            organization_id=organization_id,
            body=body,
        )
        return response

    def delete_team(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        team_id: Annotated[StrictStr, Field(..., description="team ID")],
    ) -> None:
        api = api_group.TeamApi(self.client)
        response = api.delete_team(
            organization_id=organization_id,
            team_id=team_id,
        )
        return response

    def delete_workspace_team(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        team_id: Annotated[StrictStr, Field(..., description="team ID")],
    ) -> None:
        api = api_group.TeamApi(self.client)
        response = api.delete_workspace_team(
            organization_id=organization_id,
            workspace_id=workspace_id,
            team_id=team_id,
        )
        return response

    def get_team(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        team_id: Annotated[StrictStr, Field(..., description="team ID")],
    ) -> Team:
        api = api_group.TeamApi(self.client)
        response = api.get_team(
            organization_id=organization_id,
            team_id=team_id,
        )
        return response

    def list_organization_teams(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
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
        search: Annotated[
            Optional[StrictStr],
            Field(description="string to search for when listing teams"),
        ],
    ) -> TeamsPaginated:
        api = api_group.TeamApi(self.client)
        response = api.list_organization_teams(
            organization_id=organization_id,
            offset=offset,
            limit=limit,
            sorts=sorts,
            search=search,
        )
        return response

    def list_workspace_teams(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
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
        search: Annotated[
            Optional[StrictStr],
            Field(description="string to search for when listing teams"),
        ],
    ) -> TeamsPaginated:
        api = api_group.TeamApi(self.client)
        response = api.list_workspace_teams(
            organization_id=organization_id,
            workspace_id=workspace_id,
            offset=offset,
            limit=limit,
            sorts=sorts,
            search=search,
        )
        return response

    def mutate_org_team_role(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        team_id: Annotated[StrictStr, Field(..., description="team ID")],
        body: Annotated[
            MutateOrgTeamRoleRequest,
            Field(
                ..., description="request body for mutating an organization team role"
            ),
        ],
    ) -> TeamRole:
        api = api_group.TeamApi(self.client)
        response = api.mutate_org_team_role(
            organization_id=organization_id,
            team_id=team_id,
            body=body,
        )
        return response

    def mutate_workspace_team_role(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        team_id: Annotated[StrictStr, Field(..., description="team ID")],
        body: Annotated[
            MutateWorkspaceTeamRoleRequest,
            Field(..., description="request body for mutating a workspace team role"),
        ],
    ) -> TeamRole:
        api = api_group.TeamApi(self.client)
        response = api.mutate_workspace_team_role(
            organization_id=organization_id,
            workspace_id=workspace_id,
            team_id=team_id,
            body=body,
        )
        return response

    def remove_team_member(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        team_id: Annotated[StrictStr, Field(..., description="team ID")],
        member_id: Annotated[StrictStr, Field(..., description="member ID")],
    ) -> None:
        api = api_group.TeamApi(self.client)
        response = api.remove_team_member(
            organization_id=organization_id,
            team_id=team_id,
            member_id=member_id,
        )
        return response

    def update_team(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        team_id: Annotated[StrictStr, Field(..., description="team ID")],
        body: Annotated[
            UpdateTeamRequest,
            Field(..., description="request body for updating a team"),
        ],
    ) -> Team:
        api = api_group.TeamApi(self.client)
        response = api.update_team(
            organization_id=organization_id,
            team_id=team_id,
            body=body,
        )
        return response

    def delete_org_user(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        user_id: Annotated[StrictStr, Field(..., description="user ID")],
    ) -> None:
        api = api_group.UserApi(self.client)
        response = api.delete_org_user(
            organization_id=organization_id,
            user_id=user_id,
        )
        return response

    def delete_workspace_user(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        user_id: Annotated[StrictStr, Field(..., description="user ID")],
    ) -> None:
        api = api_group.UserApi(self.client)
        response = api.delete_workspace_user(
            organization_id=organization_id,
            workspace_id=workspace_id,
            user_id=user_id,
        )
        return response

    def get_self_user(
        self,
        create_if_not_exist: Annotated[
            Optional[StrictBool],
            Field(description="create self user if it does not already exist"),
        ],
    ) -> ModelSelf:
        api = api_group.UserApi(self.client)
        response = api.get_self_user(
            create_if_not_exist=create_if_not_exist,
        )
        return response

    def get_user(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        user_id: Annotated[StrictStr, Field(..., description="user ID")],
    ) -> User:
        api = api_group.UserApi(self.client)
        response = api.get_user(
            organization_id=organization_id,
            user_id=user_id,
        )
        return response

    def list_org_users(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
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
        search: Annotated[
            Optional[StrictStr],
            Field(description="string to search for when listing users"),
        ],
        has_invites: Annotated[
            Optional[StrictBool], Field(description="filter on users with invites only")
        ],
    ) -> UsersPaginated:
        api = api_group.UserApi(self.client)
        response = api.list_org_users(
            organization_id=organization_id,
            offset=offset,
            limit=limit,
            sorts=sorts,
            search=search,
            has_invites=has_invites,
        )
        return response

    def list_workspace_users(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
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
        search: Annotated[
            Optional[StrictStr],
            Field(description="string to search for when listing users"),
        ],
    ) -> UsersPaginated:
        api = api_group.UserApi(self.client)
        response = api.list_workspace_users(
            organization_id=organization_id,
            workspace_id=workspace_id,
            offset=offset,
            limit=limit,
            sorts=sorts,
            search=search,
        )
        return response

    def mutate_org_user_role(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        user_id: Annotated[StrictStr, Field(..., description="user ID")],
        body: Annotated[
            MutateOrgUserRoleRequest,
            Field(
                ..., description="request body for mutating an organization user role"
            ),
        ],
    ) -> UserRole:
        api = api_group.UserApi(self.client)
        response = api.mutate_org_user_role(
            organization_id=organization_id,
            user_id=user_id,
            body=body,
        )
        return response

    def mutate_workspace_user_role(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        user_id: Annotated[StrictStr, Field(..., description="user ID")],
        body: Annotated[
            MutateWorkspaceUserRoleRequest,
            Field(
                ..., description="request body for mutating an organization user role"
            ),
        ],
    ) -> UserRole:
        api = api_group.UserApi(self.client)
        response = api.mutate_workspace_user_role(
            organization_id=organization_id,
            workspace_id=workspace_id,
            user_id=user_id,
            body=body,
        )
        return response

    def create_connection(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
        data: Annotated[
            MutateConnectionRequest,
            Field(..., description="request body for creating a new connection"),
        ],
    ) -> Connection:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.create_connection(
            organization_id=organization_id,
            workspace_id=workspace_id,
            virtual_runtime_id=virtual_runtime_id,
            data=data,
        )
        return response

    def create_virtual_runtime(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        body: Annotated[
            MutateVirtualRuntimeRequest,
            Field(..., description="request body for creating a virtual runtime"),
        ],
    ) -> VirtualRuntime:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.create_virtual_runtime(
            organization_id=organization_id,
            workspace_id=workspace_id,
            body=body,
        )
        return response

    def delete_connection(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
        connection_id: Annotated[
            StrictStr, Field(..., description="ID of the connection")
        ],
    ) -> None:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.delete_connection(
            organization_id=organization_id,
            workspace_id=workspace_id,
            virtual_runtime_id=virtual_runtime_id,
            connection_id=connection_id,
        )
        return response

    def delete_virtual_runtime(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
    ) -> None:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.delete_virtual_runtime(
            organization_id=organization_id,
            workspace_id=workspace_id,
            virtual_runtime_id=virtual_runtime_id,
        )
        return response

    def get_connection(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
        connection_id: Annotated[
            StrictStr, Field(..., description="ID of the connection")
        ],
    ) -> Connection:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.get_connection(
            organization_id=organization_id,
            virtual_runtime_id=virtual_runtime_id,
            connection_id=connection_id,
        )
        return response

    def get_virtual_runtime(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
    ) -> VirtualRuntime:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.get_virtual_runtime(
            organization_id=organization_id,
            virtual_runtime_id=virtual_runtime_id,
        )
        return response

    def list_connections(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
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
    ) -> ConnectionsPaginated:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.list_connections(
            organization_id=organization_id,
            virtual_runtime_id=virtual_runtime_id,
            offset=offset,
            limit=limit,
            sorts=sorts,
        )
        return response

    def list_requirements(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
    ) -> VRRequirements:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.list_requirements(
            organization_id=organization_id,
            virtual_runtime_id=virtual_runtime_id,
        )
        return response

    def list_variables(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
    ) -> VRVariables:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.list_variables(
            organization_id=organization_id,
            virtual_runtime_id=virtual_runtime_id,
        )
        return response

    def list_virtual_runtimes(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="IDs that define the workspaces where virtual runtimes belong to"
            ),
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
    ) -> VirtualRuntimesPaginated:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.list_virtual_runtimes(
            organization_id=organization_id,
            workspace_ids=workspace_ids,
            offset=offset,
            limit=limit,
            sorts=sorts,
        )
        return response

    def list_vr_dag_run_task_instances(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
        dag_id: Annotated[StrictStr, Field(..., description="ID of the dag")],
        dag_run_id: Annotated[StrictStr, Field(..., description="ID of the dag run")],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for pagination"),
        ],
        execution_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="execution date is greater or equal to the specified date"
            ),
        ],
        execution_date_lte: Annotated[
            Optional[datetime],
            Field(
                description="execution date is less than or equal to the specified date"
            ),
        ],
        start_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="start date is greater than or equal to the specified date"
            ),
        ],
        start_date_lte: Annotated[
            Optional[datetime],
            Field(description="start date is less than or equal to the specified date"),
        ],
        end_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="end date is greater than or equal to the specified date"
            ),
        ],
        end_date_lte: Annotated[
            Optional[datetime],
            Field(description="end date is less than or equal to the specified date"),
        ],
        duration_sec_gte: Annotated[
            Optional[Union[StrictFloat, StrictInt]],
            Field(
                description="duration is greater than or equal to the specified in seconds"
            ),
        ],
        duration_sec_lte: Annotated[
            Optional[Union[StrictFloat, StrictInt]],
            Field(
                description="duration is less than or equal to the specified in seconds"
            ),
        ],
        states: Annotated[
            Optional[conlist(StrictStr)], Field(description="task states")
        ],
        pools: Annotated[Optional[conlist(StrictStr)], Field(description="task pools")],
        queues: Annotated[
            Optional[conlist(StrictStr)], Field(description="task queues")
        ],
    ) -> VRDagRunTaskInstancesPaginated:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.list_vr_dag_run_task_instances(
            organization_id=organization_id,
            workspace_id=workspace_id,
            virtual_runtime_id=virtual_runtime_id,
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            offset=offset,
            limit=limit,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
            duration_sec_gte=duration_sec_gte,
            duration_sec_lte=duration_sec_lte,
            states=states,
            pools=pools,
            queues=queues,
        )
        return response

    def list_vr_dag_runs(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
        dag_id: Annotated[StrictStr, Field(..., description="ID of the dag")],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="limit for pagination"),
        ],
        order_by: Annotated[
            Optional[StrictStr], Field(description="order list by the field name")
        ],
        state: Annotated[
            Optional[StrictStr],
            Field(
                description="list of state of dag runs, separated by comma (OR condition)"
            ),
        ],
        execution_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs executed on date greater than or equal to specified date"
            ),
        ],
        execution_date_lte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs executed on date less than or equal to specified date"
            ),
        ],
        start_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs started on date greater than or equal to specified date"
            ),
        ],
        start_date_lte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs started on date less than or equal to specified date"
            ),
        ],
        end_date_gte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs ended on date greater than or equal to specified date"
            ),
        ],
        end_date_lte: Annotated[
            Optional[datetime],
            Field(
                description="returns runs ended on date less than or equal to specified date"
            ),
        ],
    ) -> VRDagRunsPaginated:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.list_vr_dag_runs(
            organization_id=organization_id,
            workspace_id=workspace_id,
            virtual_runtime_id=virtual_runtime_id,
            dag_id=dag_id,
            offset=offset,
            limit=limit,
            order_by=order_by,
            state=state,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
        )
        return response

    def list_vr_dags(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=1)],
            Field(description="limit for pagination"),
        ],
        order_by: Annotated[
            Optional[StrictStr], Field(description="order list by the field name")
        ],
        tags: Annotated[Optional[StrictStr], Field(description="tags")],
        only_active: Annotated[
            Optional[StrictBool], Field(description="show only active dags")
        ],
        dag_id_pattern: Annotated[
            Optional[StrictStr], Field(description="show dags that match this pattern")
        ],
    ) -> VRDagsPaginated:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.list_vr_dags(
            organization_id=organization_id,
            workspace_id=workspace_id,
            virtual_runtime_id=virtual_runtime_id,
            offset=offset,
            limit=limit,
            order_by=order_by,
            tags=tags,
            only_active=only_active,
            dag_id_pattern=dag_id_pattern,
        )
        return response

    def list_vr_import_errors(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
        offset: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="offset for pagination"),
        ],
        limit: Annotated[
            Optional[conint(strict=True, ge=1)],
            Field(description="limit for pagination"),
        ],
        order_by: Annotated[
            Optional[StrictStr], Field(description="order list by the field name")
        ],
    ) -> VRImportErrorsPaginated:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.list_vr_import_errors(
            organization_id=organization_id,
            workspace_id=workspace_id,
            virtual_runtime_id=virtual_runtime_id,
            offset=offset,
            limit=limit,
            order_by=order_by,
        )
        return response

    def mutate_requirements(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
        data: Annotated[
            MutateVRRequirementsRequest,
            Field(
                ...,
                description="request body for mutating virtual runtime requirements",
            ),
        ],
    ) -> VRRequirements:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.mutate_requirements(
            organization_id=organization_id,
            workspace_id=workspace_id,
            virtual_runtime_id=virtual_runtime_id,
            data=data,
        )
        return response

    def mutate_variables(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
        data: Annotated[
            MutateVRVariablesRequest,
            Field(
                ..., description="request body for mutating virtual runtime variables"
            ),
        ],
    ) -> VRVariables:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.mutate_variables(
            organization_id=organization_id,
            workspace_id=workspace_id,
            virtual_runtime_id=virtual_runtime_id,
            data=data,
        )
        return response

    def pause_dag(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
        dag_id: Annotated[StrictStr, Field(..., description="ID of the dag")],
    ) -> UpdateDag:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.pause_dag(
            organization_id=organization_id,
            workspace_id=workspace_id,
            virtual_runtime_id=virtual_runtime_id,
            dag_id=dag_id,
        )
        return response

    def post_dag_run(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
        dag_id: Annotated[StrictStr, Field(..., description="ID of the dag")],
        data: Annotated[
            PostDagRunRequest,
            Field(..., description="request body for trigger a dag run"),
        ],
    ) -> PostDagRun:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.post_dag_run(
            organization_id=organization_id,
            workspace_id=workspace_id,
            virtual_runtime_id=virtual_runtime_id,
            dag_id=dag_id,
            data=data,
        )
        return response

    def resume_dag(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
        dag_id: Annotated[StrictStr, Field(..., description="ID of the dag")],
    ) -> UpdateDag:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.resume_dag(
            organization_id=organization_id,
            workspace_id=workspace_id,
            virtual_runtime_id=virtual_runtime_id,
            dag_id=dag_id,
        )
        return response

    def update_connection(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
        connection_id: Annotated[
            StrictStr, Field(..., description="ID of the connection")
        ],
        data: Annotated[
            MutateConnectionRequest,
            Field(..., description="request body for updating a connection"),
        ],
    ) -> Connection:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.update_connection(
            organization_id=organization_id,
            workspace_id=workspace_id,
            virtual_runtime_id=virtual_runtime_id,
            connection_id=connection_id,
            data=data,
        )
        return response

    def update_virtual_runtime(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
        virtual_runtime_id: Annotated[
            StrictStr, Field(..., description="ID of the virtual runtime")
        ],
        body: Annotated[
            MutateVirtualRuntimeRequest,
            Field(..., description="request body for updating a virtual runtime"),
        ],
    ) -> VirtualRuntime:
        api = api_group.VirtualRuntimeApi(self.client)
        response = api.update_virtual_runtime(
            organization_id=organization_id,
            workspace_id=workspace_id,
            virtual_runtime_id=virtual_runtime_id,
            body=body,
        )
        return response

    def create_workspace(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        body: Annotated[
            CreateWorkspaceRequest,
            Field(..., description="request body for creating a new workspace"),
        ],
    ) -> Workspace:
        api = api_group.WorkspaceApi(self.client)
        response = api.create_workspace(
            organization_id=organization_id,
            body=body,
        )
        return response

    def delete_workspace(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
    ) -> None:
        api = api_group.WorkspaceApi(self.client)
        response = api.delete_workspace(
            organization_id=organization_id,
            workspace_id=workspace_id,
        )
        return response

    def get_workspace(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID of the workspace")
        ],
    ) -> Workspace:
        api = api_group.WorkspaceApi(self.client)
        response = api.get_workspace(
            organization_id=organization_id,
            workspace_id=workspace_id,
        )
        return response

    def list_workspace_dag_filters(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
    ) -> DagFilters:
        api = api_group.WorkspaceApi(self.client)
        response = api.list_workspace_dag_filters(
            organization_id=organization_id,
            workspace_id=workspace_id,
        )
        return response

    def list_workspace_dags(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        page_size: Annotated[
            Optional[conint(strict=True, le=100, ge=1)],
            Field(description="page size, default of 20"),
        ],
        order_by: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="order-by fields, comma separated"),
        ],
        cursor: Annotated[Optional[StrictStr], Field(description="pagination cursor")],
        num_runs: Annotated[
            Optional[conint(strict=True, le=50, ge=0)],
            Field(description="number of runs to include per dag, default of 0"),
        ],
        name: Annotated[
            Optional[StrictStr], Field(description="filter by name of DAG (dagId)")
        ],
        name__like: Annotated[
            Optional[StrictStr],
            Field(
                description="filter by pattern for name of DAG (dagId),  SQL  syntax"
            ),
        ],
        owner: Annotated[
            Optional[StrictStr], Field(description="filter by an owner of the dag")
        ],
        is_paused: Annotated[
            Optional[StrictBool], Field(description="filter by paused dags")
        ],
        is_active: Annotated[
            Optional[StrictBool], Field(description="filter by active dags")
        ],
        last_run_state__in: Annotated[
            Optional[conlist(StrictStr)],
            Field(
                description="filter by dag runs with any of these run states for its last run"
            ),
        ],
        run_state__in: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="filter by dag runs with any of these run states"),
        ],
        run_after: Annotated[
            Optional[datetime],
            Field(
                description="filter by dag run after specified datetime (RFC3339 format)"
            ),
        ],
        tag__in: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="filter by any of these tags"),
        ],
        deployment_id__in: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="filter by any of these deployment IDs"),
        ],
    ) -> ListWorkspaceDags:
        api = api_group.WorkspaceApi(self.client)
        response = api.list_workspace_dags(
            organization_id=organization_id,
            workspace_id=workspace_id,
            page_size=page_size,
            order_by=order_by,
            cursor=cursor,
            num_runs=num_runs,
            name=name,
            name__like=name__like,
            owner=owner,
            is_paused=is_paused,
            is_active=is_active,
            last_run_state__in=last_run_state__in,
            run_state__in=run_state__in,
            run_after=run_after,
            tag__in=tag__in,
            deployment_id__in=deployment_id__in,
        )
        return response

    def list_workspaces(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_ids: Annotated[
            Optional[conlist(StrictStr)],
            Field(description="list of workspace ids to get detail of"),
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
        search: Annotated[
            Optional[StrictStr],
            Field(description="string to search for when listing workspaces"),
        ],
    ) -> WorkspacesPaginated:
        api = api_group.WorkspaceApi(self.client)
        response = api.list_workspaces(
            organization_id=organization_id,
            workspace_ids=workspace_ids,
            offset=offset,
            limit=limit,
            sorts=sorts,
            search=search,
        )
        return response

    def update_workspace(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[StrictStr, Field(..., description="workspace ID")],
        body: Annotated[
            UpdateWorkspaceRequest,
            Field(..., description="request body for updating a workspace"),
        ],
    ) -> Workspace:
        api = api_group.WorkspaceApi(self.client)
        response = api.update_workspace(
            organization_id=organization_id,
            workspace_id=workspace_id,
            body=body,
        )
        return response

    def get_workspace_dag_runs(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID that defines the workspace")
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(..., description="range of the DAG runs metrics in seconds"),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(..., description="step interval of the DAG runs metrics in seconds"),
        ],
        deployment_ids: Annotated[
            Optional[StrictStr],
            Field(description="IDs that define the deployments, separated by comma"),
        ],
        virtual_runtime_ids: Annotated[
            Optional[StrictStr],
            Field(
                description="IDs that define the virtual runtimes, separated by comma"
            ),
        ],
        runtime_type: Annotated[
            Optional[StrictStr], Field(description="type of runtime")
        ],
        status: Annotated[Optional[StrictStr], Field(description="status of dag runs")],
    ) -> List[WorkspaceRangeMetricPerStatus]:
        api = api_group.WorkspaceMetricsApi(self.client)
        response = api.get_workspace_dag_runs(
            organization_id=organization_id,
            workspace_id=workspace_id,
            range=range,
            step=step,
            deployment_ids=deployment_ids,
            virtual_runtime_ids=virtual_runtime_ids,
            runtime_type=runtime_type,
            status=status,
        )
        return response

    def get_workspace_task_runs(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        workspace_id: Annotated[
            StrictStr, Field(..., description="ID that defines the workspace")
        ],
        range: Annotated[
            conint(strict=True, ge=1800),
            Field(..., description="range of the task runs metric in seconds"),
        ],
        step: Annotated[
            conint(strict=True, ge=60),
            Field(..., description="step interval of task runs metric in seconds"),
        ],
        deployment_ids: Annotated[
            Optional[StrictStr],
            Field(description="IDs that define the deployments, separated by comma"),
        ],
        virtual_runtime_ids: Annotated[
            Optional[StrictStr],
            Field(
                description="IDs that define the virtual runtimes, separated by comma"
            ),
        ],
        runtime_type: Annotated[
            Optional[StrictStr], Field(description="type of runtime")
        ],
        status: Annotated[
            Optional[StrictStr], Field(description="status of task runs")
        ],
        include_deleted_deployments: Annotated[
            Optional[StrictBool],
            Field(
                description="results should include data from soft deleted deployments"
            ),
        ],
    ) -> List[WorkspaceRangeMetricPerStatus]:
        api = api_group.WorkspaceMetricsApi(self.client)
        response = api.get_workspace_task_runs(
            organization_id=organization_id,
            workspace_id=workspace_id,
            range=range,
            step=step,
            deployment_ids=deployment_ids,
            virtual_runtime_ids=virtual_runtime_ids,
            runtime_type=runtime_type,
            status=status,
            include_deleted_deployments=include_deleted_deployments,
        )
        return response

