from abc import abstractmethod, ABC

from converter_factory import ConverterFactory
from exception import ConverterNotFoundException
from file import VideoFile, AudioFile, PhotoFile, File


class Converter(ABC):
    _converter_factory = None

    def __init__(self):
        if not self._converter_factory:
            self._converter_factory = ConverterFactory()

    @abstractmethod
    def convert(self, file:File,format_to ):
        pass

class VideoConverter(Converter):
    def __init__(self):
        super().__init__()

    def convert(self, file:VideoFile, format_to):
        try:
            converter = self._converter_factory.get_converter(file.format, format_to)
            return  converter.convert(file)
        except ConverterNotFoundException:
            print(f"Конвертер не найден для данных форматов {file.format} - {format_to}!")
        except:
            print("Неизвестная ошибка")


class AudioConverter(Converter):
    def __init__(self):
        super().__init__()

    def convert(self, file:AudioFile, format_to):
        try:
            converter = self._converter_factory.get_converter(file.format, format_to)
            return  converter.convert(file)
        except ConverterNotFoundException:
            print(f"Конвертер не найден для данных форматов {file.format} - {format_to}!")
        except:
            print("Неизвестная ошибка")



class PhotoConverter(Converter):

    def __init__(self):
        super().__init__()

    def convert(self, file:PhotoFile, format_to):
        try:
            converter = self._converter_factory.get_converter(file.format, format_to)
            return  converter.convert(file)
        except ConverterNotFoundException:
            print(f"Конвертер не найден для данных форматов {file.format} - {format_to}!")
        except:
            print("Неизвестная ошибка")