from datetime import datetime
from fast_snmp.libs.server.execute import ExecuteCommand
from fast_snmp.libs.server.local import LocalServer
from fast_snmp.libs.server.remote import RemoteServer
from fast_snmp.utils import Configuration, logger


class Device:
    _instance: 'Device | None' = None
    _config: Configuration
    _server: ExecuteCommand
    _connected: bool
    date: datetime
    host: str
    community: str | None

    def __new__(cls, *args) -> 'Device':
        if not cls._instance:
            cls._instance = super(Device, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, "_initiliazed"):
            self._connected = False
            self._initiliazed = True

    def set_configuration(self, dev: bool = False, testing: bool = False) -> None:
        try:
            if not self._connected:
                self._config = Configuration(dev=dev, testing=testing)
                config = self._config.get_config()
                if config.localConnection:
                    self._server = LocalServer(config)
                else:
                    self._server = RemoteServer(config)
        except Exception as error:
            logger.error(f"Failure when connecting to the server - {error}")
            self._connected = False
        else:
            self._connected = True

    def set_credentials(self, host: str, community: str | None = None) -> None:
        self.date = datetime.now()
        self.host = host
        self.community = community

    def ping(self) -> bool:
        """Ping a host.

        :returns bool: True if the host is reachable, False otherwise.
        """
        return self._server.ping(self.host)

    def snmp(self, oid: str, options: str | None = None) -> str | None:
        """Execute the SNMP query on the device.

        :params oid: The OID to query.
        :returns str | None: The response from the device.
        """
        if not self.ping:
            return None
        command_snmp = self._config.get_config().commandSNMP
        if not options:
            response = self._server.execute(
                f"{command_snmp} -v 2c -c {self.community} {self.host} {oid}"
            )
        else:
            response = self._server.execute(
                f"{command_snmp} -v 2c -c {self.community} {options} {self.host} {oid}"
            )
        return response
