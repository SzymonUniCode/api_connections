from webapp.services.comparison_service import ComparisonService


def main():
    service = ComparisonService()

    result = service.fetch_two_sources(
        source_a="big_mac",
        source_b="bitcoin",   # albo "new_york_times"
        start_date="2020-01-01",
        end_date="2023-12-31",
    )

    print("\n=== BIG MAC ===")
    print("Records:", len(result["big_mac"]))
    print(result["big_mac"][:5])

    print("\n=== BITCOION ===")
    print("Records:", len(result["bitcoin"]))
    print(result["bitcoin"][:5])


if __name__ == "__main__":
    main()