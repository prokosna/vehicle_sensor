import json
from abc import ABCMeta, abstractmethod
from typing import Dict


class Telemetry:
    def __init__(self, app_state, timestamp, sensor_values: Dict):
        self.app_state = app_state
        self.timestamp = timestamp
        self.sensor_values = sensor_values

    def to_json(self):
        payload = {**{"vehicle_id": self.app_state.vehicle_id,
                      "created_at": self.timestamp.isoformat()},
                   **self.sensor_values}
        return json.dumps(payload.__dict__)


class TelemetrySender(metaclass=ABCMeta):
    @abstractmethod
    def send(self, telemetry: Telemetry):
        pass
