from pytest import fixture
from typing import Dict


@fixture
def formatted_booking() -> Dict:
    return {
        "pnr": "AAAAAA",
        "marker": "abcabcabcabc",
        "booked_at": "2021-01-01 00:00:00",
        "price": 40000,
        "price_currency": "KZT",
        "profit": 40000 * 0.0133,
        "profit_currency": "KZT",
        "state": "paid",
    }


@fixture
def order_numbers() -> Dict:
    return {"order_numbers": '["AAAAAA", "BBBBBB", "CCCCCC"]'}


@fixture
def report_file() -> Dict:
    return {"file": open("tests/test_data/air_astana/test_report.xlsx", "rb")}