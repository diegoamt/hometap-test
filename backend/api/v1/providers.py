import asyncio

from fastapi import APIRouter, Request
from pydantic import BaseModel

import httpx
from config import settings

router = APIRouter()

RELEVANT_KEYS = [
    "Normalized_Address",
    "Square_Footage",
    "Lot_Size_(Acres)",
    "Year_Built",
    "Property_Type",
    "Bedrooms",
    "Bathrooms",
    "Room_Count",
    "Septic_System",
    "Sale_Price"
]

STANDARD_KEY_MAPPING = {
    "formattedAddress": "Normalized_Address",
    "NormalizedAddress": "Normalized_Address",
    "SquareFootage": "Square_Footage",
    "squareFootage": "Square_Footage",
    "LotSizeAcres": "Lot_Size_(Acres)",
    "YearConstructed": "Year_Built",
    "yearBuilt": "Year_Built",
    "PropertyType": "Property_Type",
    "propertyType": "Property_Type",
    "bedrooms": "Bedrooms",
    "bathrooms": "Bathrooms",
    "RoomCount": "Room_Count",
    "SepticSystem": "Septic_System",
    "SalePrice": "Sale_Price",
    "lastSalePrice": "Sale_Price"
}

def standardize_data(data: dict) -> dict:
    if "lotSizeSqFt" in data:
        data["Lot_Size_(Acres)"] = convert_feet_to_acres(data["lotSizeSqFt"])
    return {STANDARD_KEY_MAPPING.get(key, key): value for key, value in data.items()}

def convert_feet_to_acres(value) -> float:
    print(type(value))
    if value:
        return round(value / 43560, 2)
    else:
        return 0

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


def format_data(data: dict) -> dict:
    invalid_values = ["none", "null", "unknown", ""]
    standardized_data = standardize_data(data)

    def format_value(value):
        return "data not found" if value in invalid_values else value

    filtered_data = {
        key: format_value(value) for key, value in standardized_data.items() if key in RELEVANT_KEYS
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
        "provider_1": format_data(data_provider_1["data"]) if "data" in data_provider_1 else {},
        "provider_2": format_data(data_provider_2["data"]) if "data" in data_provider_2 else {}
    }
