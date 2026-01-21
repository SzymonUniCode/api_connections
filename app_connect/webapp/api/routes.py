from flask import Blueprint, request

from webapp.api.schema import ComparisonPayloadSchema
from webapp.api.mapper import (
    to_service_payload,
    to_schema_response_service,
)
from webapp.services.comparison_service import ComparisonService


bp = Blueprint("comparison", __name__, url_prefix="/comparison")


@bp.post("/")
def compare():
    payload = ComparisonPayloadSchema.model_validate(request.get_json())

    service_payload = to_service_payload(payload)

    service = ComparisonService()
    raw_result = service.fetch_two_sources(**service_payload)

    response = to_schema_response_service(raw_result)

    return response.model_dump(mode="json"), 200