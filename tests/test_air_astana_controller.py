from controllers.air_astana import AirAstanaHandler
from tests.fixtures import *
from fastapi import Response
from fastapi.testclient import TestClient
from main import app

import pandas as pd


handler = AirAstanaHandler()
client = TestClient(app)


def test_format_booking(formatted_booking):
    workbook = pd.ExcelFile("tests/test_data/test_report.xlsx")
    dataframe = pd.read_excel(
        workbook, handler.config["sheet_name"], skiprows=handler.config["skip_rows"]
    )
    row = list(dataframe.itertuples())[0]
    booking = handler.format_booking(row)
    assert booking == formatted_booking


def test_add_new_booking_to_stats_admin_bookings(booking):
    handler.stats_admin_bookings = {}

    handler.add_booking_to_stats_admin_bookings(booking)
    booking_after_changes = handler.stats_admin_bookings["AAAAAA"]
    assert booking_after_changes["price"] == 60000.00
    assert booking_after_changes["profit"] == 60000.00 * 0.0133


def test_add_existing_booking_to_stats_admin_bookings(stats_admin_bookings, booking):
    handler.stats_admin_bookings = stats_admin_bookings

    handler.add_booking_to_stats_admin_bookings(booking)
    booking_after_changes = handler.stats_admin_bookings["AAAAAA"]
    assert booking_after_changes["price"] == 60000 + 40000
    assert booking_after_changes["profit"] == 60000 * 0.0133 + 40000 * 0.0133


def test_export_to_csv_file(stats_admin_bookings):
    handler.stats_admin_bookings = stats_admin_bookings
    with open("tests/test_data/test_csv_file.csv") as example_file:
        example_file_value = example_file.read()
        exported_file = handler.export_to_csv_file()
        exported_file_value = exported_file.getvalue()
        # removing the last character of exported_file_value,
        # as it is a newline character
        assert example_file_value == exported_file_value[:-1]


def test_return_csv_file(stats_admin_bookings):
    handler.stats_admin_bookings = stats_admin_bookings
    exported_file = handler.export_to_csv_file()
    exported_file_name = "stats-admin-air-astana.csv"

    handler_response = handler.return_csv_file(exported_file, exported_file_name)

    expected_response = Response(
        content=handler.export_to_csv_file().read(),
        media_type="text/csv",
        headers={
            "Access-Control-Expose-Headers": "Content-Disposition",
            "Content-Disposition": f"attachment; filename={exported_file_name}",
            "content-length": str(len(exported_file.getvalue())),
        },
    )
    assert handler_response.body == expected_response.body
    assert handler_response.headers == expected_response.headers


def test_get_bookings_for_stats_admin():
    data = {"order_numbers": '["AAAAAA", "BBBBBB", "CCCCCC"]'}
    file = {"file": open("tests/test_data/test_report.xlsx", "rb")}
    response = client.post("/api/astana/", data=data, files=file)
    assert response.status_code == 200
    with open("tests/test_data/test_csv_file.csv") as example_file:
        example_file_value = example_file.read()
        # removing the last character of response.text,
        # as it is a newline character
        assert example_file_value == response.text[:-1]
