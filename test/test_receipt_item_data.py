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
import datetime

from clientapi_billingo.models.receipt_item_data import ReceiptItemData  # noqa: E501

class TestReceiptItemData(unittest.TestCase):
    """ReceiptItemData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReceiptItemData:
        """Test ReceiptItemData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReceiptItemData`
        """
        model = ReceiptItemData()  # noqa: E501
        if include_optional:
            return ReceiptItemData(
                product_id = 56
            )
        else:
            return ReceiptItemData(
                product_id = 56,
        )
        """

    def testReceiptItemData(self):
        """Test ReceiptItemData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
