import pytest
from app.logger import Logger
from pathlib import Path
from unittest.mock import Mock, patch, PropertyMock
from app.calculator_config import CalculatorConfig
'''
#Doesn't work. Not sure how "assert_any_call" works
@patch('app.logger')
def test_logging_setup(logging_info_mock):
    with patch.object(CalculatorConfig, 'log_dir', new_callable=PropertyMock) as mock_log_dir, \
         patch.object(CalculatorConfig, 'log_file', new_callable=PropertyMock) as mock_log_file:
        mock_log_dir.return_value = Path('/tmp/logs')
        mock_log_file.return_value = Path('/tmp/logs/calculator.log')
        # Instantiate calculator to trigger logging
        log_file = mock_log_file.return_value
        Logger._setup_logging(CalculatorConfig())
        logging_info_mock.assert_any_call(f"Logging initialized at: {log_file}")

@patch('app.logger')
def test_infoLog(logging_info_mock):
    with patch.object(CalculatorConfig, 'log_dir', new_callable=PropertyMock) as mock_log_dir, \
         patch.object(CalculatorConfig, 'log_file', new_callable=PropertyMock) as mock_log_file:
        mock_log_dir.return_value = Path('/tmp/logs')
        mock_log_file.return_value = Path('/tmp/logs/calculator.log')
        Logger.infoLog("test")
        logging_info_mock.assert_any_call("test")
@patch('app.logger')
def test_warnLog(logging_info_mock):
    with patch.object(CalculatorConfig, 'log_dir', new_callable=PropertyMock) as mock_log_dir, \
         patch.object(CalculatorConfig, 'log_file', new_callable=PropertyMock) as mock_log_file:
        mock_log_dir.return_value = Path('/tmp/logs')
        mock_log_file.return_value = Path('/tmp/logs/calculator.log')
        Logger.warnLog("test")
        logging_info_mock.assert_any_call("test")
@patch('app.logger')
def test_errorLog(logging_info_mock):
    with patch.object(CalculatorConfig, 'log_dir', new_callable=PropertyMock) as mock_log_dir, \
         patch.object(CalculatorConfig, 'log_file', new_callable=PropertyMock) as mock_log_file:
        mock_log_dir.return_value = Path('/tmp/logs')
        mock_log_file.return_value = Path('/tmp/logs/calculator.log')
        Logger.errorLog("test")
        logging_info_mock.assert_any_call("test")
'''