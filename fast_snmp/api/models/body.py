from pydantic import BaseModel


class BodySNMPModel(BaseModel):
    ip: str
    community: str