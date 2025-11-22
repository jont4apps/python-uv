# ruff: noqa: EXE002
import logging
import sys
from typing import TYPE_CHECKING

from tools.logger.type import LogType

if TYPE_CHECKING:
    from google.auth.credentials import Credentials


class Logger(logging.Logger):
    """Logger.

    Examples:
        >>> from tools.logger import Logger
        >>>
        >>>
        >>> logger = Logger(__name__)
        >>> logger.info("Logger")

    """

    def __init__(
        self,
        name: str,
        project: str | None = None,
        credentials: Credentials | None = None,
        log_type: LogType = LogType.LOCAL,
    ) -> None:
        """Initialize local logger formatter.

        Args:
            name (str): Logger name
            project (str | None, optional): Google Cloud Project ID. Defaults to None.
            credentials (Credentials | None, optional): Credentials for Google Cloud.
                                                        Defaults to None.
            log_type (LogType, optional): Local or something.
                                          Defaults to LogType.LOCAL.

        """
        super().__init__(name=name)

        # Keep `project` and `credentials` parameters for API compatibility.
        # They are intentionally unused in this console-only implementation.
        _ = (project, credentials)

        # This project uses standard console logging only. Ignore any
        # requests to use Google Cloud logging and always configure the
        # local console formatter. Keeping `LogType.GOOGLE_CLOUD` in the
        # enum preserves compatibility for callers that may pass it.
        if log_type == LogType.GOOGLE_CLOUD:
            logging.getLogger(__name__).debug(
                "LogType.GOOGLE_CLOUD specified but Google Cloud integration "
                "is disabled; using local console logger instead",
            )

        from tools.logger import LocalFormatter

        formatter = LocalFormatter()
        handler = logging.StreamHandler(stream=sys.stdout)

        handler.setFormatter(formatter)
        self.addHandler(handler)


def get_logger(
    name: str,
    level: int = logging.INFO,
    project: str | None = None,
    credentials: object | None = None,
    log_type: LogType = LogType.LOCAL,
) -> Logger:
    """Create a configured logger.

    Keep the public surface small for PoC use while preserving the
    existing `Logger` class for compatibility in tests and other
    callers.

    Returns:
        Logger: Configured logger instance.


    """
    logger = Logger(
        name=name,
        project=project,
        credentials=credentials,
        log_type=log_type,
    )
    logger.setLevel(level)
    return logger
