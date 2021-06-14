# from controllers.esky import EskyHandler

from fastapi import Response
from fastapi.testclient import TestClient
from main import app

import pandas as pd

# handler = EskyHandler()
client = TestClient(app)

# def test_format_booking(formatted_booking):