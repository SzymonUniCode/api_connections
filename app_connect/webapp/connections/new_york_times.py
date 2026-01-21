from collections import defaultdict
from datetime import datetime
from typing import List, Dict
import os
import time

from dotenv import load_dotenv
from webapp.connections.base import BaseConnection

load_dotenv()


class NewYorkTimesArchiveAPI(BaseConnection):
    name = "new_york_times_archive"

    BASE_URL = "https://api.nytimes.com/svc/archive/v1"

    def __init__(self):
        self.api_key = os.getenv("NY_TIMES_KEY")
        if not self.api_key:
            raise ValueError("NY_TIMES_KEY is not set")

    def fetch(self, start_date: str, end_date: str) -> List[Dict]:
        """
        start_date, end_date: YYYY-MM-DD
        """

        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        counter = defaultdict(int)

        year = start.year
        month = start.month

        while (year, month) <= (end.year, end.month):
            raw = self._get(
                f"{self.BASE_URL}/{year}/{month}.json",
                params={"api-key": self.api_key},
            )

            self._mapper(raw, counter)

            # ⬅️ szanujemy API
            time.sleep(1)

            # przejście do kolejnego miesiąca
            if month == 12:
                year += 1
                month = 1
            else:
                month += 1

        return [
            {"date": date, "value": value}
            for date, value in sorted(counter.items())
            if start_date <= date <= end_date
        ]

    def _mapper(self, data: dict, counter: defaultdict) -> None:
        docs = data.get("response", {}).get("docs", [])

        for doc in docs:
            pub_date = doc.get("pub_date")
            if not pub_date:
                continue

            date = pub_date[:10]  # YYYY-MM-DD

            # interesuje nas tylko słowo "president"
            text = (
                (doc.get("abstract") or "") +
                (doc.get("snippet") or "") +
                (doc.get("headline", {}).get("main") or "")
            ).lower()

            if "president" in text:
                counter[date] += 1