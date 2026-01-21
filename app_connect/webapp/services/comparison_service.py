from typing import Dict, List
from webapp.services.data_sources import DATA_SOURCES

class ComparisonService:
    def fetch_two_sources(
            self,
            source_a: str,
            source_b: str,
            start_date: str,
            end_date: str
    ) -> Dict[str, List[Dict]]:

        if source_a not in DATA_SOURCES or source_b not in DATA_SOURCES:
            raise ValueError("Invalid data source")

        api_a = DATA_SOURCES[source_a]()
        api_b = DATA_SOURCES[source_b]()

        data_a = api_a.fetch(start_date, end_date)
        data_b = api_b.fetch(start_date, end_date)

        return {source_a: data_a, source_b: data_b}
