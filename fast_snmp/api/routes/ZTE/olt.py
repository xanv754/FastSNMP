import json
from fastapi import APIRouter, HTTPException, status as StatusAPI
from fast_snmp.libs import Device, ZxAnServicePort
from fast_snmp.utils import Validation


SNMPRouter = APIRouter()


@SNMPRouter.get("/clients")
def clients(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = ZxAnServicePort.get_total_admin_status_up(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )
