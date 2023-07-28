# coding: utf-8

"""
    Astro Registry API

    Astro Registry API  # noqa: E501

    The version of the OpenAPI document: v1alpha1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import astronomerregistry
from astronomerregistry.models.modules_paginated import ModulesPaginated  # noqa: E501
from astronomerregistry.rest import ApiException

class TestModulesPaginated(unittest.TestCase):
    """ModulesPaginated unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ModulesPaginated
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModulesPaginated`
        """
        model = astronomerregistry.models.modules_paginated.ModulesPaginated()  # noqa: E501
        if include_optional :
            return ModulesPaginated(
                filters = astronomerregistry.models.module_filters.ModuleFilters(
                    badges = [
                        astronomerregistry.models.short_label.ShortLabel(
                            description = '', 
                            id = '', 
                            name = '', )
                        ], 
                    categories = [
                        astronomerregistry.models.short_label.ShortLabel(
                            description = '', 
                            id = '', 
                            name = '', )
                        ], 
                    providers = [
                        astronomerregistry.models.short_provider.ShortProvider(
                            display_name = '', 
                            logo = '', 
                            name = '', 
                            search_id = '', )
                        ], 
                    tiers = [
                        
                        ], ), 
                limit = 56, 
                modules = [
                    astronomerregistry.models.module.Module(
                        badges = [
                            astronomerregistry.models.short_label.ShortLabel(
                                description = '', 
                                id = '', 
                                name = '', )
                            ], 
                        categories = [
                            astronomerregistry.models.short_label.ShortLabel(
                                description = '', 
                                id = '', 
                                name = '', )
                            ], 
                        created_at = '', 
                        created_by = '', 
                        description = '', 
                        display_name = '', 
                        documentation = '', 
                        github_url = '', 
                        import_path = '', 
                        is_certified = True, 
                        is_cloud_ide_compatible = True, 
                        is_display_name_manual = True, 
                        is_featured = True, 
                        is_global = True, 
                        is_latest_version = True, 
                        is_logo_manual = True, 
                        is_private = True, 
                        logo = '', 
                        name = '', 
                        organization_id = '', 
                        other_versions = [
                            ''
                            ], 
                        parameters = [
                            astronomerregistry.models.module_parameter.ModuleParameter(
                                default_value = '', 
                                description = '', 
                                inherits_from = astronomerregistry.models.module_inherits_from.ModuleInheritsFrom(
                                    module_name = '', 
                                    organization_id = '', 
                                    provider_name = '', 
                                    version = '', ), 
                                name = '', 
                                required = True, 
                                type = '', 
                                type_def = astronomerregistry.models.type_def.TypeDef(
                                    annotation_type = '', 
                                    raw_annotation = '', 
                                    type_variables = [
                                        astronomerregistry.models.type_def.TypeDef(
                                            annotation_type = '', 
                                            raw_annotation = '', )
                                        ], ), )
                            ], 
                        provider_display_name = '', 
                        provider_name = '', 
                        search_id = '', 
                        search_rank = 56, 
                        short_name_id = '', 
                        social_stats = astronomerregistry.models.social_stats.SocialStats(
                            stars = 56, 
                            views = 56, ), 
                        tiers = [
                            
                            ], 
                        type = '', 
                        updated_at = '', 
                        updated_by = '', 
                        version = '', )
                    ], 
                offset = 56, 
                total_count = 56
            )
        else :
            return ModulesPaginated(
                filters = astronomerregistry.models.module_filters.ModuleFilters(
                    badges = [
                        astronomerregistry.models.short_label.ShortLabel(
                            description = '', 
                            id = '', 
                            name = '', )
                        ], 
                    categories = [
                        astronomerregistry.models.short_label.ShortLabel(
                            description = '', 
                            id = '', 
                            name = '', )
                        ], 
                    providers = [
                        astronomerregistry.models.short_provider.ShortProvider(
                            display_name = '', 
                            logo = '', 
                            name = '', 
                            search_id = '', )
                        ], 
                    tiers = [
                        
                        ], ),
                limit = 56,
                modules = [
                    astronomerregistry.models.module.Module(
                        badges = [
                            astronomerregistry.models.short_label.ShortLabel(
                                description = '', 
                                id = '', 
                                name = '', )
                            ], 
                        categories = [
                            astronomerregistry.models.short_label.ShortLabel(
                                description = '', 
                                id = '', 
                                name = '', )
                            ], 
                        created_at = '', 
                        created_by = '', 
                        description = '', 
                        display_name = '', 
                        documentation = '', 
                        github_url = '', 
                        import_path = '', 
                        is_certified = True, 
                        is_cloud_ide_compatible = True, 
                        is_display_name_manual = True, 
                        is_featured = True, 
                        is_global = True, 
                        is_latest_version = True, 
                        is_logo_manual = True, 
                        is_private = True, 
                        logo = '', 
                        name = '', 
                        organization_id = '', 
                        other_versions = [
                            ''
                            ], 
                        parameters = [
                            astronomerregistry.models.module_parameter.ModuleParameter(
                                default_value = '', 
                                description = '', 
                                inherits_from = astronomerregistry.models.module_inherits_from.ModuleInheritsFrom(
                                    module_name = '', 
                                    organization_id = '', 
                                    provider_name = '', 
                                    version = '', ), 
                                name = '', 
                                required = True, 
                                type = '', 
                                type_def = astronomerregistry.models.type_def.TypeDef(
                                    annotation_type = '', 
                                    raw_annotation = '', 
                                    type_variables = [
                                        astronomerregistry.models.type_def.TypeDef(
                                            annotation_type = '', 
                                            raw_annotation = '', )
                                        ], ), )
                            ], 
                        provider_display_name = '', 
                        provider_name = '', 
                        search_id = '', 
                        search_rank = 56, 
                        short_name_id = '', 
                        social_stats = astronomerregistry.models.social_stats.SocialStats(
                            stars = 56, 
                            views = 56, ), 
                        tiers = [
                            
                            ], 
                        type = '', 
                        updated_at = '', 
                        updated_by = '', 
                        version = '', )
                    ],
                offset = 56,
                total_count = 56,
        )
        """

    def testModulesPaginated(self):
        """Test ModulesPaginated"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
