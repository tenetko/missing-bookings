import pandas as pd

from fastapi import File, Form, UploadFile
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from typing import Dict

from .basic import BasicHandler

router = InferringRouter()


@cbv(router)
class AirAstanaHandler(BasicHandler):
    NAME = "air_astana"

    @router.post("/")
    def get_bookings_for_stats_admin(
        self,
        order_numbers: str = Form(...),
        sheet_number: str = Form(...),
        file: UploadFile = File(...),
    ) -> Dict:
        workbook = pd.ExcelFile(file.file.read())
        sheet_number = int(sheet_number) - 1
        dataframe = pd.read_excel(
            workbook,
            sheet_name=sheet_number,
            engine="openpyxl",
            skiprows=self.get_empty_rows_number(workbook, sheet_number),
        )
        for _, row in dataframe.iterrows():
            order_number = str(row["PNR"])
            if order_number in order_numbers:
                booking = self.format_booking(row)
                self.add_booking_to_stats_admin_bookings(booking)

        filename = "stats-admin-air-astana.csv"
        file = self.export_to_csv_file()
        return self.return_csv_file(file, filename)

    def format_booking(self, row: pd.Series) -> Dict:
        price = float(row["Total Value"])
        profit = price * self.config["profit"]
        booking = {
            "order_number": str(row["PNR"]),
            "marker": row["Marker ID"],
            "booked_at": str(row["Date of issue "]),  # mm-dd-YY in XLSX reports
            "price": price,
            "price_currency": row["Currency"],
            "profit": profit,
            "profit_currency": row["Currency"],
            "state": "paid",
        }

        return booking