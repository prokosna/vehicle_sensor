from abc import ABCMeta, abstractmethod


class TemperatureTelemetry:
    def __init__(self, decibel):
        self.decibel = decibel


class TemperatureSensor(metaclass=ABCMeta):
    @abstractmethod
    def fetch(self) -> TemperatureTelemetry:
        pass
