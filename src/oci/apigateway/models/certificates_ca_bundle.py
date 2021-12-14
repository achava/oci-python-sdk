# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .ca_bundle import CaBundle
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificatesCaBundle(CaBundle):
    """
    CA bundle from Certificates Service that should be used on the gateway for TLS validation
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CertificatesCaBundle object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.CertificatesCaBundle.type` attribute
        of this class is ``CA_BUNDLE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CertificatesCaBundle.
            Allowed values for this property are: "CA_BUNDLE", "CERTIFICATE_AUTHORITY"
        :type type: str

        :param ca_bundle_id:
            The value to assign to the ca_bundle_id property of this CertificatesCaBundle.
        :type ca_bundle_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'ca_bundle_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'ca_bundle_id': 'caBundleId'
        }

        self._type = None
        self._ca_bundle_id = None
        self._type = 'CA_BUNDLE'

    @property
    def ca_bundle_id(self):
        """
        Gets the ca_bundle_id of this CertificatesCaBundle.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The ca_bundle_id of this CertificatesCaBundle.
        :rtype: str
        """
        return self._ca_bundle_id

    @ca_bundle_id.setter
    def ca_bundle_id(self, ca_bundle_id):
        """
        Sets the ca_bundle_id of this CertificatesCaBundle.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param ca_bundle_id: The ca_bundle_id of this CertificatesCaBundle.
        :type: str
        """
        self._ca_bundle_id = ca_bundle_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
