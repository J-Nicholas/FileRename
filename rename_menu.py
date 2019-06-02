"""This module contains menus for sorting options
"""
from platform import system
import os
from enum import Enum

class Prompts(Enum):
    SORT_MENU = 1
    SORT_DIRECTION_MENU = 2

class SortType(Enum):
    NAME = 1
    DATE_CREATED = 2
    LAST_MODIFIED = 3
    SIZE = 4
    CUSTOM = 5
    CANCEL = 6

class SortDirection(Enum):
    ASCENDING = 1
    DESCENDING = 2
    CANCEL = 3


SORT_MENU_OPTIONS = 6
SORT_DIRECTION_MENU_OPTIONS = 3


def __show_sort_menu() -> int:
    """Displays a menu asking the user how they would like to sort their files before they are renamed.
    """
    print("How do you want to sort files? Enter a number to make a selection:\n"
          "1: Name\n"
          "2: Date Created\n"
          "3: Last Modified\n"
          "4: Size\n"
          "5: Custom\n"
          "6: Cancel")


def __get_menu_input(menu_range: range) -> int:
    """Gets input from user and returns an int to represent the choice.

    Arguments:
        menu_range -- specifies the valid range of menu choices. Example: 3 menu options -> range(1,4).
    Returns:
        int -- represents the option they picked. 0 if choice was invalid.
    """
    option = input()

    if option.isnumeric() and int(option) > 0 and int(option) in menu_range:
        return int(option)
    else:
        print("\033[31;1;40mError. Invalid input.\033[0m")
        return 0


def menu_prompt(show_menu: Prompts) -> int:
    """Displays a menu and gets appropriate input based on the show_menu value which uses int enums

        Arguments:
            Prompts(Enum) -- Determines which menu to show based on an int value or enum 

        Returns:
            int -- represents the option they picked. 
    """
    sort_choice = 0
    menu_range = 0
    # Type of sorting
    if show_menu == Prompts.SORT_MENU:
        menu_range = range(1, SORT_MENU_OPTIONS+1)
        __show_sort_menu()

    # Direction of sorting
    elif show_menu == Prompts.SORT_DIRECTION_MENU:
        menu_range = range(1, SORT_DIRECTION_MENU_OPTIONS+1)
        __show_direction_prompt()

    while sort_choice == 0:
        sort_choice = __get_menu_input(menu_range)
    return sort_choice


def __show_direction_prompt():
    """Simply shows a menu asking if the files should be sorted in ascending or descending order."""

    print("What direction do you want the files to be sorted?\n"
          "1: Ascending\n"
          "2: Descending\n"
          "3: Cancel")


def clear_terminal() -> None:
    """Clears the terminal appropriately based on the operating system."""

    os.system('cls') if system().lower().startswith(
        "win") else os.system('clear')
