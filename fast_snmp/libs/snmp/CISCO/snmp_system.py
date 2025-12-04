import re
import pandas as pd
from datetime import timedelta
from fast_snmp.libs.server.device import Device
from fast_snmp.constants import SNMPv2MIB, HeaderResponseInterfacesSNMP, response_snmp
from fast_snmp.utils import logger, TransformSNMP


class SNMPSystem:
    @staticmethod
    def get_sysName(device: Device) -> pd.DataFrame:
        try:
            oid_type = "STRING"
            response = device.snmp(SNMPv2MIB.SYSNAME, options="-On")
            if not response:
                return pd.DataFrame(columns=response_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPv2MIB.SYSNAME,
                type_response=oid_type,
                date_time=device.date,
            )
            response = response[
                [
                    HeaderResponseInterfacesSNMP.HOST,
                    HeaderResponseInterfacesSNMP.VALUES,
                    HeaderResponseInterfacesSNMP.DATE,
                    HeaderResponseInterfacesSNMP.TIME,
                ]
            ]
            return response
        except Exception as error:
            logger.error(f"SNMP System error: Failed to obtain SysName - {error}")
            return pd.DataFrame(columns=response_snmp)

    @staticmethod
    def get_sysLocation(device: Device) -> pd.DataFrame:
        try:
            oid_type = "STRING"
            response = device.snmp(SNMPv2MIB.SYSLOCATION, options="-On")
            if not response:
                return pd.DataFrame(columns=response_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPv2MIB.SYSLOCATION,
                type_response=oid_type,
                date_time=device.date,
            )
            response = response[
                [
                    HeaderResponseInterfacesSNMP.HOST,
                    HeaderResponseInterfacesSNMP.VALUES,
                    HeaderResponseInterfacesSNMP.DATE,
                    HeaderResponseInterfacesSNMP.TIME,
                ]
            ]
            return response
        except Exception as error:
            logger.error(f"SNMP System error: Failed to obtain sysLocation - {error}")
            return None

    @staticmethod
    def get_sysDescr(device: Device) -> pd.DataFrame:
        try:
            oid_type = "STRING"
            response = device.snmp(SNMPv2MIB.SYSDESCR, options="-On")
            if not response:
                return pd.DataFrame(columns=response_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPv2MIB.SYSDESCR,
                type_response=oid_type,
                date_time=device.date,
            )
            response = response[
                [
                    HeaderResponseInterfacesSNMP.HOST,
                    HeaderResponseInterfacesSNMP.VALUES,
                    HeaderResponseInterfacesSNMP.DATE,
                    HeaderResponseInterfacesSNMP.TIME,
                ]
            ]
            return response
        except Exception as error:
            logger.error(f"SNMP System error: Failed to obtain sysDescr - {error}")
            return None

    @staticmethod
    def get_sysContact(device: Device) -> pd.DataFrame:
        try:
            oid_type = "STRING"
            response = device.snmp(SNMPv2MIB.SYSCONTACT, options="-On")
            if not response:
                return pd.DataFrame(columns=response_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPv2MIB.SYSCONTACT,
                type_response=oid_type,
                date_time=device.date,
            )
            response = response[
                [
                    HeaderResponseInterfacesSNMP.HOST,
                    HeaderResponseInterfacesSNMP.VALUES,
                    HeaderResponseInterfacesSNMP.DATE,
                    HeaderResponseInterfacesSNMP.TIME,
                ]
            ]
            return response
        except Exception as error:
            logger.error(f"SNMP System error: Failed to obtain sysContact - {error}")
            return None

    @staticmethod
    def get_sysUpTime(device: Device) -> timedelta | None:
        try:
            response = device.snmp(SNMPv2MIB.SYSUPTIME, options="-On")
            if not response:
                return pd.DataFrame(columns=response_snmp)
            value_match = re.search(r"\((\d+)\)", response)
            if not value_match:
                raise ValueError(f"Unexpected SNMP sysUptime format {response}")
            timeticks = int(value_match.group(1))
            uptime = timedelta(seconds=(timeticks / 100))
            return pd.DataFrame(
                {
                    HeaderResponseInterfacesSNMP.HOST: [device.host],
                    HeaderResponseInterfacesSNMP.VALUES: [uptime],
                    HeaderResponseInterfacesSNMP.DATE: [
                        device.date.strftime("%Y-%m-%d")
                    ],
                    HeaderResponseInterfacesSNMP.TIME: [
                        device.date.strftime("%H:%M:%S")
                    ],
                }
            )
        except Exception as error:
            logger.error(f"SNMP System error: Failed to obtain sysUpTime - {error}")
            return None
