
from src.menu.menu_item import MenuItem


class Menu:
    __options = []

    def __init__(self, option_list: list = None):
        self.options = option_list

    @property
    def options(self) -> list:
        return self.__options

    @options.setter
    def options(self, options) -> None:
        if type(options) is list:
            # Ensure every object is a string
            self.__options = [str(item) for item in options]
        elif options == None:
            self.__options = []
        else:
            self.__options.append(str(options))

    def __str__(self):
        menu_items = ""
        if self.options != []:
            for item in self.options:
                menu_items += item + "\n"
            return menu_items
        else:
            return "The menu has not been given any options yet."

    # TODO write a method to get input based on number of menu items (get_input())
    # i.e.
    # menu.show_options()
    # menu.get_input()


menu = Menu()
