LOGGING_CONFIG = { 
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': { 
        'basic': { 
            'format': '%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
        },
    },
    'handlers': { 
        'console': { 
            'level': 'INFO',
            'formatter': 'basic',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'WARNING',
            'formatter': 'basic',
            'filename': 'GPT-Simple-bot.log',
            'maxBytes': 1048576,
            'backupCount': 5,
            'mode': 'a'
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': [
            'console',
            'file'
        ]
    }
}