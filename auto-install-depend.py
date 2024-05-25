import urllib.request
from utils import *
from p_tqdm import p_map

opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0')]
urllib.request.install_opener(opener)


def download_file(meta):
    name, url = meta
    urllib.request.urlretrieve(url, os.path.join(os.getcwd(), "plugins", name + ".jar"))


def downloads():
    # 下载各个插件
    plugins = [
        ("ProtocolLib",
         "https://ci.dmulloy2.net/job/ProtocolLib/lastSuccessfulBuild/artifact/build/libs/ProtocolLib.jar"),
        ("Luckperms", "https://download.luckperms.net/1535/bukkit/loader/LuckPerms-Bukkit-5.4.122.jar"),
        ("PlaceholderAPI",
         "https://ci.extendedclip.com/job/PlaceholderAPI/193/artifact/build/libs/PlaceholderAPI-2.11.6-DEV-193.jar"),
        ("PlugManx", "https://qcymc.cloud/f/QRCo/PlugManX-2.3.8.jar"),
        ("WorldEdit",
         "https://ci.enginehub.org/repository/download/bt10/23766:id/worldedit-bukkit-7.3.1-SNAPSHOT-dist.jar?branch"
         "=version/7.3.x&guest=1"),
        ("EssentialsX", "https://qcymc.cloud/f/XBSO/EssentialsX-2.21.0-dev+81-cde7184.jar"),
        ("Multiverse-Core",
         "https://ci.onarandombox.com/job/Multiverse-Core/870/artifact/target/Multiverse-Core-4.3.2-SNAPSHOT.jar"),
        ("ViaVersion", "https://qcymc.cloud/f/VjHg/ViaVersion-4.10.1-SNAPSHOT.jar"),
        ("ViaBackwards", "https://qcymc.cloud/f/W9ID/ViaBackwards-4.10.1-SNAPSHOT.jar"),
        ("AuthMe", "https://qcymc.cloud/f/RDF5/AuthMe-5.6.0-FORK-Universal.jar"),
        ("spark", "https://ci.lucko.me/job/spark/410/artifact/spark-bukkit/build/libs/spark-1.10.65-bukkit.jar"),
        ("SkinRestorer",
         "https://ci.codemc.io/job/SkinsRestorer/job/SkinsRestorer/lastSuccessfulBuild/artifact/build/libs"
         "/SkinsRestorer.jar")
    ]
    if not os.path.exists("plugins/spark"):
        plugins.append(("spark", "https://ci.lucko.me/job/spark/410/artifact/spark-bukkit/build/libs/spark-1.10.65"
                                 "-bukkit.jar"))

    p_map(download_file, plugins, num_cpus=4)


if __name__ == "__main__":
    script_license()
    downloads()
    print("完成！")
    exit_()
