from abc import ABC, abstractmethod


class ExecuteCommand(ABC):
    @abstractmethod
    def execute(self, command: str) -> str | None:
        """Run a command on the server.
        
        :params command: The command to be executed on the server.
        :returns str | None: The output of the command. If the command fails, returns None.
        """
        pass

    @abstractmethod
    def ping(self, host: str) -> bool:
        """Ping a host.
        
        :params host: The host to be pinged.
        :returns bool: True if the host is reachable, False otherwise.
        """
        pass