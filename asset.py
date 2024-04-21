# Default asset type
import os


class Asset:
    def __init__(self, name, filename, path):
        self.name = name
        self.filename = filename
        self.path = os.path.normpath(path)

    def __str__(self):
        return f"Name: {self.name}, Filename: {self.filename}, Path: {self.path}"
