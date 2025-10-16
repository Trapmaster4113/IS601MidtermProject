import logging
from app.calculator_config import CalculatorConfig
from typing import Optional
from app.operations import Operation
import os
from pathlib import Path

class Logger:
    @staticmethod
    def _setup_logging(path : Path, config: Optional[CalculatorConfig] = None) -> None:
        """
        Configure the logging system.

        Sets up logging to a file with a specified format and log level.
        """
        config = CalculatorConfig(base_dir=path)
        os.makedirs(config.log_dir, exist_ok=True)
        try:
            # Ensure the log directory exists
            os.makedirs(config.log_dir, exist_ok=True)
            log_file = config.log_file.resolve()

            # Configure the basic logging settings
            logging.basicConfig(
                filename=str(log_file),
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s',
                force=True  # Overwrite any existing logging configuration
            )
            logging.info(f"Logging initialized at: {log_file}")
        except Exception as e:
            # Print an error message and re-raise the exception if logging setup fails
            print(f"Error setting up logging: {e}")
            raise
    @staticmethod
    def infoLog(text: str) -> None:
        logging.info(text)
    @staticmethod
    def warnLog(text: str) -> None:
        logging.warning(text)
    @staticmethod
    def errorLog(text: str) -> None:
        logging.error(text)