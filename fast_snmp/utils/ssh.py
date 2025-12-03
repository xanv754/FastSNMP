import threading
import time
import paramiko
from fast_snmp.utils.configuration.server import (
    ConfigurationSchema,
    SSHCredentialSchema,
)
from fast_snmp.utils.log import logger


class SSHConnection:
    _instance: "SSHConnection | None" = None
    _config: ConfigurationSchema | None = None
    _initialized: bool
    _client: list[paramiko.SSHClient]
    _last_used: float 
    _lock: threading.Lock
    isConnected: bool

    def __new__(cls, *args, **kwargs) -> "SSHConnection":
        if not cls._instance:
            cls._instance = super(SSHConnection, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, "_initialized"):
            self.isConnected = False
            self._client = []
            self._last_used = 0
            self._lock = threading.Lock()
            self._initialized = True
            
    def _ssh_jump(self, credentials: list[SSHCredentialSchema]) -> None:
        try:
            sock: paramiko.Channel | None = None
            jumps: int = len(credentials) - 1
            for i, credential in enumerate(credentials):
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(
                    username=credential.user,
                    password=credential.password,
                    hostname=credential.host,
                    port=credential.port,
                    sock=sock,
                )
                self._client.append(client)
                if i == jumps:
                    break
                transport = client.get_transport()
                if not transport:
                    raise ValueError("The SSH jump transport failed. Transport is None")
                next_credential = credentials[i + 1]
                dest_addr = (next_credential.host, next_credential.port)
                local_addr = ("127.0.0.1", 0)
                sock = transport.open_channel("direct-tcpip", dest_addr, local_addr)
        except Exception as error:
            logger.error(f"SSH Connection: Failed SSH jump to connect - {error}")
            
    def _auto_close(self, timeout=120) -> None:
        if hasattr(self, '_monitor_thread') and self._monitor_thread.is_alive():
            return
        def monitor() -> None:
            while True:
                time.sleep(5)
                with self._lock:
                    if not self.isConnected: break
                    idle_time = time.time() - self._last_used
                    if idle_time > timeout:
                        logger.info(f"SSH auto-close triggered after {int(idle_time)}s of inactivity.")
                        self.disconnect()
                        break
        self._monitor_thread = threading.Thread(target=monitor, daemon=True)
        self._monitor_thread.start()

    def set_config(self, config: ConfigurationSchema) -> None:
        self._config = config

    def get_config(self) -> ConfigurationSchema | None:
        return self._config

    def get_client(self) -> paramiko.SSHClient:
        return self._client[-1]

    def connect(self) -> None:
        try:
            with self._lock:
                if self.isConnected:
                    self._last_used = time.time()
                    return
                if not self._config: raise ValueError("SSH Configuration not set")
                if self._config.localConnection: raise ValueError("The configuration does not allow SSH connections")
                self._ssh_jump(self._config.credentials)
                self.isConnected = True
                self._last_used = time.time()
            self._auto_close()
        except ValueError as error:
            self.isConnected = False
            logger.error(f"SSH Connection - {error}")
        except Exception as error:
            self.isConnected = False
            logger.error(f"SSH Connection: Failed to connect to server - {error}")
            
    def disconnect(self) -> None:
        try:
            if self.isConnected:
                while len(self._client) > 0:
                    client = self._client.pop()
                    client.close()
        except Exception as error:
            logger.error(f"SSH Connection: Failed to disconnect from server - {error}")
        else:
            self.isConnected = False
