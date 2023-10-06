import os

import requests
from dotenv import load_dotenv

from challenge2.utils import convert_hex_string_to_address
from constants import API_URL, TRANSACTION_HASH, TRANSFER_EVENT_ID

load_dotenv()
api_key = os.getenv('API_KEY')


def print_transfers(transaction_hash: str) -> list:
    """
    Retrieve transaction logs using the Etherscan API and return the list of transfers.

    Args:
        transaction_hash (str): Hash of the Ethereum transaction.

    Returns:
        list: List of transfer objects, each containing "from", "to", and "amount" fields.
    """
    params = {
        "module": "proxy",
        "action": "eth_getTransactionReceipt",
        "txhash": transaction_hash,
        "apikey": api_key
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        if "result" in data:
            result = data["result"]

            if result["status"] == "0x1":
                logs = result["logs"]
                transfers = []

                for log in logs:

                    if log["topics"][0] == TRANSFER_EVENT_ID:
                        transfer = {
                            "from": convert_hex_string_to_address(log["topics"][1]),
                            "to": convert_hex_string_to_address(log["topics"][2]),
                            "amount": int(log["data"], 16)
                        }

                        transfers.append(transfer)

                return transfers
            else:
                print("Transaction failed.")
        else:
            print("No result in the response.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

    return []


if __name__ == '__main__':
    transfers = print_transfers(TRANSACTION_HASH)
    print(transfers)
