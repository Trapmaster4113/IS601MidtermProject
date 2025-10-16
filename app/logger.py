import logging
from app.calculator_config import CalculatorConfig
import os
from app.color import Color
class Logger:
    @staticmethod
    def _setup_logging(config: CalculatorConfig) -> None:
        """
        Configure the logging system.

        Sets up logging to a file with a specified format and log level.
        """
        # Create required directories for history management
        Logger._setup_directories
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
            Logger.infoLog(f"Logging initialized at: {log_file}")
        except Exception as e:
            # Print an error message and re-raise the exception if logging setup fails
            Color.printError(f"Error setting up logging: {e}")
            raise
    @staticmethod
    def _setup_directories(config: CalculatorConfig) -> None:
        """
        Create required directories.

        Ensures that all necessary directories for history management exist.
        """
        config.history_dir.mkdir(parents=True, exist_ok=True)
    #Logs any message as an info log
    @staticmethod
    def infoLog(text: str) -> None:
        logging.info(text)
    #Logs any message as warning log
    @staticmethod
    def warnLog(text: str) -> None:
        logging.warning(text)
    #Logs any message as an error log
    @staticmethod
    def errorLog(text: str) -> None:
        logging.error(text)