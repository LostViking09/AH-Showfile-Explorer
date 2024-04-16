class Directories:
    def __init__(self):
        self.directories = []

    def add_directory(self, directory):
        self.directories.append(directory)

    def __str__(self):
        directory_str = "\n".join(str(directory) for directory in self.directories)
        return f"All Directories:\n{directory_str}"
