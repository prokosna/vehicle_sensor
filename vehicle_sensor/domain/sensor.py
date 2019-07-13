from abc import ABCMeta, abstractmethod
from typing import Dict


class Sensor(metaclass=ABCMeta):
    @abstractmethod
    def fetch(self) -> Dict:
        pass
