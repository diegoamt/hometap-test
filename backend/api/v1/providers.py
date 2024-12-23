import asyncio

from fastapi import APIRouter, Request
from pydantic import BaseModel

import httpx
from config import settings

router = APIRouter()


async def fetch_provider_1(address: str) -> dict:
    if not address:
        return {}
    url_provider_1 = f"{settings.API_ENDPOINT_PROVIDER_1}?address={address}"
    headers = {
        "X-API-KEY": settings.X_API_KEY_PROVIDER_1
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url_provider_1, headers=headers)
        return response.json()


async def fetch_provider_2(address: str) -> dict:
    if not address:
        return {}
    url_provider_2 = f"{settings.API_ENDPOINT_PROVIDER_2}?address={address}"
    headers = {
        "X-API-KEY": settings.X_API_KEY_PROVIDER_2
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url_provider_2, headers=headers)
        return response.json()


def filter_data(data: dict) -> dict:
    invalid_values = ["none", "null", "unknown", ""]

    def is_valid_value(value):
        return not isinstance(value, (dict, list)) and value not in invalid_values

    filtered_data = {
        key: value for key, value in data.items() if is_valid_value(value)
    }

    return filtered_data


@router.get("/property-details/")
async def get_property_details(request: Request):
    query_params = dict(request.query_params)
    print(query_params)
    address = query_params["address"] if "address" in query_params else None
    print(address)
    data_provider_1, data_provider_2 = await asyncio.gather(fetch_provider_1(address), fetch_provider_2(address))
    return {
        "provider_1": data_provider_1["data"] if "data" in data_provider_1 else {},
        "provider_2": data_provider_2["data"] if "data" in data_provider_2 else {}
    }
