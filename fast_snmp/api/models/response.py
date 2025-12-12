from pydantic import BaseModel


class ResponseSNMPModel(BaseModel):
    ip: str
    date: str
    time: str
    response: str | float | int


class ResponsePingModel(BaseModel):
    ip: str
    isAlive: bool