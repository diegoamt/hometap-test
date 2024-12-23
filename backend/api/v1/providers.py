import asyncio

from fastapi import APIRouter
from pydantic import BaseModel

import httpx

router = APIRouter()

async def fetch_provider_1(address: str) -> dict:
    url_provider_1 = f"https://property-detail-api.fly.dev/provider-1/property?address={address}"
    headers = {
        "X-API-KEY": "3e1a9f18-86c7-4e11-babe-4fd2c7e5e12d"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url_provider_1, headers=headers)
        return response.json()

async def fetch_provider_2(address: str) -> dict:
    url_provider_2 = "https://property-detail-api.fly.dev/provider-2/property?address={address}"
    headers = {
        "X-API-KEY": "9f3b5c32-77a4-423c-b63f-90c123e6c1a8"
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

class ProviderRequest(BaseModel):
    address: str

@router.post("/property-details/")
async def get_property_details(request: ProviderRequest):
    address = request.address
    data_provider_1, data_provider_2 = await asyncio.gather(fetch_provider_1(address), fetch_provider_2(address))
    return {
        "provider_1": filter_data(data_provider_1["data"]),
        "provider_2": filter_data(data_provider_2["data"])
    }
