from abc import ABCMeta, abstractmethod


class NoiseTelemetry:
    def __init__(self, decibel):
        self.decibel = decibel


class NoiseSensor(metaclass=ABCMeta):
    @abstractmethod
    def fetch(self) -> NoiseTelemetry:
        pass
