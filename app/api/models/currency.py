from pydantic import BaseModel


class Convert(BaseModel):
    from_currency: str
    to_currency: str
    amount: str
