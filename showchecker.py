import os
import tkinter as tk
from tkinter import filedialog

def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt the user to select a directory
    directory = filedialog.askdirectory(title="Select AHQU Folder")

    return directory

def list_show_names_with_scenes(directory):
    shows_folder = os.path.join(directory, "SHOWS")
    orphan_scenes_folder = os.path.join(directory, "SCENES")

    # Check if the SHOWS folder exists
    if not os.path.exists(shows_folder):
        print("SHOWS folder not found.")
        return

    # Get a list of all subdirectories in the SHOWS folder
    show_folders = [f for f in os.listdir(shows_folder) if os.path.isdir(os.path.join(shows_folder, f))]

    if not show_folders:
        print("No shows found.")
        return

    #print("List of shows with scenes:")
    for show_folder in show_folders:
        show_dat_file = os.path.join(shows_folder, show_folder, "SHOW.DAT")

        # Check if the SHOW.DAT file exists
        if os.path.exists(show_dat_file):
            with open(show_dat_file, "rb") as file:
                # Read the first 16 bytes which represent the show name
                show_name_bytes = file.read(16)
                try:
                    show_name = show_name_bytes.decode("utf-8")
                except UnicodeDecodeError:
                    print(f"Cannot decode show name for {show_folder}.")
                    continue

                # Print the show folder name and show name
                print(f"")
                #print(f"--------------------------------------")
                print(f"")
                print(f"- Show: [{show_folder}] > {show_name}")
                print(f"")


                # List scenes in the show folder
                scenes_folder = os.path.join(shows_folder, show_folder)
                scene_files = [f for f in os.listdir(scenes_folder) if f.startswith("SCENE") and f.endswith(".DAT")]
                if scene_files:
                    #print("\tScenes:")
                    for scene_file in scene_files:
                        scene_file_path = os.path.join(scenes_folder, scene_file)
                        with open(scene_file_path, "rb") as scene_file_content:
                            # Read the scene name from byte offset 8
                            scene_file_content.seek(8)
                            scene_name_bytes = scene_file_content.read(16)
                            try:
                                scene_name = scene_name_bytes.decode("utf-8")
                            except UnicodeDecodeError:
                                print(f"    Cannot decode scene name for {scene_file}.")
                                continue
                            print(f"    \t- [{scene_file}] > {scene_name}")

    #List orphan scenes
    # Print the show folder name and show name
    print(f"")
    print(f"")
    print(f"- Orphan scenes in [SCENES] folder:")
    print(f"")
    scene_files = [f for f in os.listdir(orphan_scenes_folder) if f.startswith("SCENE") and f.endswith(".DAT")]
    if scene_files:
        #print("\tScenes:")
        for scene_file in scene_files:
            scene_file_path = os.path.join(orphan_scenes_folder, scene_file)
            with open(scene_file_path, "rb") as scene_file_content:
                # Read the scene name from byte offset 8
                scene_file_content.seek(8)
                scene_name_bytes = scene_file_content.read(16)
                try:
                    scene_name = scene_name_bytes.decode("utf-8")
                except UnicodeDecodeError:
                    print(f"    Cannot decode scene name for {scene_file}.")
                    continue
                print(f"    \t- [{scene_file}] > {scene_name}")
    print(f"")
    print(f"")


if __name__ == "__main__":
    directory = select_directory()
    if directory:
        list_show_names_with_scenes(directory)
