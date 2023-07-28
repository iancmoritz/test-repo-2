# coding: utf-8

"""
    Astro Core API

    Astro Core API  # noqa: E501

    The version of the OpenAPI document: v1alpha1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import astronomercoreapi
from astronomercoreapi.api.cloud_ide_cell_api import CloudIDECellApi  # noqa: E501
from astronomercoreapi.rest import ApiException


class TestCloudIDECellApi(unittest.TestCase):
    """CloudIDECellApi unit test stubs"""

    def setUp(self):
        self.api = astronomercoreapi.api.cloud_ide_cell_api.CloudIDECellApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_cell(self):
        """Test case for create_cell

        Create a new cell  # noqa: E501
        """
        pass

    def test_delete_cell(self):
        """Test case for delete_cell

        Delete a cell  # noqa: E501
        """
        pass

    def test_duplicate_cell(self):
        """Test case for duplicate_cell

        Duplicate a cell  # noqa: E501
        """
        pass

    def test_get_cell(self):
        """Test case for get_cell

        Get a cell  # noqa: E501
        """
        pass

    def test_list_cells(self):
        """Test case for list_cells

        List cells for a project  # noqa: E501
        """
        pass

    def test_update_cell(self):
        """Test case for update_cell

        Update a cell  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()