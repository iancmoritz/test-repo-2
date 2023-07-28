# coding: utf-8

"""
    Astro Core API

    Astro Core API  # noqa: E501

    The version of the OpenAPI document: v1alpha1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import astronomercoreapi
from astronomercoreapi.models.cell_type_metadata import CellTypeMetadata  # noqa: E501
from astronomercoreapi.rest import ApiException

class TestCellTypeMetadata(unittest.TestCase):
    """CellTypeMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CellTypeMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CellTypeMetadata`
        """
        model = astronomercoreapi.models.cell_type_metadata.CellTypeMetadata()  # noqa: E501
        if include_optional :
            return CellTypeMetadata(
                created_at = '', 
                created_by = '', 
                definition = astronomercoreapi.models.ctm_definition.CtmDefinition(
                    behavior = astronomercoreapi.models.ctm_behavior.CtmBehavior(
                        exclude_from_graph = True, 
                        generates_data = True, 
                        naming_strategy = 'increment', 
                        returns_raw_value = True, 
                        runnable = True, ), 
                    configs = [
                        astronomercoreapi.models.ctm_config.CtmConfig(
                            applicability = astronomercoreapi.models.ctm_config_applicability.CtmConfigApplicability(
                                when_siblings = [
                                    astronomercoreapi.models.ctm_clause.CtmClause(
                                        key = '', 
                                        operator = 'eq', 
                                        value = astronomercoreapi.models.ctm_value.CtmValue(
                                            boolean = True, 
                                            duration = astronomercoreapi.models.ctm_value_duration.CtmValueDuration(
                                                length = 56, 
                                                unit = 'microseconds', ), 
                                            file = astronomercoreapi.models.ctm_value_file.CtmValueFile(
                                                conn_id = '', 
                                                file_type = '', 
                                                path = '', ), 
                                            float = 1.337, 
                                            integer = 56, 
                                            string = '', 
                                            string_list = [
                                                ''
                                                ], 
                                            string_list_map = {
                                                'key' : [
                                                    ''
                                                    ]
                                                }, 
                                            string_map = {
                                                'key' : ''
                                                }, 
                                            string_map_list = [
                                                {
                                                    'key' : ''
                                                    }
                                                ], 
                                            string_set = {
                                                'key' : True
                                                }, 
                                            table = astronomercoreapi.models.ctm_value_table.CtmValueTable(
                                                conn_id = '', 
                                                database = '', 
                                                name = '', 
                                                schema = '', ), ), )
                                    ], ), 
                            data_type = 'string', 
                            display = astronomercoreapi.models.ctm_config_display.CtmConfigDisplay(
                                default = astronomercoreapi.models.ctm_value.CtmValue(
                                    boolean = True, 
                                    float = 1.337, 
                                    integer = 56, 
                                    string = '', ), 
                                description = '', 
                                example = , 
                                fixed_width_font = True, 
                                highlight_language = 'python', 
                                label = '', 
                                num_lines = 56, 
                                raw_type = '', ), 
                            generation = astronomercoreapi.models.ctm_config_generation.CtmConfigGeneration(
                                disallow_expressions = True, ), 
                            key = '', 
                            validity = astronomercoreapi.models.ctm_config_validity.CtmConfigValidity(
                                domain = astronomercoreapi.models.ctm_config_domain.CtmConfigDomain(
                                    source = 'stringList', 
                                    values_string_list = [
                                        ''
                                        ], ), 
                                mandatory = True, ), )
                        ], 
                    display = astronomercoreapi.models.ctm_display.CtmDisplay(
                        description = '', 
                        label = '', 
                        logo_url = '', ), 
                    generation = astronomercoreapi.models.ctm_generation.CtmGeneration(
                        decorator = astronomercoreapi.models.ctm_generation_decorator.CtmGenerationDecorator(
                            decorator_arg_configs = [
                                ''
                                ], 
                            decorator_function_params = [
                                ''
                                ], 
                            decorator_name = '', 
                            function_arg_configs = [
                                ''
                                ], 
                            function_code_config = '', 
                            imports = [
                                ''
                                ], 
                            include_implicit_deps = True, 
                            include_task_id_as_decorator_arg = True, 
                            include_task_id_as_function_arg = True, ), 
                        invoke = astronomercoreapi.models.ctm_generation_invoke.CtmGenerationInvoke(
                            exclude_task_id_arg = True, 
                            function_name = '', ), 
                        type = 'invoke', ), ), 
                name = '', 
                organization_id = '', 
                project_id = '', 
                source = 'provided', 
                updated_at = '', 
                updated_by = '', 
                workspace_id = ''
            )
        else :
            return CellTypeMetadata(
                name = '',
                source = 'provided',
        )
        """

    def testCellTypeMetadata(self):
        """Test CellTypeMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
