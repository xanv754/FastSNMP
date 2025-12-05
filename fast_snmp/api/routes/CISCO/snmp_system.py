import json
from fastapi import APIRouter, HTTPException, status as StatusAPI
from fast_snmp.libs import Device, SNMPSystem
from fast_snmp.utils import Validation


SNMPRouter = APIRouter()


@SNMPRouter.get("/sysName")
def get_sysname(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device(host=host, community=community)
        response = SNMPSystem.get_sysName(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later"
        )
        
@SNMPRouter.get("/sysLocation")
def get_sysname(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device(host=host, community=community)
        response = SNMPSystem.get_sysLocation(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later"
        )
        
@SNMPRouter.get("/sysDescr")
def get_sysname(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device(host=host, community=community)
        response = SNMPSystem.get_sysDescr(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later"
        )
        
@SNMPRouter.get("/sysContact")
def get_sysname(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device(host=host, community=community)
        response = SNMPSystem.get_sysContact(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later"
        )
        
@SNMPRouter.get("/sysUpTime")
def get_sysname(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device(host=host, community=community)
        response = SNMPSystem.get_sysUpTime(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later"
        )