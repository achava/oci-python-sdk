# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_build_pipeline_stage_details import CreateBuildPipelineStageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateWaitStageDetails(CreateBuildPipelineStageDetails):
    """
    Specifies the Wait stage. You can specify variable wait times or an absolute duration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateWaitStageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CreateWaitStageDetails.build_pipeline_stage_type` attribute
        of this class is ``WAIT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateWaitStageDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateWaitStageDetails.
        :type description: str

        :param build_pipeline_stage_type:
            The value to assign to the build_pipeline_stage_type property of this CreateWaitStageDetails.
        :type build_pipeline_stage_type: str

        :param build_pipeline_id:
            The value to assign to the build_pipeline_id property of this CreateWaitStageDetails.
        :type build_pipeline_id: str

        :param build_pipeline_stage_predecessor_collection:
            The value to assign to the build_pipeline_stage_predecessor_collection property of this CreateWaitStageDetails.
        :type build_pipeline_stage_predecessor_collection: oci.devops.models.BuildPipelineStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateWaitStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateWaitStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param wait_criteria:
            The value to assign to the wait_criteria property of this CreateWaitStageDetails.
        :type wait_criteria: oci.devops.models.CreateWaitCriteriaDetails

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'build_pipeline_stage_type': 'str',
            'build_pipeline_id': 'str',
            'build_pipeline_stage_predecessor_collection': 'BuildPipelineStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'wait_criteria': 'CreateWaitCriteriaDetails'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'build_pipeline_stage_type': 'buildPipelineStageType',
            'build_pipeline_id': 'buildPipelineId',
            'build_pipeline_stage_predecessor_collection': 'buildPipelineStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'wait_criteria': 'waitCriteria'
        }

        self._display_name = None
        self._description = None
        self._build_pipeline_stage_type = None
        self._build_pipeline_id = None
        self._build_pipeline_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._wait_criteria = None
        self._build_pipeline_stage_type = 'WAIT'

    @property
    def wait_criteria(self):
        """
        **[Required]** Gets the wait_criteria of this CreateWaitStageDetails.

        :return: The wait_criteria of this CreateWaitStageDetails.
        :rtype: oci.devops.models.CreateWaitCriteriaDetails
        """
        return self._wait_criteria

    @wait_criteria.setter
    def wait_criteria(self, wait_criteria):
        """
        Sets the wait_criteria of this CreateWaitStageDetails.

        :param wait_criteria: The wait_criteria of this CreateWaitStageDetails.
        :type: oci.devops.models.CreateWaitCriteriaDetails
        """
        self._wait_criteria = wait_criteria

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other