from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from app.utils.external_api import get_convert, get_list
from app.api.models.currency import Convert
from app.core.security import get_user_from_token, get_user_from_db

router = APIRouter(prefix="/currency")


@router.get("/convert")
def convert_currency(from_currency: str, to_currency: str, amount: float, current_user: Annotated[str, Depends(get_user_from_token)]):
    user = get_user_from_db(current_user)
    if user is None:
        raise HTTPException(status_code=403,
                            detail="Not authorized",
                            headers={"WWW-Authenticate": "Bearer"}
                            )
    return get_convert(Convert(amount=amount, from_currency=from_currency, to_currency=to_currency))


@router.get("/list")
def currency_list(current_user: Annotated[str, Depends(get_user_from_token)]):
    user = get_user_from_db(current_user)
    if user is None:
        raise HTTPException(status_code=403,
                            detail="Not authorized",
                            headers={"WWW-Authenticate": "Bearer"}
                            )
    return get_list()
