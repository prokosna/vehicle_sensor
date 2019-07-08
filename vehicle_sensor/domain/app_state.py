from enum import Enum, auto


class AppStatus(Enum):
    RUNNING = auto()
    STOPPED = auto()


class AppState:
    def __init__(self, vehicle_id, status):
        self.vehicle_id = vehicle_id
        self.status = status


class AppStateRepository:
    def __init__(self):
        self.state = AppState(None, AppStatus.STOPPED)

    def get(self):
        return self.state

    def store(self, state):
        self.state = state
