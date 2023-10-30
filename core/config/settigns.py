from environs import Env
from dataclasses import dataclass


@dataclass
class StateStorage:
    username: str
    passwd: str
    host: str
    port: int
    db: int


@dataclass
class BotSettings:
    botToken: str
    adminId: int
    baseUrl: str
    authToken: str


@dataclass
class Settings:
    botSetting: BotSettings
    storage: StateStorage


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        botSetting=BotSettings(
            botToken=env.str("TOKEN"),
            adminId=env.int("ADMIN_ID"),
            baseUrl=env.str("BASE_URL"),
            authToken=env.str("AI_AUTH_TOKEN"),
        ),
        storage=StateStorage(
            username=env.str("USERNAME"),
            passwd=env.str("PASSWD"),
            host=env.str("HOST"),
            port=env.int("PORT"),
            db=env.int("DB"),
        ),
    )


app = get_settings(".env")
