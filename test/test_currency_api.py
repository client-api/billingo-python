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

from clientapi_billingo.api.currency_api import CurrencyApi


class TestCurrencyApi(unittest.TestCase):
    """CurrencyApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CurrencyApi()

    def tearDown(self) -> None:
        pass

    def test_get_conversion_rate(self) -> None:
        """Test case for get_conversion_rate

        Get currencies exchange rate.
        """
        pass


if __name__ == '__main__':
    unittest.main()
