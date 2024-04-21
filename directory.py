import os


class Directory:
    def __init__(self, name, path):
        self.name = name
        self.path = os.path.normpath(path)
        self.shows = []
        self.libraries = []
        self.scenes = []

    def add_show(self, show):
        self.shows.append(show)

    def add_library(self, in_library):
        self.libraries.append(in_library)

    def add_scene(self, scene):
        self.scenes.append(scene)

    def set_name(self, name):
        self.name = name

    def __str__(self):
        show_str = "\n".join(str(show) for show in self.shows)
        library_str = "\n".join(str(library) for library in self.libraries)
        scene_str = "\n".join(str(scene) for scene in self.scenes)
        return f"Directory: {self.name}, Path: {self.path}\nShows:\n{show_str}\nLibraries:\n{library_str}\nScenes:\n{scene_str}"
