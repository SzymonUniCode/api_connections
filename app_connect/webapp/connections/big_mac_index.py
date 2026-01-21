import csv
import io
from typing import List, Dict

from webapp.connections.base import BaseConnection


class BigMacIndex(BaseConnection):
    name = "big_mac"

    BASE_URL = (
        "https://raw.githubusercontent.com/"
        "TheEconomist/big-mac-data/master/"
        "output-data/big-mac-full-index.csv"
    )

    def __init__(self, country: str = "United States"):
        self.country = country

    def fetch(self, start_date: str, end_date: str) -> List[Dict]:
        raw_csv = self._get(self.BASE_URL, raw=True)

        mapped = self._mapper(raw_csv)

        return [
            item
            for item in mapped
            if start_date <= item["date"] <= end_date
        ]

    def _mapper(self, raw_csv: str) -> List[Dict]:
        reader = csv.DictReader(io.StringIO(raw_csv))

        result: List[Dict] = []

        for row in reader:
            # kraj w CSV to kolumna "name"
            if row["name"] != self.country:
                continue

            result.append(
                {
                    "date": row["date"],                     # YYYY-MM-DD
                    "value": float(row["local_price"]),      # cena Big Maca
                }
            )

        return result