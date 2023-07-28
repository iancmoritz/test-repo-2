# coding: utf-8

"""
    Astro Core API

    Astro Core API  # noqa: E501

    The version of the OpenAPI document: v1alpha1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr

from astronomer_core_api.sdk.models.clear_dag_run import ClearDagRun
from astronomer_core_api.sdk.models.clear_dag_run_request import ClearDagRunRequest
from astronomer_core_api.sdk.models.dag_run import DagRun
from astronomer_core_api.sdk.models.update_dag_run_request import UpdateDagRunRequest

from astronomer_core_api.sdk.api_client import ApiClient
from astronomer_core_api.sdk.api_response import ApiResponse
from astronomer_core_api.sdk.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class DagRunApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
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
        **kwargs
    ) -> ClearDagRun:  # noqa: E501
        """Clear a dag run  # noqa: E501

        Clear a dag run  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clear_dag_run(organization_id, workspace_id, runtime_id, dag_id, dag_run_id, data, async_req=True)
        >>> result = thread.get()

        :param organization_id: organization ID (required)
        :type organization_id: str
        :param workspace_id: ID of the workspace (required)
        :type workspace_id: str
        :param runtime_id: ID of the runtime (required)
        :type runtime_id: str
        :param dag_id: dag ID (required)
        :type dag_id: str
        :param dag_run_id: dag run ID (required)
        :type dag_run_id: str
        :param data: request body for clearing a dag run (required)
        :type data: ClearDagRunRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ClearDagRun
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the clear_dag_run_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        return self.clear_dag_run_with_http_info(
            organization_id,
            workspace_id,
            runtime_id,
            dag_id,
            dag_run_id,
            data,
            **kwargs
        )  # noqa: E501

    @validate_arguments
    def clear_dag_run_with_http_info(
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
        **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Clear a dag run  # noqa: E501

        Clear a dag run  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clear_dag_run_with_http_info(organization_id, workspace_id, runtime_id, dag_id, dag_run_id, data, async_req=True)
        >>> result = thread.get()

        :param organization_id: organization ID (required)
        :type organization_id: str
        :param workspace_id: ID of the workspace (required)
        :type workspace_id: str
        :param runtime_id: ID of the runtime (required)
        :type runtime_id: str
        :param dag_id: dag ID (required)
        :type dag_id: str
        :param dag_run_id: dag run ID (required)
        :type dag_run_id: str
        :param data: request body for clearing a dag run (required)
        :type data: ClearDagRunRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ClearDagRun, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            "organization_id",
            "workspace_id",
            "runtime_id",
            "dag_id",
            "dag_run_id",
            "data",
        ]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clear_dag_run" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["organization_id"]:
            _path_params["organizationId"] = _params["organization_id"]

        if _params["workspace_id"]:
            _path_params["workspaceId"] = _params["workspace_id"]

        if _params["runtime_id"]:
            _path_params["runtimeId"] = _params["runtime_id"]

        if _params["dag_id"]:
            _path_params["dagId"] = _params["dag_id"]

        if _params["dag_run_id"]:
            _path_params["dagRunId"] = _params["dag_run_id"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params["data"] is not None:
            _body_params = _params["data"]

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["application/json"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list

        # authentication setting
        _auth_settings = ["JWT"]  # noqa: E501

        _response_types_map = {
            "200": "ClearDagRun",
            "400": "Error",
            "401": "Error",
            "403": "Error",
            "404": "Error",
            "500": "Error",
        }

        return self.api_client.call_api(
            "/organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/dags/{dagId}/runs/{dagRunId}/clear",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
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
        **kwargs
    ) -> DagRun:  # noqa: E501
        """Set the state of a dag run  # noqa: E501

        Set the state of a dag run  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_dag_run(organization_id, workspace_id, runtime_id, dag_id, dag_run_id, data, async_req=True)
        >>> result = thread.get()

        :param organization_id: organization ID (required)
        :type organization_id: str
        :param workspace_id: ID of the workspace (required)
        :type workspace_id: str
        :param runtime_id: ID of the runtime (required)
        :type runtime_id: str
        :param dag_id: dag ID (required)
        :type dag_id: str
        :param dag_run_id: dag run ID (required)
        :type dag_run_id: str
        :param data: request body for updating a dag run (required)
        :type data: UpdateDagRunRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DagRun
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the update_dag_run_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        return self.update_dag_run_with_http_info(
            organization_id,
            workspace_id,
            runtime_id,
            dag_id,
            dag_run_id,
            data,
            **kwargs
        )  # noqa: E501

    @validate_arguments
    def update_dag_run_with_http_info(
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
        **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Set the state of a dag run  # noqa: E501

        Set the state of a dag run  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_dag_run_with_http_info(organization_id, workspace_id, runtime_id, dag_id, dag_run_id, data, async_req=True)
        >>> result = thread.get()

        :param organization_id: organization ID (required)
        :type organization_id: str
        :param workspace_id: ID of the workspace (required)
        :type workspace_id: str
        :param runtime_id: ID of the runtime (required)
        :type runtime_id: str
        :param dag_id: dag ID (required)
        :type dag_id: str
        :param dag_run_id: dag run ID (required)
        :type dag_run_id: str
        :param data: request body for updating a dag run (required)
        :type data: UpdateDagRunRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(DagRun, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            "organization_id",
            "workspace_id",
            "runtime_id",
            "dag_id",
            "dag_run_id",
            "data",
        ]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dag_run" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["organization_id"]:
            _path_params["organizationId"] = _params["organization_id"]

        if _params["workspace_id"]:
            _path_params["workspaceId"] = _params["workspace_id"]

        if _params["runtime_id"]:
            _path_params["runtimeId"] = _params["runtime_id"]

        if _params["dag_id"]:
            _path_params["dagId"] = _params["dag_id"]

        if _params["dag_run_id"]:
            _path_params["dagRunId"] = _params["dag_run_id"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params["data"] is not None:
            _body_params = _params["data"]

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["application/json"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list

        # authentication setting
        _auth_settings = ["JWT"]  # noqa: E501

        _response_types_map = {
            "200": "DagRun",
            "400": "Error",
            "401": "Error",
            "403": "Error",
            "404": "Error",
            "500": "Error",
        }

        return self.api_client.call_api(
            "/organizations/{organizationId}/workspaces/{workspaceId}/runtimes/{runtimeId}/dags/{dagId}/runs/{dagRunId}",
            "PATCH",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )