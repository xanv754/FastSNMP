from pydantic import BaseModel


class ResponseSNMPSchema(BaseModel):
    ip: str
    date: str
    time: str
    response: str | float | int


class ResponsePingSchema(BaseModel):
    ip: str
    isAlive: bool