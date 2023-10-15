# coding: utf-8

"""
    Billingo API v3

    This is a Billingo API v3 documentation. Our API based on REST software architectural style. API has resource-oriented URLs, accepts JSON-encoded request bodies and returns JSON-encoded responses. To use this API you have to generate a new API key on our [site](https://app.billingo.hu/api-key). After that, you can test your API key on this page.

    The version of the OpenAPI document: 3.0.14
    Contact: hello@billingo.hu
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class DiscountType(str, Enum):
    """
    DiscountType
    """

    """
    allowed enum values
    """
    PERCENT = 'percent'

    @classmethod
    def from_json(cls, json_str: str) -> DiscountType:
        """Create an instance of DiscountType from a JSON string"""
        return DiscountType(json.loads(json_str))


