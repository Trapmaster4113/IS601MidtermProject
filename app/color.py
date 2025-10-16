from colorama import Fore, Back, Style, init
from termcolor import colored

class Color:
    init()
    @staticmethod
    def reset():
        print(Style.RESET_ALL)
    def printColorOutput(message: str, color: str, style: str = "bright") -> None:
        if not style:
            print(colored(message, color))
        else:
            match style.lower():
                case "bright":
                    print(Style.BRIGHT + colored(message, color))
                case "dim":
                    print(Style.DIM + colored(message, color))
                case "normal":
                    print(Style.NORMAL + colored(message,color))
        Color.reset()
    def printColorInput(message: str, color: str, style = "bright") -> str:
        if not style:
            inputted = input(colored(message,color))
        else:
            match style.lower():
                case "bright":
                    inputted = input(Style.BRIGHT + colored(message,color))
                case "dim":
                    inputted = input(Style.DIM + colored(message,color))
                case "normal":
                    inputted = input(Style.NORMAL + colored(message,color))
        Color.reset()
        return inputted.lower().strip()
    def printError(message:str) -> None:
        print(Style.BRIGHT + Fore.RED + message)
        Color.reset()