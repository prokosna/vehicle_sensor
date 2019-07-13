from abc import ABCMeta, abstractmethod



class AppDisplayWriter(metaclass=ABCMeta):
  @abstractmethod
  def send(self, message: str):
    pass
