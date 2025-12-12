import json
from fastapi import APIRouter, HTTPException, status as StatusAPI
from fast_snmp.libs import Device, SNMPIF
from fast_snmp.utils import Validation


SNMPRouter = APIRouter()


@SNMPRouter.get("/ifIndex")
def get_ifIndex(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifIndex(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifNumber")
def get_ifNumber(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifNumber(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifName")
def get_ifNumber(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifName(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifAlias")
def get_ifNumber(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifAlias(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifDescr")
def get_ifNumber(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifDescr(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifHighSpeed")
def get_ifHighSpeed(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifHighSpeed(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifAdminStatus")
def get_ifAdminStatus(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifAdminStatus(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifOperStatus")
def get_ifOperStatus(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifOperStatus(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifCounterDiscontinuityTime")
def get_ifCounterDiscontinuityTime(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifCounterDiscontinuityTime(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifHCInOctets")
def get_ifHCInOctets(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifHCInOctets(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifHCInUcastPkts")
def get_ifHCInUcastPkts(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifHCInUcastPkts(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifHCInMulticastPkts")
def get_ifHCInMulticastPkts(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifHCInMulticastPkts(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifHCInBroadcastPkts")
def get_ifHCInBroadcastPkts(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifHCInBroadcastPkts(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifInErrors")
def get_ifInErrors(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifInErrors(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifInDiscards")
def get_ifInDiscards(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifInDiscards(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifHCOutOctets")
def get_ifHCOutOctets(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifHCOutOctets(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifHCOutUcastPkts")
def get_ifHCOutUcastPkts(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifHCOutUcastPkts(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifHCOutMulticastPkts")
def get_ifHCOutMulticastPkts(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifHCOutMulticastPkts(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifHCOutBroadcastPkts")
def get_ifHCOutBroadcastPkts(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifHCOutBroadcastPkts(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifOutErrors")
def get_ifOutErrors(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifOutErrors(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )


@SNMPRouter.get("/ifOutDiscards")
def get_ifOutDiscards(host: str, community: str):
    try:
        if not Validation.ip(host):
            raise HTTPException(
                status_code=StatusAPI.HTTP_400_BAD_REQUEST,
                detail="Invalid IP format",
            )
        server = Device()
        server.set_configuration()
        server.set_credentials(host=host, community=community)
        response = SNMPIF.get_ifOutDiscards(device=server)
        data = response.to_json(orient="records")
        return json.loads(data)
    except HTTPException:
        raise
    except:
        raise HTTPException(
            status_code=StatusAPI.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ups... Something went wrong. Please try again later",
        )
