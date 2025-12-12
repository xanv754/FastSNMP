from pydantic import BaseModel


class BodySNMPSchema(BaseModel):
    ip: str
    community: str

class BodyPingSchema(BaseModel):
    ip: str