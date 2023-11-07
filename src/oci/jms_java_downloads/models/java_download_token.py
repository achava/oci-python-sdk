# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JavaDownloadToken(object):
    """
    A JavaDownloadToken is a primary resource for the script friendly URLs. The value of this token serves as the authorization token for the download.
    """

    #: A constant which can be used with the lifecycle_state property of a JavaDownloadToken.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a JavaDownloadToken.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a JavaDownloadToken.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a JavaDownloadToken.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a JavaDownloadToken.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a JavaDownloadToken.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a JavaDownloadToken.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_details property of a JavaDownloadToken.
    #: This constant has a value of "EXPIRED"
    LIFECYCLE_DETAILS_EXPIRED = "EXPIRED"

    #: A constant which can be used with the lifecycle_details property of a JavaDownloadToken.
    #: This constant has a value of "REVOKING"
    LIFECYCLE_DETAILS_REVOKING = "REVOKING"

    #: A constant which can be used with the lifecycle_details property of a JavaDownloadToken.
    #: This constant has a value of "REVOKED"
    LIFECYCLE_DETAILS_REVOKED = "REVOKED"

    def __init__(self, **kwargs):
        """
        Initializes a new JavaDownloadToken object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this JavaDownloadToken.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this JavaDownloadToken.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this JavaDownloadToken.
        :type compartment_id: str

        :param created_by:
            The value to assign to the created_by property of this JavaDownloadToken.
        :type created_by: oci.jms_java_downloads.models.Principal

        :param last_updated_by:
            The value to assign to the last_updated_by property of this JavaDownloadToken.
        :type last_updated_by: oci.jms_java_downloads.models.Principal

        :param description:
            The value to assign to the description property of this JavaDownloadToken.
        :type description: str

        :param value:
            The value to assign to the value property of this JavaDownloadToken.
        :type value: str

        :param time_created:
            The value to assign to the time_created property of this JavaDownloadToken.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this JavaDownloadToken.
        :type time_updated: datetime

        :param time_last_used:
            The value to assign to the time_last_used property of this JavaDownloadToken.
        :type time_last_used: datetime

        :param time_expires:
            The value to assign to the time_expires property of this JavaDownloadToken.
        :type time_expires: datetime

        :param java_version:
            The value to assign to the java_version property of this JavaDownloadToken.
        :type java_version: str

        :param license_type:
            The value to assign to the license_type property of this JavaDownloadToken.
        :type license_type: list[oci.jms_java_downloads.models.LicenseType]

        :param is_default:
            The value to assign to the is_default property of this JavaDownloadToken.
        :type is_default: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this JavaDownloadToken.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "NEEDS_ATTENTION", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this JavaDownloadToken.
            Allowed values for this property are: "EXPIRED", "REVOKING", "REVOKED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this JavaDownloadToken.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this JavaDownloadToken.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this JavaDownloadToken.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'created_by': 'Principal',
            'last_updated_by': 'Principal',
            'description': 'str',
            'value': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_last_used': 'datetime',
            'time_expires': 'datetime',
            'java_version': 'str',
            'license_type': 'list[LicenseType]',
            'is_default': 'bool',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'created_by': 'createdBy',
            'last_updated_by': 'lastUpdatedBy',
            'description': 'description',
            'value': 'value',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_last_used': 'timeLastUsed',
            'time_expires': 'timeExpires',
            'java_version': 'javaVersion',
            'license_type': 'licenseType',
            'is_default': 'isDefault',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._created_by = None
        self._last_updated_by = None
        self._description = None
        self._value = None
        self._time_created = None
        self._time_updated = None
        self._time_last_used = None
        self._time_expires = None
        self._java_version = None
        self._license_type = None
        self._is_default = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this JavaDownloadToken.
        The `OCID`__ of the JavaDownloadToken.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this JavaDownloadToken.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this JavaDownloadToken.
        The `OCID`__ of the JavaDownloadToken.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this JavaDownloadToken.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this JavaDownloadToken.
        User provided display name of the JavaDownloadToken.


        :return: The display_name of this JavaDownloadToken.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this JavaDownloadToken.
        User provided display name of the JavaDownloadToken.


        :param display_name: The display_name of this JavaDownloadToken.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this JavaDownloadToken.
        The `OCID`__ of the tenancy scoped to the JavaDownloadToken.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this JavaDownloadToken.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this JavaDownloadToken.
        The `OCID`__ of the tenancy scoped to the JavaDownloadToken.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this JavaDownloadToken.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def created_by(self):
        """
        **[Required]** Gets the created_by of this JavaDownloadToken.

        :return: The created_by of this JavaDownloadToken.
        :rtype: oci.jms_java_downloads.models.Principal
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this JavaDownloadToken.

        :param created_by: The created_by of this JavaDownloadToken.
        :type: oci.jms_java_downloads.models.Principal
        """
        self._created_by = created_by

    @property
    def last_updated_by(self):
        """
        Gets the last_updated_by of this JavaDownloadToken.

        :return: The last_updated_by of this JavaDownloadToken.
        :rtype: oci.jms_java_downloads.models.Principal
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """
        Sets the last_updated_by of this JavaDownloadToken.

        :param last_updated_by: The last_updated_by of this JavaDownloadToken.
        :type: oci.jms_java_downloads.models.Principal
        """
        self._last_updated_by = last_updated_by

    @property
    def description(self):
        """
        **[Required]** Gets the description of this JavaDownloadToken.
        User provided description of the JavaDownloadToken.


        :return: The description of this JavaDownloadToken.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this JavaDownloadToken.
        User provided description of the JavaDownloadToken.


        :param description: The description of this JavaDownloadToken.
        :type: str
        """
        self._description = description

    @property
    def value(self):
        """
        **[Required]** Gets the value of this JavaDownloadToken.
        Uniquely generated value for the JavaDownloadToken.


        :return: The value of this JavaDownloadToken.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this JavaDownloadToken.
        Uniquely generated value for the JavaDownloadToken.


        :param value: The value of this JavaDownloadToken.
        :type: str
        """
        self._value = value

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this JavaDownloadToken.
        The time the JavaDownloadToken was created. An RFC3339 formatted datetime string.


        :return: The time_created of this JavaDownloadToken.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this JavaDownloadToken.
        The time the JavaDownloadToken was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this JavaDownloadToken.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this JavaDownloadToken.
        The time the JavaDownloadToken was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this JavaDownloadToken.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this JavaDownloadToken.
        The time the JavaDownloadToken was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this JavaDownloadToken.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_last_used(self):
        """
        Gets the time_last_used of this JavaDownloadToken.
        The time the JavaDownloadToken was last used for download. An RFC3339 formatted datetime string.


        :return: The time_last_used of this JavaDownloadToken.
        :rtype: datetime
        """
        return self._time_last_used

    @time_last_used.setter
    def time_last_used(self, time_last_used):
        """
        Sets the time_last_used of this JavaDownloadToken.
        The time the JavaDownloadToken was last used for download. An RFC3339 formatted datetime string.


        :param time_last_used: The time_last_used of this JavaDownloadToken.
        :type: datetime
        """
        self._time_last_used = time_last_used

    @property
    def time_expires(self):
        """
        **[Required]** Gets the time_expires of this JavaDownloadToken.
        The expiry time of the JavaDownloadToken. An RFC3339 formatted datetime string.


        :return: The time_expires of this JavaDownloadToken.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this JavaDownloadToken.
        The expiry time of the JavaDownloadToken. An RFC3339 formatted datetime string.


        :param time_expires: The time_expires of this JavaDownloadToken.
        :type: datetime
        """
        self._time_expires = time_expires

    @property
    def java_version(self):
        """
        **[Required]** Gets the java_version of this JavaDownloadToken.
        The associated Java version of the JavaDownloadToken.


        :return: The java_version of this JavaDownloadToken.
        :rtype: str
        """
        return self._java_version

    @java_version.setter
    def java_version(self, java_version):
        """
        Sets the java_version of this JavaDownloadToken.
        The associated Java version of the JavaDownloadToken.


        :param java_version: The java_version of this JavaDownloadToken.
        :type: str
        """
        self._java_version = java_version

    @property
    def license_type(self):
        """
        Gets the license_type of this JavaDownloadToken.
        The license type(s) associated with the JavaDownloadToken.


        :return: The license_type of this JavaDownloadToken.
        :rtype: list[oci.jms_java_downloads.models.LicenseType]
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this JavaDownloadToken.
        The license type(s) associated with the JavaDownloadToken.


        :param license_type: The license_type of this JavaDownloadToken.
        :type: list[oci.jms_java_downloads.models.LicenseType]
        """
        self._license_type = license_type

    @property
    def is_default(self):
        """
        Gets the is_default of this JavaDownloadToken.
        A flag to indicate if the token is default.


        :return: The is_default of this JavaDownloadToken.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this JavaDownloadToken.
        A flag to indicate if the token is default.


        :param is_default: The is_default of this JavaDownloadToken.
        :type: bool
        """
        self._is_default = is_default

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this JavaDownloadToken.
        The current state of the JavaDownloadToken.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "NEEDS_ATTENTION", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this JavaDownloadToken.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this JavaDownloadToken.
        The current state of the JavaDownloadToken.


        :param lifecycle_state: The lifecycle_state of this JavaDownloadToken.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "NEEDS_ATTENTION", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this JavaDownloadToken.
        Possible lifecycle substates.

        Allowed values for this property are: "EXPIRED", "REVOKING", "REVOKED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_details of this JavaDownloadToken.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this JavaDownloadToken.
        Possible lifecycle substates.


        :param lifecycle_details: The lifecycle_details of this JavaDownloadToken.
        :type: str
        """
        allowed_values = ["EXPIRED", "REVOKING", "REVOKED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_details, allowed_values):
            lifecycle_details = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this JavaDownloadToken.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`. (See `Managing Tags and Tag Namespaces`__.)

        __ https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm


        :return: The freeform_tags of this JavaDownloadToken.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this JavaDownloadToken.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`. (See `Managing Tags and Tag Namespaces`__.)

        __ https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm


        :param freeform_tags: The freeform_tags of this JavaDownloadToken.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this JavaDownloadToken.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See `Understanding Free-form Tags`__).

        __ https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm


        :return: The defined_tags of this JavaDownloadToken.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this JavaDownloadToken.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See `Understanding Free-form Tags`__).

        __ https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm


        :param defined_tags: The defined_tags of this JavaDownloadToken.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this JavaDownloadToken.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this JavaDownloadToken.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this JavaDownloadToken.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this JavaDownloadToken.
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
