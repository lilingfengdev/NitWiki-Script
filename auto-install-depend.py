import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor, wait
from utils import *

print("Minecraft自动安装常用插件")
print("作者:lilingfeng")

opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0')]
urllib.request.install_opener(opener)
pool = ThreadPoolExecutor(6)
task = []


def download_task(name: str, url: str):
    def _download():
        print(f"开始下载{name}")
        try:
            urllib.request.urlretrieve(url, os.path.join(os.getcwd(), "plugins", name + ".jar"))
        except Exception as e:
            print(f"下载错误{e},在下载{name}")
            print("重试")
            _download()
        else:
            print(f"下载完成{name}")

    task.append(pool.submit(_download))


def downloads():
    # 下载各个插件
    download_task("ProtocolLib", "https://ci.dmulloy2.net/job/ProtocolLib/lastSuccessfulBuild/artifact/build/libs"
                                 "/ProtocolLib.jar")
    download_task("Luckperms", "https://download.luckperms.net/1535/bukkit/loader/LuckPerms-Bukkit-5.4.122.jar")
    download_task("PlaceholderAPI", "https://ci.extendedclip.com/job/PlaceholderAPI/lastSuccessfulBuild/artifact/build"
                                    "/libs/PlaceholderAPI-2.11.6-DEV-191.jar")
    download_task("PlugManx", "https://cloud.qcymc.top/f/wmxTy/PlugManx.jar")
    download_task("WorldEdit", "https://ci.enginehub.org/repository/download/bt10/23766:id/worldedit-bukkit-7.3.1"
                               "-SNAPSHOT-dist.jar?branch=version/7.3.x&guest=1")
    download_task("item-nbt-api", "https://ci.codemc.io/job/Tr7zw/job/Item-NBT-API/lastSuccessfulBuild/artifact/item"
                                  "-nbt-plugin/target/item-nbt-api-plugin-2.12.4-SNAPSHOT.jar")
    download_task("EssentialsX", "https://cloud.qcymc.top/f/voxHA/EssentialsX-2.21.0-dev+78-c60ed56.jar")
    download_task("Multiverse-Core", "https://ci.onarandombox.com/job/Multiverse-Core/lastSuccessfulBuild/artifact"
                                     "/target/Multiverse-Core-4.3.2-SNAPSHOT.jar")
    download_task("ViaVersion", "https://ci.viaversion.com/job/ViaVersion/lastSuccessfulBuild/artifact/build/libs"
                                "/ViaVersion-4.9.4-SNAPSHOT.jar")
    download_task("ViaBackwards", "https://ci.viaversion.com/view/ViaBackwards/job/ViaBackwards/lastSuccessfulBuild"
                                  "/artifact/build/libs/ViaBackwards-4.9.3-SNAPSHOT.jar")
    download_task("AuthMe", "https://cloud.qcymc.top/f/xv5sx/AuthMe-5.6.0-FORK-Universal.jar")
    download_task("CoreProtect", "https://cloud.qcymc.top/f/yrOHL/CoreProtect-22.2.jar")


if __name__ == "__main__":
    downloads()
    wait(task)
    print("完成！")
    exit_()
