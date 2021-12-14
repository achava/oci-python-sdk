# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthenticationPrincipal(object):
    """
    AuthenticationPrincipal model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AuthenticationPrincipal object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tenant:
            The value to assign to the tenant property of this AuthenticationPrincipal.
        :type tenant: oci.identity_data_plane.models.Tenant

        :param user:
            The value to assign to the user property of this AuthenticationPrincipal.
        :type user: oci.identity_data_plane.models.User

        """
        self.swagger_types = {
            'tenant': 'Tenant',
            'user': 'User'
        }

        self.attribute_map = {
            'tenant': 'tenant',
            'user': 'user'
        }

        self._tenant = None
        self._user = None

    @property
    def tenant(self):
        """
        **[Required]** Gets the tenant of this AuthenticationPrincipal.
        The tenancy object.


        :return: The tenant of this AuthenticationPrincipal.
        :rtype: oci.identity_data_plane.models.Tenant
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """
        Sets the tenant of this AuthenticationPrincipal.
        The tenancy object.


        :param tenant: The tenant of this AuthenticationPrincipal.
        :type: oci.identity_data_plane.models.Tenant
        """
        self._tenant = tenant

    @property
    def user(self):
        """
        **[Required]** Gets the user of this AuthenticationPrincipal.
        The user object.


        :return: The user of this AuthenticationPrincipal.
        :rtype: oci.identity_data_plane.models.User
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this AuthenticationPrincipal.
        The user object.


        :param user: The user of this AuthenticationPrincipal.
        :type: oci.identity_data_plane.models.User
        """
        self._user = user

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
