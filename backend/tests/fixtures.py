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
def stats_admin_bookings() -> Dict:
    return {
        "AAAAAA": {
            "pnr": "AAAAAA",
            "marker": "abcabcabcabc",
            "booked_at": "2021-01-01 00:00:00",
            "price": 40000.00,
            "price_currency": "KZT",
            "profit": 40000.00 * 0.0133,
            "profit_currency": "KZT",
            "state": "paid",
        },
        "BBBBBB": {
            "pnr": "BBBBBB",
            "marker": "bcdbcdbcdbcd",
            "booked_at": "2021-01-02 00:00:00",
            "price": 100000.00,
            "price_currency": "KZT",
            "profit": 100000.00 * 0.0133,
            "profit_currency": "KZT",
            "state": "paid",
        },
        "CCCCCC": {
            "pnr": "CCCCCC",
            "marker": "cdecdecdecde",
            "booked_at": "2021-10-05 00:00:00",
            "price": 5800.75,
            "price_currency": "RUB",
            "profit": 5800.75 * 0.0133,
            "profit_currency": "RUB",
            "state": "paid",
        },
    }


@fixture
def booking() -> Dict:
    return {
        "pnr": "AAAAAA",
        "marker": "abcabcabcabc",
        "booked_at": "2021-01-01 00:00:00",
        "price": 60000.00,
        "price_currency": "KZT",
        "profit": 798.00,
        "profit_currency": "KZT",
        "state": "paid",
    }


@fixture
def order_numbers() -> str:
    return '["AAAAAA", "BBBBBB", "CCCCCC"]'