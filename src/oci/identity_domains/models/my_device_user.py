# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MyDeviceUser(object):
    """
    Device member

    **Deprecated Since: 17.3.4**

    **SCIM++ Properties:**
    - caseExact: false
    - idcsSearchable: true
    - multiValued: false
    - mutability: immutable
    - required: true
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MyDeviceUser object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this MyDeviceUser.
        :type value: str

        :param ref:
            The value to assign to the ref property of this MyDeviceUser.
        :type ref: str

        :param display:
            The value to assign to the display property of this MyDeviceUser.
        :type display: str

        :param ocid:
            The value to assign to the ocid property of this MyDeviceUser.
        :type ocid: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'display': 'str',
            'ocid': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'display': 'display',
            'ocid': 'ocid'
        }

        self._value = None
        self._ref = None
        self._display = None
        self._ocid = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this MyDeviceUser.
        The identifier of the user

        **Deprecated Since: 17.3.4**

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this MyDeviceUser.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this MyDeviceUser.
        The identifier of the user

        **Deprecated Since: 17.3.4**

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this MyDeviceUser.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this MyDeviceUser.
        The URI that corresponds to the member Resource of this device

        **Deprecated Since: 17.3.4**

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this MyDeviceUser.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this MyDeviceUser.
        The URI that corresponds to the member Resource of this device

        **Deprecated Since: 17.3.4**

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this MyDeviceUser.
        :type: str
        """
        self._ref = ref

    @property
    def display(self):
        """
        Gets the display of this MyDeviceUser.
        User display name

        **Deprecated Since: 17.3.4**

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this MyDeviceUser.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this MyDeviceUser.
        User display name

        **Deprecated Since: 17.3.4**

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this MyDeviceUser.
        :type: str
        """
        self._display = display

    @property
    def ocid(self):
        """
        Gets the ocid of this MyDeviceUser.
        The OCID of the user

        **Added In:** 2105091740

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :return: The ocid of this MyDeviceUser.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this MyDeviceUser.
        The OCID of the user

        **Added In:** 2105091740

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :param ocid: The ocid of this MyDeviceUser.
        :type: str
        """
        self._ocid = ocid

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
