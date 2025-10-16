from colorama import Fore, Back, Style, init
from termcolor import colored

#Color Class so all other programs that print to the terminal can use static methods to print in color
class Color:
    init()
    #Resets all styles and colors
    @staticmethod
    def reset():
        print(Style.RESET_ALL)
    #Prints to the terminal in a certain color and style. If no style is inputted, default is "bright"
    def printColorOutput(message: str, color: str, style: str = "bright") -> None:
        if not style:
            print(colored(message, color.lower()))
        else:
            match style.lower():
                case "bright":
                    print(Style.BRIGHT + colored(message, color.lower()))
                case "dim":
                    print(Style.DIM + colored(message, color.lower()))
                case "normal":
                    print(Style.NORMAL + colored(message,color.lower()))
        Color.reset()
    #Prints to the terminal in a certain color and style. If no style is inputted, default is "bright". Expects a return input from the user after printing
    def printColorInput(message: str, color: str, style = "bright") -> str:
        if not style:
            inputted = input(colored(message,color))
        else:
            match style.lower():
                case "bright":
                    inputted = input(Style.BRIGHT + colored(message,color.lower()))
                case "dim":
                    inputted = input(Style.DIM + colored(message,color.lower()))
                case "normal":
                    inputted = input(Style.NORMAL + colored(message,color.lower()))
        Color.reset()
        return inputted.lower().strip()
    #Prints a message in a specific style (bright) and color (Red) indicating an error has occurred
    def printError(message:str) -> None:
        print(Style.BRIGHT + Fore.RED + message)
        Color.reset()