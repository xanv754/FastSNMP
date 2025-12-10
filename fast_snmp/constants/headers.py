class HeaderResponseInterfacesSNMP:
    HOST: str = "ip"
    COMMUNITY: str = "community"
    INDEX: str = "index"
    VALUES: str = "response"
    DATE: str = "date"
    TIME: str = "time"


response_interface_snmp = [
    HeaderResponseInterfacesSNMP.HOST,
    HeaderResponseInterfacesSNMP.INDEX,
    HeaderResponseInterfacesSNMP.VALUES,
    HeaderResponseInterfacesSNMP.DATE,
    HeaderResponseInterfacesSNMP.TIME,
]

response_snmp = [
    HeaderResponseInterfacesSNMP.HOST,
    HeaderResponseInterfacesSNMP.VALUES,
    HeaderResponseInterfacesSNMP.DATE,
    HeaderResponseInterfacesSNMP.TIME,
]
