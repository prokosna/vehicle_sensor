from abc import ABCMeta, abstractmethod


class VibrationTelemetry:
    def __init__(self, decibel):
        self.decibel = decibel


class VibrationSensor(metaclass=ABCMeta):
    @abstractmethod
    def fetch(self) -> VibrationTelemetry:
        pass
