# library.py
from asset import Asset


class Library(Asset):
    def __init__(self, name, filename, path):
        super().__init__(name, filename, path)
