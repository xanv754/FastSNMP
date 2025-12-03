from os import path, makedirs


class FilePaths:
    SSH_CONFIG: str = path.abspath(
        path.join(path.dirname(__file__), "..", "..", "ssh.json")
    )
    SSH_CONFIG_DEVELOPMENT: str = path.abspath(
        path.join(path.dirname(__file__), "..", "..", "ssh.development.json")
    )
    SSH_CONFIG_PRODUCTION: str = path.abspath(
        path.join(path.dirname(__file__), "..", "..", "ssh.production.json")
    )
    SSH_CONFIG_TESTING: str = path.abspath(
        path.join(path.dirname(__file__), "..", "..", "ssh.testing.json")
    )
    LOG_FOLDER: str = path.abspath(
        path.join(path.dirname(__file__), "..", "..", "logs")
    )
    LOG_FILE: str = path.join(LOG_FOLDER, "Fast-SNMP.log")

    def __init__(self) -> None:
        makedirs(self.LOG_FOLDER, exist_ok=True)


if __name__ == "__main__":
    print(FilePaths.SSH_CONFIG)
