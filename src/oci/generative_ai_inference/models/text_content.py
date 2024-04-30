# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130

from .chat_content import ChatContent
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TextContent(ChatContent):
    """
    Represents a single instance of text chat content.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TextContent object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai_inference.models.TextContent.type` attribute
        of this class is ``TEXT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this TextContent.
            Allowed values for this property are: "TEXT"
        :type type: str

        :param text:
            The value to assign to the text property of this TextContent.
        :type text: str

        """
        self.swagger_types = {
            'type': 'str',
            'text': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'text': 'text'
        }

        self._type = None
        self._text = None
        self._type = 'TEXT'

    @property
    def text(self):
        """
        Gets the text of this TextContent.
        The text content.


        :return: The text of this TextContent.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this TextContent.
        The text content.


        :param text: The text of this TextContent.
        :type: str
        """
        self._text = text

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other