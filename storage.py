from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def save(self,file, path):
        pass

    @abstractmethod
    def get(self,path):
        pass

    @abstractmethod
    def delete(self, path):
        pass

class LocalStorage(Storage):

    def save(self, file, path):
        print ("Локальное сохранение файла")

    def get(self, path):
        print ("Локальное получение файла")

    def delete(self, path):
        print ("Локальное удаление файла")


class RemoteStorage(Storage):

    def save(self, file, path):
        print ("Удаленное сохранение файла")

    def get(self, path):
        print ("Удаленное получение файла")

    def delete(self, path):
        print ("Удаленное удаление файла")

class CloudStorage(Storage):

    def save(self, file, path):
        print ("Сохранение файла в облаке")

    def get(self, path):
        print ("Получение файла в облаке")

    def delete(self, path):
        print ("Удаление файла в облаке")