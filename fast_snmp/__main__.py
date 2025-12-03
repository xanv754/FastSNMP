import click
from fast_snmp.libs import Device, SNMPSystem, SNMPIF, HwXponDeviceControlObjects


@click.group()
def cli():
    """SNMP SIRTIR CLI
    
    Command line interface for performing SNMP queries on different devices on the network.
    
    Designed for easy consultation of network equipment via the terminal.
    """
    pass
    
@cli.command(help="Get the sysName of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def sysName(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPSystem.get_sysName(device))
    
@cli.command(help="Get the sysLocation of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def sysLocation(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPSystem.get_sysLocation(device))
    
@cli.command(help="Get the sysDescription of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def sysDescr(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPSystem.get_sysDescr(device))
    
@cli.command(help="Get the sysContact of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def sysContact(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPSystem.get_sysContact(device))
    
@cli.command(help="Get the sysUpTime of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def sysUpTime(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPSystem.get_sysUpTime(device))
    
@cli.command(help="Get the ifIndex of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifIndex(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifIndex(device))

@cli.command(help="Get the ifNumber of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifNumber(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifNumber(device))

@cli.command(help="Get the ifName of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifName(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifName(device))
    
@cli.command(help="Get the ifAlias of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifAlias(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifAlias(device))
    
@cli.command(help="Get the ifDescr of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifDescr(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifDescr(device))
    
@cli.command(help="Get the ifHighSpeed of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifHighSpeed(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifHighSpeed(device))
    
@cli.command(help="Get the ifAdminStatus of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifAdminStatus(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifAdminStatus(device))
    
@cli.command(help="Get the ifOperStatus of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifOperStatus(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifOperStatus(device))

@cli.command(help="Get the ifCounterDiscontinuityTime of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifCounterDiscontinuityTime(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifCounterDiscontinuityTime(device))
    
@cli.command(help="Get the ifHCInOctets of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifHCInOctets(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifHCInOctets(device))
    
@cli.command(help="Get the ifHCInUcastPkts of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifHCInUcastPkts(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifHCInUcastPkts(device))
    
@cli.command(help="Get the ifHCInMulticastPkts of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifHCInMulticastPkts(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifHCInMulticastPkts(device))
    
@cli.command(help="Get the ifHCInBroadcastPkts of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifHCInBroadcastPkts(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifHCInBroadcastPkts(device))
    
@cli.command(help="Get the ifInErrors of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifInErrors(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifInErrors(device))
    
@cli.command(help="Get the ifInDiscards of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifInDiscards(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifInDiscards(device))
    
@cli.command(help="Get the ifHCOutOctets of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifHCOutOctets(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifHCOutOctets(device))

@cli.command(help="Get the ifHCOutUcastPkts of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifHCOutUcastPkts(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifHCOutUcastPkts(device))
    
@cli.command(help="Get the ifHCOutMulticastPkts of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifHCOutMulticastPkts(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifHCOutMulticastPkts(device))
    
@cli.command(help="Get the ifHCOutBroadcastPkts of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifHCOutBroadcastPkts(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifHCOutBroadcastPkts(device))
    
@cli.command(help="Get the ifOutErrors of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifOutErrors(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifOutErrors(device))
    
@cli.command(help="Get the ifOutDiscards of all interfaces of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ifOutDiscards(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(SNMPIF.get_ifOutDiscards(device))
    
@cli.command(help="Get the ONT status of all ONT of a device")
@click.option("-h", "-ip", "--host", "--ip", type=str, required=True, help="IP address of the device")
@click.option("-c", "--community", type=str, required=True, help="SNMP community string. In cases of special characters, place them within quotation marks.")
@click.option("-d", "--dev", is_flag=True, help="Load of the development environment.")
def ont_status(host: str, community: str, dev: bool = False) -> None:
    device = Device(host=host, community=community, dev=dev)
    print(HwXponDeviceControlObjects.get_run_status(device))


if __name__ == "__main__":
    cli()