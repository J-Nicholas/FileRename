""" 
Purpose:
This application is intended to open a file dialog to allow the user to select multople
files that they wish to rename. It then asks them for a stem name for the files and 
an index will be supplied to the files based on specified sorting method

Author: Johnathan Nicholas 
Date: 20/05/2019
"""
from rename_file_manager import rename_files
from rename_file_manager import list_files
from rename_menu import RenameMenu as menu
from tkinter import filedialog
import tkinter as tk
import sys


print("Welcome to File Re:name\n" +
      "Please select the files that you wish to rename\n")

input("Press Enter to begin.")

# file dialog
root = tk.Tk()
root.withdraw()
files_to_rename = filedialog.askopenfilenames()
root.destroy()

if len(files_to_rename) == 0:
    sys.exit("Did not select any files.\nExiting...")

# sorting
list_files(files_to_rename)
while(True):
    sort_response = input(
        "Would you like to change order of files first? (y/n)")
    if sort_response.lower() == "y":

        sort_choice = menu.get_sort_choice()
        # TODO write sorting functionality
        print("Sort choice:",sort_choice)
        break
    elif sort_response.lower() == "n":
        break
    else:
        print("\033[31;1;40mError. Invalid input.\033[0m")

 # getting new file name stem
new_filenames = input("\x1b[1;36;40mNote that all files will be given the same name plus an index.\033[0m\n"
                      "What would like to rename the files to? ")

if rename_files(files_to_rename, new_filenames):
    print("Success! Renamed files.")

else:
    print("Error. Could not rename files.")
