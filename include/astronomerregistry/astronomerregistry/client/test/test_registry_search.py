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
from astronomerregistry.models.registry_search import RegistrySearch  # noqa: E501
from astronomerregistry.rest import ApiException

class TestRegistrySearch(unittest.TestCase):
    """RegistrySearch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RegistrySearch
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RegistrySearch`
        """
        model = astronomerregistry.models.registry_search.RegistrySearch()  # noqa: E501
        if include_optional :
            return RegistrySearch(
                registry_objects = [
                    astronomerregistry.models.registry_search_hit.RegistrySearchHit(
                        display_name = '', 
                        id = '', 
                        logo = '', 
                        name = '', 
                        other_versions = [
                            ''
                            ], 
                        provider_name = '', 
                        registry_object_type = '', 
                        search_rank = 56, 
                        version = '', )
                    ], 
                total_dag_count = 56, 
                total_module_count = 56, 
                total_provider_count = 56
            )
        else :
            return RegistrySearch(
                registry_objects = [
                    astronomerregistry.models.registry_search_hit.RegistrySearchHit(
                        display_name = '', 
                        id = '', 
                        logo = '', 
                        name = '', 
                        other_versions = [
                            ''
                            ], 
                        provider_name = '', 
                        registry_object_type = '', 
                        search_rank = 56, 
                        version = '', )
                    ],
                total_dag_count = 56,
                total_module_count = 56,
                total_provider_count = 56,
        )
        """

    def testRegistrySearch(self):
        """Test RegistrySearch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()