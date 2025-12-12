import json
from fastapi import APIRouter, HTTPException, status as StatusAPI
from fast_snmp.api.models.body import BodySNMPModel
from fast_snmp.api.models.response import ResponseSNMPModel
from fast_snmp.libs import Device, SNMPIF
from fast_snmp.utils import Validation


SNMPRouter = APIRouter()


@SNMPRouter.get("/ifIndex")
def get_ifIndex(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifIndex(device=server)
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


@SNMPRouter.get("/ifNumber")
def get_ifNumber(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifNumber(device=server)
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


@SNMPRouter.get("/ifName")
def get_ifNumber(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifName(device=server)
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


@SNMPRouter.get("/ifAlias")
def get_ifNumber(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifAlias(device=server)
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


@SNMPRouter.get("/ifDescr")
def get_ifNumber(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifDescr(device=server)
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


@SNMPRouter.get("/ifHighSpeed")
def get_ifHighSpeed(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifHighSpeed(device=server)
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


@SNMPRouter.get("/ifAdminStatus")
def get_ifAdminStatus(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifAdminStatus(device=server)
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


@SNMPRouter.get("/ifOperStatus")
def get_ifOperStatus(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifOperStatus(device=server)
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


@SNMPRouter.get("/ifCounterDiscontinuityTime")
def get_ifCounterDiscontinuityTime(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifCounterDiscontinuityTime(device=server)
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


@SNMPRouter.get("/ifHCInOctets")
def get_ifHCInOctets(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifHCInOctets(device=server)
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


@SNMPRouter.get("/ifHCInUcastPkts")
def get_ifHCInUcastPkts(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifHCInUcastPkts(device=server)
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


@SNMPRouter.get("/ifHCInMulticastPkts")
def get_ifHCInMulticastPkts(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifHCInMulticastPkts(device=server)
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


@SNMPRouter.get("/ifHCInBroadcastPkts")
def get_ifHCInBroadcastPkts(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifHCInBroadcastPkts(device=server)
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


@SNMPRouter.get("/ifInErrors")
def get_ifInErrors(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifInErrors(device=server)
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


@SNMPRouter.get("/ifInDiscards")
def get_ifInDiscards(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifInDiscards(device=server)
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


@SNMPRouter.get("/ifHCOutOctets")
def get_ifHCOutOctets(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifHCOutOctets(device=server)
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


@SNMPRouter.get("/ifHCOutUcastPkts")
def get_ifHCOutUcastPkts(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifHCOutUcastPkts(device=server)
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


@SNMPRouter.get("/ifHCOutMulticastPkts")
def get_ifHCOutMulticastPkts(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifHCOutMulticastPkts(device=server)
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


@SNMPRouter.get("/ifHCOutBroadcastPkts")
def get_ifHCOutBroadcastPkts(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifHCOutBroadcastPkts(device=server)
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


@SNMPRouter.get("/ifOutErrors")
def get_ifOutErrors(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifOutErrors(device=server)
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


@SNMPRouter.get("/ifOutDiscards")
def get_ifOutDiscards(devices: list[BodySNMPModel]) -> list[ResponseSNMPModel]:
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
            response_snmp = SNMPIF.get_ifOutDiscards(device=server)
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
