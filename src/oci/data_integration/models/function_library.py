# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FunctionLibrary(object):
    """
    The FunctionLibrary type contains the audit summary information and the definition of the FunctionLibrary.
    """

    #: A constant which can be used with the model_type property of a FunctionLibrary.
    #: This constant has a value of "FUNCTION_LIBRARY"
    MODEL_TYPE_FUNCTION_LIBRARY = "FUNCTION_LIBRARY"

    def __init__(self, **kwargs):
        """
        Initializes a new FunctionLibrary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this FunctionLibrary.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this FunctionLibrary.
            Allowed values for this property are: "FUNCTION_LIBRARY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this FunctionLibrary.
        :type model_version: str

        :param name:
            The value to assign to the name property of this FunctionLibrary.
        :type name: str

        :param description:
            The value to assign to the description property of this FunctionLibrary.
        :type description: str

        :param category_name:
            The value to assign to the category_name property of this FunctionLibrary.
        :type category_name: str

        :param object_status:
            The value to assign to the object_status property of this FunctionLibrary.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this FunctionLibrary.
        :type identifier: str

        :param parent_ref:
            The value to assign to the parent_ref property of this FunctionLibrary.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param object_version:
            The value to assign to the object_version property of this FunctionLibrary.
        :type object_version: int

        :param metadata:
            The value to assign to the metadata property of this FunctionLibrary.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this FunctionLibrary.
        :type key_map: dict(str, str)

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'category_name': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'parent_ref': 'ParentReference',
            'object_version': 'int',
            'metadata': 'ObjectMetadata',
            'key_map': 'dict(str, str)'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'category_name': 'categoryName',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'parent_ref': 'parentRef',
            'object_version': 'objectVersion',
            'metadata': 'metadata',
            'key_map': 'keyMap'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._name = None
        self._description = None
        self._category_name = None
        self._object_status = None
        self._identifier = None
        self._parent_ref = None
        self._object_version = None
        self._metadata = None
        self._key_map = None

    @property
    def key(self):
        """
        Gets the key of this FunctionLibrary.
        Generated key that can be used in API calls to identify FunctionLibrary.


        :return: The key of this FunctionLibrary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this FunctionLibrary.
        Generated key that can be used in API calls to identify FunctionLibrary.


        :param key: The key of this FunctionLibrary.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this FunctionLibrary.
        The type of the object.

        Allowed values for this property are: "FUNCTION_LIBRARY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this FunctionLibrary.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this FunctionLibrary.
        The type of the object.


        :param model_type: The model_type of this FunctionLibrary.
        :type: str
        """
        allowed_values = ["FUNCTION_LIBRARY"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this FunctionLibrary.
        The model version of an object.


        :return: The model_version of this FunctionLibrary.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this FunctionLibrary.
        The model version of an object.


        :param model_version: The model_version of this FunctionLibrary.
        :type: str
        """
        self._model_version = model_version

    @property
    def name(self):
        """
        Gets the name of this FunctionLibrary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this FunctionLibrary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FunctionLibrary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this FunctionLibrary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this FunctionLibrary.
        A user defined description for the Function Library.


        :return: The description of this FunctionLibrary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FunctionLibrary.
        A user defined description for the Function Library.


        :param description: The description of this FunctionLibrary.
        :type: str
        """
        self._description = description

    @property
    def category_name(self):
        """
        Gets the category_name of this FunctionLibrary.
        The category name.


        :return: The category_name of this FunctionLibrary.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """
        Sets the category_name of this FunctionLibrary.
        The category name.


        :param category_name: The category_name of this FunctionLibrary.
        :type: str
        """
        self._category_name = category_name

    @property
    def object_status(self):
        """
        Gets the object_status of this FunctionLibrary.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this FunctionLibrary.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this FunctionLibrary.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this FunctionLibrary.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this FunctionLibrary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this FunctionLibrary.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this FunctionLibrary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this FunctionLibrary.
        :type: str
        """
        self._identifier = identifier

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this FunctionLibrary.

        :return: The parent_ref of this FunctionLibrary.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this FunctionLibrary.

        :param parent_ref: The parent_ref of this FunctionLibrary.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def object_version(self):
        """
        Gets the object_version of this FunctionLibrary.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this FunctionLibrary.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this FunctionLibrary.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this FunctionLibrary.
        :type: int
        """
        self._object_version = object_version

    @property
    def metadata(self):
        """
        Gets the metadata of this FunctionLibrary.

        :return: The metadata of this FunctionLibrary.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this FunctionLibrary.

        :param metadata: The metadata of this FunctionLibrary.
        :type: oci.data_integration.models.ObjectMetadata
        """
        self._metadata = metadata

    @property
    def key_map(self):
        """
        Gets the key_map of this FunctionLibrary.
        A key map. If provided, the key is replaced with generated key. This structure provides mapping between user provided key and generated key.


        :return: The key_map of this FunctionLibrary.
        :rtype: dict(str, str)
        """
        return self._key_map

    @key_map.setter
    def key_map(self, key_map):
        """
        Sets the key_map of this FunctionLibrary.
        A key map. If provided, the key is replaced with generated key. This structure provides mapping between user provided key and generated key.


        :param key_map: The key_map of this FunctionLibrary.
        :type: dict(str, str)
        """
        self._key_map = key_map

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other