import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from directory import Directory
from directories import Directories
from qureader import QuReader

dir_storage = Directories()


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Main Application")

        # Create a top menu bar
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)
        self.option_add("*tearOff", False)

        # Create a "File" menu
        self.file_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.open_qu_menu = tk.Menu(self.file_menu)
        self.file_menu.add_cascade(label="Open - Qu", menu=self.open_qu_menu)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)

        # Create an "Open - Qu" submenu
        self.open_qu_menu.add_command(label="Open * folder")
        self.open_qu_menu.add_command(label="Open AHQU folder")
        self.open_qu_menu.add_command(label="Open SHOW folder", command=self.open_qu_show)

        # Create an "About" menu
        self.about_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="About", menu=self.about_menu)
        self.about_menu.add_command(label="About", command=self.show_about)

    def open_qu_show(self):
        folder_path = filedialog.askdirectory(title="Select a SHOW folder")
        if folder_path:
            temp_dir = Directory(os.path.basename(folder_path), folder_path)
            temp_dir.add_show(QuReader.read_show(folder_path))
            dir_storage.add_directory(temp_dir)
            print("cica")

    def open_qu(self):
        folder_path = filedialog.askdirectory(title="Select a folder containing AHQU data")
        if folder_path:
            temp_dir = Directory(os.path.basename(folder_path), folder_path)

            # Check for Library folder
            if os.path.exists(os.path.join(folder_path, "LIBRARY")):
                temp_dir.add_library(QuReader.read_library(folder_path))

    def exit_app(self):
        self.destroy()

    def show_about(self):
        messagebox.showinfo("About", "Made with love")


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
