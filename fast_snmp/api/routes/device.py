from fastapi import APIRouter, HTTPException, status as StatusAPI
from fast_snmp.api.models.body import BodySNMPModel
from fast_snmp.api.models.response import ResponsePingModel
from fast_snmp.libs import Device
from fast_snmp.utils import Validation


SNMPRouter = APIRouter()


@SNMPRouter.get("/ping")
def ping(devices: list[BodySNMPModel]) -> list[ResponsePingModel]:
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
            server.set_credentials(host=device.ip, community=device.community)
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
