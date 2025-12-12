import json
from fastapi import APIRouter, HTTPException, status as StatusAPI
from fast_snmp.api.schemas.body import BodySNMPSchema
from fast_snmp.api.schemas.response import ResponseSNMPSchema
from fast_snmp.libs import Device, SNMPIF
from fast_snmp.utils import Validation


SNMPRouter = APIRouter()


@SNMPRouter.post("/ifIndex")
def get_ifIndex(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifNumber")
def get_ifNumber(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifName")
def get_ifNumber(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifAlias")
def get_ifNumber(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifDescr")
def get_ifNumber(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifHighSpeed")
def get_ifHighSpeed(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifAdminStatus")
def get_ifAdminStatus(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifOperStatus")
def get_ifOperStatus(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifCounterDiscontinuityTime")
def get_ifCounterDiscontinuityTime(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifHCInOctets")
def get_ifHCInOctets(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifHCInUcastPkts")
def get_ifHCInUcastPkts(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifHCInMulticastPkts")
def get_ifHCInMulticastPkts(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifHCInBroadcastPkts")
def get_ifHCInBroadcastPkts(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifInErrors")
def get_ifInErrors(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifInDiscards")
def get_ifInDiscards(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifHCOutOctets")
def get_ifHCOutOctets(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifHCOutUcastPkts")
def get_ifHCOutUcastPkts(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifHCOutMulticastPkts")
def get_ifHCOutMulticastPkts(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifHCOutBroadcastPkts")
def get_ifHCOutBroadcastPkts(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifOutErrors")
def get_ifOutErrors(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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


@SNMPRouter.post("/ifOutDiscards")
def get_ifOutDiscards(devices: list[BodySNMPSchema]) -> list[ResponseSNMPSchema]:
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
