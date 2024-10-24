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

from clientapi_billingo.models.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    """BankAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BankAccount:
        """Test BankAccount
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BankAccount`
        """
        model = BankAccount()
        if include_optional:
            return BankAccount(
                id = 56,
                name = '',
                account_number = '',
                account_number_iban = '',
                swift = '',
                currency = 'AED',
                need_qr = True
            )
        else:
            return BankAccount(
                name = '',
                account_number = '',
                currency = 'AED',
        )
        """

    def testBankAccount(self):
        """Test BankAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
