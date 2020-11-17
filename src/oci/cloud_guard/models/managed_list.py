# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedList(object):
    """
    A cloud guard list containing one or more items of a list type
    """

    #: A constant which can be used with the list_type property of a ManagedList.
    #: This constant has a value of "CIDR_BLOCK"
    LIST_TYPE_CIDR_BLOCK = "CIDR_BLOCK"

    #: A constant which can be used with the list_type property of a ManagedList.
    #: This constant has a value of "USERS"
    LIST_TYPE_USERS = "USERS"

    #: A constant which can be used with the list_type property of a ManagedList.
    #: This constant has a value of "GROUPS"
    LIST_TYPE_GROUPS = "GROUPS"

    #: A constant which can be used with the list_type property of a ManagedList.
    #: This constant has a value of "IPV4ADDRESS"
    LIST_TYPE_IPV4_ADDRESS = "IPV4ADDRESS"

    #: A constant which can be used with the list_type property of a ManagedList.
    #: This constant has a value of "IPV6ADDRESS"
    LIST_TYPE_IPV6_ADDRESS = "IPV6ADDRESS"

    #: A constant which can be used with the list_type property of a ManagedList.
    #: This constant has a value of "RESOURCE_OCID"
    LIST_TYPE_RESOURCE_OCID = "RESOURCE_OCID"

    #: A constant which can be used with the list_type property of a ManagedList.
    #: This constant has a value of "REGION"
    LIST_TYPE_REGION = "REGION"

    #: A constant which can be used with the list_type property of a ManagedList.
    #: This constant has a value of "COUNTRY"
    LIST_TYPE_COUNTRY = "COUNTRY"

    #: A constant which can be used with the list_type property of a ManagedList.
    #: This constant has a value of "STATE"
    LIST_TYPE_STATE = "STATE"

    #: A constant which can be used with the list_type property of a ManagedList.
    #: This constant has a value of "CITY"
    LIST_TYPE_CITY = "CITY"

    #: A constant which can be used with the list_type property of a ManagedList.
    #: This constant has a value of "TAGS"
    LIST_TYPE_TAGS = "TAGS"

    #: A constant which can be used with the feed_provider property of a ManagedList.
    #: This constant has a value of "CUSTOMER"
    FEED_PROVIDER_CUSTOMER = "CUSTOMER"

    #: A constant which can be used with the feed_provider property of a ManagedList.
    #: This constant has a value of "ORACLE"
    FEED_PROVIDER_ORACLE = "ORACLE"

    #: A constant which can be used with the lifecycle_state property of a ManagedList.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ManagedList.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ManagedList.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ManagedList.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ManagedList.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ManagedList.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ManagedList.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedList object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ManagedList.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ManagedList.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ManagedList.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagedList.
        :type compartment_id: str

        :param source_managed_list_id:
            The value to assign to the source_managed_list_id property of this ManagedList.
        :type source_managed_list_id: str

        :param list_type:
            The value to assign to the list_type property of this ManagedList.
            Allowed values for this property are: "CIDR_BLOCK", "USERS", "GROUPS", "IPV4ADDRESS", "IPV6ADDRESS", "RESOURCE_OCID", "REGION", "COUNTRY", "STATE", "CITY", "TAGS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type list_type: str

        :param list_items:
            The value to assign to the list_items property of this ManagedList.
        :type list_items: list[str]

        :param feed_provider:
            The value to assign to the feed_provider property of this ManagedList.
            Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type feed_provider: str

        :param is_editable:
            The value to assign to the is_editable property of this ManagedList.
        :type is_editable: bool

        :param time_created:
            The value to assign to the time_created property of this ManagedList.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ManagedList.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ManagedList.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecyle_details:
            The value to assign to the lifecyle_details property of this ManagedList.
        :type lifecyle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ManagedList.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ManagedList.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ManagedList.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'source_managed_list_id': 'str',
            'list_type': 'str',
            'list_items': 'list[str]',
            'feed_provider': 'str',
            'is_editable': 'bool',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecyle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'source_managed_list_id': 'sourceManagedListId',
            'list_type': 'listType',
            'list_items': 'listItems',
            'feed_provider': 'feedProvider',
            'is_editable': 'isEditable',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecyle_details': 'lifecyleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._source_managed_list_id = None
        self._list_type = None
        self._list_items = None
        self._feed_provider = None
        self._is_editable = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecyle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagedList.
        Unique identifier that is immutable on creation


        :return: The id of this ManagedList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagedList.
        Unique identifier that is immutable on creation


        :param id: The id of this ManagedList.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ManagedList.
        ManagedList display name


        :return: The display_name of this ManagedList.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagedList.
        ManagedList display name


        :param display_name: The display_name of this ManagedList.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ManagedList.
        ManagedList description


        :return: The description of this ManagedList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ManagedList.
        ManagedList description


        :param description: The description of this ManagedList.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagedList.
        Compartment Identifier where the resource is created


        :return: The compartment_id of this ManagedList.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagedList.
        Compartment Identifier where the resource is created


        :param compartment_id: The compartment_id of this ManagedList.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def source_managed_list_id(self):
        """
        Gets the source_managed_list_id of this ManagedList.
        OCID of the Source ManagedList


        :return: The source_managed_list_id of this ManagedList.
        :rtype: str
        """
        return self._source_managed_list_id

    @source_managed_list_id.setter
    def source_managed_list_id(self, source_managed_list_id):
        """
        Sets the source_managed_list_id of this ManagedList.
        OCID of the Source ManagedList


        :param source_managed_list_id: The source_managed_list_id of this ManagedList.
        :type: str
        """
        self._source_managed_list_id = source_managed_list_id

    @property
    def list_type(self):
        """
        **[Required]** Gets the list_type of this ManagedList.
        type of the list

        Allowed values for this property are: "CIDR_BLOCK", "USERS", "GROUPS", "IPV4ADDRESS", "IPV6ADDRESS", "RESOURCE_OCID", "REGION", "COUNTRY", "STATE", "CITY", "TAGS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The list_type of this ManagedList.
        :rtype: str
        """
        return self._list_type

    @list_type.setter
    def list_type(self, list_type):
        """
        Sets the list_type of this ManagedList.
        type of the list


        :param list_type: The list_type of this ManagedList.
        :type: str
        """
        allowed_values = ["CIDR_BLOCK", "USERS", "GROUPS", "IPV4ADDRESS", "IPV6ADDRESS", "RESOURCE_OCID", "REGION", "COUNTRY", "STATE", "CITY", "TAGS"]
        if not value_allowed_none_or_none_sentinel(list_type, allowed_values):
            list_type = 'UNKNOWN_ENUM_VALUE'
        self._list_type = list_type

    @property
    def list_items(self):
        """
        Gets the list_items of this ManagedList.
        List of ManagedListItem


        :return: The list_items of this ManagedList.
        :rtype: list[str]
        """
        return self._list_items

    @list_items.setter
    def list_items(self, list_items):
        """
        Sets the list_items of this ManagedList.
        List of ManagedListItem


        :param list_items: The list_items of this ManagedList.
        :type: list[str]
        """
        self._list_items = list_items

    @property
    def feed_provider(self):
        """
        Gets the feed_provider of this ManagedList.
        provider of the feed

        Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The feed_provider of this ManagedList.
        :rtype: str
        """
        return self._feed_provider

    @feed_provider.setter
    def feed_provider(self, feed_provider):
        """
        Sets the feed_provider of this ManagedList.
        provider of the feed


        :param feed_provider: The feed_provider of this ManagedList.
        :type: str
        """
        allowed_values = ["CUSTOMER", "ORACLE"]
        if not value_allowed_none_or_none_sentinel(feed_provider, allowed_values):
            feed_provider = 'UNKNOWN_ENUM_VALUE'
        self._feed_provider = feed_provider

    @property
    def is_editable(self):
        """
        Gets the is_editable of this ManagedList.
        If this list is editable or not


        :return: The is_editable of this ManagedList.
        :rtype: bool
        """
        return self._is_editable

    @is_editable.setter
    def is_editable(self, is_editable):
        """
        Sets the is_editable of this ManagedList.
        If this list is editable or not


        :param is_editable: The is_editable of this ManagedList.
        :type: bool
        """
        self._is_editable = is_editable

    @property
    def time_created(self):
        """
        Gets the time_created of this ManagedList.
        The date and time the managed list was created. Format defined by RFC3339.


        :return: The time_created of this ManagedList.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ManagedList.
        The date and time the managed list was created. Format defined by RFC3339.


        :param time_created: The time_created of this ManagedList.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ManagedList.
        The date and time the managed list was updated. Format defined by RFC3339.


        :return: The time_updated of this ManagedList.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ManagedList.
        The date and time the managed list was updated. Format defined by RFC3339.


        :param time_updated: The time_updated of this ManagedList.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ManagedList.
        The current state of the resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ManagedList.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ManagedList.
        The current state of the resource.


        :param lifecycle_state: The lifecycle_state of this ManagedList.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecyle_details(self):
        """
        Gets the lifecyle_details of this ManagedList.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecyle_details of this ManagedList.
        :rtype: str
        """
        return self._lifecyle_details

    @lifecyle_details.setter
    def lifecyle_details(self, lifecyle_details):
        """
        Sets the lifecyle_details of this ManagedList.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecyle_details: The lifecyle_details of this ManagedList.
        :type: str
        """
        self._lifecyle_details = lifecyle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ManagedList.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ManagedList.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ManagedList.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ManagedList.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ManagedList.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ManagedList.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ManagedList.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ManagedList.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ManagedList.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this ManagedList.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ManagedList.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this ManagedList.
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