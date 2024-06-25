# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MySqlInitialLoadSettings(object):
    """
    Optional dump settings
    """

    #: A constant which can be used with the primary_key_compatibility property of a MySqlInitialLoadSettings.
    #: This constant has a value of "NONE"
    PRIMARY_KEY_COMPATIBILITY_NONE = "NONE"

    #: A constant which can be used with the primary_key_compatibility property of a MySqlInitialLoadSettings.
    #: This constant has a value of "IGNORE_MISSING_PKS"
    PRIMARY_KEY_COMPATIBILITY_IGNORE_MISSING_PKS = "IGNORE_MISSING_PKS"

    #: A constant which can be used with the primary_key_compatibility property of a MySqlInitialLoadSettings.
    #: This constant has a value of "CREATE_INVISIBLE_PKS"
    PRIMARY_KEY_COMPATIBILITY_CREATE_INVISIBLE_PKS = "CREATE_INVISIBLE_PKS"

    #: A constant which can be used with the handle_grant_errors property of a MySqlInitialLoadSettings.
    #: This constant has a value of "ABORT"
    HANDLE_GRANT_ERRORS_ABORT = "ABORT"

    #: A constant which can be used with the handle_grant_errors property of a MySqlInitialLoadSettings.
    #: This constant has a value of "DROP_ACCOUNT"
    HANDLE_GRANT_ERRORS_DROP_ACCOUNT = "DROP_ACCOUNT"

    #: A constant which can be used with the handle_grant_errors property of a MySqlInitialLoadSettings.
    #: This constant has a value of "IGNORE"
    HANDLE_GRANT_ERRORS_IGNORE = "IGNORE"

    #: A constant which can be used with the job_mode property of a MySqlInitialLoadSettings.
    #: This constant has a value of "FULL"
    JOB_MODE_FULL = "FULL"

    #: A constant which can be used with the job_mode property of a MySqlInitialLoadSettings.
    #: This constant has a value of "SCHEMA"
    JOB_MODE_SCHEMA = "SCHEMA"

    def __init__(self, **kwargs):
        """
        Initializes a new MySqlInitialLoadSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_consistent:
            The value to assign to the is_consistent property of this MySqlInitialLoadSettings.
        :type is_consistent: bool

        :param is_tz_utc:
            The value to assign to the is_tz_utc property of this MySqlInitialLoadSettings.
        :type is_tz_utc: bool

        :param compatibility:
            The value to assign to the compatibility property of this MySqlInitialLoadSettings.
        :type compatibility: list[oci.database_migration.models.CompatibilityOption]

        :param primary_key_compatibility:
            The value to assign to the primary_key_compatibility property of this MySqlInitialLoadSettings.
            Allowed values for this property are: "NONE", "IGNORE_MISSING_PKS", "CREATE_INVISIBLE_PKS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type primary_key_compatibility: str

        :param is_ignore_existing_objects:
            The value to assign to the is_ignore_existing_objects property of this MySqlInitialLoadSettings.
        :type is_ignore_existing_objects: bool

        :param handle_grant_errors:
            The value to assign to the handle_grant_errors property of this MySqlInitialLoadSettings.
            Allowed values for this property are: "ABORT", "DROP_ACCOUNT", "IGNORE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type handle_grant_errors: str

        :param job_mode:
            The value to assign to the job_mode property of this MySqlInitialLoadSettings.
            Allowed values for this property are: "FULL", "SCHEMA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type job_mode: str

        """
        self.swagger_types = {
            'is_consistent': 'bool',
            'is_tz_utc': 'bool',
            'compatibility': 'list[CompatibilityOption]',
            'primary_key_compatibility': 'str',
            'is_ignore_existing_objects': 'bool',
            'handle_grant_errors': 'str',
            'job_mode': 'str'
        }

        self.attribute_map = {
            'is_consistent': 'isConsistent',
            'is_tz_utc': 'isTzUtc',
            'compatibility': 'compatibility',
            'primary_key_compatibility': 'primaryKeyCompatibility',
            'is_ignore_existing_objects': 'isIgnoreExistingObjects',
            'handle_grant_errors': 'handleGrantErrors',
            'job_mode': 'jobMode'
        }

        self._is_consistent = None
        self._is_tz_utc = None
        self._compatibility = None
        self._primary_key_compatibility = None
        self._is_ignore_existing_objects = None
        self._handle_grant_errors = None
        self._job_mode = None

    @property
    def is_consistent(self):
        """
        Gets the is_consistent of this MySqlInitialLoadSettings.
        Enable (true) or disable (false) consistent data dumps by locking the instance for backup during the dump.


        :return: The is_consistent of this MySqlInitialLoadSettings.
        :rtype: bool
        """
        return self._is_consistent

    @is_consistent.setter
    def is_consistent(self, is_consistent):
        """
        Sets the is_consistent of this MySqlInitialLoadSettings.
        Enable (true) or disable (false) consistent data dumps by locking the instance for backup during the dump.


        :param is_consistent: The is_consistent of this MySqlInitialLoadSettings.
        :type: bool
        """
        self._is_consistent = is_consistent

    @property
    def is_tz_utc(self):
        """
        Gets the is_tz_utc of this MySqlInitialLoadSettings.
        Include a statement at the start of the dump to set the time zone to UTC.


        :return: The is_tz_utc of this MySqlInitialLoadSettings.
        :rtype: bool
        """
        return self._is_tz_utc

    @is_tz_utc.setter
    def is_tz_utc(self, is_tz_utc):
        """
        Sets the is_tz_utc of this MySqlInitialLoadSettings.
        Include a statement at the start of the dump to set the time zone to UTC.


        :param is_tz_utc: The is_tz_utc of this MySqlInitialLoadSettings.
        :type: bool
        """
        self._is_tz_utc = is_tz_utc

    @property
    def compatibility(self):
        """
        Gets the compatibility of this MySqlInitialLoadSettings.
        Apply the specified requirements for compatibility with MySQL Database Service for all tables in the dump
        output, altering the dump files as necessary.


        :return: The compatibility of this MySqlInitialLoadSettings.
        :rtype: list[oci.database_migration.models.CompatibilityOption]
        """
        return self._compatibility

    @compatibility.setter
    def compatibility(self, compatibility):
        """
        Sets the compatibility of this MySqlInitialLoadSettings.
        Apply the specified requirements for compatibility with MySQL Database Service for all tables in the dump
        output, altering the dump files as necessary.


        :param compatibility: The compatibility of this MySqlInitialLoadSettings.
        :type: list[oci.database_migration.models.CompatibilityOption]
        """
        self._compatibility = compatibility

    @property
    def primary_key_compatibility(self):
        """
        Gets the primary_key_compatibility of this MySqlInitialLoadSettings.
        Primary key compatibility option

        Allowed values for this property are: "NONE", "IGNORE_MISSING_PKS", "CREATE_INVISIBLE_PKS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The primary_key_compatibility of this MySqlInitialLoadSettings.
        :rtype: str
        """
        return self._primary_key_compatibility

    @primary_key_compatibility.setter
    def primary_key_compatibility(self, primary_key_compatibility):
        """
        Sets the primary_key_compatibility of this MySqlInitialLoadSettings.
        Primary key compatibility option


        :param primary_key_compatibility: The primary_key_compatibility of this MySqlInitialLoadSettings.
        :type: str
        """
        allowed_values = ["NONE", "IGNORE_MISSING_PKS", "CREATE_INVISIBLE_PKS"]
        if not value_allowed_none_or_none_sentinel(primary_key_compatibility, allowed_values):
            primary_key_compatibility = 'UNKNOWN_ENUM_VALUE'
        self._primary_key_compatibility = primary_key_compatibility

    @property
    def is_ignore_existing_objects(self):
        """
        Gets the is_ignore_existing_objects of this MySqlInitialLoadSettings.
        Import the dump even if it contains objects that already exist in the target schema in the MySQL instance.


        :return: The is_ignore_existing_objects of this MySqlInitialLoadSettings.
        :rtype: bool
        """
        return self._is_ignore_existing_objects

    @is_ignore_existing_objects.setter
    def is_ignore_existing_objects(self, is_ignore_existing_objects):
        """
        Sets the is_ignore_existing_objects of this MySqlInitialLoadSettings.
        Import the dump even if it contains objects that already exist in the target schema in the MySQL instance.


        :param is_ignore_existing_objects: The is_ignore_existing_objects of this MySqlInitialLoadSettings.
        :type: bool
        """
        self._is_ignore_existing_objects = is_ignore_existing_objects

    @property
    def handle_grant_errors(self):
        """
        Gets the handle_grant_errors of this MySqlInitialLoadSettings.
        The action taken in the event of errors related to GRANT or REVOKE errors.

        Allowed values for this property are: "ABORT", "DROP_ACCOUNT", "IGNORE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The handle_grant_errors of this MySqlInitialLoadSettings.
        :rtype: str
        """
        return self._handle_grant_errors

    @handle_grant_errors.setter
    def handle_grant_errors(self, handle_grant_errors):
        """
        Sets the handle_grant_errors of this MySqlInitialLoadSettings.
        The action taken in the event of errors related to GRANT or REVOKE errors.


        :param handle_grant_errors: The handle_grant_errors of this MySqlInitialLoadSettings.
        :type: str
        """
        allowed_values = ["ABORT", "DROP_ACCOUNT", "IGNORE"]
        if not value_allowed_none_or_none_sentinel(handle_grant_errors, allowed_values):
            handle_grant_errors = 'UNKNOWN_ENUM_VALUE'
        self._handle_grant_errors = handle_grant_errors

    @property
    def job_mode(self):
        """
        **[Required]** Gets the job_mode of this MySqlInitialLoadSettings.
        MySql Job Mode

        Allowed values for this property are: "FULL", "SCHEMA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The job_mode of this MySqlInitialLoadSettings.
        :rtype: str
        """
        return self._job_mode

    @job_mode.setter
    def job_mode(self, job_mode):
        """
        Sets the job_mode of this MySqlInitialLoadSettings.
        MySql Job Mode


        :param job_mode: The job_mode of this MySqlInitialLoadSettings.
        :type: str
        """
        allowed_values = ["FULL", "SCHEMA"]
        if not value_allowed_none_or_none_sentinel(job_mode, allowed_values):
            job_mode = 'UNKNOWN_ENUM_VALUE'
        self._job_mode = job_mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
