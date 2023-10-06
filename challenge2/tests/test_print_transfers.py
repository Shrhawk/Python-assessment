import json

import pytest
import responses

from challenge2.tests.test_data import resp_data
from challenge2.transaction_logs import print_transfers
from constants import API_URL


@responses.activate
def test_print_transfers_success():
    responses.add(
        responses.GET,
        API_URL,
        body=json.dumps(resp_data),
        content_type='application/json',
        status=200
    )

    transaction_hash = "0xTransactionHash"

    transfers = print_transfers(transaction_hash)

    assert isinstance(transfers, list)
    assert transfers
    assert isinstance(transfers[0], dict)
    assert "from" in transfers[0]
    assert "to" in transfers[0]
    assert "amount" in transfers[0]


if __name__ == "__main__":
    pytest.main()
