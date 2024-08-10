import logging


class Logger(object):
    """Logger utility"""

    def __init__(self, logger_name, log_file=None, level=logging.DEBUG):
        """
        Initialize a logger instance.

        Args:
            - logger_name: Name of the logger (typically the name of the module).
            - log_file: Optional log file path. If None, logs will not be written to a file.
            - level: Logging level (e.g., logging.DEBUG, logging.INFO).
        """
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(level)

        # formatter for the log messages
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # output handler
        if log_file:
            handler = logging.FileHandler(log_file)
        else:
            handler = logging.StreamHandler()
        handler.setLevel(level)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        """get the logger instance."""
        return self.logger
