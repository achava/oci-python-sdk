# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518

from .update_connection_details import UpdateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMysqlConnectionDetails(UpdateConnectionDetails):
    """
    The information to update a MySQL Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMysqlConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.UpdateMysqlConnectionDetails.connection_type` attribute
        of this class is ``MYSQL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this UpdateMysqlConnectionDetails.
            Allowed values for this property are: "MYSQL", "ORACLE"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateMysqlConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateMysqlConnectionDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateMysqlConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateMysqlConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this UpdateMysqlConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this UpdateMysqlConnectionDetails.
        :type key_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this UpdateMysqlConnectionDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateMysqlConnectionDetails.
        :type nsg_ids: list[str]

        :param username:
            The value to assign to the username property of this UpdateMysqlConnectionDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this UpdateMysqlConnectionDetails.
        :type password: str

        :param replication_username:
            The value to assign to the replication_username property of this UpdateMysqlConnectionDetails.
        :type replication_username: str

        :param replication_password:
            The value to assign to the replication_password property of this UpdateMysqlConnectionDetails.
        :type replication_password: str

        :param host:
            The value to assign to the host property of this UpdateMysqlConnectionDetails.
        :type host: str

        :param port:
            The value to assign to the port property of this UpdateMysqlConnectionDetails.
        :type port: int

        :param database_name:
            The value to assign to the database_name property of this UpdateMysqlConnectionDetails.
        :type database_name: str

        :param security_protocol:
            The value to assign to the security_protocol property of this UpdateMysqlConnectionDetails.
        :type security_protocol: str

        :param ssl_mode:
            The value to assign to the ssl_mode property of this UpdateMysqlConnectionDetails.
        :type ssl_mode: str

        :param ssl_ca:
            The value to assign to the ssl_ca property of this UpdateMysqlConnectionDetails.
        :type ssl_ca: str

        :param ssl_crl:
            The value to assign to the ssl_crl property of this UpdateMysqlConnectionDetails.
        :type ssl_crl: str

        :param ssl_cert:
            The value to assign to the ssl_cert property of this UpdateMysqlConnectionDetails.
        :type ssl_cert: str

        :param ssl_key:
            The value to assign to the ssl_key property of this UpdateMysqlConnectionDetails.
        :type ssl_key: str

        :param additional_attributes:
            The value to assign to the additional_attributes property of this UpdateMysqlConnectionDetails.
        :type additional_attributes: list[oci.database_migration.models.NameValuePair]

        :param db_system_id:
            The value to assign to the db_system_id property of this UpdateMysqlConnectionDetails.
        :type db_system_id: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vault_id': 'str',
            'key_id': 'str',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'username': 'str',
            'password': 'str',
            'replication_username': 'str',
            'replication_password': 'str',
            'host': 'str',
            'port': 'int',
            'database_name': 'str',
            'security_protocol': 'str',
            'ssl_mode': 'str',
            'ssl_ca': 'str',
            'ssl_crl': 'str',
            'ssl_cert': 'str',
            'ssl_key': 'str',
            'additional_attributes': 'list[NameValuePair]',
            'db_system_id': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'username': 'username',
            'password': 'password',
            'replication_username': 'replicationUsername',
            'replication_password': 'replicationPassword',
            'host': 'host',
            'port': 'port',
            'database_name': 'databaseName',
            'security_protocol': 'securityProtocol',
            'ssl_mode': 'sslMode',
            'ssl_ca': 'sslCa',
            'ssl_crl': 'sslCrl',
            'ssl_cert': 'sslCert',
            'ssl_key': 'sslKey',
            'additional_attributes': 'additionalAttributes',
            'db_system_id': 'dbSystemId'
        }

        self._connection_type = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._subnet_id = None
        self._nsg_ids = None
        self._username = None
        self._password = None
        self._replication_username = None
        self._replication_password = None
        self._host = None
        self._port = None
        self._database_name = None
        self._security_protocol = None
        self._ssl_mode = None
        self._ssl_ca = None
        self._ssl_crl = None
        self._ssl_cert = None
        self._ssl_key = None
        self._additional_attributes = None
        self._db_system_id = None
        self._connection_type = 'MYSQL'

    @property
    def host(self):
        """
        Gets the host of this UpdateMysqlConnectionDetails.
        The IP Address of the host.


        :return: The host of this UpdateMysqlConnectionDetails.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this UpdateMysqlConnectionDetails.
        The IP Address of the host.


        :param host: The host of this UpdateMysqlConnectionDetails.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        Gets the port of this UpdateMysqlConnectionDetails.
        The port to be used for the connection.


        :return: The port of this UpdateMysqlConnectionDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this UpdateMysqlConnectionDetails.
        The port to be used for the connection.


        :param port: The port of this UpdateMysqlConnectionDetails.
        :type: int
        """
        self._port = port

    @property
    def database_name(self):
        """
        Gets the database_name of this UpdateMysqlConnectionDetails.
        The name of the database being referenced.


        :return: The database_name of this UpdateMysqlConnectionDetails.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """
        Sets the database_name of this UpdateMysqlConnectionDetails.
        The name of the database being referenced.


        :param database_name: The database_name of this UpdateMysqlConnectionDetails.
        :type: str
        """
        self._database_name = database_name

    @property
    def security_protocol(self):
        """
        Gets the security_protocol of this UpdateMysqlConnectionDetails.
        Security Type for MySQL.


        :return: The security_protocol of this UpdateMysqlConnectionDetails.
        :rtype: str
        """
        return self._security_protocol

    @security_protocol.setter
    def security_protocol(self, security_protocol):
        """
        Sets the security_protocol of this UpdateMysqlConnectionDetails.
        Security Type for MySQL.


        :param security_protocol: The security_protocol of this UpdateMysqlConnectionDetails.
        :type: str
        """
        self._security_protocol = security_protocol

    @property
    def ssl_mode(self):
        """
        Gets the ssl_mode of this UpdateMysqlConnectionDetails.
        SSL modes for MySQL.


        :return: The ssl_mode of this UpdateMysqlConnectionDetails.
        :rtype: str
        """
        return self._ssl_mode

    @ssl_mode.setter
    def ssl_mode(self, ssl_mode):
        """
        Sets the ssl_mode of this UpdateMysqlConnectionDetails.
        SSL modes for MySQL.


        :param ssl_mode: The ssl_mode of this UpdateMysqlConnectionDetails.
        :type: str
        """
        self._ssl_mode = ssl_mode

    @property
    def ssl_ca(self):
        """
        Gets the ssl_ca of this UpdateMysqlConnectionDetails.
        Database Certificate - The base64 encoded content of mysql.pem file
        containing the server public key (for 1 and 2-way SSL).


        :return: The ssl_ca of this UpdateMysqlConnectionDetails.
        :rtype: str
        """
        return self._ssl_ca

    @ssl_ca.setter
    def ssl_ca(self, ssl_ca):
        """
        Sets the ssl_ca of this UpdateMysqlConnectionDetails.
        Database Certificate - The base64 encoded content of mysql.pem file
        containing the server public key (for 1 and 2-way SSL).


        :param ssl_ca: The ssl_ca of this UpdateMysqlConnectionDetails.
        :type: str
        """
        self._ssl_ca = ssl_ca

    @property
    def ssl_crl(self):
        """
        Gets the ssl_crl of this UpdateMysqlConnectionDetails.
        Certificates revoked by certificate authorities (CA).
        Server certificate must not be on this list (for 1 and 2-way SSL).
        Note: This is an optional and that too only applicable if TLS/MTLS option is selected.


        :return: The ssl_crl of this UpdateMysqlConnectionDetails.
        :rtype: str
        """
        return self._ssl_crl

    @ssl_crl.setter
    def ssl_crl(self, ssl_crl):
        """
        Sets the ssl_crl of this UpdateMysqlConnectionDetails.
        Certificates revoked by certificate authorities (CA).
        Server certificate must not be on this list (for 1 and 2-way SSL).
        Note: This is an optional and that too only applicable if TLS/MTLS option is selected.


        :param ssl_crl: The ssl_crl of this UpdateMysqlConnectionDetails.
        :type: str
        """
        self._ssl_crl = ssl_crl

    @property
    def ssl_cert(self):
        """
        Gets the ssl_cert of this UpdateMysqlConnectionDetails.
        Client Certificate - The base64 encoded content of client-cert.pem file
        containing the client public key (for 2-way SSL).


        :return: The ssl_cert of this UpdateMysqlConnectionDetails.
        :rtype: str
        """
        return self._ssl_cert

    @ssl_cert.setter
    def ssl_cert(self, ssl_cert):
        """
        Sets the ssl_cert of this UpdateMysqlConnectionDetails.
        Client Certificate - The base64 encoded content of client-cert.pem file
        containing the client public key (for 2-way SSL).


        :param ssl_cert: The ssl_cert of this UpdateMysqlConnectionDetails.
        :type: str
        """
        self._ssl_cert = ssl_cert

    @property
    def ssl_key(self):
        """
        Gets the ssl_key of this UpdateMysqlConnectionDetails.
        Client Key - The client-key.pem containing the client private key (for 2-way SSL).


        :return: The ssl_key of this UpdateMysqlConnectionDetails.
        :rtype: str
        """
        return self._ssl_key

    @ssl_key.setter
    def ssl_key(self, ssl_key):
        """
        Sets the ssl_key of this UpdateMysqlConnectionDetails.
        Client Key - The client-key.pem containing the client private key (for 2-way SSL).


        :param ssl_key: The ssl_key of this UpdateMysqlConnectionDetails.
        :type: str
        """
        self._ssl_key = ssl_key

    @property
    def additional_attributes(self):
        """
        Gets the additional_attributes of this UpdateMysqlConnectionDetails.
        An array of name-value pair attribute entries.


        :return: The additional_attributes of this UpdateMysqlConnectionDetails.
        :rtype: list[oci.database_migration.models.NameValuePair]
        """
        return self._additional_attributes

    @additional_attributes.setter
    def additional_attributes(self, additional_attributes):
        """
        Sets the additional_attributes of this UpdateMysqlConnectionDetails.
        An array of name-value pair attribute entries.


        :param additional_attributes: The additional_attributes of this UpdateMysqlConnectionDetails.
        :type: list[oci.database_migration.models.NameValuePair]
        """
        self._additional_attributes = additional_attributes

    @property
    def db_system_id(self):
        """
        Gets the db_system_id of this UpdateMysqlConnectionDetails.
        The OCID of the database system being referenced.


        :return: The db_system_id of this UpdateMysqlConnectionDetails.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this UpdateMysqlConnectionDetails.
        The OCID of the database system being referenced.


        :param db_system_id: The db_system_id of this UpdateMysqlConnectionDetails.
        :type: str
        """
        self._db_system_id = db_system_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
