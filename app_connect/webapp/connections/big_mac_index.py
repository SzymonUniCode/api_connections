from typing import List, Dict
from datetime import date

from webapp.connections.base import BaseConnection


class BigMacIndex(BaseConnection):
    name = "big_mac"

    BASE_URL = (
        "https://raw.githubusercontent.com/"
        "TheEconomist/big-mac-data/master/"
        "output-data/big-mac-full-index.json"
    )

    def __init__(self, country: str):
        self.country = country

    def fetch(self, start_date: date, end_date: date) -> List[Dict]:
        raw_data = self._get(self.BASE_URL)

        mapped = self._mapper(raw_data)

        return [
            item
            for item in mapped
            if start_date <= item["date"] <= end_date
        ]

    def _mapper(self, data: dict) -> List[Dict]:
        result = []

        for row in data:
            if row["country"] != self.country:
                continue

            result.append(
                {
                    "date": row["date"],              # YYYY-MM-DD
                    "value": float(row["local"]),     # Big Mac price (float)
                }
            )

        return result