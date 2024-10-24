
import clientapi_billingo
from clientapi_billingo import DocumentBlockApi, DocumentApi, PartnerApi, ProductApi, BankAccountApi, CurrencyApi, DocumentExportApi, OrganizationApi, SpendingApi, UtilApi

class Billingo:

    def __init__(self, api_key: str):
        self.configuration = clientapi_billingo.Configuration(
            host="https://api.billingo.hu/v3",
        )
        self.configuration.api_key['api_key'] = api_key
        self.validate()

    def validate(self):
        if not self.configuration.api_key:
            raise Exception("The Billingo API key is not set.")

    def DocumentApi(self) -> DocumentApi:
        with clientapi_billingo.ApiClient(self.configuration) as api_client:
            return clientapi_billingo.DocumentApi(api_client)

    def DocumentBlockApi(self) -> DocumentBlockApi:
        with clientapi_billingo.ApiClient(self.configuration) as api_client:
            return clientapi_billingo.DocumentBlockApi(api_client)

    def PartnerApi(self) -> PartnerApi:
        with clientapi_billingo.ApiClient(self.configuration) as api_client:
            return clientapi_billingo.PartnerApi(api_client)

    def ProductApi(self) -> ProductApi:
        with clientapi_billingo.ApiClient(self.configuration) as api_client:
            return clientapi_billingo.ProductApi(api_client)

    def BankAccountApi(self) -> BankAccountApi:
        with clientapi_billingo.ApiClient(self.configuration) as api_client:
            return clientapi_billingo.BankAccountApi(api_client)

    def CurrencyApi(self) -> CurrencyApi:
        with clientapi_billingo.ApiClient(self.configuration) as api_client:
            return clientapi_billingo.CurrencyApi(api_client)

    def DocumentExportApi(self) -> DocumentExportApi:
        with clientapi_billingo.ApiClient(self.configuration) as api_client:
            return clientapi_billingo.DocumentExportApi(api_client)

    def OrganizationApi(self) -> OrganizationApi:
        with clientapi_billingo.ApiClient(self.configuration) as api_client:
            return clientapi_billingo.OrganizationApi(api_client)

    def SpendingApi(self) -> SpendingApi:
        with clientapi_billingo.ApiClient(self.configuration) as api_client:
            return clientapi_billingo.SpendingApi(api_client)

    def UtilApi(self) -> UtilApi:
        with clientapi_billingo.ApiClient(self.configuration) as api_client:
            return clientapi_billingo.UtilApi(api_client)
