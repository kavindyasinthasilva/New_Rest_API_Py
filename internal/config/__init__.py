from config.appConfig import AppConfig
import logging


class ConfigContainer:
    def __init__(self, app_config):
        self.app_config = app_config


def get_config():
    app_config = AppConfig()
    return ConfigContainer(app_config)
