from typing import Dict, List

from webapp.api.schema import (
    ComparisonPayloadSchema,
    ComparisonOutputSchema,
    DataPointSchema,
)


def to_service_payload(payload: ComparisonPayloadSchema) -> dict:
    """
    API -> Service
    """
    return {
        "source_a": payload.source_a,
        "source_b": payload.source_b,
        "start_date": payload.start_date,
        "end_date": payload.end_date,
    }


def to_schema_response_service(
    data: Dict[str, List[dict]]
) -> ComparisonOutputSchema:
    """
    Service -> API
    """
    mapped: Dict[str, List[DataPointSchema]] = {}

    for source, points in data.items():
        mapped[source] = [
            DataPointSchema(
                date=item["date"],
                value=float(item["value"]),
            )
            for item in points
        ]

    return ComparisonOutputSchema(data=mapped)