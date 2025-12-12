import json
from fastapi import APIRouter, HTTPException, status as StatusAPI
from fast_snmp.api.schemas.body import BodySNMPSchema
from fast_snmp.api.schemas.response import ResponseSNMPSchema
from fast_snmp.libs import Device, ZxAnServicePort
from fast_snmp.utils import Validation


SNMPRouter = APIRouter()


@SNMPRouter.post("/clients")
def clients(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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
            response_snmp = ZxAnServicePort.get_total_admin_status_up(device=server)
            data = response_snmp.to_json(orient="records")
            data = json.loads(data)[0]
        return response
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )
