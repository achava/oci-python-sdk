# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .boot_volume_source_details import BootVolumeSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BootVolumeSourceFromBootVolumeReplicaDetails(BootVolumeSourceDetails):
    """
    Specifies the source boot volume replica which the boot volume will be created from.
    The boot volume replica shoulbe be in the same availability domain as the boot volume.
    Only one volume can be created from a replica at the same time.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BootVolumeSourceFromBootVolumeReplicaDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.BootVolumeSourceFromBootVolumeReplicaDetails.type` attribute
        of this class is ``bootVolumeReplica`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this BootVolumeSourceFromBootVolumeReplicaDetails.
        :type type: str

        :param id:
            The value to assign to the id property of this BootVolumeSourceFromBootVolumeReplicaDetails.
        :type id: str

        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id'
        }

        self._type = None
        self._id = None
        self._type = 'bootVolumeReplica'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BootVolumeSourceFromBootVolumeReplicaDetails.
        The OCID of the boot volume replica.


        :return: The id of this BootVolumeSourceFromBootVolumeReplicaDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BootVolumeSourceFromBootVolumeReplicaDetails.
        The OCID of the boot volume replica.


        :param id: The id of this BootVolumeSourceFromBootVolumeReplicaDetails.
        :type: str
        """
        self._id = id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
