import json
from fastapi import APIRouter, HTTPException, status as StatusAPI
from fast_snmp.api.models.body import BodySNMPModel
from fast_snmp.api.models.response import ResponseSNMPModel
from fast_snmp.libs import Device, SNMPSystem
from fast_snmp.utils import Validation


SNMPRouter = APIRouter()


@SNMPRouter.get("/sysName")
def get_sysname(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPSystem.get_sysName(device=server)
            data = response_snmp.to_json(orient="records")
            data = json.loads(data)[0]
            response.append(data)
        return response
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/sysLocation")
def get_sysname(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPSystem.get_sysLocation(device=server)
            data = response_snmp.to_json(orient="records")
            data = json.loads(data)[0]
            response.append(data)
        return response
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/sysDescr")
def get_sysname(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPSystem.get_sysDescr(device=server)
            data = response_snmp.to_json(orient="records")
            data = json.loads(data)[0]
            response.append(data)
        return response
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/sysContact")
def get_sysname(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPSystem.get_sysContact(device=server)
            data = response_snmp.to_json(orient="records")
            data = json.loads(data)[0]
            response.append(data)
        return response
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/sysUpTime")
def get_sysname(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPSystem.get_sysUpTime(device=server)
            data = response_snmp.to_json(orient="records")
            data = json.loads(data)[0]
            response.append(data)
        return response
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )
