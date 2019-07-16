from vehicle_sensor.domain.telemetry_sender import Telemetry
from vehicle_sensor.domain.telemetry_sender import TelemetrySender
from vehicle_sensor.infra.coral_board import CoralEnviroBoard


class TelemetrySenderCoral(TelemetrySender):
    def __init__(self, coral_enviro_board: CoralEnviroBoard):
        self._coral_enviro_board = coral_enviro_board

    def send(self, telemetry: Telemetry):
        self._coral_enviro_board.publish(telemetry.to_json())
