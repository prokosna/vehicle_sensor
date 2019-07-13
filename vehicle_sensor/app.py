import signal
import threading
from logging import basicConfig, getLogger, DEBUG

from vehicle_sensor.infra.trigger_time import TriggerTimeConfig, TriggerTime
from vehicle_sensor.usecase.telemetry import TelemetryUsecase


basicConfig(level=DEBUG)
logger = getLogger(__name__)


def main():
    us = TelemetryUsecase()
    tc = TriggerTimeConfig(3)
    tt = TriggerTime(tc, us)

    lock = threading.Lock()
    t1 = threading.Thread(target=tt.run, args=(lock,))
    t1.start()

    try:
        signal.pause()
    except KeyboardInterrupt as ex:
        tt.stop()
        t1.join()
        logger.info("interrupted")


if __name__ == '__main__':
    main()
