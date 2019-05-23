"""This module contains menus for sorting options
"""


class RenameMenu:
    """Contains numerous menus to display to users renaming their files using FileRename"""
    @staticmethod
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

    @staticmethod
    def __get_sort_menu_input() -> int:
        """Gets input from user and returns an int to represent the choice.

        Returns:
            int -- represents the option they picked. 0 if choice was invalid.
        """
        option = input()

        if not option.isnumeric():
            print("\033[31;1;40mError. Invalid input.\033[0m")
            return 0

        if option.strip() == "1":
            return 1
        elif option.strip() == "2":
            return 2
        elif option.strip() == "3":
            return 3
        elif option.strip() == "4":
            return 4
        elif option.strip() == "5":
            return 5
        elif option.strip() == "6":
            return 6
        else:
            print("\033[31;1;40mError. Invalid input.\033[0m")
            return 0

    @staticmethod
    def get_sort_choice() -> int:
        """Displays a menu asking the user how they would like to sort their files before they are renamed.

            Returns:
                int -- represents the option they picked. 0 if choice was invalid.
        """
        sort_choice = 0
        RenameMenu.__show_sort_menu()
        while sort_choice == 0:
            sort_choice = RenameMenu.__get_sort_menu_input()
        return sort_choice
