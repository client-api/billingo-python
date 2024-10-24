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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from clientapi_billingo.models.document_type import DocumentType
from clientapi_billingo.models.online_payment import OnlinePayment
from clientapi_billingo.models.round import Round
from typing import Optional, Set
from typing_extensions import Self

class DocumentSettings(BaseModel):
    """
    DocumentSettings
    """ # noqa: E501
    mediated_service: Optional[StrictBool] = False
    without_financial_fulfillment: Optional[StrictBool] = False
    online_payment: Optional[OnlinePayment] = None
    round: Optional[Round] = None
    no_send_onlineszamla_by_user: Optional[StrictBool] = None
    order_number: Optional[StrictStr] = None
    place_id: Optional[StrictInt] = None
    instant_payment: Optional[StrictBool] = None
    selected_type: Optional[DocumentType] = None
    __properties: ClassVar[List[str]] = ["mediated_service", "without_financial_fulfillment", "online_payment", "round", "no_send_onlineszamla_by_user", "order_number", "place_id", "instant_payment", "selected_type"]

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
        """Create an instance of DocumentSettings from a JSON string"""
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
        # set to None if place_id (nullable) is None
        # and model_fields_set contains the field
        if self.place_id is None and "place_id" in self.model_fields_set:
            _dict['place_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocumentSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mediated_service": obj.get("mediated_service") if obj.get("mediated_service") is not None else False,
            "without_financial_fulfillment": obj.get("without_financial_fulfillment") if obj.get("without_financial_fulfillment") is not None else False,
            "online_payment": obj.get("online_payment"),
            "round": obj.get("round"),
            "no_send_onlineszamla_by_user": obj.get("no_send_onlineszamla_by_user"),
            "order_number": obj.get("order_number"),
            "place_id": obj.get("place_id"),
            "instant_payment": obj.get("instant_payment"),
            "selected_type": obj.get("selected_type")
        })
        return _obj


