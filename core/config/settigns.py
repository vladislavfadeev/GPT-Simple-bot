from environs import Env
from dataclasses import dataclass



@dataclass
class BotSettings:
    botToken: str
    adminId: int
    baseUrl: str
    authToken: str


@dataclass
class Settings:
    botSetting: BotSettings
    


def get_settings(path: str):
    
    env = Env()
    env.read_env(path)

    return Settings(
        botSetting=BotSettings(
            botToken=env.str("TOKEN"),
            adminId=env.int("ADMIN_ID"),
            baseUrl=env.str("BASE_URL"),
            authToken=env.str("AI_AUTH_TOKEN")
        )
    )


app = get_settings('.env')

