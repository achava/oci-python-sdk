# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SoftwareUpdateEventData(object):
    """
    Provides additional information for a software update event.
    """

    #: A constant which can be used with the operation_type property of a SoftwareUpdateEventData.
    #: This constant has a value of "UPDATE_ALL_PACKAGES"
    OPERATION_TYPE_UPDATE_ALL_PACKAGES = "UPDATE_ALL_PACKAGES"

    #: A constant which can be used with the operation_type property of a SoftwareUpdateEventData.
    #: This constant has a value of "INSTALL_PACKAGES"
    OPERATION_TYPE_INSTALL_PACKAGES = "INSTALL_PACKAGES"

    #: A constant which can be used with the operation_type property of a SoftwareUpdateEventData.
    #: This constant has a value of "REMOVE_PACKAGES"
    OPERATION_TYPE_REMOVE_PACKAGES = "REMOVE_PACKAGES"

    #: A constant which can be used with the operation_type property of a SoftwareUpdateEventData.
    #: This constant has a value of "UPDATE_PACKAGES"
    OPERATION_TYPE_UPDATE_PACKAGES = "UPDATE_PACKAGES"

    #: A constant which can be used with the operation_type property of a SoftwareUpdateEventData.
    #: This constant has a value of "UPDATE_SECURITY"
    OPERATION_TYPE_UPDATE_SECURITY = "UPDATE_SECURITY"

    #: A constant which can be used with the operation_type property of a SoftwareUpdateEventData.
    #: This constant has a value of "UPDATE_BUGFIX"
    OPERATION_TYPE_UPDATE_BUGFIX = "UPDATE_BUGFIX"

    #: A constant which can be used with the operation_type property of a SoftwareUpdateEventData.
    #: This constant has a value of "UPDATE_ENHANCEMENT"
    OPERATION_TYPE_UPDATE_ENHANCEMENT = "UPDATE_ENHANCEMENT"

    #: A constant which can be used with the operation_type property of a SoftwareUpdateEventData.
    #: This constant has a value of "UPDATE_OTHER"
    OPERATION_TYPE_UPDATE_OTHER = "UPDATE_OTHER"

    #: A constant which can be used with the status property of a SoftwareUpdateEventData.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a SoftwareUpdateEventData.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new SoftwareUpdateEventData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation_type:
            The value to assign to the operation_type property of this SoftwareUpdateEventData.
            Allowed values for this property are: "UPDATE_ALL_PACKAGES", "INSTALL_PACKAGES", "REMOVE_PACKAGES", "UPDATE_PACKAGES", "UPDATE_SECURITY", "UPDATE_BUGFIX", "UPDATE_ENHANCEMENT", "UPDATE_OTHER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param status:
            The value to assign to the status property of this SoftwareUpdateEventData.
            Allowed values for this property are: "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param additional_details:
            The value to assign to the additional_details property of this SoftwareUpdateEventData.
        :type additional_details: oci.os_management_hub.models.WorkRequestEventDataAdditionalDetails

        """
        self.swagger_types = {
            'operation_type': 'str',
            'status': 'str',
            'additional_details': 'WorkRequestEventDataAdditionalDetails'
        }

        self.attribute_map = {
            'operation_type': 'operationType',
            'status': 'status',
            'additional_details': 'additionalDetails'
        }

        self._operation_type = None
        self._status = None
        self._additional_details = None

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this SoftwareUpdateEventData.
        Type of software update operation.

        Allowed values for this property are: "UPDATE_ALL_PACKAGES", "INSTALL_PACKAGES", "REMOVE_PACKAGES", "UPDATE_PACKAGES", "UPDATE_SECURITY", "UPDATE_BUGFIX", "UPDATE_ENHANCEMENT", "UPDATE_OTHER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this SoftwareUpdateEventData.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this SoftwareUpdateEventData.
        Type of software update operation.


        :param operation_type: The operation_type of this SoftwareUpdateEventData.
        :type: str
        """
        allowed_values = ["UPDATE_ALL_PACKAGES", "INSTALL_PACKAGES", "REMOVE_PACKAGES", "UPDATE_PACKAGES", "UPDATE_SECURITY", "UPDATE_BUGFIX", "UPDATE_ENHANCEMENT", "UPDATE_OTHER"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this SoftwareUpdateEventData.
        Status of the software update.

        Allowed values for this property are: "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this SoftwareUpdateEventData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SoftwareUpdateEventData.
        Status of the software update.


        :param status: The status of this SoftwareUpdateEventData.
        :type: str
        """
        allowed_values = ["SUCCEEDED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def additional_details(self):
        """
        Gets the additional_details of this SoftwareUpdateEventData.

        :return: The additional_details of this SoftwareUpdateEventData.
        :rtype: oci.os_management_hub.models.WorkRequestEventDataAdditionalDetails
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(self, additional_details):
        """
        Sets the additional_details of this SoftwareUpdateEventData.

        :param additional_details: The additional_details of this SoftwareUpdateEventData.
        :type: oci.os_management_hub.models.WorkRequestEventDataAdditionalDetails
        """
        self._additional_details = additional_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other