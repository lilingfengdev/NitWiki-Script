from urllib import request
import urllib.parse
from utils import *
import json

script_license()
api = "https://api.mclo.gs/1/log"


def update_log(content):
    data = {
        "content": content
    }
    datas = urllib.parse.urlencode(data).encode('utf-8')
    res = json.loads(request.urlopen(request.Request(api, data=datas)).read().decode('utf-8'))
    if res["success"]:
        return res["url"]
    else:
        raise RuntimeError(res["error"])


if __name__ == "__main__":
    print("上传服务端日志")
    if not os.path.exists("logs/latest.log"):
        print("CNM,没启动上传你妈的日志")
    else:
        with open("logs/latest.log", "r", encoding="utf8") as fp:
            try:
                url = update_log(fp.read())
            except RuntimeError as e:
                print(f"日志上传错误！！！{e}")
            else:
                print(f"日志成功上传，访问地址：{url}")
    exit_()
