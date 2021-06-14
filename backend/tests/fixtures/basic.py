from pytest import fixture
from typing import Dict


@fixture
def booking() -> Dict:
    return {
        "order_number": "AAAAAA",
        "marker": "abcabcabcabc",
        "booked_at": "2021-01-01 00:00:00",
        "price": 60000.00,
        "price_currency": "RUB",
        "profit": 60000.00 * 0.025,
        "profit_currency": "RUB",
        "state": "paid",
    }


@fixture
def stats_admin_bookings() -> Dict:
    return {
        "AAAAAA": {
            "order_number": "AAAAAA",
            "marker": "abcabcabcabc",
            "booked_at": "2021-01-01 00:00:00",
            "price": 40000.00,
            "price_currency": "RUB",
            "profit": 40000.00 * 0.025,
            "profit_currency": "RUB",
            "state": "paid",
        },
        "BBBBBB": {
            "order_number": "BBBBBB",
            "marker": "bcdbcdbcdbcd",
            "booked_at": "2021-01-02 00:00:00",
            "price": 100000.00,
            "price_currency": "RUB",
            "profit": 100000.00 * 0.025,
            "profit_currency": "RUB",
            "state": "paid",
        },
        "CCCCCC": {
            "order_number": "CCCCCC",
            "marker": "cdecdecdecde",
            "booked_at": "2021-10-05 00:00:00",
            "price": 5800.75,
            "price_currency": "RUB",
            "profit": 5800.75 * 0.025,
            "profit_currency": "RUB",
            "state": "paid",
        },
    }