from vehicle_sensor.domain.app_state import AppState, AppStatus, AppStateRepository


class AppStateUsecase:
    def __init__(self, app_state_repo: AppStateRepository):
        self._app_state_repo = app_state_repo

    def update_state(self, vehicle_id: str, status: AppStatus):
        state = AppState(vehicle_id, status)
        self._app_state_repo.store(state)
