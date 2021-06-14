from pytest import fixture
from typing import Dict
from controllers.basic import BasicHandler

handler = BasicHandler()
config = handler.get_config("esky")


@fixture
def formatted_booking() -> Dict:
    return {
        "order_number": "1234567890",
        "marker": "",
        "booked_at": "2021-05-11 00:00:00",
        "price": 150,
        "price_currency": "AUD",
        "profit": 150 * config["profit"],
        "profit_currency": "AUD",
        "state": "paid",
    }


@fixture
def order_numbers() -> Dict:
    return {"order_numbers": '["1234567890", "9876543210", "1122334455"]'}


@fixture
def report_file() -> Dict:
    return {"file": open("tests/test_data/esky/test_report.xlsx", "rb")}
