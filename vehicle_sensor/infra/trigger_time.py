import time
from datetime import datetime

from vehicle_sensor.usecase.telemetry import TelemetryUsecase


class TriggerTimeConfig:
    def __init__(self, interval):
        self.interval = interval


class TriggerTime:
    def __init__(self, conf: TriggerTimeConfig, telemetry_usecase: TelemetryUsecase):
        self._conf = conf
        self._us = telemetry_usecase
        self._is_canceled = True

    def run(self, lock):
        self._is_canceled = False
        while not self._is_canceled:
            start = datetime.now()
            with lock:
                self._us.send_telemetries(start)
            end = datetime.now()
            duration = self._conf.interval - (end - start).total_seconds()
            time.sleep(duration)

    def stop(self):
        self._is_canceled = True
