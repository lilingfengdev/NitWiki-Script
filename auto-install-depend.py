import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor, wait
from utils import *

script_license()

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
    download_task("PlaceholderAPI", "https://ci.extendedclip.com/job/PlaceholderAPI/193/artifact/build/libs"
                                    "/PlaceholderAPI-2.11.6-DEV-193.jar")
    download_task("PlugManx", "https://qcymc.cloud/f/QRCo/PlugManX-2.3.8.jar")
    download_task("WorldEdit", "https://ci.enginehub.org/repository/download/bt10/23766:id/worldedit-bukkit-7.3.1"
                               "-SNAPSHOT-dist.jar?branch=version/7.3.x&guest=1")
    download_task("EssentialsX", "https://qcymc.cloud/f/XBSO/EssentialsX-2.21.0-dev+81-cde7184.jar")
    download_task("Multiverse-Core", "https://ci.onarandombox.com/job/Multiverse-Core/870/artifact/target/Multiverse"
                                     "-Core-4.3.2-SNAPSHOT.jar")
    download_task("ViaVersion", "https://qcymc.cloud/f/VjHg/ViaVersion-4.10.1-SNAPSHOT.jar")
    download_task("ViaBackwards", "https://qcymc.cloud/f/W9ID/ViaBackwards-4.10.1-SNAPSHOT.jar")
    download_task("AuthMe", "https://qcymc.cloud/f/RDF5/AuthMe-5.6.0-FORK-Universal.jar")
    if not os.path.exists("plugins/spark"):
        download_task("spark",
                      "https://ci.lucko.me/job/spark/410/artifact/spark-bukkit/build/libs/spark-1.10.65-bukkit.jar")
    download_task("SkinRestorer", "https://ci.codemc.io/job/SkinsRestorer/job/SkinsRestorer/lastSuccessfulBuild"
                                  "/artifact/build/libs/SkinsRestorer.jar")


if __name__ == "__main__":
    downloads()
    wait(task)
    print("完成！")
    exit_()
