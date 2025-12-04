import pandas as pd
from fast_snmp.libs.server.device import Device
from fast_snmp.constants import (
    SNMPIF_MIB,
    HeaderResponseInterfacesSNMP,
    response_interface_snmp,
    response_snmp,
)
from fast_snmp.utils import logger, TransformSNMP


class SNMPIF:
    @staticmethod
    def get_ifIndex(device: Device) -> pd.DataFrame:
        try:
            oid_type = "INTEGER"
            response = device.snmp(SNMPIF_MIB.IFINDEX, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFINDEX,
                type_response=oid_type,
                date_time=device.date,
            )
            response = response[
                [
                    HeaderResponseInterfacesSNMP.HOST,
                    HeaderResponseInterfacesSNMP.INDEX,
                    HeaderResponseInterfacesSNMP.DATE,
                    HeaderResponseInterfacesSNMP.TIME,
                ]
            ]
            return response
        except Exception as error:
            logger.error(f"SNMP IF-MIB error: Failed to obtain ifIndex - {error}")
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifNumber(device: Device) -> pd.DataFrame:
        try:
            oid_type = "INTEGER"
            response = device.snmp(SNMPIF_MIB.IFNUMBER, options="-On")
            if not response:
                return pd.DataFrame(columns=response_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFNUMBER,
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
            logger.error(f"SNMP IF-MIB error: Failed to obtain ifNumber - {error}")
            return pd.DataFrame(columns=response_snmp)

    @staticmethod
    def get_ifName(device: Device) -> pd.DataFrame:
        try:
            oid_type = "STRING"
            response = device.snmp(SNMPIF_MIB.IFNAME, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFNAME,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(f"SNMP IF-MIB error: Failed to obtain ifName - {error}")
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifAlias(device: Device) -> pd.DataFrame:
        try:
            oid_type = "STRING"
            response = device.snmp(SNMPIF_MIB.IFALIAS, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFALIAS,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(f"SNMP IF-MIB error: Failed to obtain ifAlias - {error}")
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifDescr(device: Device) -> pd.DataFrame:
        try:
            oid_type = "STRING"
            response = device.snmp(SNMPIF_MIB.IFDESCR, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFDESCR,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(f"SNMP IF-MIB error: Failed to obtain ifDescr - {error}")
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifHighSpeed(device: Device) -> pd.DataFrame:
        try:
            oid_type = "Gauge32"
            response = device.snmp(SNMPIF_MIB.IFHIGHSPEED, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFHIGHSPEED,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(f"SNMP IF-MIB error: Failed to obtain ifHighSpeed - {error}")
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifAdminStatus(device: Device) -> pd.DataFrame:
        try:
            oid_type = "INTEGER"
            response = device.snmp(SNMPIF_MIB.IFADMINSTATUS, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFADMINSTATUS,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(f"SNMP IF-MIB error: Failed to obtain ifAdminStatus - {error}")
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifOperStatus(device: Device) -> pd.DataFrame:
        try:
            oid_type = "INTEGER"
            response = device.snmp(SNMPIF_MIB.IFOPERSTATUS, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFOPERSTATUS,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(f"SNMP IF-MIB error: Failed to obtain ifOperStatus - {error}")
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifCounterDiscontinuityTime(device: Device) -> pd.DataFrame:
        try:
            oid_type = "Timeticks"
            response = device.snmp(SNMPIF_MIB.IFCOUNTERDISCONTINUITYTIME, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFCOUNTERDISCONTINUITYTIME,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(
                f"SNMP IF-MIB error: Failed to obtain ifCounterDiscontinuityTime - {error}"
            )
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifHCInOctets(device: Device) -> pd.DataFrame:
        try:
            oid_type = "Counter64"
            response = device.snmp(SNMPIF_MIB.IFHCINOCTETS, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFHCINOCTETS,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(f"SNMP IF-MIB error: Failed to obtain ifHCInOctets - {error}")
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifHCInUcastPkts(device: Device) -> pd.DataFrame:
        try:
            oid_type = "Counter64"
            response = device.snmp(SNMPIF_MIB.IFHCINUCASTPKTS, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFHCINUCASTPKTS,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(
                f"SNMP IF-MIB error: Failed to obtain ifHCInUcastPkts - {error}"
            )
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifHCInMulticastPkts(device: Device) -> pd.DataFrame:
        try:
            oid_type = "Counter64"
            response = device.snmp(SNMPIF_MIB.IFHCINMULTICASTPKTS, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFHCINMULTICASTPKTS,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(
                f"SNMP IF-MIB error: Failed to obtain ifHCInMulticastPkts - {error}"
            )
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifHCInBroadcastPkts(device: Device) -> pd.DataFrame:
        try:
            oid_type = "Counter64"
            response = device.snmp(SNMPIF_MIB.IFHCINBROADCASTPKTS, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFHCINBROADCASTPKTS,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(
                f"SNMP IF-MIB error: Failed to obtain ifHCInBroadcastPkts - {error}"
            )
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifInErrors(device: Device) -> pd.DataFrame:
        try:
            oid_type = "Counter32"
            response = device.snmp(SNMPIF_MIB.IFINERRORS, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFINERRORS,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(f"SNMP IF-MIB error: Failed to obtain ifInErrors - {error}")
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifInDiscards(device: Device) -> pd.DataFrame:
        try:
            oid_type = "Counter32"
            response = device.snmp(SNMPIF_MIB.IFINDISCARDS, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFINDISCARDS,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(f"SNMP IF-MIB error: Failed to obtain ifInDiscards - {error}")
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifHCOutOctets(device: Device) -> pd.DataFrame:
        try:
            oid_type = "Counter64"
            response = device.snmp(SNMPIF_MIB.IFHCOUTOCTETS, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFHCOUTOCTETS,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(f"SNMP IF-MIB error: Failed to obtain ifHCOutOctets - {error}")
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifHCOutUcastPkts(device: Device) -> pd.DataFrame:
        try:
            oid_type = "Counter64"
            response = device.snmp(SNMPIF_MIB.IFHCOUTUCASTPKTS, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFHCOUTUCASTPKTS,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(
                f"SNMP IF-MIB error: Failed to obtain ifHCOutUcastPkts - {error}"
            )
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifHCOutMulticastPkts(device: Device) -> pd.DataFrame:
        try:
            oid_type = "Counter64"
            response = device.snmp(SNMPIF_MIB.IFHCOUTMULTICASTPKTS, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFHCOUTMULTICASTPKTS,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(
                f"SNMP IF-MIB error: Failed to obtain ifHCOutMulticastPkts - {error}"
            )
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifHCOutBroadcastPkts(device: Device) -> pd.DataFrame:
        try:
            oid_type = "Counter64"
            response = device.snmp(SNMPIF_MIB.IFHCOUTBROADCASTPKTS, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFHCOUTBROADCASTPKTS,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(
                f"SNMP IF-MIB error: Failed to obtain ifHCOutBroadcastPkts - {error}"
            )
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifOutErrors(device: Device) -> pd.DataFrame:
        try:
            oid_type = "Counter32"
            response = device.snmp(SNMPIF_MIB.IFOUTERRORS, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFOUTERRORS,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(f"SNMP IF-MIB error: Failed to obtain ifOutErrors - {error}")
            return pd.DataFrame(columns=response_interface_snmp)

    @staticmethod
    def get_ifOutDiscards(device: Device) -> pd.DataFrame:
        try:
            oid_type = "Counter32"
            response = device.snmp(SNMPIF_MIB.IFOUTDISCARDS, options="-On")
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=SNMPIF_MIB.IFOUTDISCARDS,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(f"SNMP IF-MIB error: Failed to obtain ifOutDiscards - {error}")
            return pd.DataFrame(columns=response_interface_snmp)
