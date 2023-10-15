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





class OnlineSzamlaStatusEnum(str, Enum):
    """
    OnlineSzamlaStatusEnum
    """

    """
    allowed enum values
    """
    ABORTED = 'aborted'
    DONE = 'done'
    EMPTY_ORGANIZATION_COUNTRY_CODE = 'empty_organization_country_code'
    EMPTY_PARTNER_COUNTRY_CODE = 'empty_partner_country_code'
    EMPTY_TAX = 'empty_tax'
    FORBIDDEN = 'forbidden'
    INVALID_ADDRESS = 'invalid_address'
    INVALID_CLIENT = 'invalid_client'
    INVALID_CONVERSION_RATE = 'invalid_conversion_rate'
    INVALID_CUSTOMER = 'invalid_customer'
    INVALID_INVOICE_REFERENCE = 'invalid_invoice_reference'
    INVALID_POSTALCODE = 'invalid_postalcode'
    INVALID_SECURITY_USER = 'invalid_security_user'
    INVALID_TAX = 'invalid_tax'
    INVALID_TAX_NUMBER = 'invalid_tax_number'
    INVALID_USER_RELATION = 'invalid_user_relation'
    INVALID_VAT_DATA = 'invalid_vat_data'
    INVOICE_NUMBER_NOT_UNIQUE = 'invoice_number_not_unique'
    KOBAK_PROCESSING = 'kobak_processing'
    MISSING_DOCUMENT_ITEM_NAME = 'missing_document_item_name'
    NAV_WARN = 'nav_warn'
    NO_ONLINE_SZAMLA_SETTINGS = 'no_online_szamla_settings'
    NO_SEND_BY_USER = 'no_send_by_user'
    NON_EXIST_TAX_NUMBER = 'non_exist_tax_number'
    NOT_UNIQUE = 'not unique'
    NOT_CHECKED = 'not_checked'
    NOT_REGISTERED_CUSTOMER = 'not_registered_customer'
    PROCESSING = 'processing'
    RECEIVED = 'received'
    SAVED = 'saved'
    SEND_FAILED = 'send_failed'
    SENT = 'sent'
    STARTED = 'started'
    TECHNICAL_ERROR = 'technical_error'
    UNDER_TAX_LIMIT = 'under_tax_limit'
    USER_HAS_INVALID_KOBAK = 'user_has_invalid_kobak'
    USER_HASNOT_KOBAK = 'user_hasnot_kobak'
    VALIDATION_OK = 'validation_ok'

    @classmethod
    def from_json(cls, json_str: str) -> OnlineSzamlaStatusEnum:
        """Create an instance of OnlineSzamlaStatusEnum from a JSON string"""
        return OnlineSzamlaStatusEnum(json.loads(json_str))


