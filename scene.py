from asset import Asset


class Scene(Asset):
    def __init__(self, name, filename, path):
        super().__init__(name, filename, path)
