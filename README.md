## 抖音app加密接口
基于安卓app调用加密so文件实现的加密服务器，不保证接口一定可用.
部分接口仅适用于7.0以下版本，建议以5.8版本的参数为基准。

### sign
`以POST方式发送请求到 http://106.12.193.246:8000/sign
参数要求
device_id # 合法的设备
iid       # 合法的
url       # 不携带 _rticket, ts , device_id, iid 的未加密链接`

响应示例
``{'as': 'a1552681083dee3da94255', 'cp': '63d8e65f8f9313d2e1McUg', 'mas': '01656f90dce2caa5a0d24a9cfcb52bdb78acac4c2c9c8626cca6a6', 'x-gorgon': '0300000000001ab50a994f6107bc5d4cd608c36ead277977ddb8', 'time': 1578724824, 'url': 'https://aweme.snssdk.com/aweme/v1/user/?user_id=57833035660&retry_type=no_retry&ac=wifi&channel=wandoujia_aweme1&aid=1128&app_name=aweme&version_code=580&version_name=5.8.0&device_platform=android&ssmix=a&device_type=OPPO+R11+Plus&device_brand=OPPO&language=zh&os_api=22&os_version=5.1.1&resolution=720*1280&dpi=192&update_version_code=5800&mcc_mnc=46002&ts=1578724824&_rticket=1578724824813&device_id=70433914677&iid=99003389687&as=a1552681083dee3da94255&cp=63d8e65f8f9313d2e1McUg&mas=01656f90dce2caa5a0d24a9cfcb52bdb78acac4c2c9c8626cca6a6'}``

数据请求时需要以下请求头

``headers = {
    "X-Khronos": str(time), # 服务器响应中的time字段
    "X-Gorgon": gorgon,
    "User-Agent": "okhttp/3.10.0.1",
    "Cookie": "odintt=1"
}``
## 问题所在
目前本地模拟设备注册，虽然能返回设备信息，但是却无法用于数据抓取，可能需要后续的激活手段，目前暂未找到，希望知情者能告知一下是哪个请求，届时将开放更多接口。。
设备注册地址 GET：http://106.12.193.246:8000/device_id ,该接口返回的都是未激活的新注册的设备信息
## Todo
 - 设备注册 