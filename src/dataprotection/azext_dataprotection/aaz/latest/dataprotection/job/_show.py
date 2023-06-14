# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "dataprotection job show",
    is_experimental=True,
)
class Show(AAZCommand):
    """Get a job with id in a backup vault.

    :example: Get Job
        az dataprotection job show --job-id "3c60cb49-63e8-4b21-b9bd-26277b3fdfae" --resource-group "BugBash1" --vault-name "BugBashVaultForCCYv11"
    """

    _aaz_info = {
        "version": "2023-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.dataprotection/backupvaults/{}/backupjobs/{}", "2023-01-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Resource Id Arguments"

        _args_schema = cls._args_schema
        _args_schema.job_id = AAZStrArg(
            options=["--job-id"],
            arg_group="Resource Id Arguments",
            help="The Job ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.vault_name = AAZStrArg(
            options=["--vault-name"],
            arg_group="Resource Id Arguments",
            help="The name of the backup vault.",
            required=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.JobsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class JobsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataProtection/backupVaults/{vaultName}/backupJobs/{jobId}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "jobId", self.ctx.args.job_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "vaultName", self.ctx.args.vault_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.activity_id = AAZStrType(
                serialized_name="activityID",
                flags={"required": True},
            )
            properties.backup_instance_friendly_name = AAZStrType(
                serialized_name="backupInstanceFriendlyName",
                flags={"required": True},
            )
            properties.backup_instance_id = AAZStrType(
                serialized_name="backupInstanceId",
                flags={"read_only": True},
            )
            properties.data_source_id = AAZStrType(
                serialized_name="dataSourceId",
                flags={"required": True},
            )
            properties.data_source_location = AAZStrType(
                serialized_name="dataSourceLocation",
                flags={"required": True},
            )
            properties.data_source_name = AAZStrType(
                serialized_name="dataSourceName",
                flags={"required": True},
            )
            properties.data_source_set_name = AAZStrType(
                serialized_name="dataSourceSetName",
            )
            properties.data_source_type = AAZStrType(
                serialized_name="dataSourceType",
                flags={"required": True},
            )
            properties.destination_data_store_name = AAZStrType(
                serialized_name="destinationDataStoreName",
            )
            properties.duration = AAZStrType()
            properties.end_time = AAZStrType(
                serialized_name="endTime",
                flags={"read_only": True},
            )
            properties.error_details = AAZListType(
                serialized_name="errorDetails",
                flags={"read_only": True},
            )
            properties.etag = AAZStrType()
            properties.extended_info = AAZObjectType(
                serialized_name="extendedInfo",
            )
            properties.is_user_triggered = AAZBoolType(
                serialized_name="isUserTriggered",
                flags={"required": True},
            )
            properties.operation = AAZStrType(
                flags={"required": True},
            )
            properties.operation_category = AAZStrType(
                serialized_name="operationCategory",
                flags={"required": True},
            )
            properties.policy_id = AAZStrType(
                serialized_name="policyId",
                flags={"read_only": True},
            )
            properties.policy_name = AAZStrType(
                serialized_name="policyName",
                flags={"read_only": True},
            )
            properties.progress_enabled = AAZBoolType(
                serialized_name="progressEnabled",
                flags={"required": True},
            )
            properties.progress_url = AAZStrType(
                serialized_name="progressUrl",
                flags={"read_only": True},
            )
            properties.restore_type = AAZStrType(
                serialized_name="restoreType",
                flags={"read_only": True},
            )
            properties.source_data_store_name = AAZStrType(
                serialized_name="sourceDataStoreName",
            )
            properties.source_resource_group = AAZStrType(
                serialized_name="sourceResourceGroup",
                flags={"required": True},
            )
            properties.source_subscription_id = AAZStrType(
                serialized_name="sourceSubscriptionID",
                flags={"required": True},
            )
            properties.start_time = AAZStrType(
                serialized_name="startTime",
                flags={"required": True},
            )
            properties.status = AAZStrType(
                flags={"required": True},
            )
            properties.subscription_id = AAZStrType(
                serialized_name="subscriptionId",
                flags={"required": True},
            )
            properties.supported_actions = AAZListType(
                serialized_name="supportedActions",
                flags={"required": True},
            )
            properties.vault_name = AAZStrType(
                serialized_name="vaultName",
                flags={"required": True},
            )

            error_details = cls._schema_on_200.properties.error_details
            error_details.Element = AAZObjectType()
            _ShowHelper._build_schema_user_facing_error_read(error_details.Element)

            extended_info = cls._schema_on_200.properties.extended_info
            extended_info.additional_details = AAZDictType(
                serialized_name="additionalDetails",
            )
            extended_info.backup_instance_state = AAZStrType(
                serialized_name="backupInstanceState",
                flags={"read_only": True},
            )
            extended_info.data_transferred_in_bytes = AAZFloatType(
                serialized_name="dataTransferredInBytes",
                flags={"read_only": True},
            )
            extended_info.recovery_destination = AAZStrType(
                serialized_name="recoveryDestination",
                flags={"read_only": True},
            )
            extended_info.source_recover_point = AAZObjectType(
                serialized_name="sourceRecoverPoint",
            )
            _ShowHelper._build_schema_restore_job_recovery_point_details_read(extended_info.source_recover_point)
            extended_info.sub_tasks = AAZListType(
                serialized_name="subTasks",
                flags={"read_only": True},
            )
            extended_info.target_recover_point = AAZObjectType(
                serialized_name="targetRecoverPoint",
            )
            _ShowHelper._build_schema_restore_job_recovery_point_details_read(extended_info.target_recover_point)

            additional_details = cls._schema_on_200.properties.extended_info.additional_details
            additional_details.Element = AAZStrType(
                flags={"read_only": True},
            )

            sub_tasks = cls._schema_on_200.properties.extended_info.sub_tasks
            sub_tasks.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.extended_info.sub_tasks.Element
            _element.additional_details = AAZDictType(
                serialized_name="additionalDetails",
            )
            _element.task_id = AAZIntType(
                serialized_name="taskId",
                flags={"required": True},
            )
            _element.task_name = AAZStrType(
                serialized_name="taskName",
                flags={"required": True},
            )
            _element.task_progress = AAZStrType(
                serialized_name="taskProgress",
                flags={"read_only": True},
            )
            _element.task_status = AAZStrType(
                serialized_name="taskStatus",
                flags={"required": True},
            )

            additional_details = cls._schema_on_200.properties.extended_info.sub_tasks.Element.additional_details
            additional_details.Element = AAZStrType(
                flags={"read_only": True},
            )

            supported_actions = cls._schema_on_200.properties.supported_actions
            supported_actions.Element = AAZStrType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_inner_error_read = None

    @classmethod
    def _build_schema_inner_error_read(cls, _schema):
        if cls._schema_inner_error_read is not None:
            _schema.additional_info = cls._schema_inner_error_read.additional_info
            _schema.code = cls._schema_inner_error_read.code
            _schema.embedded_inner_error = cls._schema_inner_error_read.embedded_inner_error
            return

        cls._schema_inner_error_read = _schema_inner_error_read = AAZObjectType()

        inner_error_read = _schema_inner_error_read
        inner_error_read.additional_info = AAZDictType(
            serialized_name="additionalInfo",
        )
        inner_error_read.code = AAZStrType()
        inner_error_read.embedded_inner_error = AAZObjectType(
            serialized_name="embeddedInnerError",
        )
        cls._build_schema_inner_error_read(inner_error_read.embedded_inner_error)

        additional_info = _schema_inner_error_read.additional_info
        additional_info.Element = AAZStrType()

        _schema.additional_info = cls._schema_inner_error_read.additional_info
        _schema.code = cls._schema_inner_error_read.code
        _schema.embedded_inner_error = cls._schema_inner_error_read.embedded_inner_error

    _schema_restore_job_recovery_point_details_read = None

    @classmethod
    def _build_schema_restore_job_recovery_point_details_read(cls, _schema):
        if cls._schema_restore_job_recovery_point_details_read is not None:
            _schema.recovery_point_id = cls._schema_restore_job_recovery_point_details_read.recovery_point_id
            _schema.recovery_point_time = cls._schema_restore_job_recovery_point_details_read.recovery_point_time
            return

        cls._schema_restore_job_recovery_point_details_read = _schema_restore_job_recovery_point_details_read = AAZObjectType()

        restore_job_recovery_point_details_read = _schema_restore_job_recovery_point_details_read
        restore_job_recovery_point_details_read.recovery_point_id = AAZStrType(
            serialized_name="recoveryPointID",
        )
        restore_job_recovery_point_details_read.recovery_point_time = AAZStrType(
            serialized_name="recoveryPointTime",
        )

        _schema.recovery_point_id = cls._schema_restore_job_recovery_point_details_read.recovery_point_id
        _schema.recovery_point_time = cls._schema_restore_job_recovery_point_details_read.recovery_point_time

    _schema_user_facing_error_read = None

    @classmethod
    def _build_schema_user_facing_error_read(cls, _schema):
        if cls._schema_user_facing_error_read is not None:
            _schema.code = cls._schema_user_facing_error_read.code
            _schema.details = cls._schema_user_facing_error_read.details
            _schema.inner_error = cls._schema_user_facing_error_read.inner_error
            _schema.is_retryable = cls._schema_user_facing_error_read.is_retryable
            _schema.is_user_error = cls._schema_user_facing_error_read.is_user_error
            _schema.message = cls._schema_user_facing_error_read.message
            _schema.properties = cls._schema_user_facing_error_read.properties
            _schema.recommended_action = cls._schema_user_facing_error_read.recommended_action
            _schema.target = cls._schema_user_facing_error_read.target
            return

        cls._schema_user_facing_error_read = _schema_user_facing_error_read = AAZObjectType()

        user_facing_error_read = _schema_user_facing_error_read
        user_facing_error_read.code = AAZStrType()
        user_facing_error_read.details = AAZListType()
        user_facing_error_read.inner_error = AAZObjectType(
            serialized_name="innerError",
        )
        cls._build_schema_inner_error_read(user_facing_error_read.inner_error)
        user_facing_error_read.is_retryable = AAZBoolType(
            serialized_name="isRetryable",
        )
        user_facing_error_read.is_user_error = AAZBoolType(
            serialized_name="isUserError",
        )
        user_facing_error_read.message = AAZStrType()
        user_facing_error_read.properties = AAZDictType()
        user_facing_error_read.recommended_action = AAZListType(
            serialized_name="recommendedAction",
        )
        user_facing_error_read.target = AAZStrType()

        details = _schema_user_facing_error_read.details
        details.Element = AAZObjectType()
        cls._build_schema_user_facing_error_read(details.Element)

        properties = _schema_user_facing_error_read.properties
        properties.Element = AAZStrType()

        recommended_action = _schema_user_facing_error_read.recommended_action
        recommended_action.Element = AAZStrType()

        _schema.code = cls._schema_user_facing_error_read.code
        _schema.details = cls._schema_user_facing_error_read.details
        _schema.inner_error = cls._schema_user_facing_error_read.inner_error
        _schema.is_retryable = cls._schema_user_facing_error_read.is_retryable
        _schema.is_user_error = cls._schema_user_facing_error_read.is_user_error
        _schema.message = cls._schema_user_facing_error_read.message
        _schema.properties = cls._schema_user_facing_error_read.properties
        _schema.recommended_action = cls._schema_user_facing_error_read.recommended_action
        _schema.target = cls._schema_user_facing_error_read.target


__all__ = ["Show"]