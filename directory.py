class Directory:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.shows = []
        self.libraries = []
        self.scenes = []

    def add_show(self, show):
        self.shows.append(show)

    def add_library(self, library):
        self.libraries.append(library)

    def add_scene(self, scene):
        self.scenes.append(scene)

    def __str__(self):
        show_str = "\n".join(str(show) for show in self.shows)
        library_str = "\n".join(str(library) for library in self.libraries)
        scene_str = "\n".join(str(scene) for scene in self.scenes)
        return f"Directory: {self.name}, Path: {self.path}\nShows:\n{show_str}\nLibraries:\n{library_str}\nScenes:\n{scene_str}"
