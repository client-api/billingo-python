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

from clientapi_billingo.models.receipt_product_data import ReceiptProductData

class TestReceiptProductData(unittest.TestCase):
    """ReceiptProductData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReceiptProductData:
        """Test ReceiptProductData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReceiptProductData`
        """
        model = ReceiptProductData()
        if include_optional:
            return ReceiptProductData(
                name = '',
                unit_price = 1.337,
                vat = '0%'
            )
        else:
            return ReceiptProductData(
                unit_price = 1.337,
                vat = '0%',
        )
        """

    def testReceiptProductData(self):
        """Test ReceiptProductData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
