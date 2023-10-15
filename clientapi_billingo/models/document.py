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
from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist
from clientapi_billingo.models.correction_type import CorrectionType
from clientapi_billingo.models.currency import Currency
from clientapi_billingo.models.discount import Discount
from clientapi_billingo.models.document_ancestor import DocumentAncestor
from clientapi_billingo.models.document_item import DocumentItem
from clientapi_billingo.models.document_language import DocumentLanguage
from clientapi_billingo.models.document_notification_status import DocumentNotificationStatus
from clientapi_billingo.models.document_organization import DocumentOrganization
from clientapi_billingo.models.document_partner import DocumentPartner
from clientapi_billingo.models.document_settings import DocumentSettings
from clientapi_billingo.models.document_summary import DocumentSummary
from clientapi_billingo.models.document_type import DocumentType
from clientapi_billingo.models.online_szamla_status_enum import OnlineSzamlaStatusEnum
from clientapi_billingo.models.partner import Partner
from clientapi_billingo.models.payment_method import PaymentMethod
from clientapi_billingo.models.payment_status import PaymentStatus

class Document(BaseModel):
    """
    Document object representing your invoice. NOTE: partner property is deprecated. Please use document_partner instead.  # noqa: E501
    """
    id: Optional[StrictInt] = Field(None, description="The document's unique identifier.")
    invoice_number: Optional[StrictStr] = Field(None, description="The document's invoice number.")
    type: Optional[DocumentType] = None
    cancelled: Optional[StrictBool] = None
    block_id: Optional[StrictInt] = Field(None, description="DocumentBlock's identifier.")
    payment_status: Optional[PaymentStatus] = None
    payment_method: Optional[PaymentMethod] = None
    gross_total: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The document's gross total price.")
    currency: Optional[Currency] = None
    conversion_rate: Optional[Union[StrictFloat, StrictInt]] = None
    invoice_date: Optional[date] = None
    fulfillment_date: Optional[date] = None
    due_date: Optional[date] = None
    paid_date: Optional[date] = None
    organization: Optional[DocumentOrganization] = None
    partner: Optional[Partner] = None
    document_partner: Optional[DocumentPartner] = None
    electronic: Optional[StrictBool] = None
    comment: Optional[StrictStr] = None
    tags: Optional[conlist(StrictStr)] = None
    notification_status: Optional[DocumentNotificationStatus] = None
    language: Optional[DocumentLanguage] = None
    items: Optional[conlist(DocumentItem)] = None
    summary: Optional[DocumentSummary] = None
    settings: Optional[DocumentSettings] = None
    online_szamla_status: Optional[OnlineSzamlaStatusEnum] = None
    related_documents: Optional[conlist(DocumentAncestor)] = None
    discount: Optional[Discount] = None
    correction_type: Optional[CorrectionType] = None
    __properties = ["id", "invoice_number", "type", "cancelled", "block_id", "payment_status", "payment_method", "gross_total", "currency", "conversion_rate", "invoice_date", "fulfillment_date", "due_date", "paid_date", "organization", "partner", "document_partner", "electronic", "comment", "tags", "notification_status", "language", "items", "summary", "settings", "online_szamla_status", "related_documents", "discount", "correction_type"]

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
    def from_json(cls, json_str: str) -> Document:
        """Create an instance of Document from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of partner
        if self.partner:
            _dict['partner'] = self.partner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_partner
        if self.document_partner:
            _dict['document_partner'] = self.document_partner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of settings
        if self.settings:
            _dict['settings'] = self.settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in related_documents (list)
        _items = []
        if self.related_documents:
            for _item in self.related_documents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['related_documents'] = _items
        # override the default output from pydantic by calling `to_dict()` of discount
        if self.discount:
            _dict['discount'] = self.discount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Document:
        """Create an instance of Document from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Document.parse_obj(obj)

        _obj = Document.parse_obj({
            "id": obj.get("id"),
            "invoice_number": obj.get("invoice_number"),
            "type": obj.get("type"),
            "cancelled": obj.get("cancelled"),
            "block_id": obj.get("block_id"),
            "payment_status": obj.get("payment_status"),
            "payment_method": obj.get("payment_method"),
            "gross_total": obj.get("gross_total"),
            "currency": obj.get("currency"),
            "conversion_rate": obj.get("conversion_rate"),
            "invoice_date": obj.get("invoice_date"),
            "fulfillment_date": obj.get("fulfillment_date"),
            "due_date": obj.get("due_date"),
            "paid_date": obj.get("paid_date"),
            "organization": DocumentOrganization.from_dict(obj.get("organization")) if obj.get("organization") is not None else None,
            "partner": Partner.from_dict(obj.get("partner")) if obj.get("partner") is not None else None,
            "document_partner": DocumentPartner.from_dict(obj.get("document_partner")) if obj.get("document_partner") is not None else None,
            "electronic": obj.get("electronic"),
            "comment": obj.get("comment"),
            "tags": obj.get("tags"),
            "notification_status": obj.get("notification_status"),
            "language": obj.get("language"),
            "items": [DocumentItem.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None,
            "summary": DocumentSummary.from_dict(obj.get("summary")) if obj.get("summary") is not None else None,
            "settings": DocumentSettings.from_dict(obj.get("settings")) if obj.get("settings") is not None else None,
            "online_szamla_status": obj.get("online_szamla_status"),
            "related_documents": [DocumentAncestor.from_dict(_item) for _item in obj.get("related_documents")] if obj.get("related_documents") is not None else None,
            "discount": Discount.from_dict(obj.get("discount")) if obj.get("discount") is not None else None,
            "correction_type": obj.get("correction_type")
        })
        return _obj


