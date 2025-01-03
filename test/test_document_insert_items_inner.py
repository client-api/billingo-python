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

from clientapi_billingo.models.document_insert_items_inner import DocumentInsertItemsInner

class TestDocumentInsertItemsInner(unittest.TestCase):
    """DocumentInsertItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocumentInsertItemsInner:
        """Test DocumentInsertItemsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocumentInsertItemsInner`
        """
        model = DocumentInsertItemsInner()
        if include_optional:
            return DocumentInsertItemsInner(
                product_id = 56,
                quantity = 1.337,
                comment = '',
                name = '',
                unit_price = 1.337,
                unit_price_type = 'gross',
                unit = '',
                vat = '0%',
                entitlement = 'AAM'
            )
        else:
            return DocumentInsertItemsInner(
                product_id = 56,
                quantity = 1.337,
                name = '',
                unit_price = 1.337,
                unit_price_type = 'gross',
                unit = '',
                vat = '0%',
        )
        """

    def testDocumentInsertItemsInner(self):
        """Test DocumentInsertItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
