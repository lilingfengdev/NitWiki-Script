from utils import *

script_license()


def config():
    prop = ServerPropLoader()
    prop.data["port"] = int(input("输入MC服务器端口(默认25565):"))
    if ask("开启正版验证"):
        prop.data["online-mode"] = "true"
    else:
        prop.data["online-mode"] = "false"
    prop.data["level-seed"] = input("输入种子,为空则随机生成:")
    prop.data["max-players"] = int(input("输入最大玩家数(默认20):"))
    prop.save()


if __name__ == "__main__":
    config()
