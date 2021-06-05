import io
import pandas as pd

from fastapi import File, Form, Response, UploadFile
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from typing import Dict, NamedTuple

from .basic import BasicHandler

router = InferringRouter()


@cbv(router)
class AirAstanaHandler(BasicHandler):
    NAME = "air_astana"

    def __init__(self):
        self.config_name = self.NAME
        super().__init__()

        self.stats_admin_bookings = {}

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

    def add_booking_to_stats_admin_bookings(self, booking: Dict) -> None:
        pnr = booking["pnr"]
        if pnr not in self.stats_admin_bookings:
            self.stats_admin_bookings[pnr] = booking
        else:
            price = booking["price"]
            existing_record = self.stats_admin_bookings[pnr]
            new_price = existing_record["price"] + price
            new_profit = new_price * self.config["profit"]
            booking["price"] = new_price
            booking["profit"] = new_profit
            self.stats_admin_bookings[pnr] = booking

    def export_to_csv_file(self):
        output = io.StringIO()

        csv_header = (
            "order_number,booked_at,marker,price,price_currency,profit,"
            "profit_currency,state\n"
        )
        output.write(csv_header)

        bookings = self.stats_admin_bookings
        for pnr in bookings:
            booking = bookings[pnr]
            row = (
                f"{pnr},{booking['booked_at']},{booking['marker']},{booking['price']},"
                f"{booking['price_currency']},{booking['profit']},"
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