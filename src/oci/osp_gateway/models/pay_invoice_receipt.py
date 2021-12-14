# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PayInvoiceReceipt(object):
    """
    Invoice payment action response
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PayInvoiceReceipt object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param url:
            The value to assign to the url property of this PayInvoiceReceipt.
        :type url: str

        :param header_id:
            The value to assign to the header_id property of this PayInvoiceReceipt.
        :type header_id: str

        :param token:
            The value to assign to the token property of this PayInvoiceReceipt.
        :type token: str

        """
        self.swagger_types = {
            'url': 'str',
            'header_id': 'str',
            'token': 'str'
        }

        self.attribute_map = {
            'url': 'url',
            'header_id': 'headerId',
            'token': 'token'
        }

        self._url = None
        self._header_id = None
        self._token = None

    @property
    def url(self):
        """
        Gets the url of this PayInvoiceReceipt.
        Url of the Payment Service


        :return: The url of this PayInvoiceReceipt.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this PayInvoiceReceipt.
        Url of the Payment Service


        :param url: The url of this PayInvoiceReceipt.
        :type: str
        """
        self._url = url

    @property
    def header_id(self):
        """
        **[Required]** Gets the header_id of this PayInvoiceReceipt.
        Payment header id


        :return: The header_id of this PayInvoiceReceipt.
        :rtype: str
        """
        return self._header_id

    @header_id.setter
    def header_id(self, header_id):
        """
        Sets the header_id of this PayInvoiceReceipt.
        Payment header id


        :param header_id: The header_id of this PayInvoiceReceipt.
        :type: str
        """
        self._header_id = header_id

    @property
    def token(self):
        """
        Gets the token of this PayInvoiceReceipt.
        Token created for Payment Service


        :return: The token of this PayInvoiceReceipt.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this PayInvoiceReceipt.
        Token created for Payment Service


        :param token: The token of this PayInvoiceReceipt.
        :type: str
        """
        self._token = token

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
