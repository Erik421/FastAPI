import requests
from fastapi import HTTPException
from app.core.config import settings
from app.api.models.currency import Convert


BASE_URL = "https://apilayer.com/marketplace/currency_data"


def get_convert(convert_pare: Convert):
    response = requests.get(BASE_URL + "/convert", params={
        "from": convert_pare.from_currency,
        "to": convert_pare.to_currency,
        "amount": convert_pare.amount,
        "api_key": settings.API_KEY})
    if response.status_code == 200:
        return response.json()["response"]["value"]
    else:
        raise HTTPException(status_code=400, detail="Bad currency code")


def get_list():
    response = requests.get(BASE_URL + "/latest", params={"api_key": settings.API_KEY})
    if response.status_code == 200:
        return response.json()
    else:
        return None