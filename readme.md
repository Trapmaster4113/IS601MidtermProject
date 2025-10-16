Project Description: 
Calculator application with a history remembering. The Calculator's math functions include: 
 - addition
 - subtraction
 - multiplication
 - division
 - exponents
 - root
 - integer division
 - modulus remainder
 - percentage
 - absolute difference
Non-math functions of the Calculator include: 
 - history (displays the calculation history)
 - clear (clears calculation history)
 - undo (removes the last calculation from the history)
 - redo (redoes the last undone calculation)
 - save (saves history into a file)
 - load (loads history from the file)
 - help (displays all available commands)
 - exit (closes the application)
Additional Calculator Features:
 - Messages in Color to help with readability
    - Red for errors
    - Blue for calculations
    - Green for history
    - Yellow for undo/redo  
To Install: 
1. Clone github repository/Download repository
2. Create Python Virtual Environment (python -m venv venv)
3. Activate Python Virtual Environment (source venv/bin/activate)
4. Install Python Packages (pip install -r requirements.txt)
5. Run the application (python main.py)
Configuration Setup:
 - CALCULATOR_LOG_DIR=str (Creates a folder in the current directory with this name to store the logs file)
 - CALCULATOR_HISTORY_DIR=str (Creates a folder in the current director with this name to store the calculation history file)
 - CALCULATOR_MAX_HISTORY_SIZE=int (Limits the size of the calculation history to this number)
 - CALCULATOR_AUTO_SAVE=bool (Turns on or off the autosave feature of the calculator history)
 - CALCULATOR_PRECISION=int (How many digits after the decimal point the calculator will calculate to)
 - CALCULATOR_MAX_INPUT_VALUE=int (Maximum number size that can be input into the calculator)
 - CALCULATOR_DEFAULT_ENCODING=utf-8 (Default coding language DO NOT CHANGE)
Usage Guide:
 - After setting everything up type into the terminal "python main.py"
 - Then, type any of the above functions to interact with the Calculator application
Testing Instructions
 - Run pytest after installing all Python Dependencies
 - Test logs stored in test_logs
 - Test files stored in directory: "tests"
