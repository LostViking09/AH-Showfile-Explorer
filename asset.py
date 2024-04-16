# Default asset type
class Asset:
    def __init__(self, name, filename, path):
        self.name = name
        self.filename = filename
        self.path = path

    def __str__(self):
        return f"Name: {self.name}, Filename: {self.filename}, Path: {self.path}"
