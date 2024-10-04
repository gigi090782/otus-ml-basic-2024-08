class File:
    def __init__(self, name, size, created_date, owner):
        self.name = name
        self.size = size
        self.created_date = created_date
        self.owner = owner

class AudioFile(File):
    def __init__(self, name, size, created_date, owner, format):
        super().__init__(name, size, created_date, owner)
        self._format = format

    @property
    def format(self):
        return self._format

class VideoFile(File):
    def __init__(self, name, size, created_date, owner,format):
        super().__init__(name, size, created_date, owner)
        self._format = format

    @property
    def format(self):
        return self._format

class PhotoFile(File):
    def __init__(self, name, size, created_date, owner, format):
        super().__init__(name, size, created_date, owner)
        self._format = format

    @property
    def format(self):
        return self._format