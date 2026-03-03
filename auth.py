#!/usr/bin/env python3
import requests
import time, datetime
import hmac
import hashlib
import base64
from urllib.parse import quote
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET") or ""
print("api_key:", api_key)
print("api_secret:", api_secret)

times = time.mktime(datetime.datetime.now().timetuple())
timestamp = str(int(round(times * 1000)))
sign = base64.b64encode(
    hmac.new(
        bytes(api_secret, "UTF-8"), bytes(timestamp, "UTF-8"), hashlib.sha1
    ).digest()
)

headers = {
    "X-AK-KEY": api_key,
    "X-AK-PIN": sign,
    "X-AK-TS": timestamp,
}

response = requests.get(
    "https://openapi.lixiaoskb.com/services/v4/rest/enterprise/searchEntByName?keyword=" + quote("阿里巴巴"),
    headers=headers,
)

print(response.text)
