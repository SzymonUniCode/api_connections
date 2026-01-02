from abc import ABC, abstractmethod
from typing import List, Dict
import requests


class BaseConnection(ABC):
    name: str  # for example. "bitcoin", "weather"

    # method which is must have to operate any API connection. It will return data for a final result
    @abstractmethod
    def fetch(self, start_date: str, end_date: str) -> List[Dict]:
        raise NotImplementedError

    # method which is used to map raw data from API to a standard format
    @abstractmethod
    def _mapper(self, data: dict) -> List[Dict]:
        raise NotImplementedError


    # method which is used to perform HTTP GET requests with common logic and return raw data
    def _get(self, url: str, params: dict | None = None) -> dict:
        """
        Wspólna metoda do wykonywania zapytań HTTP GET.
        """
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
