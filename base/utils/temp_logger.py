import logging
import sys


class TempLogger(logging.Logger):
    loggers = set()

    def __init__(self, name, format="%(asctime)s | %(levelname)s | %(message)s", level=logging.INFO):
        super().__init__(name, level)
        self.format = format
        self.level = level
        self.name = name
        self.console_formatter = logging.Formatter(self.format)
        self.console_logger = logging.StreamHandler(sys.stdout)
        self.console_logger.setFormatter(self.console_formatter)

        self.logger = logging.getLogger(name)
        if name not in self.loggers:
            self.loggers.add(name)
            self.logger.setLevel(self.level)
            self.logger.addHandler(self.console_logger)
