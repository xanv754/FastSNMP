import pandas as pd
from datetime import datetime
from fast_snmp.constants import HeaderResponseInterfacesSNMP


MESSAGE_ERROR = "No Such Object available on this agent at this OID"


class TransformSNMP:
    @staticmethod
    def output(host: str, stdout: str, oid: str, type_response: str, date_time: datetime) -> pd.DataFrame:
        """Transform raw SNMP outputs into manageable data.
        
        :params host: Host of the device.
        :type host: str
        :params stdout: Raw output of the SNMP query.
        :type stdout: str
        :params oid: OID of the SNMP query.
        :type oid: str
        :params type: Type of the OID.
        :type type: str
        :params date_time: Date and time of the SNMP query.
        :type date_time: datetime
        :returns DataFrame: DataFrame with the transformed data.
        """
        if MESSAGE_ERROR in stdout: raise ValueError(MESSAGE_ERROR)
        date = date_time.strftime("%Y-%m-%d")
        time = date_time.strftime("%H:%M:%S")
        data = {
            HeaderResponseInterfacesSNMP.HOST: [],
            HeaderResponseInterfacesSNMP.INDEX: [],    
            HeaderResponseInterfacesSNMP.VALUES: [],
            HeaderResponseInterfacesSNMP.DATE: [],
            HeaderResponseInterfacesSNMP.TIME: []
        }
        for line in stdout.splitlines():
            try:
                raw_oid, raw_value = line.split(f"= {type_response}:", 1)
            except ValueError:
                continue
            if len(raw_oid.strip().split(f"{oid}.")) > 1:
                index = raw_oid.strip().split(f"{oid}.")[1]
            else: index = 0
            value = raw_value.strip()
            data[HeaderResponseInterfacesSNMP.HOST].append(host)
            data[HeaderResponseInterfacesSNMP.INDEX].append(index)
            data[HeaderResponseInterfacesSNMP.VALUES].append(value)
            data[HeaderResponseInterfacesSNMP.DATE].append(date)
            data[HeaderResponseInterfacesSNMP.TIME].append(time)
        return pd.DataFrame(data)
        