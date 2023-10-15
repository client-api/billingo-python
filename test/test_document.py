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

from clientapi_billingo.models.document import Document  # noqa: E501

class TestDocument(unittest.TestCase):
    """Document unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Document:
        """Test Document
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Document`
        """
        model = Document()  # noqa: E501
        if include_optional:
            return Document(
                id = 56,
                invoice_number = 'PREFIX / 2020-000001',
                type = 'advance',
                cancelled = True,
                block_id = 56,
                payment_status = 'expired',
                payment_method = 'aruhitel',
                gross_total = 1.337,
                currency = 'AED',
                conversion_rate = 1.337,
                invoice_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                fulfillment_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                due_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                paid_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                organization = clientapi_billingo.models.document_organization.DocumentOrganization(
                    name = '', 
                    tax_number = '', 
                    bank_account = clientapi_billingo.models.document_bank_account.DocumentBankAccount(
                        id = 56, 
                        name = '', 
                        account_number = '', 
                        account_number_iban = '', 
                        swift = '', ), 
                    address = clientapi_billingo.models.address.Address(
                        country_code = '', 
                        post_code = '', 
                        city = '', 
                        address = '', ), 
                    small_taxpayer = True, 
                    ev_number = '', 
                    eu_tax_number = '', 
                    cash_settled = True, ),
                partner = clientapi_billingo.models.partner.Partner(
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
                    group_member_tax_number = '', ),
                document_partner = clientapi_billingo.models.document_partner.DocumentPartner(
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
                    tax_type = '', ),
                electronic = True,
                comment = '',
                tags = [
                    ''
                    ],
                notification_status = 'closed',
                language = 'de',
                items = [
                    clientapi_billingo.models.document_item.DocumentItem(
                        product_id = 56, 
                        name = '', 
                        net_unit_amount = 1.337, 
                        quantity = 1.337, 
                        unit = '', 
                        net_amount = 1.337, 
                        gross_amount = 1.337, 
                        vat = '0%', 
                        vat_amount = 1.337, 
                        entitlement = 'AAM', 
                        comment = '', )
                    ],
                summary = clientapi_billingo.models.document_summary.DocumentSummary(
                    net_amount = 1.337, 
                    net_amount_local = 1.337, 
                    gross_amount_local = 1.337, 
                    vat_amount = 1.337, 
                    vat_amount_local = 1.337, 
                    vat_rate_summary = [
                        clientapi_billingo.models.document_vat_rate_summary.DocumentVatRateSummary(
                            vat_name = '', 
                            vat_percentage = 1.337, 
                            vat_rate_net_amount = 1.337, 
                            vat_rate_vat_amount = 1.337, 
                            vat_rate_vat_amount_local = 1.337, 
                            vat_rate_gross_amount = 1.337, )
                        ], ),
                settings = clientapi_billingo.models.document_settings.DocumentSettings(
                    mediated_service = True, 
                    without_financial_fulfillment = True, 
                    online_payment = '', 
                    round = 'five', 
                    no_send_onlineszamla_by_user = True, 
                    order_number = '', 
                    place_id = 56, 
                    instant_payment = True, 
                    selected_type = 'advance', ),
                online_szamla_status = 'aborted',
                related_documents = [
                    clientapi_billingo.models.document_ancestor.DocumentAncestor(
                        id = 56, 
                        invoice_number = 'PREFIX / 2020-000001', )
                    ],
                discount = clientapi_billingo.models.discount.Discount(
                    type = 'percent', 
                    value = 56, ),
                correction_type = 'advance'
            )
        else:
            return Document(
        )
        """

    def testDocument(self):
        """Test Document"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
