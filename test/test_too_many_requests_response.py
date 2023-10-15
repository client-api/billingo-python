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

from clientapi_billingo.models.too_many_requests_response import TooManyRequestsResponse  # noqa: E501

class TestTooManyRequestsResponse(unittest.TestCase):
    """TooManyRequestsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TooManyRequestsResponse:
        """Test TooManyRequestsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TooManyRequestsResponse`
        """
        model = TooManyRequestsResponse()  # noqa: E501
        if include_optional:
            return TooManyRequestsResponse(
                error = clientapi_billingo.models.client_error.ClientError(
                    message = '', )
            )
        else:
            return TooManyRequestsResponse(
        )
        """

    def testTooManyRequestsResponse(self):
        """Test TooManyRequestsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
