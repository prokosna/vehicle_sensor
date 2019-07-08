import json
from abc import ABCMeta, abstractmethod


class Telemetry:
    def __init__(self, app_state, noise, temperature, vibration, timestamp):
        self.app_state = app_state
        self.noise = noise
        self.temperature = temperature
        self.vibration = vibration
        self.timestamp = timestamp

    def to_json(self):
        d = {"vehicle_id": self.app_state.vehicle_id, "noise": self.noise, "temperature": self.temperature,
             "vibration": self.vibration, "created_at": self.timestamp.isoformat()}
        return json.dumps(d.__dict__)


class TelemetrySender(metaclass=ABCMeta):
    @abstractmethod
    def send(self, telemetry: Telemetry):
        pass
