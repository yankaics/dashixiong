# -*- coding: utf-8 -*-
LOG_CFG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s: %(message)s[in %(pathname)s:%(lineno)d]'
        }
    },
    'handlers': {
        'wechatHandlers': {
            'class': 'logging.handlers.GroupWriteRotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'filename': './logs/wechat.log',
            'maxBytes': 10485760,
            'backupCount': 100,
            'encoding': 'utf8'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        'wechat': {
            'handlers': ['wechatHandlers', 'console'],
            'level': 'INFO'
        }
    }
}


SQLALCHEMY_DATABASE_URI = 'mysql://root:KingMaster@localhost:3306/dashixiong?charset=utf8'
SQLALCHEMY_POOL_SIZE = 50
SQLALCHEMY_MAX_OVERFLOW = 15

API_PORT = 8080


OSS_ACCESS_KEY_ID = "LTAIurzjmlt3nFud"
OSS_ACCESS_KEY_SECRET = "v3kwc4oTNx4Dk5YpCNaERv8WfFMN7K"
OSS_BUCKET = 'wechatpublic'
OSS_ENDPOINT = 'oss-cn-beijing.aliyuncs.com'
OSS_INTER_ENDPOINT = "oss-cn-beijing-internal.aliyuncs.com"
IMAGE_URL = "http://wechatpublic.oss-cn-beijing.aliyuncs.com/exam-score"

# INTERNAL = True
INTERNAL = False

IMAGE_CACHE_DIR = "./image_cache"
