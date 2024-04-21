import os

from directory import Directory
from library import Library
from scene import Scene
from show import Show


class SQReader:

    @staticmethod
    def is_library(path):
        if os.path.basename(path).lower().startswith("lib") and os.path.basename(path).lower().endswith(".dat"):
            return True
        return False

    @staticmethod
    def is_scene(path):
        if os.path.basename(path).lower().startswith("scene") and os.path.basename(path).lower().endswith(".dat"):
            return True
        return False

    @staticmethod
    def is_show(path):
        path = os.path.join(path, "SHOW.DAT")
        if os.path.exists(path):
            return True
        return False

    @staticmethod
    def read_library(path):
        # Check if the file exists
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")

        # Check if the filename matches the required pattern
        filename = os.path.basename(path)
        if not filename.lower().startswith("lib") or not filename.lower().endswith(".dat"):
            raise ValueError("Invalid filename format. Filename should start with 'LIB' and end with '.DAT'.")

        # Read the name from the file
        with open(path, "rb") as file:
            # Seek to the start of the name field
            file.seek(0x00000170)
            name_bytes = file.read(16)
            # Convert bytes to string and strip whitespace
            name = name_bytes.decode("utf-8").strip().strip("\x00")

        # Create and return the library object
        return Library(name, filename, path)

    @staticmethod
    def read_scene(path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")

        # Check if the filename matches the required pattern
        filename = os.path.basename(path)
        if not filename.lower().startswith("scene") or not filename.lower().endswith(".dat"):
            raise ValueError("Invalid filename format. Filename should start with 'SCENE' and end with '.DAT'.")

        with open(path, "rb") as file:
            file.seek(0x00000014)
            name_bytes = file.read(16)
            name = name_bytes.decode("utf-8").strip().strip("\x00")

        return Scene(name, filename, path)

    @staticmethod
    def read_show(path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Folder not found: {path}")

        filename = os.path.basename(path)
        if not filename.lower().startswith("show"):
            raise ValueError("Invalid folder name. It should start with 'SHOW'")

        showfilepath = os.path.join(path, "SHOW.DAT")

        if not os.path.exists(showfilepath):
            raise FileNotFoundError(f"File not found: {path}")

        with open(os.path.join(path, "SHOW.DAT"), "rb") as file:
            name_bytes = file.read(16)
            name = name_bytes.decode("utf-8").strip().strip("\x00")

        show = Show(name, filename, path)

        for temp_filename in os.listdir(path):
            temp_filepath = os.path.join(path, temp_filename)

            if temp_filename.lower().startswith("scene") and temp_filename.lower().endswith(".dat"):
                scene = SQReader.read_scene(temp_filepath)
                show.add_scene(scene)

            if temp_filename.lower().startswith("lib") and temp_filename.lower().endswith(".dat"):
                library = SQReader.read_library(temp_filepath)
                show.add_library(library)

        return show

    @staticmethod
    def scan_folder(path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Folder not found: {path}")

        # If the data is in the AHSQ subfolder, use that, no more scanning
        # (to avoid user mistake of not opening the AHSQ folder)
        if os.path.exists(os.path.join(path, "AHSQ")):
            temp_directory = SQReader.scan_folder(os.path.join(path, "AHSQ"))
            # Update directory name to the parent (AHSQ would not be too recognisable)
            temp_directory.set_name(os.path.basename(path))
            return temp_directory

        temp_directory = Directory(os.path.basename(path), path)

        # Check for libraries folder
        if os.path.exists(os.path.join(path, "LIBRARY")):
            for filename in os.listdir(os.path.join(path, "LIBRARY")):
                file_path = os.path.join(path, "LIBRARY", filename)
                if SQReader.is_library(file_path):
                    temp_directory.add_library(SQReader.read_library(file_path))

        # Check for scenes
        if os.path.exists(os.path.join(path, "SCENES")):
            for filename in os.listdir(os.path.join(path, "SCENES")):
                file_path = os.path.join(path, "SCENES", filename)
                if SQReader.is_library(file_path):
                    temp_directory.add_library(SQReader.read_scene(file_path))

        # Check for shows
        if os.path.exists(os.path.join(path, "SHOWS")):
            for show_folder_name in os.listdir(os.path.join(path, "SHOWS")):
                show_folder_path = os.path.join(path, "SHOWS", show_folder_name)
                if SQReader.is_show(show_folder_path):
                    temp_directory.add_show(SQReader.read_show(show_folder_path))

        # Check for shows not in the SHOWS folder
        for current_path in os.listdir(path):
            current_path = os.path.join(path, current_path)
            if os.path.isdir(current_path) and SQReader.is_show(current_path):
                temp_directory.add_show(SQReader.read_show(current_path))

        # Check for orphan libraries / scenes
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if SQReader.is_library(file_path):
                temp_directory.add_library(SQReader.read_library(file_path))
            if SQReader.is_scene(file_path):
                temp_directory.add_scene(SQReader.read_scene(file_path))

        return temp_directory
