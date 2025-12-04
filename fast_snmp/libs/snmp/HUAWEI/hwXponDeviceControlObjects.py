import pandas as pd
from fast_snmp.libs.server.device import Device
from fast_snmp.constants import response_interface_snmp, HWXPONDEVICECONTROLOBJECTS
from fast_snmp.utils import logger, TransformSNMP


class HwXponDeviceControlObjects:
    @staticmethod
    def get_run_status(device: Device) -> pd.DataFrame:
        try:
            oid_type = "INTEGER"
            response = device.snmp(
                HWXPONDEVICECONTROLOBJECTS.hwGponDeviceOntControlRunStatus,
                options="-On",
            )
            if not response:
                return pd.DataFrame(columns=response_interface_snmp)
            response = TransformSNMP.output(
                host=device.host,
                stdout=response,
                oid=HWXPONDEVICECONTROLOBJECTS.hwGponDeviceOntControlRunStatus,
                type_response=oid_type,
                date_time=device.date,
            )
            return response
        except Exception as error:
            logger.error(
                f"hwXponDeviceControlObjects error: Failed to obtain ONT status - {error}"
            )
            return pd.DataFrame(columns=response_interface_snmp)
