import json

from utils import *
from urllib import request

opener = request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0')]
request.install_opener(opener)
script_license()


def get_version():
    return input("您想开的Minecraft版本(格式:1.x.x或1.x,比如1.20.4或1.20)?")


def generate_select(selects):
    for index, i in enumerate(selects):
        print(str(index + 1) + ". " + selects[index]["name"])
    select = int(input("请选择:"))
    return selects[select - 1]["call"]()


class PluginServer:
    @staticmethod
    def plugin_select():
        print("请选择服务器版本")
        return generate_select([{"name": "1.8服务器", "call": PluginServer.select_18},
                                {"name": "1.12.2服务器", "call": PluginServer.select_1122},
                                {"name": "1.16.5以上服务器", "call": PluginServer.select_1165}])

    @staticmethod
    def select_18():
        if ask("PVP服务器"):
            print("PandaSpigot是你的选择!")
            return "https://vip.123pan.cn/1821558579/Lingyi/core/pandaspigot-116-mcres.cn.jar"
        else:
            print("SportPaper是你的选择!")
            return "https://qcymc.cloud/f/ERGcp/sportpaper-1.8.8-R0.1-SNAPSHOT.jar"

    @staticmethod
    def select_1122():
        print("Beast是你的选择!")
        return "https://qcymc.cloud/f/G6ziA/beast-1.12.2.jar"

    @staticmethod
    def select_1165():
        print("请选择服务器类型")
        return generate_select([{"name": "生存，RPG,还有一堆端", "call": PluginServer.select_normal},
                                {"name": "红石-生电端", "call": PluginServer.select_redstone}])

    @staticmethod
    def select_normal():
        if ask("需要高性能"):
            print("Leaf是你的选择!(支持1.19.3以上)")
            return f"https://vip.123pan.cn/1821558579/Lingyi/core/leaf/leaf-{get_version()}-mcres.cn.jar"
        else:
            if ask("需要超级强的稳定性(性能并不好)"):
                print("Paper是你的选择!")
                return f"https://vip.123pan.cn/1821558579/Lingyi/core/paper/paper-{get_version()}-mcres.cn.jar"
            else:
                print("Purpur是你的选择!")
                print("此核心目前不支持自动下载")
                print("你可以前往https://mcres.cn/downloads/purpur.html或https://purpurmc.org/downloads/下载")
                exit_()

    @staticmethod
    def select_redstone():
        print("Leaves是你的选择!")
        return f"https://vip.123pan.cn/1821558579/Lingyi/core/leaves/leaves-{get_version()}.jar"


class ModServer:
    @staticmethod
    def mod_select():
        print("就Fabric和Forge可以选择，没什么好说的")
        print("mod目前不支持下载,请自行下载")
        exit_()


class MinixServer:
    @staticmethod
    def minix_select():
        print("选择你的服务器类型")
        return generate_select([{"name": "Fabric端", "call": MinixServer.select_fabric},
                                {"name": "Forge端", "call": MinixServer.select_forge}])

    @staticmethod
    def select_fabric():
        print("Banner和ArcLight-Fabric都可以!")
        print("我们为您选择了Banner")
        print("支持版本：1.19.4,1.20,1.20.1")
        r = request.urlopen(f"https://mohistmc.com/api/v2/projects/banner/{get_version()}/builds").read().decode(
            "utf-8")
        r = json.loads(r)
        return r["builds"][-1]["url"]

    @staticmethod
    def select_forge():
        print("请选择服务器版本")
        return generate_select([{"name": "1.7服务器", "call": MinixServer.select_17},
                                {"name": "1.12.2服务器", "call": MinixServer.select_1122},
                                {"name": "1.16.5以上服务器", "call": MinixServer.select_1165}])

    @staticmethod
    def select_17():
        print("Crucible是你的选择!")
        return "https://qcymc.cloud/f/J6WsK/Crucible-1.7.10-5.4.jar"

    @staticmethod
    def select_1122():
        print("CatServer是你的选择!")
        return "https://vip.123pan.cn/1821558579/Lingyi/core/CatServer-1.12.2-mcres.cn.jar"

    @staticmethod
    def select_1165():
        print("Mohist和ArcLight都可以!")
        print("我们为您自动下载了Mohist")
        print("支持版本:1.7.10,1.12.2,1.16.5,1.18.2,1.19.2,1.19.4,1.20,1.20.1,1.20.2")
        r = request.urlopen(f"https://mohistmc.com/api/v2/projects/mohist/{get_version()}/builds").read().decode(
            "utf-8")
        r = json.loads(r)
        return r["builds"][-1]["url"]


def select_main():
    print("请选择服务器类型")
    return generate_select(
        [{"name": "插件端", "call": PluginServer.plugin_select},
         {"name": "混合(插件+模组)端", "call": MinixServer.minix_select},
         {"name": "模组端", "call": ModServer.mod_select}])


if __name__ == "__main__":
    url = select_main()
    if not ask("自动安装"):
        exit_()
    print("开始下载")
    try:
        request.urlretrieve(url, "server.jar")
    except Exception as e:
        print(f"下载失败: {e}")
    else:
        print("下载完成")
    finally:
        exit_()
