from controllers.basic import BasicHandler
from tests.fixtures.basic import *
from fastapi import Response

handler = BasicHandler()


def test_get_config():
    assert handler.config["name"] == "test"
    assert handler.config["profit"] == 0.025


def test_add_new_booking_to_stats_admin_bookings(booking):
    handler.stats_admin_bookings = {}

    handler.add_booking_to_stats_admin_bookings(booking)
    booking_after_changes = handler.stats_admin_bookings["AAAAAA"]
    assert booking_after_changes["price"] == 60000.00
    assert booking_after_changes["profit"] == 60000.00 * 0.025


def test_add_existing_booking_to_stats_admin_bookings(stats_admin_bookings, booking):
    handler.stats_admin_bookings = stats_admin_bookings

    handler.add_booking_to_stats_admin_bookings(booking)
    booking_after_changes = handler.stats_admin_bookings["AAAAAA"]
    assert booking_after_changes["price"] == 60000 + 40000
    assert booking_after_changes["profit"] == (60000 + 40000) * 0.025


def test_export_to_csv_file(stats_admin_bookings):
    handler.stats_admin_bookings = stats_admin_bookings
    with open("tests/test_data/basic/test_csv_file.csv") as example_file:
        example_file_value = example_file.read()
        exported_file = handler.export_to_csv_file()
        exported_file_value = exported_file.getvalue()
        # removing the last character of exported_file_value,
        # as it is a newline character
        assert example_file_value == exported_file_value[:-1]


def test_return_csv_file(stats_admin_bookings):
    handler.stats_admin_bookings = stats_admin_bookings
    exported_file = handler.export_to_csv_file()
    exported_file_name = "stats-admin-basic.csv"

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
