# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StorageUsageTrend(object):
    """
    Usage data samples.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StorageUsageTrend object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param end_timestamp:
            The value to assign to the end_timestamp property of this StorageUsageTrend.
        :type end_timestamp: datetime

        :param file_system_usage_in_gbs:
            The value to assign to the file_system_usage_in_gbs property of this StorageUsageTrend.
        :type file_system_usage_in_gbs: float

        :param file_system_avail_in_percent:
            The value to assign to the file_system_avail_in_percent property of this StorageUsageTrend.
        :type file_system_avail_in_percent: float

        """
        self.swagger_types = {
            'end_timestamp': 'datetime',
            'file_system_usage_in_gbs': 'float',
            'file_system_avail_in_percent': 'float'
        }

        self.attribute_map = {
            'end_timestamp': 'endTimestamp',
            'file_system_usage_in_gbs': 'fileSystemUsageInGBs',
            'file_system_avail_in_percent': 'fileSystemAvailInPercent'
        }

        self._end_timestamp = None
        self._file_system_usage_in_gbs = None
        self._file_system_avail_in_percent = None

    @property
    def end_timestamp(self):
        """
        **[Required]** Gets the end_timestamp of this StorageUsageTrend.
        The timestamp in which the current sampling period ends in RFC 3339 format.


        :return: The end_timestamp of this StorageUsageTrend.
        :rtype: datetime
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """
        Sets the end_timestamp of this StorageUsageTrend.
        The timestamp in which the current sampling period ends in RFC 3339 format.


        :param end_timestamp: The end_timestamp of this StorageUsageTrend.
        :type: datetime
        """
        self._end_timestamp = end_timestamp

    @property
    def file_system_usage_in_gbs(self):
        """
        **[Required]** Gets the file_system_usage_in_gbs of this StorageUsageTrend.
        Filesystem usage in GB.


        :return: The file_system_usage_in_gbs of this StorageUsageTrend.
        :rtype: float
        """
        return self._file_system_usage_in_gbs

    @file_system_usage_in_gbs.setter
    def file_system_usage_in_gbs(self, file_system_usage_in_gbs):
        """
        Sets the file_system_usage_in_gbs of this StorageUsageTrend.
        Filesystem usage in GB.


        :param file_system_usage_in_gbs: The file_system_usage_in_gbs of this StorageUsageTrend.
        :type: float
        """
        self._file_system_usage_in_gbs = file_system_usage_in_gbs

    @property
    def file_system_avail_in_percent(self):
        """
        **[Required]** Gets the file_system_avail_in_percent of this StorageUsageTrend.
        Filesystem available in percent.


        :return: The file_system_avail_in_percent of this StorageUsageTrend.
        :rtype: float
        """
        return self._file_system_avail_in_percent

    @file_system_avail_in_percent.setter
    def file_system_avail_in_percent(self, file_system_avail_in_percent):
        """
        Sets the file_system_avail_in_percent of this StorageUsageTrend.
        Filesystem available in percent.


        :param file_system_avail_in_percent: The file_system_avail_in_percent of this StorageUsageTrend.
        :type: float
        """
        self._file_system_avail_in_percent = file_system_avail_in_percent

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other