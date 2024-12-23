# FastAPI

This application provides an endpoint `"/api/v1/property-details/"` that returns a subset of property data pulled from two automated valuation model (AVM) providers.

## Setup

1. Install python env (venv). You should have installed Python 3.8+:
`python3 -m venv env`

2. Activate env:
`source env/bin/activate`

3. Install dependencies:
`pip install -r requirements.txt`

## Environment variables

1. Create the `.env` file following .env.example

```
    API_ENDPOINT_PROVIDER_1=

    X_API_KEY_PROVIDER_1=

    API_ENDPOINT_PROVIDER_2=

    X_API_KEY_PROVIDER_2=
```
## Development

1. Run project: `uvicorn main:app --reload`

2. Go to `http://localhost:8000/api/v1/property-details/`
