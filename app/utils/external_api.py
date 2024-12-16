import requests
from fastapi import HTTPException
from app.core.config import settings
from app.api.models.currency import Convert


BASE_URL = "https://api.apilayer.com/currency_data"
headers = {"apikey": settings.API_KEY}



def get_convert(convert_pare: Convert):
    response = requests.get(url=BASE_URL + "/convert", headers=headers, params={
        "from": convert_pare.from_currency,
        "to": convert_pare.to_currency,
        "amount": convert_pare.amount})
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=400, detail="Неправильный код валюты")



def get_list():
    response = requests.get(url=BASE_URL + "/list", headers=headers)
    if response.status_code != 200:
        raise "Не удалось получить список валют."
    data = response.json()
    currencies = data.get("currencies", {})
    return currencies