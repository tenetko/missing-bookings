from pytest import fixture
from typing import Dict
from controllers.basic import BasicHandler

handler = BasicHandler()
config = handler.get_config("air_astana")


@fixture
def formatted_booking() -> Dict:
    return {
        "order_number": "AAAAAA",
        "marker": "abcabcabcabc",
        "booked_at": "2021-01-01 00:00:00",
        "price": 40000,
        "price_currency": "KZT",
        "profit": 40000 * config["profit"],
        "profit_currency": "KZT",
        "state": "paid",
    }


@fixture
def data() -> Dict:
    return {"order_numbers": '["AAAAAA", "BBBBBB", "CCCCCC"]', "sheet_number": 0}


@fixture
def report_file() -> Dict:
    return {"file": open("tests/test_data/air_astana/test_report.xlsx", "rb")}