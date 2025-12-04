from fastapi import APIRouter, HTTPException, status as StatusAPI
from fast_snmp.libs import Device
from fast_snmp.utils import Validation


SNMPRouter = APIRouter()


@SNMPRouter.get("/ping")
def ping(host: str, community: str) -> dict[str, str | bool]:
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device(host=host, community=community)
        response = server.ping()
        return {
            "IP": host,
            "isAlive": response
        }
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later"
        )
