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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from clientapi_billingo.models.ledger_number_information import LedgerNumberInformation
from typing import Optional, Set
from typing_extensions import Self

class DocumentExportFilterExtra(BaseModel):
    """
    DocumentExportFilterExtra
    """ # noqa: E501
    tensoft_vkod: Optional[StrictStr] = None
    ledger_number: Optional[LedgerNumberInformation] = None
    forintsoft_konyvelesi_naplo_szam: Optional[StrictStr] = None
    positive_ledger_number: Optional[StrictStr] = None
    negative_ledger_number: Optional[StrictStr] = None
    rlb_kata: Optional[StrictBool] = None
    rlb_note: Optional[StrictStr] = None
    novitax_naplokod: Optional[StrictStr] = None
    use_gross_values: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["tensoft_vkod", "ledger_number", "forintsoft_konyvelesi_naplo_szam", "positive_ledger_number", "negative_ledger_number", "rlb_kata", "rlb_note", "novitax_naplokod", "use_gross_values"]

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
        """Create an instance of DocumentExportFilterExtra from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ledger_number
        if self.ledger_number:
            _dict['ledger_number'] = self.ledger_number.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocumentExportFilterExtra from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tensoft_vkod": obj.get("tensoft_vkod"),
            "ledger_number": LedgerNumberInformation.from_dict(obj["ledger_number"]) if obj.get("ledger_number") is not None else None,
            "forintsoft_konyvelesi_naplo_szam": obj.get("forintsoft_konyvelesi_naplo_szam"),
            "positive_ledger_number": obj.get("positive_ledger_number"),
            "negative_ledger_number": obj.get("negative_ledger_number"),
            "rlb_kata": obj.get("rlb_kata"),
            "rlb_note": obj.get("rlb_note"),
            "novitax_naplokod": obj.get("novitax_naplokod"),
            "use_gross_values": obj.get("use_gross_values")
        })
        return _obj


