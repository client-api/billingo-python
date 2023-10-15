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





class SpendingPaymentMethod(str, Enum):
    """
    SpendingPaymentMethod
    """

    """
    allowed enum values
    """
    ARUHITEL = 'aruhitel'
    BANKCARD = 'bankcard'
    BARION = 'barion'
    BARTER = 'barter'
    CASH = 'cash'
    CASH_ON_DELIVERY = 'cash_on_delivery'
    COUPON = 'coupon'
    ELORE_UTALAS = 'elore_utalas'
    EP_KARTYA = 'ep_kartya'
    KOMPENZACIO = 'kompenzacio'
    LEVONAS = 'levonas'
    ONLINE_BANKCARD = 'online_bankcard'
    OTHER = 'other'
    PAYLIKE = 'paylike'
    PAYONEER = 'payoneer'
    PAYPAL = 'paypal'
    PAYPAL_UTOLAG = 'paypal_utolag'
    PAYU = 'payu'
    PICK_PACK_PONT = 'pick_pack_pont'
    POSTAI_CSEKK = 'postai_csekk'
    POSTAUTALVANY = 'postautalvany'
    SKRILL = 'skrill'
    SZEP_CARD = 'szep_card'
    TRANSFERWISE = 'transferwise'
    UPWORK = 'upwork'
    UTALVANY = 'utalvany'
    VALTO = 'valto'
    WIRE_TRANSFER = 'wire_transfer'

    @classmethod
    def from_json(cls, json_str: str) -> SpendingPaymentMethod:
        """Create an instance of SpendingPaymentMethod from a JSON string"""
        return SpendingPaymentMethod(json.loads(json_str))


