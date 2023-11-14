# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RuleReturn(object):
    """
    The return values are the then portion of a Rule
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RuleReturn object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this RuleReturn.
        :type name: str

        :param value:
            The value to assign to the value property of this RuleReturn.
        :type value: str

        :param return_groovy:
            The value to assign to the return_groovy property of this RuleReturn.
        :type return_groovy: str

        """
        self.swagger_types = {
            'name': 'str',
            'value': 'str',
            'return_groovy': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'value': 'value',
            'return_groovy': 'returnGroovy'
        }

        self._name = None
        self._value = None
        self._return_groovy = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this RuleReturn.
        Attribute name of an individual value to be returned.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The name of this RuleReturn.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RuleReturn.
        Attribute name of an individual value to be returned.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param name: The name of this RuleReturn.
        :type: str
        """
        self._name = name

    @property
    def value(self):
        """
        **[Required]** Gets the value of this RuleReturn.
        Attribute value of some attribute to be returned.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this RuleReturn.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this RuleReturn.
        Attribute value of some attribute to be returned.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this RuleReturn.
        :type: str
        """
        self._value = value

    @property
    def return_groovy(self):
        """
        Gets the return_groovy of this RuleReturn.
        The Groovy script that is run to generate output for the rule, if the policy type allows the return value to be a Groovy script.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The return_groovy of this RuleReturn.
        :rtype: str
        """
        return self._return_groovy

    @return_groovy.setter
    def return_groovy(self, return_groovy):
        """
        Sets the return_groovy of this RuleReturn.
        The Groovy script that is run to generate output for the rule, if the policy type allows the return value to be a Groovy script.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param return_groovy: The return_groovy of this RuleReturn.
        :type: str
        """
        self._return_groovy = return_groovy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other