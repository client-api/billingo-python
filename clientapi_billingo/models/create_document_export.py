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
from pydantic import BaseModel, Field, StrictInt
from clientapi_billingo.models.document_export_filter_extra import DocumentExportFilterExtra
from clientapi_billingo.models.document_export_other_options import DocumentExportOtherOptions
from clientapi_billingo.models.document_export_query_type import DocumentExportQueryType
from clientapi_billingo.models.document_export_sort_by import DocumentExportSortBy
from clientapi_billingo.models.document_export_type import DocumentExportType
from clientapi_billingo.models.payment_method import PaymentMethod

class CreateDocumentExport(BaseModel):
    """
    CreateDocumentExport
    """
    query_type: DocumentExportQueryType = Field(...)
    start_date: date = Field(...)
    end_date: date = Field(...)
    document_block_id: Optional[StrictInt] = None
    export_type: DocumentExportType = Field(...)
    number_start_year: Optional[StrictInt] = None
    number_start_sequence: Optional[StrictInt] = None
    number_end_year: Optional[StrictInt] = None
    number_end_sequence: Optional[StrictInt] = None
    payment_method: Optional[PaymentMethod] = None
    sort_by: Optional[DocumentExportSortBy] = None
    other_options: Optional[DocumentExportOtherOptions] = None
    filter_extra: Optional[DocumentExportFilterExtra] = None
    __properties = ["query_type", "start_date", "end_date", "document_block_id", "export_type", "number_start_year", "number_start_sequence", "number_end_year", "number_end_sequence", "payment_method", "sort_by", "other_options", "filter_extra"]

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
    def from_json(cls, json_str: str) -> CreateDocumentExport:
        """Create an instance of CreateDocumentExport from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of filter_extra
        if self.filter_extra:
            _dict['filter_extra'] = self.filter_extra.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateDocumentExport:
        """Create an instance of CreateDocumentExport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateDocumentExport.parse_obj(obj)

        _obj = CreateDocumentExport.parse_obj({
            "query_type": obj.get("query_type"),
            "start_date": obj.get("start_date"),
            "end_date": obj.get("end_date"),
            "document_block_id": obj.get("document_block_id"),
            "export_type": obj.get("export_type"),
            "number_start_year": obj.get("number_start_year"),
            "number_start_sequence": obj.get("number_start_sequence"),
            "number_end_year": obj.get("number_end_year"),
            "number_end_sequence": obj.get("number_end_sequence"),
            "payment_method": obj.get("payment_method"),
            "sort_by": obj.get("sort_by"),
            "other_options": obj.get("other_options"),
            "filter_extra": DocumentExportFilterExtra.from_dict(obj.get("filter_extra")) if obj.get("filter_extra") is not None else None
        })
        return _obj


