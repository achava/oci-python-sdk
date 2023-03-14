# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExtensionDbUserUser(object):
    """
    DB User extension
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExtensionDbUserUser object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_db_user:
            The value to assign to the is_db_user property of this ExtensionDbUserUser.
        :type is_db_user: bool

        :param password_verifiers:
            The value to assign to the password_verifiers property of this ExtensionDbUserUser.
        :type password_verifiers: list[oci.identity_domains.models.UserExtPasswordVerifiers]

        :param domain_level_schema:
            The value to assign to the domain_level_schema property of this ExtensionDbUserUser.
        :type domain_level_schema: str

        :param instance_level_schema:
            The value to assign to the instance_level_schema property of this ExtensionDbUserUser.
        :type instance_level_schema: str

        :param db_global_roles:
            The value to assign to the db_global_roles property of this ExtensionDbUserUser.
        :type db_global_roles: list[str]

        """
        self.swagger_types = {
            'is_db_user': 'bool',
            'password_verifiers': 'list[UserExtPasswordVerifiers]',
            'domain_level_schema': 'str',
            'instance_level_schema': 'str',
            'db_global_roles': 'list[str]'
        }

        self.attribute_map = {
            'is_db_user': 'isDbUser',
            'password_verifiers': 'passwordVerifiers',
            'domain_level_schema': 'domainLevelSchema',
            'instance_level_schema': 'instanceLevelSchema',
            'db_global_roles': 'dbGlobalRoles'
        }

        self._is_db_user = None
        self._password_verifiers = None
        self._domain_level_schema = None
        self._instance_level_schema = None
        self._db_global_roles = None

    @property
    def is_db_user(self):
        """
        Gets the is_db_user of this ExtensionDbUserUser.
        If true, indicates this is a database user.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :return: The is_db_user of this ExtensionDbUserUser.
        :rtype: bool
        """
        return self._is_db_user

    @is_db_user.setter
    def is_db_user(self, is_db_user):
        """
        Sets the is_db_user of this ExtensionDbUserUser.
        If true, indicates this is a database user.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :param is_db_user: The is_db_user of this ExtensionDbUserUser.
        :type: bool
        """
        self._is_db_user = is_db_user

    @property
    def password_verifiers(self):
        """
        Gets the password_verifiers of this ExtensionDbUserUser.
        Password Verifiers for DB User.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - idcsCompositeKey: [type]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :return: The password_verifiers of this ExtensionDbUserUser.
        :rtype: list[oci.identity_domains.models.UserExtPasswordVerifiers]
        """
        return self._password_verifiers

    @password_verifiers.setter
    def password_verifiers(self, password_verifiers):
        """
        Sets the password_verifiers of this ExtensionDbUserUser.
        Password Verifiers for DB User.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - idcsCompositeKey: [type]
         - idcsSearchable: true
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: complex
         - uniqueness: none


        :param password_verifiers: The password_verifiers of this ExtensionDbUserUser.
        :type: list[oci.identity_domains.models.UserExtPasswordVerifiers]
        """
        self._password_verifiers = password_verifiers

    @property
    def domain_level_schema(self):
        """
        Gets the domain_level_schema of this ExtensionDbUserUser.
        DB domain level schema to which the user is granted access.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - idcsSensitive: none
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The domain_level_schema of this ExtensionDbUserUser.
        :rtype: str
        """
        return self._domain_level_schema

    @domain_level_schema.setter
    def domain_level_schema(self, domain_level_schema):
        """
        Sets the domain_level_schema of this ExtensionDbUserUser.
        DB domain level schema to which the user is granted access.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - idcsSensitive: none
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param domain_level_schema: The domain_level_schema of this ExtensionDbUserUser.
        :type: str
        """
        self._domain_level_schema = domain_level_schema

    @property
    def instance_level_schema(self):
        """
        Gets the instance_level_schema of this ExtensionDbUserUser.
        DB instance level schema to which the user is granted access.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - idcsSensitive: none
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The instance_level_schema of this ExtensionDbUserUser.
        :rtype: str
        """
        return self._instance_level_schema

    @instance_level_schema.setter
    def instance_level_schema(self, instance_level_schema):
        """
        Sets the instance_level_schema of this ExtensionDbUserUser.
        DB instance level schema to which the user is granted access.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - idcsSensitive: none
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param instance_level_schema: The instance_level_schema of this ExtensionDbUserUser.
        :type: str
        """
        self._instance_level_schema = instance_level_schema

    @property
    def db_global_roles(self):
        """
        Gets the db_global_roles of this ExtensionDbUserUser.
        DB global roles to which the user is granted access.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - idcsSensitive: none
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The db_global_roles of this ExtensionDbUserUser.
        :rtype: list[str]
        """
        return self._db_global_roles

    @db_global_roles.setter
    def db_global_roles(self, db_global_roles):
        """
        Sets the db_global_roles of this ExtensionDbUserUser.
        DB global roles to which the user is granted access.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - idcsSensitive: none
         - multiValued: true
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param db_global_roles: The db_global_roles of this ExtensionDbUserUser.
        :type: list[str]
        """
        self._db_global_roles = db_global_roles

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
