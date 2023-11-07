# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JavaDownloadReport(object):
    """
    Details about a Java download report in a tenancy.
    The report is a file in Object Storage. It contains the download records in a specific format.
    """

    #: A constant which can be used with the format property of a JavaDownloadReport.
    #: This constant has a value of "CSV"
    FORMAT_CSV = "CSV"

    #: A constant which can be used with the checksum_type property of a JavaDownloadReport.
    #: This constant has a value of "SHA256"
    CHECKSUM_TYPE_SHA256 = "SHA256"

    #: A constant which can be used with the lifecycle_state property of a JavaDownloadReport.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a JavaDownloadReport.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a JavaDownloadReport.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a JavaDownloadReport.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a JavaDownloadReport.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a JavaDownloadReport.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a JavaDownloadReport.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new JavaDownloadReport object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this JavaDownloadReport.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this JavaDownloadReport.
        :type display_name: str

        :param format:
            The value to assign to the format property of this JavaDownloadReport.
            Allowed values for this property are: "CSV", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type format: str

        :param file_size_in_bytes:
            The value to assign to the file_size_in_bytes property of this JavaDownloadReport.
        :type file_size_in_bytes: int

        :param checksum_type:
            The value to assign to the checksum_type property of this JavaDownloadReport.
            Allowed values for this property are: "SHA256", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type checksum_type: str

        :param checksum_value:
            The value to assign to the checksum_value property of this JavaDownloadReport.
        :type checksum_value: str

        :param compartment_id:
            The value to assign to the compartment_id property of this JavaDownloadReport.
        :type compartment_id: str

        :param created_by:
            The value to assign to the created_by property of this JavaDownloadReport.
        :type created_by: oci.jms_java_downloads.models.Principal

        :param time_created:
            The value to assign to the time_created property of this JavaDownloadReport.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this JavaDownloadReport.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "NEEDS_ATTENTION", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this JavaDownloadReport.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this JavaDownloadReport.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this JavaDownloadReport.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'format': 'str',
            'file_size_in_bytes': 'int',
            'checksum_type': 'str',
            'checksum_value': 'str',
            'compartment_id': 'str',
            'created_by': 'Principal',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'format': 'format',
            'file_size_in_bytes': 'fileSizeInBytes',
            'checksum_type': 'checksumType',
            'checksum_value': 'checksumValue',
            'compartment_id': 'compartmentId',
            'created_by': 'createdBy',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._format = None
        self._file_size_in_bytes = None
        self._checksum_type = None
        self._checksum_value = None
        self._compartment_id = None
        self._created_by = None
        self._time_created = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this JavaDownloadReport.
        The `OCID`__ of the Java download report.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this JavaDownloadReport.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this JavaDownloadReport.
        The `OCID`__ of the Java download report.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this JavaDownloadReport.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this JavaDownloadReport.
        Display name for the Java download report.


        :return: The display_name of this JavaDownloadReport.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this JavaDownloadReport.
        Display name for the Java download report.


        :param display_name: The display_name of this JavaDownloadReport.
        :type: str
        """
        self._display_name = display_name

    @property
    def format(self):
        """
        **[Required]** Gets the format of this JavaDownloadReport.
        The file format of the Java download report.

        Allowed values for this property are: "CSV", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The format of this JavaDownloadReport.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this JavaDownloadReport.
        The file format of the Java download report.


        :param format: The format of this JavaDownloadReport.
        :type: str
        """
        allowed_values = ["CSV"]
        if not value_allowed_none_or_none_sentinel(format, allowed_values):
            format = 'UNKNOWN_ENUM_VALUE'
        self._format = format

    @property
    def file_size_in_bytes(self):
        """
        **[Required]** Gets the file_size_in_bytes of this JavaDownloadReport.
        Approximate size of the Java download report file in bytes.


        :return: The file_size_in_bytes of this JavaDownloadReport.
        :rtype: int
        """
        return self._file_size_in_bytes

    @file_size_in_bytes.setter
    def file_size_in_bytes(self, file_size_in_bytes):
        """
        Sets the file_size_in_bytes of this JavaDownloadReport.
        Approximate size of the Java download report file in bytes.


        :param file_size_in_bytes: The file_size_in_bytes of this JavaDownloadReport.
        :type: int
        """
        self._file_size_in_bytes = file_size_in_bytes

    @property
    def checksum_type(self):
        """
        **[Required]** Gets the checksum_type of this JavaDownloadReport.
        The algorithm used for calculating the checksum.

        Allowed values for this property are: "SHA256", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The checksum_type of this JavaDownloadReport.
        :rtype: str
        """
        return self._checksum_type

    @checksum_type.setter
    def checksum_type(self, checksum_type):
        """
        Sets the checksum_type of this JavaDownloadReport.
        The algorithm used for calculating the checksum.


        :param checksum_type: The checksum_type of this JavaDownloadReport.
        :type: str
        """
        allowed_values = ["SHA256"]
        if not value_allowed_none_or_none_sentinel(checksum_type, allowed_values):
            checksum_type = 'UNKNOWN_ENUM_VALUE'
        self._checksum_type = checksum_type

    @property
    def checksum_value(self):
        """
        **[Required]** Gets the checksum_value of this JavaDownloadReport.
        The checksum value of the Java download report file.


        :return: The checksum_value of this JavaDownloadReport.
        :rtype: str
        """
        return self._checksum_value

    @checksum_value.setter
    def checksum_value(self, checksum_value):
        """
        Sets the checksum_value of this JavaDownloadReport.
        The checksum value of the Java download report file.


        :param checksum_value: The checksum_value of this JavaDownloadReport.
        :type: str
        """
        self._checksum_value = checksum_value

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this JavaDownloadReport.
        The `OCID`__ of the tenancy scoped to the Java download report.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this JavaDownloadReport.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this JavaDownloadReport.
        The `OCID`__ of the tenancy scoped to the Java download report.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this JavaDownloadReport.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def created_by(self):
        """
        **[Required]** Gets the created_by of this JavaDownloadReport.

        :return: The created_by of this JavaDownloadReport.
        :rtype: oci.jms_java_downloads.models.Principal
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this JavaDownloadReport.

        :param created_by: The created_by of this JavaDownloadReport.
        :type: oci.jms_java_downloads.models.Principal
        """
        self._created_by = created_by

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this JavaDownloadReport.
        The time the Java download report was created. An RFC3339 formatted datetime string.


        :return: The time_created of this JavaDownloadReport.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this JavaDownloadReport.
        The time the Java download report was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this JavaDownloadReport.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this JavaDownloadReport.
        The current state of the Java download report.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "NEEDS_ATTENTION", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this JavaDownloadReport.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this JavaDownloadReport.
        The current state of the Java download report.


        :param lifecycle_state: The lifecycle_state of this JavaDownloadReport.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "NEEDS_ATTENTION", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this JavaDownloadReport.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`. (See `Managing Tags and Tag Namespaces`__.)

        __ https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm


        :return: The freeform_tags of this JavaDownloadReport.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this JavaDownloadReport.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`. (See `Managing Tags and Tag Namespaces`__.)

        __ https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm


        :param freeform_tags: The freeform_tags of this JavaDownloadReport.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this JavaDownloadReport.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See `Understanding Free-form Tags`__).

        __ https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm


        :return: The defined_tags of this JavaDownloadReport.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this JavaDownloadReport.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See `Understanding Free-form Tags`__).

        __ https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm


        :param defined_tags: The defined_tags of this JavaDownloadReport.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this JavaDownloadReport.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this JavaDownloadReport.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this JavaDownloadReport.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this JavaDownloadReport.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
