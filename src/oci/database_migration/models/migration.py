# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Migration(object):
    """
    Migration resource
    """

    #: A constant which can be used with the database_combination property of a Migration.
    #: This constant has a value of "MYSQL"
    DATABASE_COMBINATION_MYSQL = "MYSQL"

    #: A constant which can be used with the database_combination property of a Migration.
    #: This constant has a value of "ORACLE"
    DATABASE_COMBINATION_ORACLE = "ORACLE"

    #: A constant which can be used with the type property of a Migration.
    #: This constant has a value of "ONLINE"
    TYPE_ONLINE = "ONLINE"

    #: A constant which can be used with the type property of a Migration.
    #: This constant has a value of "OFFLINE"
    TYPE_OFFLINE = "OFFLINE"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_TGT"
    WAIT_AFTER_ODMS_VALIDATE_TGT = "ODMS_VALIDATE_TGT"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_SRC"
    WAIT_AFTER_ODMS_VALIDATE_SRC = "ODMS_VALIDATE_SRC"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_PREMIGRATION_ADVISOR"
    WAIT_AFTER_ODMS_VALIDATE_PREMIGRATION_ADVISOR = "ODMS_VALIDATE_PREMIGRATION_ADVISOR"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_GG_HUB"
    WAIT_AFTER_ODMS_VALIDATE_GG_HUB = "ODMS_VALIDATE_GG_HUB"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SETTINGS"
    WAIT_AFTER_ODMS_VALIDATE_DATAPUMP_SETTINGS = "ODMS_VALIDATE_DATAPUMP_SETTINGS"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC"
    WAIT_AFTER_ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC = "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT"
    WAIT_AFTER_ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT = "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SRC"
    WAIT_AFTER_ODMS_VALIDATE_DATAPUMP_SRC = "ODMS_VALIDATE_DATAPUMP_SRC"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC"
    WAIT_AFTER_ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC = "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_FETCH_METADATA_SRC"
    WAIT_AFTER_ODMS_FETCH_METADATA_SRC = "ODMS_FETCH_METADATA_SRC"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_FETCH_METADATA_TGT"
    WAIT_AFTER_ODMS_FETCH_METADATA_TGT = "ODMS_FETCH_METADATA_TGT"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_VALIDATE"
    WAIT_AFTER_ODMS_VALIDATE = "ODMS_VALIDATE"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_PREPARE"
    WAIT_AFTER_ODMS_PREPARE = "ODMS_PREPARE"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_INITIALIZE_REPLICATION_INFRASTRUCTURE"
    WAIT_AFTER_ODMS_INITIALIZE_REPLICATION_INFRASTRUCTURE = "ODMS_INITIALIZE_REPLICATION_INFRASTRUCTURE"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_INITIAL_LOAD_EXPORT"
    WAIT_AFTER_ODMS_INITIAL_LOAD_EXPORT = "ODMS_INITIAL_LOAD_EXPORT"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_DATA_UPLOAD"
    WAIT_AFTER_ODMS_DATA_UPLOAD = "ODMS_DATA_UPLOAD"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_INITIAL_LOAD_EXPORT_DATA_UPLOAD"
    WAIT_AFTER_ODMS_INITIAL_LOAD_EXPORT_DATA_UPLOAD = "ODMS_INITIAL_LOAD_EXPORT_DATA_UPLOAD"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_INITIAL_LOAD_IMPORT"
    WAIT_AFTER_ODMS_INITIAL_LOAD_IMPORT = "ODMS_INITIAL_LOAD_IMPORT"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_POST_INITIAL_LOAD"
    WAIT_AFTER_ODMS_POST_INITIAL_LOAD = "ODMS_POST_INITIAL_LOAD"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_PREPARE_REPLICATION_TARGET"
    WAIT_AFTER_ODMS_PREPARE_REPLICATION_TARGET = "ODMS_PREPARE_REPLICATION_TARGET"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_MONITOR_REPLICATION_LAG"
    WAIT_AFTER_ODMS_MONITOR_REPLICATION_LAG = "ODMS_MONITOR_REPLICATION_LAG"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_SWITCHOVER"
    WAIT_AFTER_ODMS_SWITCHOVER = "ODMS_SWITCHOVER"

    #: A constant which can be used with the wait_after property of a Migration.
    #: This constant has a value of "ODMS_CLEANUP"
    WAIT_AFTER_ODMS_CLEANUP = "ODMS_CLEANUP"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "WAITING"
    LIFECYCLE_STATE_WAITING = "WAITING"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_details property of a Migration.
    #: This constant has a value of "READY"
    LIFECYCLE_DETAILS_READY = "READY"

    #: A constant which can be used with the lifecycle_details property of a Migration.
    #: This constant has a value of "ABORTING"
    LIFECYCLE_DETAILS_ABORTING = "ABORTING"

    #: A constant which can be used with the lifecycle_details property of a Migration.
    #: This constant has a value of "VALIDATING"
    LIFECYCLE_DETAILS_VALIDATING = "VALIDATING"

    #: A constant which can be used with the lifecycle_details property of a Migration.
    #: This constant has a value of "VALIDATED"
    LIFECYCLE_DETAILS_VALIDATED = "VALIDATED"

    #: A constant which can be used with the lifecycle_details property of a Migration.
    #: This constant has a value of "WAITING"
    LIFECYCLE_DETAILS_WAITING = "WAITING"

    #: A constant which can be used with the lifecycle_details property of a Migration.
    #: This constant has a value of "MIGRATING"
    LIFECYCLE_DETAILS_MIGRATING = "MIGRATING"

    #: A constant which can be used with the lifecycle_details property of a Migration.
    #: This constant has a value of "DONE"
    LIFECYCLE_DETAILS_DONE = "DONE"

    def __init__(self, **kwargs):
        """
        Initializes a new Migration object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_migration.models.OracleMigration`
        * :class:`~oci.database_migration.models.MySqlMigration`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Migration.
        :type id: str

        :param description:
            The value to assign to the description property of this Migration.
        :type description: str

        :param database_combination:
            The value to assign to the database_combination property of this Migration.
            Allowed values for this property are: "MYSQL", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_combination: str

        :param display_name:
            The value to assign to the display_name property of this Migration.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Migration.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this Migration.
            Allowed values for this property are: "ONLINE", "OFFLINE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param wait_after:
            The value to assign to the wait_after property of this Migration.
            Allowed values for this property are: "ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_PREMIGRATION_ADVISOR", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE_DATAPUMP_SRC", "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC", "ODMS_FETCH_METADATA_SRC", "ODMS_FETCH_METADATA_TGT", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIALIZE_REPLICATION_INFRASTRUCTURE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_EXPORT_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type wait_after: str

        :param source_database_connection_id:
            The value to assign to the source_database_connection_id property of this Migration.
        :type source_database_connection_id: str

        :param target_database_connection_id:
            The value to assign to the target_database_connection_id property of this Migration.
        :type target_database_connection_id: str

        :param executing_job_id:
            The value to assign to the executing_job_id property of this Migration.
        :type executing_job_id: str

        :param time_created:
            The value to assign to the time_created property of this Migration.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Migration.
        :type time_updated: datetime

        :param time_last_migration:
            The value to assign to the time_last_migration property of this Migration.
        :type time_last_migration: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Migration.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "IN_PROGRESS", "ACCEPTED", "SUCCEEDED", "CANCELED", "WAITING", "NEEDS_ATTENTION", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Migration.
            Allowed values for this property are: "READY", "ABORTING", "VALIDATING", "VALIDATED", "WAITING", "MIGRATING", "DONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Migration.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Migration.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Migration.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'database_combination': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'type': 'str',
            'wait_after': 'str',
            'source_database_connection_id': 'str',
            'target_database_connection_id': 'str',
            'executing_job_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_last_migration': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'database_combination': 'databaseCombination',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'type': 'type',
            'wait_after': 'waitAfter',
            'source_database_connection_id': 'sourceDatabaseConnectionId',
            'target_database_connection_id': 'targetDatabaseConnectionId',
            'executing_job_id': 'executingJobId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_last_migration': 'timeLastMigration',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._description = None
        self._database_combination = None
        self._display_name = None
        self._compartment_id = None
        self._type = None
        self._wait_after = None
        self._source_database_connection_id = None
        self._target_database_connection_id = None
        self._executing_job_id = None
        self._time_created = None
        self._time_updated = None
        self._time_last_migration = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['databaseCombination']

        if type == 'ORACLE':
            return 'OracleMigration'

        if type == 'MYSQL':
            return 'MySqlMigration'
        else:
            return 'Migration'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Migration.
        The OCID of the resource being referenced.


        :return: The id of this Migration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Migration.
        The OCID of the resource being referenced.


        :param id: The id of this Migration.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        Gets the description of this Migration.
        A user-friendly description. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The description of this Migration.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Migration.
        A user-friendly description. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param description: The description of this Migration.
        :type: str
        """
        self._description = description

    @property
    def database_combination(self):
        """
        **[Required]** Gets the database_combination of this Migration.
        The combination of source and target databases participating in a migration.
        Example: ORACLE means the migration is meant for migrating Oracle source and target databases.

        Allowed values for this property are: "MYSQL", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_combination of this Migration.
        :rtype: str
        """
        return self._database_combination

    @database_combination.setter
    def database_combination(self, database_combination):
        """
        Sets the database_combination of this Migration.
        The combination of source and target databases participating in a migration.
        Example: ORACLE means the migration is meant for migrating Oracle source and target databases.


        :param database_combination: The database_combination of this Migration.
        :type: str
        """
        allowed_values = ["MYSQL", "ORACLE"]
        if not value_allowed_none_or_none_sentinel(database_combination, allowed_values):
            database_combination = 'UNKNOWN_ENUM_VALUE'
        self._database_combination = database_combination

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Migration.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this Migration.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Migration.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Migration.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Migration.
        The OCID of the resource being referenced.


        :return: The compartment_id of this Migration.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Migration.
        The OCID of the resource being referenced.


        :param compartment_id: The compartment_id of this Migration.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Migration.
        The type of the migration to be performed.
        Example: ONLINE if no downtime is preferred for a migration. This method uses Oracle GoldenGate for replication.

        Allowed values for this property are: "ONLINE", "OFFLINE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Migration.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Migration.
        The type of the migration to be performed.
        Example: ONLINE if no downtime is preferred for a migration. This method uses Oracle GoldenGate for replication.


        :param type: The type of this Migration.
        :type: str
        """
        allowed_values = ["ONLINE", "OFFLINE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def wait_after(self):
        """
        Gets the wait_after of this Migration.
        You can optionally pause a migration after a job phase.
        This property allows you to optionally specify the phase after which you can pause the migration.

        Allowed values for this property are: "ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_PREMIGRATION_ADVISOR", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE_DATAPUMP_SRC", "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC", "ODMS_FETCH_METADATA_SRC", "ODMS_FETCH_METADATA_TGT", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIALIZE_REPLICATION_INFRASTRUCTURE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_EXPORT_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The wait_after of this Migration.
        :rtype: str
        """
        return self._wait_after

    @wait_after.setter
    def wait_after(self, wait_after):
        """
        Sets the wait_after of this Migration.
        You can optionally pause a migration after a job phase.
        This property allows you to optionally specify the phase after which you can pause the migration.


        :param wait_after: The wait_after of this Migration.
        :type: str
        """
        allowed_values = ["ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_PREMIGRATION_ADVISOR", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE_DATAPUMP_SRC", "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC", "ODMS_FETCH_METADATA_SRC", "ODMS_FETCH_METADATA_TGT", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIALIZE_REPLICATION_INFRASTRUCTURE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_EXPORT_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP"]
        if not value_allowed_none_or_none_sentinel(wait_after, allowed_values):
            wait_after = 'UNKNOWN_ENUM_VALUE'
        self._wait_after = wait_after

    @property
    def source_database_connection_id(self):
        """
        **[Required]** Gets the source_database_connection_id of this Migration.
        The OCID of the resource being referenced.


        :return: The source_database_connection_id of this Migration.
        :rtype: str
        """
        return self._source_database_connection_id

    @source_database_connection_id.setter
    def source_database_connection_id(self, source_database_connection_id):
        """
        Sets the source_database_connection_id of this Migration.
        The OCID of the resource being referenced.


        :param source_database_connection_id: The source_database_connection_id of this Migration.
        :type: str
        """
        self._source_database_connection_id = source_database_connection_id

    @property
    def target_database_connection_id(self):
        """
        **[Required]** Gets the target_database_connection_id of this Migration.
        The OCID of the resource being referenced.


        :return: The target_database_connection_id of this Migration.
        :rtype: str
        """
        return self._target_database_connection_id

    @target_database_connection_id.setter
    def target_database_connection_id(self, target_database_connection_id):
        """
        Sets the target_database_connection_id of this Migration.
        The OCID of the resource being referenced.


        :param target_database_connection_id: The target_database_connection_id of this Migration.
        :type: str
        """
        self._target_database_connection_id = target_database_connection_id

    @property
    def executing_job_id(self):
        """
        Gets the executing_job_id of this Migration.
        The OCID of the resource being referenced.


        :return: The executing_job_id of this Migration.
        :rtype: str
        """
        return self._executing_job_id

    @executing_job_id.setter
    def executing_job_id(self, executing_job_id):
        """
        Sets the executing_job_id of this Migration.
        The OCID of the resource being referenced.


        :param executing_job_id: The executing_job_id of this Migration.
        :type: str
        """
        self._executing_job_id = executing_job_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Migration.
        An RFC3339 formatted datetime string such as `2016-08-25T21:10:29.600Z`.


        :return: The time_created of this Migration.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Migration.
        An RFC3339 formatted datetime string such as `2016-08-25T21:10:29.600Z`.


        :param time_created: The time_created of this Migration.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Migration.
        An RFC3339 formatted datetime string such as `2016-08-25T21:10:29.600Z`.


        :return: The time_updated of this Migration.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Migration.
        An RFC3339 formatted datetime string such as `2016-08-25T21:10:29.600Z`.


        :param time_updated: The time_updated of this Migration.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_last_migration(self):
        """
        Gets the time_last_migration of this Migration.
        An RFC3339 formatted datetime string such as `2016-08-25T21:10:29.600Z`.


        :return: The time_last_migration of this Migration.
        :rtype: datetime
        """
        return self._time_last_migration

    @time_last_migration.setter
    def time_last_migration(self, time_last_migration):
        """
        Sets the time_last_migration of this Migration.
        An RFC3339 formatted datetime string such as `2016-08-25T21:10:29.600Z`.


        :param time_last_migration: The time_last_migration of this Migration.
        :type: datetime
        """
        self._time_last_migration = time_last_migration

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Migration.
        The current state of the Migration resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "IN_PROGRESS", "ACCEPTED", "SUCCEEDED", "CANCELED", "WAITING", "NEEDS_ATTENTION", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Migration.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Migration.
        The current state of the Migration resource.


        :param lifecycle_state: The lifecycle_state of this Migration.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "IN_PROGRESS", "ACCEPTED", "SUCCEEDED", "CANCELED", "WAITING", "NEEDS_ATTENTION", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Migration.
        Additional status related to the execution and current state of the Migration.

        Allowed values for this property are: "READY", "ABORTING", "VALIDATING", "VALIDATED", "WAITING", "MIGRATING", "DONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_details of this Migration.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Migration.
        Additional status related to the execution and current state of the Migration.


        :param lifecycle_details: The lifecycle_details of this Migration.
        :type: str
        """
        allowed_values = ["READY", "ABORTING", "VALIDATING", "VALIDATED", "WAITING", "MIGRATING", "DONE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_details, allowed_values):
            lifecycle_details = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Migration.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see Resource Tags. Example: {\"Department\": \"Finance\"}


        :return: The freeform_tags of this Migration.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Migration.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see Resource Tags. Example: {\"Department\": \"Finance\"}


        :param freeform_tags: The freeform_tags of this Migration.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Migration.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Migration.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Migration.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Migration.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Migration.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this Migration.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Migration.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this Migration.
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
