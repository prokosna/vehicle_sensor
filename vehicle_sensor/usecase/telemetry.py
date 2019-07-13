from vehicle_sensor.domain.app_state import AppStatus, AppStateRepository
from vehicle_sensor.domain.sensor import Sensor
from vehicle_sensor.domain.telemetry_sender import Telemetry, TelemetrySender
from typing import Sequence
from logging import getLogger


logger = getLogger(__name__)


class TelemetryUsecase:
    def __init__(self, app_state_repo: AppStateRepository,
                 sensors: Sequence[Sensor],
                 telemetry_sender: TelemetrySender):
        self.app_state_repo = app_state_repo
        self.sensors = sensors
        self.telemetry_sender = telemetry_sender

    def send_telemetries(self, timestamp):
        state = self.app_state_repo.get()
        if state.vehicle_id is None or state.status == AppStatus.STOPPED:
            return

        sensor_values = {}
        for sensor in self.sensors:
            sensor_values.update(sensor.fetch())

        telemetry = Telemetry(state, timestamp, sensor_values)
        self.telemetry_sender.send(telemetry)
