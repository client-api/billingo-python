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

from clientapi_billingo.api.document_block_api import DocumentBlockApi  # noqa: E501


class TestDocumentBlockApi(unittest.TestCase):
    """DocumentBlockApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DocumentBlockApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_list_document_block(self) -> None:
        """Test case for list_document_block

        List all document blocks  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
