from vehicle_sensor.domain.app_state import AppStatus, AppStateRepository
from vehicle_sensor.domain.noise_sensor import NoiseSensor
from vehicle_sensor.domain.telemetry_sender import Telemetry, TelemetrySender
from vehicle_sensor.domain.temperature_sensor import TemperatureSensor
from vehicle_sensor.domain.vibration_sensor import VibrationSensor


class TelemetryUsecase:
    def __init__(self, app_state_repo: AppStateRepository, noise_sensor: NoiseSensor,
                 temperature_sensor: TemperatureSensor, vibration_sensor: VibrationSensor,
                 telemetry_sender: TelemetrySender):
        self.app_state_repo = app_state_repo
        self.noise_sensor = noise_sensor
        self.temperature_sensor = temperature_sensor
        self.vibration_sensor = vibration_sensor
        self.telemetry_sender = telemetry_sender

    def send_telemetries(self, timestamp):
        state = self.app_state_repo.get()
        if state.vehicle_id is None or state.status == AppStatus.STOPPED:
            return

        noise = self.noise_sensor.fetch()
        temp = self.temperature_sensor.fetch()
        vib = self.vibration_sensor.fetch()

        telemetry = Telemetry(state, noise, temp, vib, timestamp)
        self.telemetry_sender.send(telemetry)
