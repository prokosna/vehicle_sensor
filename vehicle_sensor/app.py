import signal
import threading

from vehicle_sensor.infra.trigger_time import TriggerTimeConfig, TriggerTime
from vehicle_sensor.usecase.telemetry import TelemetryUsecase


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
        print("interrupted")


if __name__ == '__main__':
    main()
