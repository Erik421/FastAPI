from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from app.utils.external_api import get_convert, get_list
from app.api.models.currency import Convert
from app.core.security import get_user_from_token, get_user_from_db

router = APIRouter()


@router.get("/currency/exchange")
def convert_currency(from_currency: str, to_currency: str, amount: str, current_user: Annotated[str, Depends(get_user_from_token)]):
    user = get_user_from_db(current_user)
    if user is None:
        raise HTTPException(status_code=403, detail="Not authorized")
    return get_convert(Convert(from_currency=from_currency, to_currency=to_currency, amount=amount))


@router.get("/currency/list")
def currency_list(current_user: Annotated[str, Depends(get_user_from_token)]):
    user = get_user_from_db(current_user)
    if user is None:
        raise HTTPException(status_code=403, detail="Not authorized")
    return get_list()
