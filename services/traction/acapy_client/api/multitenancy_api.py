"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.7.2
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from acapy_client.api_client import ApiClient, Endpoint as _Endpoint
from acapy_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from acapy_client.model.create_wallet_request import CreateWalletRequest
from acapy_client.model.create_wallet_response import CreateWalletResponse
from acapy_client.model.create_wallet_token_request import CreateWalletTokenRequest
from acapy_client.model.create_wallet_token_response import CreateWalletTokenResponse
from acapy_client.model.remove_wallet_request import RemoveWalletRequest
from acapy_client.model.update_wallet_request import UpdateWalletRequest
from acapy_client.model.wallet_list import WalletList
from acapy_client.model.wallet_record import WalletRecord


class MultitenancyApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.multitenancy_wallet_post_endpoint = _Endpoint(
            settings={
                "response_type": (CreateWalletResponse,),
                "auth": ["AuthorizationHeader"],
                "endpoint_path": "/multitenancy/wallet",
                "operation_id": "multitenancy_wallet_post",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "body",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (CreateWalletRequest,),
                },
                "attribute_map": {},
                "location_map": {
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.multitenancy_wallet_wallet_id_get_endpoint = _Endpoint(
            settings={
                "response_type": (WalletRecord,),
                "auth": ["AuthorizationHeader"],
                "endpoint_path": "/multitenancy/wallet/{wallet_id}",
                "operation_id": "multitenancy_wallet_wallet_id_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "wallet_id",
                ],
                "required": [
                    "wallet_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "wallet_id": (str,),
                },
                "attribute_map": {
                    "wallet_id": "wallet_id",
                },
                "location_map": {
                    "wallet_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.multitenancy_wallet_wallet_id_put_endpoint = _Endpoint(
            settings={
                "response_type": (WalletRecord,),
                "auth": ["AuthorizationHeader"],
                "endpoint_path": "/multitenancy/wallet/{wallet_id}",
                "operation_id": "multitenancy_wallet_wallet_id_put",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": [
                    "wallet_id",
                    "body",
                ],
                "required": [
                    "wallet_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "wallet_id": (str,),
                    "body": (UpdateWalletRequest,),
                },
                "attribute_map": {
                    "wallet_id": "wallet_id",
                },
                "location_map": {
                    "wallet_id": "path",
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.multitenancy_wallet_wallet_id_remove_post_endpoint = _Endpoint(
            settings={
                "response_type": (
                    bool,
                    date,
                    datetime,
                    dict,
                    float,
                    int,
                    list,
                    str,
                    none_type,
                ),
                "auth": ["AuthorizationHeader"],
                "endpoint_path": "/multitenancy/wallet/{wallet_id}/remove",
                "operation_id": "multitenancy_wallet_wallet_id_remove_post",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "wallet_id",
                    "body",
                ],
                "required": [
                    "wallet_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "wallet_id": (str,),
                    "body": (RemoveWalletRequest,),
                },
                "attribute_map": {
                    "wallet_id": "wallet_id",
                },
                "location_map": {
                    "wallet_id": "path",
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.multitenancy_wallet_wallet_id_token_post_endpoint = _Endpoint(
            settings={
                "response_type": (CreateWalletTokenResponse,),
                "auth": ["AuthorizationHeader"],
                "endpoint_path": "/multitenancy/wallet/{wallet_id}/token",
                "operation_id": "multitenancy_wallet_wallet_id_token_post",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "wallet_id",
                    "body",
                ],
                "required": [
                    "wallet_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "wallet_id": (str,),
                    "body": (CreateWalletTokenRequest,),
                },
                "attribute_map": {
                    "wallet_id": "wallet_id",
                },
                "location_map": {
                    "wallet_id": "path",
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.multitenancy_wallets_get_endpoint = _Endpoint(
            settings={
                "response_type": (WalletList,),
                "auth": ["AuthorizationHeader"],
                "endpoint_path": "/multitenancy/wallets",
                "operation_id": "multitenancy_wallets_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "wallet_name",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "wallet_name": (str,),
                },
                "attribute_map": {
                    "wallet_name": "wallet_name",
                },
                "location_map": {
                    "wallet_name": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def multitenancy_wallet_post(self, **kwargs):
        """Create a subwallet  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.multitenancy_wallet_post(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            body (CreateWalletRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CreateWalletResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        return self.multitenancy_wallet_post_endpoint.call_with_http_info(**kwargs)

    def multitenancy_wallet_wallet_id_get(self, wallet_id, **kwargs):
        """Get a single subwallet  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.multitenancy_wallet_wallet_id_get(wallet_id, async_req=True)
        >>> result = thread.get()

        Args:
            wallet_id (str): Subwallet identifier

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            WalletRecord
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["wallet_id"] = wallet_id
        return self.multitenancy_wallet_wallet_id_get_endpoint.call_with_http_info(
            **kwargs
        )

    def multitenancy_wallet_wallet_id_put(self, wallet_id, **kwargs):
        """Update a subwallet  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.multitenancy_wallet_wallet_id_put(wallet_id, async_req=True)
        >>> result = thread.get()

        Args:
            wallet_id (str): Subwallet identifier

        Keyword Args:
            body (UpdateWalletRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            WalletRecord
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["wallet_id"] = wallet_id
        return self.multitenancy_wallet_wallet_id_put_endpoint.call_with_http_info(
            **kwargs
        )

    def multitenancy_wallet_wallet_id_remove_post(self, wallet_id, **kwargs):
        """Remove a subwallet  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.multitenancy_wallet_wallet_id_remove_post(wallet_id, async_req=True)
        >>> result = thread.get()

        Args:
            wallet_id (str): Subwallet identifier

        Keyword Args:
            body (RemoveWalletRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["wallet_id"] = wallet_id
        return (
            self.multitenancy_wallet_wallet_id_remove_post_endpoint.call_with_http_info(
                **kwargs
            )
        )

    def multitenancy_wallet_wallet_id_token_post(self, wallet_id, **kwargs):
        """Get auth token for a subwallet  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.multitenancy_wallet_wallet_id_token_post(wallet_id, async_req=True)
        >>> result = thread.get()

        Args:
            wallet_id (str):

        Keyword Args:
            body (CreateWalletTokenRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CreateWalletTokenResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["wallet_id"] = wallet_id
        return (
            self.multitenancy_wallet_wallet_id_token_post_endpoint.call_with_http_info(
                **kwargs
            )
        )

    def multitenancy_wallets_get(self, **kwargs):
        """Query subwallets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.multitenancy_wallets_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            wallet_name (str): Wallet name. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            WalletList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        return self.multitenancy_wallets_get_endpoint.call_with_http_info(**kwargs)
