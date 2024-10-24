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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from clientapi_billingo.models.payment_method import PaymentMethod
from typing import Optional, Set
from typing_extensions import Self

class PaymentHistory(BaseModel):
    """
    PaymentHistory
    """ # noqa: E501
    var_date: date = Field(alias="date")
    price: Union[StrictFloat, StrictInt]
    payment_method: PaymentMethod
    voucher_number: Optional[StrictStr] = None
    conversion_rate: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["date", "price", "payment_method", "voucher_number", "conversion_rate"]

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
        """Create an instance of PaymentHistory from a JSON string"""
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
        # set to None if voucher_number (nullable) is None
        # and model_fields_set contains the field
        if self.voucher_number is None and "voucher_number" in self.model_fields_set:
            _dict['voucher_number'] = None

        # set to None if conversion_rate (nullable) is None
        # and model_fields_set contains the field
        if self.conversion_rate is None and "conversion_rate" in self.model_fields_set:
            _dict['conversion_rate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentHistory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "price": obj.get("price"),
            "payment_method": obj.get("payment_method"),
            "voucher_number": obj.get("voucher_number"),
            "conversion_rate": obj.get("conversion_rate")
        })
        return _obj


