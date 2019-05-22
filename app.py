""" 
Purpose:
This application is intended to open a file dialog to allow the user to select multople
files that they wish to rename. It then asks them for a stem name for the files and 
an index will be supplied to the files based on specified sorting method

Author: Johnathan Nicholas 
Date: 20/05/2019
"""
from file_manager import rename_files
import tkinter as tk
from tkinter import filedialog
import sys

print("Welcome to File Re:name\n" +
      "Please select the files that you wish to rename\n")

input("Press Enter to begin.")

root = tk.Tk()
root.withdraw()
files_to_rename = filedialog.askopenfilenames()
root.destroy()

if len(files_to_rename) == 0:
    sys.exit("Did not select any files.\nExiting...")

new_filenames = input("\x1b[1;36;40mNote that all files will be given the same name plus an index.\n" +
                      "\033[0;0mWhat would like to rename the files to? ")

if rename_files(files_to_rename, new_filenames):
    print("Success! Renamed files.")

else:
    print("Error. Could not rename files.")
