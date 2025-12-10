from pydantic import BaseModel


class BodySNMP(BaseModel):
    ip: str
    community: str