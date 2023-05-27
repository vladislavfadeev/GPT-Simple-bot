from aiogram.fsm.storage.redis import RedisStorage
from core.config.settigns import app



storage = RedisStorage.from_url(
    'redis://'
    f'{app.storage.username}:'
    f'{app.storage.passwd}@'
    f'{app.storage.host}:'
    f'{app.storage.port}/'
    f'{app.storage.db}'
)