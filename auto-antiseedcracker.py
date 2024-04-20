import urllib.request
import os, sys

print("Minecraft自动AntiSeedCracker")
print("作者:lilingfeng")

try:
    import yaml

    try:
        from yaml import CFullLoader as Loader, CDumper as Dumper
    except:
        from yaml import FullLoader as Loader, Dumper as Dumper
except ModuleNotFoundError:
    print("PyYaml尚未安装,开始自动安装")
    from pip._internal.cli.main import main as _main

    try:
        _main(["install", "pyyaml", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
    except Exception as e:
        print("安装失败!")
        sys.exit(0)
    import yaml

    try:
        from yaml import CFullLoader as Loader, CDumper as Dumper
    except:
        from yaml import FullLoader as Loader, Dumper as Dumper
print("开始配置!")


def handler(filename):
    def a(func):
        def b():
            print(f"开始配置{filename}")
            if not os.path.exists(filename):
                print(f"{filename}不存在,跳过")
            try:
                with open(filename, 'r+', encoding="utf8") as fp:
                    config = yaml.load(fp, Loader=Loader)
                func(config)
                with open(filename, 'w+', encoding="utf8") as fp:
                    yaml.dump(config, fp, Dumper=Dumper)
            except Exception as e:
                print(f"错误:{e}")
            else:
                print(f"完成配置{filename}")

        return b

    return a


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
