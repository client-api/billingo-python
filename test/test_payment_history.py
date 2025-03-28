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

from clientapi_billingo.models.payment_history import PaymentHistory

class TestPaymentHistory(unittest.TestCase):
    """PaymentHistory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentHistory:
        """Test PaymentHistory
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentHistory`
        """
        model = PaymentHistory()
        if include_optional:
            return PaymentHistory(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                price = 1.337,
                payment_method = 'aruhitel',
                voucher_number = '',
                conversion_rate = 1.337
            )
        else:
            return PaymentHistory(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                price = 1.337,
                payment_method = 'aruhitel',
        )
        """

    def testPaymentHistory(self):
        """Test PaymentHistory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
