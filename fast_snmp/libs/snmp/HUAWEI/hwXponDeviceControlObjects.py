import pandas as pd
from fast_snmp.constants.headers import HeaderResponseInterfacesSNMP
from fast_snmp.libs.server.device import Device
from fast_snmp.constants import response_interface_snmp, HWXPONDEVICECONTROLOBJECTS
from fast_snmp.utils import logger, TransformSNMP


class HwXponDeviceControlObjects:
    @staticmethod
    def get_total_ont_status_online(device: Device) -> pd.DataFrame:
        try:
            oid_type = "INTEGER"
            response_snmp = device.snmp(
                HWXPONDEVICECONTROLOBJECTS.hwGponDeviceOntControlRunStatus,
                options="-On",
            )
            if not response_snmp:
                return pd.DataFrame(columns=response_interface_snmp)
            data = TransformSNMP.output(
                host=device.host,
                stdout=response_snmp,
                oid=HWXPONDEVICECONTROLOBJECTS.hwGponDeviceOntControlRunStatus,
                type_response=oid_type,
                date_time=device.date,
            )
            total_clients_online = len(data[data[HeaderResponseInterfacesSNMP.VALUES] == "1"])
            response = {
                HeaderResponseInterfacesSNMP.HOST: [data[HeaderResponseInterfacesSNMP.HOST].iloc[0]],
                HeaderResponseInterfacesSNMP.DATE: [data[HeaderResponseInterfacesSNMP.DATE].iloc[0]],
                HeaderResponseInterfacesSNMP.TIME: [data[HeaderResponseInterfacesSNMP.TIME].iloc[0]],
                HeaderResponseInterfacesSNMP.VALUES: [total_clients_online]
            }
            return pd.DataFrame(response)
        except Exception as error:
            logger.error(
                f"hwXponDeviceControlObjects error: Failed to obtain ONT status - {error}"
            )
            return pd.DataFrame(columns=response_interface_snmp)
