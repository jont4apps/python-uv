import logging
import os
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

        if log_type == LogType.GOOGLE_CLOUD:
            # Feature flag to allow disabling Google Cloud logging integration
            # without changing code that requests LogType.GOOGLE_CLOUD.
            # Default behavior remains enabled unless the env var is explicitly
            # set to a falsey value (0/false/no).
            flag = os.getenv("TOOLS_GOOGLE_CLOUD_LOGGING", "0").lower()
            enabled = flag in ("1", "true", "yes", "on")

            if not enabled:
                logging.getLogger(__name__).debug(
                    "Google Cloud logging integration disabled by TOOLS_GOOGLE_CLOUD_LOGGING"
                )
            else:
                try:
                    import google.cloud.logging
                    from google.cloud.logging_v2.handlers import StructuredLogHandler

                    from tools.logger import GoogleCloudFormatter

                    client = google.cloud.logging.Client(
                        project=project, credentials=credentials
                    )
                    client.setup_logging()

                    formatter = GoogleCloudFormatter()
                    handler = StructuredLogHandler(stream=sys.stdout)

                    handler.setFormatter(formatter)
                    self.addHandler(handler)
                    return
                except Exception as exc:  # ImportError or runtime errors
                    # Fall back to local formatter if Google Cloud libs are missing
                    logging.getLogger(__name__).warning(
                        "Google Cloud logging unavailable (%s); falling back to local logger",
                        exc,
                    )

        from tools.logger import LocalFormatter

        formatter = LocalFormatter()
        handler = logging.StreamHandler(stream=sys.stdout)

        handler.setFormatter(formatter)
        self.addHandler(handler)
