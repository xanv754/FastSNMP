from datetime import datetime
from fast_snmp.libs.server.execute import ExecuteCommand
from fast_snmp.libs.server.local import LocalServer
from fast_snmp.libs.server.remote import RemoteServer
from fast_snmp.utils import Configuration


class Device:
    _config: Configuration
    _server: ExecuteCommand
    date: datetime
    host: str
    community: str

    def __init__(
        self, host: str, community: str, dev: bool = False, testing: bool = False
    ) -> None:
        self.date = datetime.now()
        self.host = host
        self.community = community
        self._config = Configuration(dev=dev, testing=testing)
        config = self._config.get_config()
        if config.localConnection:
            self._server = LocalServer(config)
        else:
            self._server = RemoteServer(config)

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
