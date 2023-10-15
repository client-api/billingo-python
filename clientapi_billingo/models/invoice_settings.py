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
from typing import Optional
from pydantic import BaseModel, StrictStr
from clientapi_billingo.models.document_format import DocumentFormat
from clientapi_billingo.models.document_type import DocumentType

class InvoiceSettings(BaseModel):
    """
    InvoiceSettings
    """
    document_type: Optional[DocumentType] = None
    fulfillment_date: Optional[date] = None
    due_date: Optional[date] = None
    document_format: Optional[DocumentFormat] = None
    comment: Optional[StrictStr] = None
    __properties = ["document_type", "fulfillment_date", "due_date", "document_format", "comment"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> InvoiceSettings:
        """Create an instance of InvoiceSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InvoiceSettings:
        """Create an instance of InvoiceSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InvoiceSettings.parse_obj(obj)

        _obj = InvoiceSettings.parse_obj({
            "document_type": obj.get("document_type"),
            "fulfillment_date": obj.get("fulfillment_date"),
            "due_date": obj.get("due_date"),
            "document_format": obj.get("document_format"),
            "comment": obj.get("comment")
        })
        return _obj


