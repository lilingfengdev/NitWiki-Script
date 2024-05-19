from utils import *
import rtoml
import urllib.request

script_license()
print("开始配置!")


@handler(r'config/paper-world-defaults.yml')
def config_paper_world(paper):
    paper["feature-seeds"]["generate-random-seeds-for-all"] = True


def config_leaf():
    with open("leaf_config/leaf_global_config.toml", "r+") as f:
        t = rtoml.load(f)
        t["misc"]["use_secure_seed"]["enabled"] = True
    with open("leaf_config/leaf_global_config.toml", "w+") as f:
        rtoml.dump(t, f, pretty=True)


def download_antiseedcracker():
    print("开始下载AntiSeedCracker")
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(r"https://qcymc.cloud/f/L91iQ/AntiSeedCracker-1.2.0.jar",
                               "plugins/AntiSeedCracker-1.2.0.jar")
    print("下载完成")


if __name__ == "__main__":
    config_paper_world()
    if ask("开启Leaf安全种子（开启前请读一遍文档）"):
        config_leaf()
    if ask("需要自动下载AntiSeedCracker"):
        download_antiseedcracker()
    exit_()
