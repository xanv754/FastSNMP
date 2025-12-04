class SNMPv2MIB:
    SYSNAME: str = "1.3.6.1.2.1.1.5.0"
    SYSLOCATION: str = "1.3.6.1.2.1.1.6"
    SYSDESCR: str = "1.3.6.1.2.1.1.1.0"
    SYSCONTACT: str = "1.3.6.1.2.1.1.4"
    SYSUPTIME: str = "1.3.6.1.2.1.1.3"


class SNMPIF_MIB:
    IFINDEX: str = "1.3.6.1.2.1.2.2.1.1"
    IFNUMBER: str = "1.3.6.1.2.1.2.1"
    IFNAME: str = "1.3.6.1.2.1.31.1.1.1.1"
    IFALIAS: str = "1.3.6.1.2.1.31.1.1.1.18"
    IFDESCR: str = "1.3.6.1.2.1.2.2.1.2"
    IFHIGHSPEED: str = "1.3.6.1.2.1.31.1.1.1.15"
    IFADMINSTATUS: str = "1.3.6.1.2.1.2.2.1.7"
    IFOPERSTATUS: str = "1.3.6.1.2.1.2.2.1.8"
    IFCOUNTERDISCONTINUITYTIME: str = "1.3.6.1.2.1.31.1.1.1.19"
    IFHCINOCTETS: str = "1.3.6.1.2.1.31.1.1.1.6"
    IFHCINUCASTPKTS: str = "1.3.6.1.2.1.31.1.1.1.7"
    IFHCINMULTICASTPKTS: str = "1.3.6.1.2.1.31.1.1.1.8"
    IFHCINBROADCASTPKTS: str = "1.3.6.1.2.1.31.1.1.1.9"
    IFINERRORS: str = "1.3.6.1.2.1.2.2.1.14"
    IFINDISCARDS: str = "1.3.6.1.2.1.2.2.1.13"
    IFHCOUTOCTETS: str = "1.3.6.1.2.1.31.1.1.1.10"
    IFHCOUTUCASTPKTS: str = "1.3.6.1.2.1.31.1.1.1.11"
    IFHCOUTMULTICASTPKTS: str = "1.3.6.1.2.1.31.1.1.1.12"
    IFHCOUTBROADCASTPKTS: str = "1.3.6.1.2.1.31.1.1.1.13"
    IFOUTERRORS: str = "1.3.6.1.2.1.2.2.1.20"
    IFOUTDISCARDS: str = "1.3.6.1.2.1.2.2.1.19"


class HWXPONDEVICECONTROLOBJECTS:
    hwGponDeviceOntControlRunStatus: str = "1.3.6.1.4.1.2011.6.128.1.1.2.46.1.15"


class UBNONUENTRY:
    ubntOnuOnline: str = "1.3.6.1.4.1.41112.1.5.6.2.1.3"


class ZXANSERVICEPORT:
    zxAnServicePortAdminStatus: str = "1.3.6.1.4.1.3902.1015.8.1.1.1.22"
