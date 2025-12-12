from fastapi import APIRouter, HTTPException, status as StatusAPI
from fast_snmp.api.schemas.body import BodyPingSchema
from fast_snmp.api.schemas.response import ResponsePingSchema
from fast_snmp.libs import Device
from fast_snmp.utils import Validation


SNMPRouter = APIRouter()


@SNMPRouter.post("/ping")
def ping(devices: list[BodyPingSchema]) -> list[ResponsePingSchema]:
    try:
        response: list = []
        for device in devices:
            if not Validation.ip(device.ip):
                raise HTTPException(
                    status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                    detail="Invalid IP format",
                )
            server = Device()
            server.set_configuration()
            server.set_credentials(host=device.ip)
            response_ping = server.ping()
            data = {"ip": device.ip, "isAlive": response_ping}
            response.append(data)
        return response
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )
