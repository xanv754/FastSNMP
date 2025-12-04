class HeaderResponseInterfacesSNMP:
    HOST: str = "IP"
    COMMUNITY: str = "Comunidad"
    INDEX: str = "Índices"
    VALUES: str = "Respuesta"
    DATE: str = "Fecha"
    TIME: str = "Tiempo"


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
