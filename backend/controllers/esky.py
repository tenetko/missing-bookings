import pandas as pd

from fastapi import File, Form, UploadFile
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from typing import Dict, NamedTuple

from .basic import BasicHandler

router = InferringRouter()


@cbv(router)
class EskyHandler(BasicHandler):
    NAME = "esky"

    @router.post("/")
    def get_bookings_for_stats_admin(
        self, order_numbers: str = Form(...), file: UploadFile = File(...)
    ) -> Dict:
        workbook = pd.ExcelFile(file.file.read())
        dataframe = pd.read_excel(
            workbook, self.config["sheet_name"], skiprows=self.config["skip_rows"]
        )

        for row in dataframe.itertuples():
            order_number = str(row.PackageNumber)
            currency = row.Currency
            if order_number in order_numbers:
                if not pd.isna(currency):
                    booking = self.format_booking(row)
                    self.add_booking_to_stats_admin_bookings(booking)

        filename = "stats-admin-esky.csv"
        file = self.export_to_csv_file()
        return self.return_csv_file(file, filename)

    def format_booking(self, row: NamedTuple) -> Dict:
        price = float(str(row.BasketValue).replace(",", "."))
        profit = price * self.config["profit"]

        booking = {
            "order_number": str(row.PackageNumber),
            "marker": "",
            "booked_at": str(row.Date),  # mm-dd-YY in XLSX reports
            "price": price,
            "price_currency": row.Currency,
            "profit": profit,
            "profit_currency": row.Currency,
            "state": "paid",
        }

        return booking
