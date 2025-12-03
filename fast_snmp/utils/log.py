import logging
from os import path
from logging.handlers import TimedRotatingFileHandler
from rich.logging import RichHandler
from fast_snmp.constants.files import FilePaths

ROOT_PATH = path.abspath(path.join(path.dirname(__file__), "..", ".."))
LOG_PATH = path.join(ROOT_PATH, "logs")
LOG_FORMAT = "%(asctime)s %(levelname)s %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
FORMATTER = logging.Formatter(LOG_FORMAT, DATE_FORMAT)


class LogHandler:
    """A handler for all log system operations."""

    __console_handler: RichHandler
    __file_handler: TimedRotatingFileHandler
    logger: logging.Logger

    def __init__(self) -> None:
        try:
            path = FilePaths()
            self.__console_handler = RichHandler(
                rich_tracebacks=True,
                markup=False,
                show_path=False,
                show_time=False,
                show_level=False,
            )
            self.__console_handler.setFormatter(FORMATTER)
            self.__file_handler = TimedRotatingFileHandler(
                path.LOG_FILE,
                when="W0",
                interval=1,
                backupCount=4,
                encoding="utf-8",
                utc=True,
            )
            self.__file_handler.setFormatter(FORMATTER)
            logging.basicConfig(
                level=logging.INFO,
                handlers=[self.__console_handler, self.__file_handler],
            )
            self.logger = logging.getLogger(__name__)
        except Exception as e:
            print(f"Log Error - {e}")


logHandler = LogHandler()
logger = logHandler.logger


if __name__ == "__main__":
    logger.info("Testing logging!")
