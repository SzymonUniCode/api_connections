from webapp.connections.bitcoin import BitcoinAPI

def main():
    api = BitcoinAPI()
    data = api.fetch("2023-01-01", "2023-01-10")
    print(data)

if __name__ == "__main__":
    main()