from vehicle_sensor.domain.app_display_writer import AppDisplayWriter
from vehicle_sensor.infra.coral_board import CoralEnviroBoard


class AppDisplayWriterCoral(AppDisplayWriter):
    def __init__(self, coral_enviro_board: CoralEnviroBoard):
        self._coral_enviro_board = coral_enviro_board

    def write(self, message: str):
        self._coral_enviro_board.draw(message)
