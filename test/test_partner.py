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

from clientapi_billingo.models.partner import Partner  # noqa: E501

class TestPartner(unittest.TestCase):
    """Partner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Partner:
        """Test Partner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Partner`
        """
        model = Partner()  # noqa: E501
        if include_optional:
            return Partner(
                id = 56,
                name = '',
                address = clientapi_billingo.models.address.Address(
                    country_code = '', 
                    post_code = '', 
                    city = '', 
                    address = '', ),
                emails = [
                    ''
                    ],
                taxcode = '',
                iban = '',
                swift = '',
                account_number = '',
                phone = '',
                general_ledger_number = '',
                tax_type = '',
                custom_billing_settings = clientapi_billingo.models.partner_custom_billing_settings.PartnerCustomBillingSettings(
                    payment_method = 'aruhitel', 
                    document_form = 'electronic', 
                    due_days = 56, 
                    document_currency = 'AED', 
                    template_language_code = 'de', 
                    discount = clientapi_billingo.models.discount.Discount(
                        type = 'percent', 
                        value = 56, ), ),
                group_member_tax_number = ''
            )
        else:
            return Partner(
        )
        """

    def testPartner(self):
        """Test Partner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
