import yaml
import os
import logging

YAML_FILE_PATH = 'app.yaml'


class AppConfig:
    _instance = None
    _config = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppConfig, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        yaml_dir = os.path.abspath("./yaml")

        # Read the YAML data from app.yaml in the /yaml directory
        yaml_path = os.path.join(yaml_dir, YAML_FILE_PATH)

        try:
            with open(yaml_path, 'r') as file:
                data = yaml.safe_load(file)

                # Ensure data is a dictionary
                if not isinstance(data, dict):
                    raise ValueError("Invalid YAML format. Expected a dictionary.")

                if 'port' not in data:
                    raise ValueError("Port is not defined.")

                self._config = data
                print("app.yaml -", data)

        except Exception as e:
            print(f"Error loading YAML file: {e}")
            self._config = None

    @property
    def port(self):
        return self._config.get('port', None)
