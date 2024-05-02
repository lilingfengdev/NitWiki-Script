import sys, os


def script_license():
    print("Minecraft笨蛋脚本")
    print("作者:lilingfeng")
    print("仓库地址:https://github.com/lilingfengdev/NitWiki-Script")
    print("未经许可,禁止用于商业用途")


def install_package(name):
    print(f"{name}尚未安装,开始自动安装")
    from pip._internal.cli.main import main as _main

    try:
        _main(["install", name, "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
    except:
        print("安装失败!")
        sys.exit(0)


try:
    import yaml

    try:
        from yaml import CLoader as Loader, CDumper as Dumper
    except ImportError:
        from yaml import Loader, Dumper
except ModuleNotFoundError:
    install_package("pyyaml")
    import yaml

    try:
        from yaml import CLoader as Loader, CDumper as Dumper
    except ImportError:
        from yaml import Loader, Dumper


def handler(filename):
    def a(func):
        def b():
            print(f"开始配置{filename}")
            if not os.path.exists(filename):
                print(f"{filename}不存在,跳过")
                return
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


def ask(title):
    select = input(title + "(y/n):")
    if select.lower().startswith("y"):
        return True
    return False


def exit_():
    print("回车退出")
    input()
    sys.exit(0)


class ServerPropLoader:

    def __init__(self):
        self.data = {}
        with open("server.properties", "r") as fp:
            for line in fp.readlines():
                if not line.startswith("#"):
                    k, v = line.split("=", 1)
                    self.data[k] = v.strip()

    def dump(self):
        with open("server.properties", "w") as fp:
            for key in self.data.keys():
                fp.write(key + "=" + str(self.data[key]) + "\n")
