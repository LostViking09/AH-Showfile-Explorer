import os
import tkinter as tk
from tkinter import filedialog


def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt the user to select a directory
    selected_dir_temp = filedialog.askdirectory(title="Select a folder containing AHQU / AHSQ data")

    # Validate selected directory
    if os.path.exists(os.path.join(selected_dir_temp, "AHQU")) or os.path.exists(
            os.path.join(selected_dir_temp, "AHSQ")) or os.path.exists(
        os.path.join(selected_dir_temp, "SCENES")) or os.path.exists(os.path.join(selected_dir_temp, "SHOWS")):
        return selected_dir_temp
    else:
        return 0


def list_to_console(directory):


if __name__ == "__main__":
    directory = select_directory()
    if not directory:
        exit("Error: no directory selected")
    list_to_console(directory)
