# -*- coding: utf-8 -*-
import oss2
from wechat import app
from PIL import Image
from wechat.exceptions import InvalidOSSRequestException
import logging
import traceback
LOG = logging.getLogger("wechat")


def upload_image_to_oss(path, image_name):
    try:
        access_key_id = app.config.get("OSS_ACCESS_KEY_ID")
        access_key_secret = app.config.get("OSS_ACCESS_KEY_SECRET")
        if app.config.get("INTERNAL"):
            endpoint = app.config.get("OSS_INTER_ENDPOINT")
        else:
            endpoint = app.config.get("OSS_ENDPOINT")
        bucket_name = app.config.get("OSS_BUCKET")
        bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

        key = 'exam-score/%s.jpg' % image_name
        ret = bucket.put_object_from_file(key, path)

        if ret.status != 200:
            LOG.error("Upload file to aliyun oss error, status:%s, request_id:%s" % (ret.status,
                                                                                     ret.request_id))
            raise InvalidOSSRequestException("Upload image error")
        LOG.info("Upload file to aliyun oss, status:%s, request_id:%s, path:%s" % (ret.status, ret.request_id, key))

        pic_url = "%s/%s" % (app.config.get("IMAGE_URL"), image_name)
        return pic_url
    except Exception as e:
        LOG.error("Upload file to aliyun oss error:%s" % traceback.format_exc())
        raise InvalidOSSRequestException("Upload image error")


def save_image_to_local(image_file, image_name):
    try:
        cache_dir = app.config.get("IMAGE_CACHE_DIR")
        image = Image.open(image_file.stream)
        image_local_name = '%s/%s.jpg' % (cache_dir, image_name)
        image = image.convert("RGB")
        image.save(image_local_name)
        return image_local_name
    except Exception as e:
        LOG.error("Upload file to aliyun oss error:%s" % traceback.format_exc())
        raise