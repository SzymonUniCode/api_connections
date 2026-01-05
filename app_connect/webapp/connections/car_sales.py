from typing import List, Dict

from webapp.connections.base import BaseConnection
from dotenv import load_dotenv
import os

load_dotenv()

class CarSalesAPI(BaseConnection):
    name = "car_sales"

    BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

    def __init__(self):
        self.api_key = os.getenv("FRED_API_KEY")


    def fetch(self, start_date: str, end_date: str) -> List[Dict]:

        raw_data = self._get(
            self.BASE_URL,
            params={
                "series_id": "TOTALSA",
                "api_key": self.api_key,
                "file_type": "json",
                "observation_start": start_date,
                "observation_end": end_date,
                "frequency": "m"
            }
        )

        return self._mapper(raw_data)

    def _mapper(self, data: dict) -> List[Dict]:
        result = []

        for obs in data["observations"]:
            annual_rate_mln = float(obs["value"])
            monthly = annual_rate_mln * 1_000_000 / 12

            result.append({
                "date": obs["date"],
                "value": round(monthly, 2)
            })

        return result