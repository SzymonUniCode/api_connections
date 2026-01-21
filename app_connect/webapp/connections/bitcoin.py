from typing import List, Dict
from datetime import datetime

from webapp.connections.base import BaseConnection
from dotenv import load_dotenv
import os

load_dotenv()


class BitcoinAPI(BaseConnection):
    name = "bitcoin"

    BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

    def __init__(self):
        self.api_key = os.getenv("FRED_API_KEY")
        if not self.api_key:
            raise ValueError("FRED_API_KEY is not set in .env file")

    def fetch(self, start_date: str, end_date: str) -> List[Dict]:
        raw_data = self._get(
            self.BASE_URL,
            params={
                "series_id": "CBBTCUSD",
                "api_key": self.api_key,
                "file_type": "json",
                "observation_start": start_date,
                "observation_end": end_date,
            },
        )

        return self._mapper(raw_data)

    def _mapper(self, data: dict) -> List[Dict]:
        results = []

        for obs in data.get("observations", []):
            if obs["value"] == ".":
                continue

            results.append(
                {
                    "date": obs["date"],          # YYYY-MM-DD
                    "value": float(obs["value"]), # BTC/USD
                }
            )

        return results