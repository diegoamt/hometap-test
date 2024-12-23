from fastapi import APIRouter

import httpx

router = APIRouter()

@router.get("/property-details/")
async def get_property_details():
    url_provider_1 = "https://property-detail-api.fly.dev/provider-1/property"
    headers = {
        "X-API-KEY": "3e1a9f18-86c7-4e11-babe-4fd2c7e5e12d"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url_provider_1, headers=headers)
    print(response.status_code)
    data = response.json()
    print(data)
    return "TBD"
