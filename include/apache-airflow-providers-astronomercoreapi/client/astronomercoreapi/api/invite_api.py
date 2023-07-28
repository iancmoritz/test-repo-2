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

from astronomercoreapi.models.create_user_invite_request import CreateUserInviteRequest
from astronomercoreapi.models.invite import Invite
from astronomercoreapi.models.update_invite_request import UpdateInviteRequest

from astronomercoreapi.api_client import ApiClient
from astronomercoreapi.api_response import ApiResponse
from astronomercoreapi.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class InviteApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_user_invite(self, organization_id : Annotated[StrictStr, Field(..., description="organization ID")], body : Annotated[CreateUserInviteRequest, Field(..., description="request body for create user invitation")], **kwargs) -> Invite:  # noqa: E501
        """Create a user invitation  # noqa: E501

        Create a user invitation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_user_invite(organization_id, body, async_req=True)
        >>> result = thread.get()

        :param organization_id: organization ID (required)
        :type organization_id: str
        :param body: request body for create user invitation (required)
        :type body: CreateUserInviteRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Invite
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_user_invite_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_user_invite_with_http_info(organization_id, body, **kwargs)  # noqa: E501

    @validate_arguments
    def create_user_invite_with_http_info(self, organization_id : Annotated[StrictStr, Field(..., description="organization ID")], body : Annotated[CreateUserInviteRequest, Field(..., description="request body for create user invitation")], **kwargs) -> ApiResponse:  # noqa: E501
        """Create a user invitation  # noqa: E501

        Create a user invitation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_user_invite_with_http_info(organization_id, body, async_req=True)
        >>> result = thread.get()

        :param organization_id: organization ID (required)
        :type organization_id: str
        :param body: request body for create user invitation (required)
        :type body: CreateUserInviteRequest
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
        :rtype: tuple(Invite, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'organization_id',
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
                    " to method create_user_invite" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['organization_id']:
            _path_params['organizationId'] = _params['organization_id']


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
            '200': "Invite",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/organizations/{organizationId}/invites', 'POST',
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

    @validate_arguments
    def delete_user_invite(self, organization_id : Annotated[StrictStr, Field(..., description="organization ID")], invite_id : Annotated[StrictStr, Field(..., description="user invite ID")], **kwargs) -> None:  # noqa: E501
        """Delete user invite  # noqa: E501

        Delete user invite  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_user_invite(organization_id, invite_id, async_req=True)
        >>> result = thread.get()

        :param organization_id: organization ID (required)
        :type organization_id: str
        :param invite_id: user invite ID (required)
        :type invite_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the delete_user_invite_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_user_invite_with_http_info(organization_id, invite_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_user_invite_with_http_info(self, organization_id : Annotated[StrictStr, Field(..., description="organization ID")], invite_id : Annotated[StrictStr, Field(..., description="user invite ID")], **kwargs) -> ApiResponse:  # noqa: E501
        """Delete user invite  # noqa: E501

        Delete user invite  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_user_invite_with_http_info(organization_id, invite_id, async_req=True)
        >>> result = thread.get()

        :param organization_id: organization ID (required)
        :type organization_id: str
        :param invite_id: user invite ID (required)
        :type invite_id: str
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
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'organization_id',
            'invite_id'
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
                    " to method delete_user_invite" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['organization_id']:
            _path_params['organizationId'] = _params['organization_id']

        if _params['invite_id']:
            _path_params['inviteId'] = _params['invite_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['JWT']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/organizations/{organizationId}/invites/{inviteId}', 'DELETE',
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

    @validate_arguments
    def get_user_invite(self, invite_id : Annotated[StrictStr, Field(..., description="invite ID or auth0 ticket ID")], **kwargs) -> Invite:  # noqa: E501
        """Get user invite  # noqa: E501

        Get user invite  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user_invite(invite_id, async_req=True)
        >>> result = thread.get()

        :param invite_id: invite ID or auth0 ticket ID (required)
        :type invite_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Invite
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_user_invite_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_user_invite_with_http_info(invite_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_user_invite_with_http_info(self, invite_id : Annotated[StrictStr, Field(..., description="invite ID or auth0 ticket ID")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get user invite  # noqa: E501

        Get user invite  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user_invite_with_http_info(invite_id, async_req=True)
        >>> result = thread.get()

        :param invite_id: invite ID or auth0 ticket ID (required)
        :type invite_id: str
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
        :rtype: tuple(Invite, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'invite_id'
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
                    " to method get_user_invite" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['invite_id']:
            _path_params['inviteId'] = _params['invite_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['JWT']  # noqa: E501

        _response_types_map = {
            '200': "Invite",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/auth/invites/{inviteId}', 'GET',
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

    @validate_arguments
    def update_self_user_invite(self, invite_id : Annotated[StrictStr, Field(..., description="invite ID")], body : Annotated[UpdateInviteRequest, Field(..., description="request body for update user self invitation")], **kwargs) -> Invite:  # noqa: E501
        """Update user invitation  # noqa: E501

        Update user invitation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_self_user_invite(invite_id, body, async_req=True)
        >>> result = thread.get()

        :param invite_id: invite ID (required)
        :type invite_id: str
        :param body: request body for update user self invitation (required)
        :type body: UpdateInviteRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Invite
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_self_user_invite_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_self_user_invite_with_http_info(invite_id, body, **kwargs)  # noqa: E501

    @validate_arguments
    def update_self_user_invite_with_http_info(self, invite_id : Annotated[StrictStr, Field(..., description="invite ID")], body : Annotated[UpdateInviteRequest, Field(..., description="request body for update user self invitation")], **kwargs) -> ApiResponse:  # noqa: E501
        """Update user invitation  # noqa: E501

        Update user invitation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_self_user_invite_with_http_info(invite_id, body, async_req=True)
        >>> result = thread.get()

        :param invite_id: invite ID (required)
        :type invite_id: str
        :param body: request body for update user self invitation (required)
        :type body: UpdateInviteRequest
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
        :rtype: tuple(Invite, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'invite_id',
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
                    " to method update_self_user_invite" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['invite_id']:
            _path_params['inviteId'] = _params['invite_id']


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
            '200': "Invite",
            '400': "Error",
            '401': "Error",
            '403': "Error",
            '404': "Error",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/users/self/invites/{inviteId}', 'POST',
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
