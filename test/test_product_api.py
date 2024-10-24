# coding: utf-8

"""
    Billingo API v3

    This is a Billingo API v3 documentation. Our API based on REST software architectural style. API has resource-oriented URLs, accepts JSON-encoded request bodies and returns JSON-encoded responses. To use this API you have to generate a new API key on our [site](https://app.billingo.hu/api-key). After that, you can test your API key on this page.

    The version of the OpenAPI document: 3.0.14
    Contact: hello@billingo.hu
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_billingo.api.product_api import ProductApi


class TestProductApi(unittest.TestCase):
    """ProductApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProductApi()

    def tearDown(self) -> None:
        pass

    def test_create_product(self) -> None:
        """Test case for create_product

        Create a product
        """
        pass

    def test_delete_product(self) -> None:
        """Test case for delete_product

        Delete a product
        """
        pass

    def test_get_product(self) -> None:
        """Test case for get_product

        Retrieve a product
        """
        pass

    def test_list_product(self) -> None:
        """Test case for list_product

        List all product
        """
        pass

    def test_update_product(self) -> None:
        """Test case for update_product

        Update a product
        """
        pass


if __name__ == '__main__':
    unittest.main()
