# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OptimizerStatisticsAdvisorExecutionReport(object):
    """
    A report that includes the rules, findings, recommendations, and actions discovered during the
    execution of the Optimizer Statistics Advisor.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OptimizerStatisticsAdvisorExecutionReport object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param summary:
            The value to assign to the summary property of this OptimizerStatisticsAdvisorExecutionReport.
        :type summary: str

        :param rules:
            The value to assign to the rules property of this OptimizerStatisticsAdvisorExecutionReport.
        :type rules: list[oci.database_management.models.AdvisorRule]

        """
        self.swagger_types = {
            'summary': 'str',
            'rules': 'list[AdvisorRule]'
        }

        self.attribute_map = {
            'summary': 'summary',
            'rules': 'rules'
        }

        self._summary = None
        self._rules = None

    @property
    def summary(self):
        """
        **[Required]** Gets the summary of this OptimizerStatisticsAdvisorExecutionReport.
        A summary of the Optimizer Statistics Advisor execution.


        :return: The summary of this OptimizerStatisticsAdvisorExecutionReport.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this OptimizerStatisticsAdvisorExecutionReport.
        A summary of the Optimizer Statistics Advisor execution.


        :param summary: The summary of this OptimizerStatisticsAdvisorExecutionReport.
        :type: str
        """
        self._summary = summary

    @property
    def rules(self):
        """
        **[Required]** Gets the rules of this OptimizerStatisticsAdvisorExecutionReport.
        The list of rules that were not adhered to by the Optimizer Statistics Collection.


        :return: The rules of this OptimizerStatisticsAdvisorExecutionReport.
        :rtype: list[oci.database_management.models.AdvisorRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this OptimizerStatisticsAdvisorExecutionReport.
        The list of rules that were not adhered to by the Optimizer Statistics Collection.


        :param rules: The rules of this OptimizerStatisticsAdvisorExecutionReport.
        :type: list[oci.database_management.models.AdvisorRule]
        """
        self._rules = rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other