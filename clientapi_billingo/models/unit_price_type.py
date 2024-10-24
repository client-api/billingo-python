# coding: utf-8

"""
    Billingo API v3

    This is a Billingo API v3 documentation. Our API based on REST software architectural style. API has resource-oriented URLs, accepts JSON-encoded request bodies and returns JSON-encoded responses. To use this API you have to generate a new API key on our [site](https://app.billingo.hu/api-key). After that, you can test your API key on this page.

    The version of the OpenAPI document: 3.0.14
    Contact: hello@billingo.hu
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class UnitPriceType(str, Enum):
    """
    UnitPriceType
    """

    """
    allowed enum values
    """
    GROSS = 'gross'
    NET = 'net'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UnitPriceType from a JSON string"""
        return cls(json.loads(json_str))


