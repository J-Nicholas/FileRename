

class MenuItem:

    def __init__(self, menu_text:str):
        """Defines a menu item that will be contained in a Menu object
        
        Arguments:
            menu_text {str} -- The menu option to be displayed.
        """
        self.menu_text = menu_text

    def __str__(self):
        return self.menu_text