from typing import List, Dict
from datetime import datetime

from .base import BaseConnection
from dotenv import load_dotenv
import os

load_dotenv()


class BitcoinAPI(BaseConnection):
    name = "bitcoin"

    BASE_URL = "https://api.massive.com/v2/aggs/ticker/X:BTCUSD"

    def __init__(self):
        self.api_key = os.getenv("BTC_API_KEY")

        if not self.api_key:
            raise ValueError("BASE_URL_BTC is not set in .env file")


    def fetch(
        self,
        start_date: str,
        end_date: str,
        timespan: str = "day",
        multiplier: int = 1,
    ) -> List[Dict]:


        url = (
            f"{self.BASE_URL}/range/"
            f"{multiplier}/{timespan}/{start_date}/{end_date}"
        )

        raw_data = self._get(
            url,
            params={"apiKey": self.api_key},
        )

        return self._mapper(raw_data)

    def _mapper(self, data: dict) -> List[Dict]:
        results = data.get("results", [])

        mapped = []
        for item in results:
            mapped.append(
                {
                    "date": datetime.utcfromtimestamp(item["t"] / 1000).date().isoformat(),
                    "value": float(item["c"])
                }
            )

        return mapped