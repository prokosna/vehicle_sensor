from coral.cloudiot.core import CloudIot
from coral.enviro.board import EnviroBoard
from luma.core.render import canvas


class CoralEnviroBoard:
    def __init__(self, config_file_path="cloud_config.ini"):
        self._config_file_path = config_file_path
        self._enviro = EnviroBoard()
        self._cloud = CloudIot(config_file_path)

    def draw(self, msg):
        with canvas(self._enviro.display, msg) as draw:
            draw.text((0, 0), msg, fill="white")

    def publish(self, msg):
        if self._cloud.enabled():
            self._cloud.publish_message(msg)
            return
        if self._cloud is not None:
            self.stop()
            self._cloud = CloudIot(self._config_file_path)

    def stop(self):
        self._cloud.__exit__()
