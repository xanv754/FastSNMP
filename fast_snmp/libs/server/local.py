from typing import override
import subprocess
from fast_snmp.libs.server.execute import ExecuteCommand
from fast_snmp.utils import ConfigurationSchema, logger


class LocalServer(ExecuteCommand):
    _config: ConfigurationSchema

    def __init__(self,config: ConfigurationSchema) -> None:
        self._config = config

    @override
    def execute(self, command: str) -> str | None:
        try:
            response = subprocess.run(command, shell=True, capture_output=True, text=True)
            if response.stderr: raise Exception(response.stderr)
            else: return response.stdout.strip()
        except Exception as error:
            logger.error(f"Server error: The query execution failed - {error}")
            return None

    @override
    def ping(self, host: str) -> bool:
        try:
            ping_command = self._config.commandPing
            response = subprocess.run(f"{ping_command} -V", shell=True, capture_output=True, text=True)
            if response.stderr: 
                response = subprocess.run(f"{ping_command} {host}", shell=True, capture_output=True, text=True)
                if response.stderr: raise Exception(response.stderr)
                else:
                    if "is alive" in response.stdout: return True
                    else: return False
            else:
                response = subprocess.run(f"{ping_command} -c 1 -W 5 {host}", shell=True, capture_output=True, text=True)
                if response.stderr: raise Exception(response.stderr)
                else:
                    if "1 received, 0% packet loss" in response.stdout: return True
                    else: return False
        except Exception as error:
            message = f"Server error: Ping failed - {error}"
            logger.error(message.strip())
            return False
