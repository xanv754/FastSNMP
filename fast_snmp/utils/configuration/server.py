import os
import json
from pydantic import BaseModel
from fast_snmp.constants import FilePaths
from fast_snmp.utils.log import logger


class SSHCredentialSchema(BaseModel):
    user: str
    password: str
    host: str
    port: int


class ConfigurationSchema(BaseModel):
    localConnection: bool
    credentials: list[SSHCredentialSchema]
    commandPing: str
    commandSNMP: str


class Configuration:
    _default_config: ConfigurationSchema = ConfigurationSchema(
        localConnection=True, credentials=[], commandPing="ping", commandSNMP="snmpwalk"
    )
    _mode_dev: bool
    _mode_testing: bool

    def __init__(self, dev: bool = False, testing: bool = False) -> None:
        self._mode_dev = dev
        self._mode_testing = testing
        if not self._get_filename_config(dev=dev, testing=testing):
            self._create_default_config(dev=dev, testing=testing)

    def _get_filename_config(self, dev: bool, testing: bool) -> str | None:
        if dev:
            if os.path.exists(FilePaths.SSH_CONFIG_DEVELOPMENT):
                return FilePaths.SSH_CONFIG_DEVELOPMENT
        elif testing:
            if os.path.exists(FilePaths.SSH_CONFIG_TESTING):
                return FilePaths.SSH_CONFIG_TESTING
        else:
            if os.path.exists(FilePaths.SSH_CONFIG):
                return FilePaths.SSH_CONFIG
            elif os.path.exists(FilePaths.SSH_CONFIG_PRODUCTION):
                return FilePaths.SSH_CONFIG_PRODUCTION
        return None

    def _create_default_config(self, dev: bool, testing: bool) -> None:
        try:
            if dev:
                filename = FilePaths.SSH_CONFIG_DEVELOPMENT
            elif testing:
                filename = FilePaths.SSH_CONFIG_TESTING
            else:
                filename = FilePaths.SSH_CONFIG_PRODUCTION
            with open(filename, "w") as file:
                json.dump(self._default_config.model_dump(), file, indent=2)
        except Exception as error:
            logger.error(
                f"SSH Configuration: Failed to create default SSH configuration - {error}"
            )

    def get_config(self) -> ConfigurationSchema:
        filename = self._get_filename_config(
            dev=self._mode_dev, testing=self._mode_testing
        )
        if filename:
            with open(filename, "r") as file:
                return ConfigurationSchema(**json.load(file))
        return self._default_config


if __name__ == "__main__":
    ssh_config = Configuration(dev=True)
    print(ssh_config.get_config())
