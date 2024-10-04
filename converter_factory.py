from abc import ABC, abstractmethod

from exception import ConverterNotFoundException
from file import VideoFile, PhotoFile, AudioFile, File


class ConverterFactory:

    def __init__(self):
        self._converting_formats = {}

    def register_converting_format(self, format_from, format_to, converter):
        self._converting_formats[format_from+"-"+format_to] = converter

    def get_converter(self, format_from, format_to):
        converter = self._converting_formats.get(format_from+"-"+format_to)
        if not converter:
            raise ConverterNotFoundException(format_from+"-"+format_to)
        return converter()


class FormatConverter(ABC):
    @abstractmethod
    def convert(self, file):
        pass

class MkvAviConverter(FormatConverter):

    def convert(self, file):
        # do convert
        return file

class JpegPngConverter(FormatConverter):

    def convert(self, file):
        # do convert
        return file

class Mp3WavConverter(FormatConverter):

    def convert(self, file):
        # do convert
        return file

factory = ConverterFactory()
factory.register_converting_format('mkv', 'avi', MkvAviConverter)
factory.register_converting_format('jpeg', 'png', JpegPngConverter)
factory.register_converting_format('mp3', 'wav', Mp3WavConverter)