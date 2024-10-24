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

from clientapi_billingo.models.modification_document_insert import ModificationDocumentInsert

class TestModificationDocumentInsert(unittest.TestCase):
    """ModificationDocumentInsert unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModificationDocumentInsert:
        """Test ModificationDocumentInsert
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModificationDocumentInsert`
        """
        model = ModificationDocumentInsert()
        if include_optional:
            return ModificationDocumentInsert(
                due_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                comment = '',
                payment_method = 'aruhitel',
                without_financial_fulfillment = True,
                items = [
                    null
                    ]
            )
        else:
            return ModificationDocumentInsert(
        )
        """

    def testModificationDocumentInsert(self):
        """Test ModificationDocumentInsert"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
