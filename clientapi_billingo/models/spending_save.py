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
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from clientapi_billingo.models.category import Category
from clientapi_billingo.models.currency import Currency
from clientapi_billingo.models.spending_payment_method import SpendingPaymentMethod
from typing import Optional, Set
from typing_extensions import Self

class SpendingSave(BaseModel):
    """
    SpendingSave
    """ # noqa: E501
    currency: Currency
    conversion_rate: Optional[Union[StrictFloat, StrictInt]] = None
    total_gross: Union[StrictFloat, StrictInt]
    total_gross_huf: Union[StrictFloat, StrictInt]
    total_vat_amount: Union[StrictFloat, StrictInt]
    total_vat_amount_huf: Union[StrictFloat, StrictInt]
    fulfillment_date: date
    paid_at: Optional[date] = None
    category: Category
    comment: Optional[StrictStr] = None
    invoice_number: Optional[StrictStr] = None
    invoice_date: Optional[date] = None
    due_date: Optional[date] = None
    payment_method: SpendingPaymentMethod
    partner_id: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["currency", "conversion_rate", "total_gross", "total_gross_huf", "total_vat_amount", "total_vat_amount_huf", "fulfillment_date", "paid_at", "category", "comment", "invoice_number", "invoice_date", "due_date", "payment_method", "partner_id"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SpendingSave from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SpendingSave from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currency": obj.get("currency"),
            "conversion_rate": obj.get("conversion_rate"),
            "total_gross": obj.get("total_gross"),
            "total_gross_huf": obj.get("total_gross_huf"),
            "total_vat_amount": obj.get("total_vat_amount"),
            "total_vat_amount_huf": obj.get("total_vat_amount_huf"),
            "fulfillment_date": obj.get("fulfillment_date"),
            "paid_at": obj.get("paid_at"),
            "category": obj.get("category"),
            "comment": obj.get("comment"),
            "invoice_number": obj.get("invoice_number"),
            "invoice_date": obj.get("invoice_date"),
            "due_date": obj.get("due_date"),
            "payment_method": obj.get("payment_method"),
            "partner_id": obj.get("partner_id")
        })
        return _obj


