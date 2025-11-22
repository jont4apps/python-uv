# ruff: noqa: EXE002
from tools.logger import Logger, LogType


class TestLocalLogger:
    """Test class for local logger."""

    def setup_method(self) -> None:
        """Set up logger."""
        self.logger = Logger(name=__name__, log_type=LogType.LOCAL)

    def test_log(self) -> None:
        """Test log method of logger."""
        assert self.logger.debug("debug") is None
        assert self.logger.info("info") is None
        assert self.logger.warning("warning") is None
        assert self.logger.error("error") is None
        assert self.logger.critical("critical") is None

    def test_name(self) -> None:
        """Test correct name of logger."""
        assert self.logger.name == __name__


class TestGoogleCloudLogger:
    """Test class for Google Cloud logger."""

    def setup_method(self) -> None:
        """Set up logger."""
        # Avoid importing the real `google` package in the minimal branch.
        # Passing `credentials=None` verifies the logger handles
        # `LogType.GOOGLE_CLOUD` gracefully without requiring external deps.
        self.logger = Logger(
            name=__name__,
            project=__name__,
            credentials=None,
            log_type=LogType.GOOGLE_CLOUD,
        )

    def test_log(self) -> None:
        """Test log method of logger."""
        assert self.logger.debug("debug") is None
        assert self.logger.info("info") is None
        assert self.logger.warning("warning") is None
        assert self.logger.error("error") is None
        assert self.logger.critical("critical") is None

    def test_name(self) -> None:
        """Test correct name of logger."""
        assert self.logger.name == __name__
