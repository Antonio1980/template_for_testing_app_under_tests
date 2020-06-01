import os
import configparser
from allure_ import allure_dir


executor = {
    "buildName": "root project:- 'fx_automation_framework'",
    "type": "Python 3.7, pytest 5.4.2",
    "IDE": "PyCharm 2019.2",
    "Builder": "tox 3.10.0"
}


def get_parser(config):
    parser = configparser.ConfigParser()
    with open(config, mode="r", buffering=-1, closefd=True):
        parser.read(config)
        return parser


def save_environment(env_dir, env_var):
    if not os.path.exists(env_dir):
        os.makedirs(env_dir)
    with open(os.path.join(env_dir + "environment.properties"), "w+") as f:
        f.write(env_var)


class BaseConfig:

    config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "base_config.cfg")
    parser = get_parser(config_file)

    ALLURE_DIR = os.path.join(allure_dir, parser.get("PATH", "allure_dir"))
    GITHUB_URL = parser.get("URLS", "github")
    save_environment(ALLURE_DIR, "env=" + "STAGING")
