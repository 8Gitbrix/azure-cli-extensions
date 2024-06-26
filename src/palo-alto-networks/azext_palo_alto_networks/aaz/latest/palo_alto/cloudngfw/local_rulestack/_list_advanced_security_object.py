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
    "palo-alto cloudngfw local-rulestack list-advanced-security-object",
)
class ListAdvancedSecurityObject(AAZCommand):
    """Get the list of advanced security objects

    :example: Get the list of advanced security objects
        az palo-alto cloudngfw local-rulestack list-advanced-security-object -g MyResourceGroup -n MyLocalRulestacks --type feeds
    """

    _aaz_info = {
        "version": "2022-08-29",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/paloaltonetworks.cloudngfw/localrulestacks/{}/listadvancedsecurityobjects", "2022-08-29"],
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
        _args_schema.local_rulestack_name = AAZStrArg(
            options=["-n", "--name", "--local-rulestack-name"],
            help="LocalRulestack resource name",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.skip = AAZStrArg(
            options=["--skip"],
            help="LocalRulestack resource skip",
        )
        _args_schema.top = AAZIntArg(
            options=["--top"],
            help="LocalRulestack resource top",
        )
        _args_schema.type = AAZStrArg(
            options=["--type"],
            help="LocalRulestack resource type",
            required=True,
            enum={"feeds": "feeds", "urlCustom": "urlCustom"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.LocalRulestacksListAdvancedSecurityObjects(ctx=self.ctx)()
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

    class LocalRulestacksListAdvancedSecurityObjects(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/PaloAltoNetworks.Cloudngfw/localRulestacks/{localRulestackName}/listAdvancedSecurityObjects",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "localRulestackName", self.ctx.args.local_rulestack_name,
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
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "skip", self.ctx.args.skip,
                ),
                **self.serialize_query_param(
                    "top", self.ctx.args.top,
                ),
                **self.serialize_query_param(
                    "type", self.ctx.args.type,
                    required=True,
                ),
                **self.serialize_query_param(
                    "api-version", "2022-08-29",
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
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZObjectType(
                flags={"required": True},
            )

            value = cls._schema_on_200.value
            value.entry = AAZListType(
                flags={"required": True},
            )
            value.type = AAZStrType()

            entry = cls._schema_on_200.value.entry
            entry.Element = AAZObjectType()

            _element = cls._schema_on_200.value.entry.Element
            _element.description = AAZStrType()
            _element.name = AAZStrType(
                flags={"required": True},
            )

            return cls._schema_on_200


class _ListAdvancedSecurityObjectHelper:
    """Helper class for ListAdvancedSecurityObject"""


__all__ = ["ListAdvancedSecurityObject"]
