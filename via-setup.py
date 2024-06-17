import requests

from utils import *
import json

script_license()


def main():
    if not os.path.exists("plugins/ViaVersion"):
        print("Via尚未安装")
        install_via()
        print("安装完成,启动服务器,在关闭后执行此脚本")
        exit_()
    print("已安装Via")
    install_extend()
    exit_()


def get_path(job_name):
    path = json.loads(
        requests.get(f"https://ci.viaversion.com/job/{job_name}/lastCompletedBuild/api/json").content)[
        "artifacts"][-1]["relativePath"]
    path = f"https://ci.viaversion.com/job/{job_name}/lastCompletedBuild/artifact/{path}"
    return path


def install_via():
    j8 = ask("使用Java8")
    if j8:
        path = get_path("ViaVersion-Java8")
    else:
        path = get_path("ViaVersion-DEV")
    download(path, "plugins/ViaVersion.jar")
    if ask("安装ViaBackward(Via向下兼容)(推荐)"):
        if j8:
            path = get_path("ViaBackwards-Java8")
        else:
            path = get_path("ViaBackwards-DEV")
        download(path, "plugins/ViaBackwards.jar")
    if ask("安装ViaRewind(Via1.7-1.8兼容)"):
        if j8:
            path = get_path("ViaRewind-Java8")
        else:
            path = get_path("ViaRewind-DEV")
        download(path, "plugins/ViaRewind.jar")
        path = get_path("ViaRewind Legacy Support DEV")
        download(path, "plugins/ViaRewind-Legacy-Support.jar")


def install_extend():
    if ask("安装锻造表修复(1.16.5+)"):
        download("https://github.com/ViaVersionAddons/AxSmithing/releases/download/1.7/AxSmithing-1.7-all.jar",
                 "plugins/Via-AxSmithing.jar")
    if ask("安装聊天修复(1.11-)"):
        download("https://github.com/ViaVersionAddons/ViaChatFixer/releases/download/v1.1.0/ViaChatFixer-1.1.0.jar",
                 "plugins/Via-ViaChatFixer.jar")
    if ask("安装Via自动更新"):
        download("https://github.com/NewAmazingPVP/AutoViaUpdater/releases/download/v8.0/AutoViaUpdater-8.0.jar",
                 "plugins/Via-AutoViaUpdater.jar")


if __name__ == '__main__':
    main()
