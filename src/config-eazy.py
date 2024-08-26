from utils import *

script_license()


@handler('server.properties', ServerPropLoader.load, ServerPropLoader.dump)
def config(properties):
    properties["port"] = int(input("输入MC服务器端口(默认25565):"))
    if ask("开启正版验证"):
        properties["online-mode"] = "true"
    else:
        properties["online-mode"] = "false"
    properties["level-seed"] = input("输入种子,为空则随机生成:")
    properties["max-players"] = int(input("输入最大玩家数(默认20):"))
    if ask("开启命令方块"):
        properties["enable-command-block"] = "true"
    else:
        properties["enable-command-block"] = "false"
    properties["allow-flight"] = "true"  # 垃圾玩意,问都不想问
    print("配置完成!")


if __name__ == "__main__":
    config()
    exit_()
