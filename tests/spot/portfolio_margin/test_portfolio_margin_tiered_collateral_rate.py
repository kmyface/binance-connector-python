import responses

from binance.spot import Spot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

send_params = {"recvWindow": 5000}
expected_params = {"recvWindow": 5000}


@mock_http_response(
    responses.GET,
    "/sapi/v2/portfolio/collateralRate\\?" + urlencode(expected_params),
    mock_item,
    200,
)
def test_portfolio_margin_tiered_collateral_rate():
    """Tests the API endpoint to get portfolio margin PRO tiered collateral rate"""

    client = Client(key, secret)
    response = client.portfolio_margin_tiered_collateral_rate(**send_params)
    response.should.equal(mock_item)
