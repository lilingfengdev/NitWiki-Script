import os.path

import requests

from utils import *
api_url="https://rscdn.imc.rip"

script_license()

def get_zip_path():
    if os.path.exists("plugins/ItemsAdder/output/generated.zip"):
        return "plugins/ItemsAdder/output/generated.zip"
    if os.path.exists("ItemsAdder/output/generated.zip"):
        return "ItemsAdder/output/generated.zip"
    if os.path.exists("output/generated.zip"):
        return "output/generated.zip"
    if os.path.exists("generated.zip"):
        return "generated.zip"
    return None

def main():
    print("欢迎使用笨蛋文档资源包分发")
    key = input("请输入 AuthKey:")
    secret = input("请输入 AuthSecret:")
    path = get_zip_path()
    if path is None:
        path = input("输入资源包路径:")
        if not os.path.exists(path):
            print(f"{path} 不存在")
    else:
        print(f"检测到资源包: {path}")

    print("开始上传")
    file={
        "file":open(path,"rb")
    }
    res=requests.post(f"{api_url}/upload?api-key={key}",
                  files=file,
                  headers={"Auth-Secret":secret})
    if res.status_code==422:
        print("验证失败")
        return
    if res.status_code==401:
        print("验证失败")
        return
    if res.status_code==400:
        print("超过最大文件体积")
        return
    if res.status_code==500:
        print("服务器故障")
        return

    print("上传成功")
    print(f"下载链接:{api_url}/download?api-key={key}")
    if ask("是否进行资源包预热(加快首次下载)"):
        requests.get(f"{api_url}/download?api-key={key}")
        print("预热成功")

main()


