import io
import os

from utils import *
import zipfile,  shutil
import urllib.request

script_license()


def extract_zipfile():
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve("https://qcymc.cloud/f/lYAfX/temp.zip","temp.zip")
    zip = zipfile.ZipFile("temp.zip")
    zip.extractall(os.path.join(os.getcwd(), "temp"))


def apply_config():
    c = set(os.listdir("temp"))
    for p in os.listdir(os.path.join(os.getcwd(), "plugins")):
        if os.path.isdir(os.path.join(os.getcwd(), "plugins", p)) and (p in c):
            shutil.rmtree(os.path.join(os.getcwd(), "plugins", p))
            shutil.move(os.path.join(os.getcwd(), "temp", p), os.path.join(os.getcwd(), "plugins"))
            print(f"成功应用配置{p}")


if __name__ == "__main__":
    print("导出/下载配置")
    extract_zipfile()
    print("导出完成")
    print("应用配置")
    apply_config()
    print("应用完毕")
    shutil.rmtree("temp")
    os.remove("temp.zip")
    exit_()
