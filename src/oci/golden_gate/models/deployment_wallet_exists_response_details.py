# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeploymentWalletExistsResponseDetails(object):
    """
    Indicates whether the wallet exists in the deployment container
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeploymentWalletExistsResponseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_ogg_wallet_exists:
            The value to assign to the is_ogg_wallet_exists property of this DeploymentWalletExistsResponseDetails.
        :type is_ogg_wallet_exists: bool

        """
        self.swagger_types = {
            'is_ogg_wallet_exists': 'bool'
        }

        self.attribute_map = {
            'is_ogg_wallet_exists': 'isOggWalletExists'
        }

        self._is_ogg_wallet_exists = None

    @property
    def is_ogg_wallet_exists(self):
        """
        **[Required]** Gets the is_ogg_wallet_exists of this DeploymentWalletExistsResponseDetails.
        Indicates if the wallet is present in the deployment container


        :return: The is_ogg_wallet_exists of this DeploymentWalletExistsResponseDetails.
        :rtype: bool
        """
        return self._is_ogg_wallet_exists

    @is_ogg_wallet_exists.setter
    def is_ogg_wallet_exists(self, is_ogg_wallet_exists):
        """
        Sets the is_ogg_wallet_exists of this DeploymentWalletExistsResponseDetails.
        Indicates if the wallet is present in the deployment container


        :param is_ogg_wallet_exists: The is_ogg_wallet_exists of this DeploymentWalletExistsResponseDetails.
        :type: bool
        """
        self._is_ogg_wallet_exists = is_ogg_wallet_exists

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other