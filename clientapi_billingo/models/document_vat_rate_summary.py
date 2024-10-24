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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class DocumentVatRateSummary(BaseModel):
    """
    DocumentVatRateSummary
    """ # noqa: E501
    vat_name: Optional[StrictStr] = None
    vat_percentage: Optional[Union[StrictFloat, StrictInt]] = None
    vat_rate_net_amount: Optional[Union[StrictFloat, StrictInt]] = None
    vat_rate_vat_amount: Optional[Union[StrictFloat, StrictInt]] = None
    vat_rate_vat_amount_local: Optional[Union[StrictFloat, StrictInt]] = None
    vat_rate_gross_amount: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["vat_name", "vat_percentage", "vat_rate_net_amount", "vat_rate_vat_amount", "vat_rate_vat_amount_local", "vat_rate_gross_amount"]

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
        """Create an instance of DocumentVatRateSummary from a JSON string"""
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
        """Create an instance of DocumentVatRateSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "vat_name": obj.get("vat_name"),
            "vat_percentage": obj.get("vat_percentage"),
            "vat_rate_net_amount": obj.get("vat_rate_net_amount"),
            "vat_rate_vat_amount": obj.get("vat_rate_vat_amount"),
            "vat_rate_vat_amount_local": obj.get("vat_rate_vat_amount_local"),
            "vat_rate_gross_amount": obj.get("vat_rate_gross_amount")
        })
        return _obj


