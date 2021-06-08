from json import load
from os.path import abspath
from typing import Dict


class BasicHandler:
    NAME = "basic"

    def __init__(self):
        self.config_name = self.NAME
        self.config = self.get_config(self.config_name)

    def get_config(self, name: str) -> Dict:
        with open(abspath(f"configs/{name}.json"), "r", encoding="utf-8") as input_file:
            return load(input_file)