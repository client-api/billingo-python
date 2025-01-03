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


class Currency(str, Enum):
    """
    Currency
    """

    """
    allowed enum values
    """
    AED = 'AED'
    AUD = 'AUD'
    BGN = 'BGN'
    BRL = 'BRL'
    CAD = 'CAD'
    CHF = 'CHF'
    CNY = 'CNY'
    CZK = 'CZK'
    DKK = 'DKK'
    EUR = 'EUR'
    GBP = 'GBP'
    HKD = 'HKD'
    HRK = 'HRK'
    HUF = 'HUF'
    IDR = 'IDR'
    ILS = 'ILS'
    INR = 'INR'
    ISK = 'ISK'
    JPY = 'JPY'
    KRW = 'KRW'
    MXN = 'MXN'
    MYR = 'MYR'
    NOK = 'NOK'
    NZD = 'NZD'
    PHP = 'PHP'
    PLN = 'PLN'
    RON = 'RON'
    RSD = 'RSD'
    RUB = 'RUB'
    SEK = 'SEK'
    SGD = 'SGD'
    THB = 'THB'
    TRY = 'TRY'
    UAH = 'UAH'
    USD = 'USD'
    ZAR = 'ZAR'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Currency from a JSON string"""
        return cls(json.loads(json_str))


