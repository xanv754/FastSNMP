from typing import override
from fast_snmp.libs.server.execute import ExecuteCommand
from fast_snmp.utils import ConfigurationSchema, SSHConnection, logger


class RemoteServer(ExecuteCommand):
    _ssh: SSHConnection

    def __init__(self, config: ConfigurationSchema) -> None:
        ssh_connection = SSHConnection()
        ssh_connection.set_config(config)
        self._ssh = ssh_connection

    @override
    def execute(self, command: str) -> str | None:
        try:
            self._ssh.connect()
            if self._ssh.isConnected:
                client = self._ssh.get_client()
                _stdin, stdout, stderr = client.exec_command(command)
                if stdout.channel.recv_exit_status() == 0:
                    return stdout.read().decode().strip()
                else:
                    raise Exception(stderr.read().decode().strip())
            else:
                raise Exception("Connection to server not established")
        except Exception as error:
            logger.error(f"Server error: The query execution failed - {error}")
            return None

    @override
    def ping(self, host: str) -> bool:
        try:
            config = self._ssh.get_config()
            if not config:
                raise Exception("SSH configuration not found")
            ping_command = config.commandPing
            self._ssh.connect()
            if self._ssh.isConnected:
                client = self._ssh.get_client()
                _stdin, stdout, stderr = client.exec_command(f"{ping_command} -V")
                if stdout.channel.recv_exit_status() == 0:
                    _stdin, stdout, stderr = client.exec_command(
                        f"{ping_command} -c 1 -W 5 {host}"
                    )
                    if stdout.channel.recv_exit_status() == 0:
                        response = stdout.read().decode().strip()
                        if "1 received, 0% packet loss" in response:
                            return True
                        else:
                            return False
                    else:
                        raise Exception(stderr.read().decode().strip())
                else:
                    _stdin, stdout, stderr = client.exec_command(
                        f"{ping_command} {host}"
                    )
                    if stdout.channel.recv_exit_status() == 0:
                        response = stdout.read().decode().strip()
                        if "is alive" in response:
                            return True
                        else:
                            return False
                    else:
                        raise Exception(stderr.read().decode().strip())
            else:
                raise Exception("Connection to server not established")
        except Exception as error:
            message = f"Server error: Ping failed - {error}"
            logger.error(message.strip())
            return False
