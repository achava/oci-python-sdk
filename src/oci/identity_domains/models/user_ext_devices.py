# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserExtDevices(object):
    """
    A list of devices enrolled by the user.

    **Added In:** 18.3.6

    **SCIM++ Properties:**
    - idcsCompositeKey: [value]
    - multiValued: true
    - mutability: readOnly
    - required: false
    - returned: request
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UserExtDevices object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this UserExtDevices.
        :type value: str

        :param ref:
            The value to assign to the ref property of this UserExtDevices.
        :type ref: str

        :param display:
            The value to assign to the display property of this UserExtDevices.
        :type display: str

        :param status:
            The value to assign to the status property of this UserExtDevices.
        :type status: str

        :param last_sync_time:
            The value to assign to the last_sync_time property of this UserExtDevices.
        :type last_sync_time: str

        :param factor_type:
            The value to assign to the factor_type property of this UserExtDevices.
        :type factor_type: str

        :param factor_status:
            The value to assign to the factor_status property of this UserExtDevices.
        :type factor_status: str

        :param authentication_method:
            The value to assign to the authentication_method property of this UserExtDevices.
        :type authentication_method: str

        :param third_party_vendor_name:
            The value to assign to the third_party_vendor_name property of this UserExtDevices.
        :type third_party_vendor_name: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'display': 'str',
            'status': 'str',
            'last_sync_time': 'str',
            'factor_type': 'str',
            'factor_status': 'str',
            'authentication_method': 'str',
            'third_party_vendor_name': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'display': 'display',
            'status': 'status',
            'last_sync_time': 'lastSyncTime',
            'factor_type': 'factorType',
            'factor_status': 'factorStatus',
            'authentication_method': 'authenticationMethod',
            'third_party_vendor_name': 'thirdPartyVendorName'
        }

        self._value = None
        self._ref = None
        self._display = None
        self._status = None
        self._last_sync_time = None
        self._factor_type = None
        self._factor_status = None
        self._authentication_method = None
        self._third_party_vendor_name = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this UserExtDevices.
        The identifier of the User's device.

        **Added In:** 18.3.6

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this UserExtDevices.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UserExtDevices.
        The identifier of the User's device.

        **Added In:** 18.3.6

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this UserExtDevices.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this UserExtDevices.
        The URI of the corresponding Device resource which belongs to user

        **Added In:** 18.3.6

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this UserExtDevices.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this UserExtDevices.
        The URI of the corresponding Device resource which belongs to user

        **Added In:** 18.3.6

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this UserExtDevices.
        :type: str
        """
        self._ref = ref

    @property
    def display(self):
        """
        Gets the display of this UserExtDevices.
        A human readable name, primarily used for display purposes. READ-ONLY.

        **Added In:** 18.3.6

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this UserExtDevices.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this UserExtDevices.
        A human readable name, primarily used for display purposes. READ-ONLY.

        **Added In:** 18.3.6

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this UserExtDevices.
        :type: str
        """
        self._display = display

    @property
    def status(self):
        """
        Gets the status of this UserExtDevices.
        Device status.

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The status of this UserExtDevices.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UserExtDevices.
        Device status.

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param status: The status of this UserExtDevices.
        :type: str
        """
        self._status = status

    @property
    def last_sync_time(self):
        """
        Gets the last_sync_time of this UserExtDevices.
        Last Sync time for device.

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :return: The last_sync_time of this UserExtDevices.
        :rtype: str
        """
        return self._last_sync_time

    @last_sync_time.setter
    def last_sync_time(self, last_sync_time):
        """
        Sets the last_sync_time of this UserExtDevices.
        Last Sync time for device.

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :param last_sync_time: The last_sync_time of this UserExtDevices.
        :type: str
        """
        self._last_sync_time = last_sync_time

    @property
    def factor_type(self):
        """
        Gets the factor_type of this UserExtDevices.
        Device authentication factor type.

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The factor_type of this UserExtDevices.
        :rtype: str
        """
        return self._factor_type

    @factor_type.setter
    def factor_type(self, factor_type):
        """
        Sets the factor_type of this UserExtDevices.
        Device authentication factor type.

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param factor_type: The factor_type of this UserExtDevices.
        :type: str
        """
        self._factor_type = factor_type

    @property
    def factor_status(self):
        """
        Gets the factor_status of this UserExtDevices.
        Device authentication factor status.

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The factor_status of this UserExtDevices.
        :rtype: str
        """
        return self._factor_status

    @factor_status.setter
    def factor_status(self, factor_status):
        """
        Sets the factor_status of this UserExtDevices.
        Device authentication factor status.

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param factor_status: The factor_status of this UserExtDevices.
        :type: str
        """
        self._factor_status = factor_status

    @property
    def authentication_method(self):
        """
        Gets the authentication_method of this UserExtDevices.
        Authentication method.

        **Added In:** 2009232244

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The authentication_method of this UserExtDevices.
        :rtype: str
        """
        return self._authentication_method

    @authentication_method.setter
    def authentication_method(self, authentication_method):
        """
        Sets the authentication_method of this UserExtDevices.
        Authentication method.

        **Added In:** 2009232244

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param authentication_method: The authentication_method of this UserExtDevices.
        :type: str
        """
        self._authentication_method = authentication_method

    @property
    def third_party_vendor_name(self):
        """
        Gets the third_party_vendor_name of this UserExtDevices.
        Third party factor vendor name.

        **Added In:** 2009232244

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The third_party_vendor_name of this UserExtDevices.
        :rtype: str
        """
        return self._third_party_vendor_name

    @third_party_vendor_name.setter
    def third_party_vendor_name(self, third_party_vendor_name):
        """
        Sets the third_party_vendor_name of this UserExtDevices.
        Third party factor vendor name.

        **Added In:** 2009232244

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param third_party_vendor_name: The third_party_vendor_name of this UserExtDevices.
        :type: str
        """
        self._third_party_vendor_name = third_party_vendor_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other