import os.path
from utils import *
import subprocess
import ctypes

script_license()

print("开始安装LiteLoaderBDS!")


def install_runtime():
    print("开始下载VC常用运行库")
    download("https://cloud.wujiyan.cc/f/D0DIW/MSVBCRT.AIO.2024.08.16.exe", "vcruntime-install.exe")
    print("下载完成")
    print("开始安装VC常用运行库")
    subprocess.run(["vcruntime-install.exe", "/VERYSILENT"], stdout=subprocess.PIPE, stderr=sys.stderr, check=True)
    print("安装完成")
    print("开始删除VC常用运行库安装文件")
    os.remove("vcruntime-install.exe")
    print("删除完成")


def install_lip():
    print("开始下载Lip")
    download("https://cloud.wujiyan.cc/f/06BSk/lip-windows-amd64-setup.exe", "lip-install.exe")
    print("下载完成")
    print("开始安装Lip")
    subprocess.run(["lip-install.exe", "/S"], stdout=subprocess.PIPE, stderr=sys.stderr, check=True)
    print("安装完成")
    print("开始删除Lip安装文件")
    os.remove("lip-install.exe")
    print("删除完成")
    print("开始配置代理")
    subprocess.run(["lip", "config", "GoModuleProxyURL", "https://goproxy.cn"], stdout=subprocess.PIPE,
                   stderr=sys.stderr, check=True)
    subprocess.run(["lip", "config", "GitHubMirrorURL", "https://github.bibk.top"], stdout=subprocess.PIPE,
                   stderr=sys.stderr, check=True)
    print("代理配置完成")


def install_levi():
    install_dir = input("输入服务器的安装目录(默认为BedrockServer):")
    if install_dir == "":
        install_dir = "BedrockServer"
    os.mkdir(install_dir)
    os.chdir(install_dir)
    print("开始安装服务器")
    subprocess.run(["lip", "install", "github.com/LiteLDev/LeviLamina"], stdout=subprocess.PIPE, stderr=sys.stderr,
                   check=True)
    print("安装完成")
    os.chdir(os.path.pardir)


def run_admin():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("请以管理员身份运行")
        print("用于安装运行库和Lip")
        exit_()


if __name__ == "__main__":
    run_admin()
    install_runtime()
    install_lip()
    install_levi()
    print("安装完成")
    print("要启动服务器，只需运行 bedrock_server_mod.exe")
    exit_()
