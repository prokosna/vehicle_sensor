from abc import ABCMeta, abstractmethod


class AppDisplayWriter(metaclass=ABCMeta):
    @abstractmethod
    def write(self, message: str):
        pass
