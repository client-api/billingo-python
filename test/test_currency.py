# coding: utf-8

"""
    Billingo API v3

    This is a Billingo API v3 documentation. Our API based on REST software architectural style. API has resource-oriented URLs, accepts JSON-encoded request bodies and returns JSON-encoded responses. To use this API you have to generate a new API key on our [site](https://app.billingo.hu/api-key). After that, you can test your API key on this page.  # noqa: E501

    OpenAPI spec version: 3.0.14
    Contact: hello@billingo.hu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import clientapi_billingo
from clientapi_billingo.models.currency import Currency  # noqa: E501
from clientapi_billingo.rest import ApiException


class TestCurrency(unittest.TestCase):
    """Currency unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCurrency(self):
        """Test Currency"""
        # FIXME: construct object with mandatory attributes with example values
        # model = clientapi_billingo.models.currency.Currency()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
