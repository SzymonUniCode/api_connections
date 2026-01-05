from webapp.connections.car_sales import CarSalesAPI

def main() -> None:
    api = CarSalesAPI()

    data = api.fetch("2023-01-31", "2023-12-31")

    print(data[:10])

if __name__ == "__main__":
    main()