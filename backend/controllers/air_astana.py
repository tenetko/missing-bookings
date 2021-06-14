import pandas as pd

from fastapi import File, Form, UploadFile
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from typing import Dict, NamedTuple

from .basic import BasicHandler

router = InferringRouter()


@cbv(router)
class AirAstanaHandler(BasicHandler):
    NAME = "air_astana"

    @router.post("/")
    def get_bookings_for_stats_admin(
        self, order_numbers: str = Form(...), file: UploadFile = File(...)
    ) -> Dict:
        workbook = pd.ExcelFile(file.file.read())
        dataframe = pd.read_excel(
            workbook, self.config["sheet_name"], skiprows=self.config["skip_rows"]
        )
        for row in dataframe.itertuples():
            pnr = row.PNR
            if pnr in order_numbers:
                booking = self.format_booking(row)
                self.add_booking_to_stats_admin_bookings(booking)

        filename = "stats-admin-air-astana.csv"
        file = self.export_to_csv_file()
        return self.return_csv_file(file, filename)

    def format_booking(self, row: NamedTuple) -> Dict:
        price = float(row[7])
        profit = self.config["profit"]
        booking = {
            "pnr": row[3],
            "marker": row[5],
            "booked_at": str(row[4]),  # mm-dd-YY in XLSX reports
            "price": price,
            "price_currency": row.Currency,
            "profit": price * profit,
            "profit_currency": row.Currency,
            "state": "paid",
        }

        return booking