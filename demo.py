import requests
url = 'http://106.12.193.246:8000/sign'
url2 = 'https://aweme.snssdk.com/aweme/v1/user/?user_id=57833035660&retry_type=no_retry&ac=wifi&channel=wandoujia_aweme1&aid=1128&app_name=aweme&version_code=580&version_name=5.8.0&device_platform=android&ssmix=a&device_type=OPPO+R11+Plus&device_brand=OPPO&language=zh&os_api=22&os_version=5.1.1&manifest_version_code=580&resolution=720*1280&dpi=192&update_version_code=5800&mcc_mnc=46002'

data = {
    "url": url2,
    "device_id":"70433914677",
    "iid":"99003389687"
    }
response = requests.post(url, data=data).json()
url2 = response.get("url")
time = response.get("time")
gorgon = response.get("x-gorgon")

headers = {
    "X-Khronos": str(time),
    "X-Gorgon": gorgon,
    "User-Agent": "okhttp/3.10.0.1",
    "Cookie": "odintt=1"
}

response = requests.get(url2, headers=headers,verify=False)

