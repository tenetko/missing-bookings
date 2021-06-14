from controllers.air_astana import AirAstanaHandler
from tests.fixtures.air_astana import *
from fastapi.testclient import TestClient
from main import app

import pandas as pd

handler = AirAstanaHandler()
client = TestClient(app)


def test_format_booking(formatted_booking):
    workbook = pd.ExcelFile("tests/test_data/air_astana/test_report.xlsx")
    dataframe = pd.read_excel(
        workbook, handler.config["sheet_name"], skiprows=handler.config["skip_rows"]
    )
    row = list(dataframe.itertuples())[0]
    booking = handler.format_booking(row)
    assert booking == formatted_booking


def test_get_bookings_for_stats_admin(order_numbers, report_file):
    response = client.post("/api/airastana/", data=order_numbers, files=report_file)
    assert response.status_code == 200
    with open("tests/test_data/air_astana/test_csv_file.csv") as example_file:
        example_file_value = example_file.read()
        # removing the last character of response.text,
        # as it is a newline character
        assert example_file_value == response.text[:-1]
