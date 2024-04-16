# show.py
from asset import Asset


class Show(Asset):
    def __init__(self, name, filename, path):
        super().__init__(name, filename, path)
        self.scenes = []
        self.libraries = []

    def add_scene(self, scene):
        self.scenes.append(scene)

    def add_library(self, library):
        self.libraries.append(library)

    def __str__(self):
        scene_str = "\n".join(str(scene) for scene in self.scenes)
        library_str = "\n".join(str(library) for library in self.libraries)
        return f"Show: {self.name}, Filename: {self.filename}, Path: {self.path}\nScenes:\n{scene_str}\nLibraries:\n{library_str}"
