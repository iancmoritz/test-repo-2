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

from typing import List, Optional

from astronomer_core_api.sdk.models.cluster_options import ClusterOptions
from astronomer_core_api.sdk.models.deployment_options import DeploymentOptions

from astronomer_core_api.sdk.api_client import ApiClient
from astronomer_core_api.sdk.api_response import ApiResponse
from astronomer_core_api.sdk.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class OptionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_cluster_options(
        self,
        type: Annotated[StrictStr, Field(..., description="cluster type")],
        provider: Annotated[
            Optional[StrictStr], Field(description="cloud provider")
        ] = None,
        **kwargs
    ) -> List[ClusterOptions]:  # noqa: E501
        """Cluster options  # noqa: E501

        Cluster options  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cluster_options(type, provider, async_req=True)
        >>> result = thread.get()

        :param type: cluster type (required)
        :type type: str
        :param provider: cloud provider
        :type provider: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[ClusterOptions]
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the get_cluster_options_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        return self.get_cluster_options_with_http_info(
            type, provider, **kwargs
        )  # noqa: E501

    @validate_arguments
    def get_cluster_options_with_http_info(
        self,
        type: Annotated[StrictStr, Field(..., description="cluster type")],
        provider: Annotated[
            Optional[StrictStr], Field(description="cloud provider")
        ] = None,
        **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Cluster options  # noqa: E501

        Cluster options  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cluster_options_with_http_info(type, provider, async_req=True)
        >>> result = thread.get()

        :param type: cluster type (required)
        :type type: str
        :param provider: cloud provider
        :type provider: str
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
        :rtype: tuple(List[ClusterOptions], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["type", "provider"]
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
                    " to method get_cluster_options" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get("provider") is not None:  # noqa: E501
            _query_params.append(("provider", _params["provider"]))

        if _params.get("type") is not None:  # noqa: E501
            _query_params.append(("type", _params["type"]))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = ["JWT"]  # noqa: E501

        _response_types_map = {
            "200": "List[ClusterOptions]",
            "400": "Error",
            "401": "Error",
            "403": "Error",
            "404": "Error",
            "500": "Error",
        }

        return self.api_client.call_api(
            "/options/cluster",
            "GET",
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
    def get_deployment_options(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        **kwargs
    ) -> DeploymentOptions:  # noqa: E501
        """Deployment options  # noqa: E501

        Deployment options  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_deployment_options(organization_id, async_req=True)
        >>> result = thread.get()

        :param organization_id: organization ID (required)
        :type organization_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DeploymentOptions
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the get_deployment_options_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        return self.get_deployment_options_with_http_info(
            organization_id, **kwargs
        )  # noqa: E501

    @validate_arguments
    def get_deployment_options_with_http_info(
        self,
        organization_id: Annotated[
            StrictStr, Field(..., description="organization ID")
        ],
        **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Deployment options  # noqa: E501

        Deployment options  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_deployment_options_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param organization_id: organization ID (required)
        :type organization_id: str
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
        :rtype: tuple(DeploymentOptions, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["organization_id"]
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
                    " to method get_deployment_options" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["organization_id"]:
            _path_params["organizationId"] = _params["organization_id"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = ["JWT"]  # noqa: E501

        _response_types_map = {
            "200": "DeploymentOptions",
            "400": "Error",
            "401": "Error",
            "403": "Error",
            "500": "Error",
        }

        return self.api_client.call_api(
            "/organizations/{organizationId}/options/deployment",
            "GET",
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