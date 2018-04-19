# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateLoadBalancerDetails(object):
    """
    Configuration details to update a load balancer.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateLoadBalancerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateLoadBalancerDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'display_name': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName'
        }

        self._display_name = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this UpdateLoadBalancerDetails.
        The user-friendly display name for the load balancer. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My load balancer`


        :return: The display_name of this UpdateLoadBalancerDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateLoadBalancerDetails.
        The user-friendly display name for the load balancer. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My load balancer`


        :param display_name: The display_name of this UpdateLoadBalancerDetails.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other