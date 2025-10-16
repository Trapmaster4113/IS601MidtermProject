import pytest
import datetime
from pathlib import Path
import pandas as pd
from unittest.mock import Mock, patch, PropertyMock
from app.calculator_repl import Calculator_repl
from colorama import Fore, Back, Style, init
from termcolor import colored
# Test REPL Commands (using patches for input/output handling)
@patch('builtins.input', side_effect=['exit'])
@patch('builtins.print')
def test_calculator_repl_exit(mock_print, mock_input):
    with patch('app.calculator.Calculator.save_history') as mock_save_history:
        Calculator_repl()
        mock_save_history.assert_called_once()
        mock_print.assert_any_call(Style.BRIGHT + colored("History saved successfully.", "green"))
        mock_print.assert_any_call(Style.DIM + colored("Goodbye!", "white"))

@patch('builtins.input', side_effect=['help', 'exit'])
@patch('builtins.print')
def test_calculator_repl_help(mock_print, mock_input):
    Calculator_repl()
    mock_print.assert_any_call(Style.BRIGHT + colored("\nAvailable commands:", "blue"))

@patch('builtins.input', side_effect=['add', '2', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_addition(mock_print, mock_input):
    Calculator_repl()
    mock_print.assert_any_call(Style.BRIGHT + colored("\nResult: 5", "blue"))

@patch('builtins.input', side_effect=['sub', '2', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_subtraction(mock_print, mock_input):
    Calculator_repl()
    mock_print.assert_any_call(Style.BRIGHT + colored("\nResult: -1", "blue"))
@patch('builtins.input', side_effect=['sub', '2', '3', 'history', 'exit'])
@patch('builtins.print')
def test_calculator_repl_history(mock_print, mock_input):
    Calculator_repl()
    mock_print.assert_any_call(Style.BRIGHT + colored("\nCalculation History:", "green"))

@patch('builtins.input', side_effect=['clear','exit'])
@patch('builtins.print')
def test_calculator_repl_clear(mock_print, mock_input):
    Calculator_repl()
    mock_print.assert_any_call(Style.BRIGHT + colored("History cleared", "red"))
@patch('builtins.input', side_effect=['sub', '2', '3', 'undo', 'exit'])
@patch('builtins.print')
def test_calculator_repl_undo(mock_print, mock_input):
    Calculator_repl()
    mock_print.assert_any_call(Style.BRIGHT + colored("Operation undone","yellow"))
@patch('builtins.input', side_effect=['undo','exit'])
@patch('builtins.print')
def test_calculator_repl_no_undo(mock_print, mock_input):
    Calculator_repl()
    mock_print.assert_any_call(Style.BRIGHT + colored("Nothing to undo", "red"))
@patch('builtins.input', side_effect=['sub', '2', '3', 'undo','redo','exit'])
@patch('builtins.print')
def test_calculator_repl_redo(mock_print, mock_input):
    Calculator_repl()
    mock_print.assert_any_call(Style.BRIGHT + colored("Operation redone","yellow"))
@patch('builtins.input', side_effect=['redo','exit'])
@patch('builtins.print')
def test_calculator_repl_no_redo(mock_print, mock_input):
    Calculator_repl()
    mock_print.assert_any_call(Style.BRIGHT + colored("Nothing to redo","red"))
@patch('builtins.input', side_effect=['sub', '2', '3', 'save','exit'])
@patch('builtins.print')
def test_calculator_repl_save(mock_print, mock_input):
    Calculator_repl()
    mock_print.assert_any_call(Style.BRIGHT + colored("History saved successfully", "green"))
@patch('builtins.input', side_effect=['sub', '2', '3', 'save','load','exit'])
@patch('builtins.print')
def test_calculator_repl_load(mock_print, mock_input):
    Calculator_repl()
    mock_print.assert_any_call(Style.BRIGHT + colored("History loaded successfully", "green"))
@patch('builtins.input', side_effect=['add', 'cancel', 'exit'])
@patch('builtins.print')
def test_calculator_repl_first_cancel(mock_print, mock_input):
    Calculator_repl()
    mock_print.assert_any_call(Style.BRIGHT + Fore.RED + "Operation cancelled")
@patch('builtins.input', side_effect=['add','5','cancel', 'exit'])
@patch('builtins.print')
def test_calculator_repl_second_cancel(mock_print, mock_input):
    Calculator_repl()
    mock_print.assert_any_call(Style.BRIGHT + Fore.RED + "Operation cancelled")