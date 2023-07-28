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

from pydantic import Field

from astronomercoreapi.models.has_permissions import HasPermissions
from astronomercoreapi.models.has_permissions_request import HasPermissionsRequest

from astronomercoreapi.api_client import ApiClient
from astronomercoreapi.api_response import ApiResponse
from astronomercoreapi.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AuthzApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def has_permissions(self, body : Annotated[HasPermissionsRequest, Field(..., description="request body for get permissions")], **kwargs) -> HasPermissions:  # noqa: E501
        """Get current user permission information  # noqa: E501

        Get current user permission information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.has_permissions(body, async_req=True)
        >>> result = thread.get()

        :param body: request body for get permissions (required)
        :type body: HasPermissionsRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: HasPermissions
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the has_permissions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.has_permissions_with_http_info(body, **kwargs)  # noqa: E501

    @validate_arguments
    def has_permissions_with_http_info(self, body : Annotated[HasPermissionsRequest, Field(..., description="request body for get permissions")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get current user permission information  # noqa: E501

        Get current user permission information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.has_permissions_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param body: request body for get permissions (required)
        :type body: HasPermissionsRequest
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
        :rtype: tuple(HasPermissions, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method has_permissions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['body'] is not None:
            _body_params = _params['body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['JWT']  # noqa: E501

        _response_types_map = {
            '200': "HasPermissions",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/authz/hasPermissions', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
