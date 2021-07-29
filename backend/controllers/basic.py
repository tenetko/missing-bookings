import io
import pandas as pd

from fastapi import Response
from json import load
from os.path import abspath
from typing import Any, Dict


class BasicHandler:
    NAME = "basic"

    def __init__(self):
        self.config_name = self.NAME
        self.config = self.get_config(self.config_name)
        self.stats_admin_bookings = {}

    def get_config(self, name: str) -> Dict:
        with open(abspath(f"configs/{name}.json"), "r", encoding="utf-8") as input_file:
            return load(input_file)

    def export_to_csv_file(self):
        output = io.StringIO()

        csv_header = (
            "order_number,booked_at,marker,price,price_currency,profit,"
            "profit_currency,state\n"
        )
        output.write(csv_header)

        bookings = self.stats_admin_bookings
        for order_number in bookings:
            booking = bookings[order_number]
            row = (
                f"{order_number},{booking['booked_at']},{booking['marker']},"
                f"{booking['price']},{booking['price_currency']},{booking['profit']},"
                f"{booking['profit_currency']},{booking['state']}\n"
            )
            output.write(row)

        output.seek(0)
        output.close

        return output

    def return_csv_file(self, file, filename):
        return Response(
            content=file.read(),
            media_type="text/csv",
            headers={
                "Access-Control-Expose-Headers": "Content-Disposition",
                "Content-Disposition": f"attachment; filename={filename}",
            },
        )

    def get_bookings_for_stats_admin(self, order_numbers: str) -> Dict:
        raise NotImplementedError

    def format_booking(self, row: Any) -> Dict:
        raise NotImplementedError

    def add_booking_to_stats_admin_bookings(self, booking: Dict) -> None:
        order_number = booking["order_number"]
        if order_number not in self.stats_admin_bookings:
            self.stats_admin_bookings[order_number] = booking
        else:
            price = booking["price"]
            existing_record = self.stats_admin_bookings[order_number]
            new_price = existing_record["price"] + price
            new_profit = new_price * self.config["profit"]
            booking["price"] = new_price
            booking["profit"] = new_profit
            self.stats_admin_bookings[order_number] = booking

    def get_empty_rows_number(self, workbook: pd.ExcelFile, sheet_number: int) -> int:
        # The number of empty rows in partner's report is inconsistent.
        # This method checks first 10 rows in dataframe (including a header row)
        # and tries to determine how many empty rows should be skipped.
        dataframe = pd.read_excel(
            workbook, header=None, sheet_name=sheet_number, engine="openpyxl"
        )
        for i in range(3):
            row_first_item = dataframe.iloc[i][0]
            if pd.isnull(row_first_item):
                continue
            else:
                return i