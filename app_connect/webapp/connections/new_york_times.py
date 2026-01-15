from collections import defaultdict
from typing import List, Dict

from webapp.connections.base import BaseConnection

from dotenv import load_dotenv
import os

load_dotenv()


class NewYorkTimesAPI(BaseConnection):
    name = "new_york_times"

    BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

    def __init__(self):
        self.api_key = os.getenv("NY_TIMES_KEY")

        if not self.api_key:
            raise ValueError("NY_TIMES_KEY is not set in .env file")


    # date is in string version -> RRRRMMDD -> 20211231
    def fetch(
        self,
        start_date: str,
        end_date: str,
    ) -> List[Dict]:

        result = []

        for page in range(0, 100):

            raw_data = self._get(
                self.BASE_URL,
                params={
                    "begin_date": start_date,
                    "end_date": end_date,
                    "q": "president",
                    "sort": "oldest",
                    "api-key": self.api_key,
                    "page": page
                }
            )

            mapped = self._mapper(raw_data)
            if not mapped:
                break

            result.extend(mapped)

        return result



    def _mapper(self, data: dict) -> List[Dict]:
        docs = data.get("response", {}).get("docs", [])
        counter = defaultdict(int)

        for doc in docs:
            # pub_date: "2023-01-01T12:34:56+0000"
            date = doc["pub_date"][:10]  # YYYY-MM-DD
            counter[date] += 1

        return [
            {"date": date, "value": count}
            for date, count in sorted(counter.items())
        ]