
class Directories:
    def __init__(self):
        self.directories = []

    def add_directory(self, in_directory):
        self.directories.append(in_directory)

    def clear_all(self):
        self.directories.clear()

    def __str__(self):
        directory_str = "\n".join(str(directory) for directory in self.directories)
        return f"All Directories:\n{directory_str}"
