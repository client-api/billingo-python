from pprint import pprint

from clientapi_billingo import ApiException
from clientapi_billingo.billingo import Billingo
from clientapi_billingo.exceptions import UnauthorizedException

try:
    billingo = Billingo(api_key="__your_api_key__")
    utils = billingo.UtilApi()
    server_time = utils.get_server_time()
    pprint(server_time.w3c)
except UnauthorizedException as e:
    pprint(e)
except ApiException as e:
    pprint(e)
except Exception as e:
    pprint(e)