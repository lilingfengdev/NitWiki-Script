from utils import *
import urllib.request

print("Minecraft自动AntiSeedCracker")
print("作者:lilingfeng")

print("开始配置!")


@handler(r'config/paper-world-defaults.yml')
def config_paper_world(paper):
    paper["feature-seeds"]["generate-random-seeds-for-all"] = True


def download_antiseedcracker():
    print("开始下载AntiSeedCracker")
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(r"https://cloud.qcymc.top/f/JZnIK/AntiSeedCracker-1.2.0.jar",
                               "plugins/AntiSeedCracker-1.2.0.jar")
    print("下载完成")


if __name__ == "__main__":
    config_paper_world()
    download_antiseedcracker()
