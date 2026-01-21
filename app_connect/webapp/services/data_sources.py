from webapp.connections.bitcoin import BitcoinAPI
from webapp.connections.car_sales import CarSalesAPI
from webapp.connections.big_mac_index import BigMacIndex
from webapp.connections.new_york_times import NewYorkTimesArchiveAPI

DATA_SOURCES = {
    "car_sales": CarSalesAPI,
    "big_mac": BigMacIndex,
    "new_york_times": NewYorkTimesArchiveAPI,
    "bitcoin": BitcoinAPI
}