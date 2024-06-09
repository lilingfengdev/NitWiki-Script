import os.path

from utils import *
import rtoml as toml

script_license()
print("开始配置!")


@handler(r'config/paper-world-defaults.yml')
def config_paper_world(paper):
    paper["feature-seeds"]["generate-random-seeds-for-all"] = True


@handler(r'leaf_config/leaf_global_config.toml', toml.load, toml.dump)
def config_leaf(leaf):
    if os.path.exists("world"):
        print("你需要删除原有存档才可以使用")
    else:
        leaf["misc"]["use_secure_seed"]["enabled"] = True


def download_antiseedcracker():
    print("开始下载AntiSeedCracker")
    download(r"https://qcymc.cloud/f/L91iQ/AntiSeedCracker-1.2.0.jar",
             "plugins/AntiSeedCracker-1.2.0.jar")
    print("下载完成")


if __name__ == "__main__":
    config_paper_world()
    if ask("开启Leaf安全种子（开启前请读一遍文档）"):
        config_leaf()
    if ask("需要自动下载AntiSeedCracker"):
        download_antiseedcracker()
    exit_()
