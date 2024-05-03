from utils import *

script_license()


def generate_select(selects):
    for index, i in enumerate(selects):
        print(str(index + 1) + ". " + selects[index]["name"])
    select = int(input("请选择:"))
    selects[select - 1]["call"]()


class PluginServer:
    @staticmethod
    def plugin_select():
        print("请选择服务器版本")
        generate_select([{"name": "1.8服务器", "call": PluginServer.select_18},
                         {"name": "1.12.2服务器", "call": PluginServer.select_1122},
                         {"name": "1.16.5以上服务器", "call": PluginServer.select_1165}])

    @staticmethod
    def select_18():
        if ask("PVP服务器"):
            print("PandaSpigot是你的选择!")
        else:
            print("SportPaper是你的选择!")

    @staticmethod
    def select_1122():
        print("Beast是你的选择!")

    @staticmethod
    def select_1165():
        print("请选择服务器类型")
        generate_select([{"name": "生存，RPG,还有一堆端", "call": PluginServer.select_normal},
                         {"name": "红石-生电端", "call": PluginServer.select_redstone}])

    @staticmethod
    def select_normal():
        if ask("需要高性能"):
            print("Leaf是你的选择!")
        else:
            if ask("需要超级强的稳定性(性能并不好)"):
                print("Paper是你的选择!")
            else:
                print("Purpur是你的选择!")

    @staticmethod
    def select_redstone():
        print("Leaves是你的选择!")


class ModServer:
    @staticmethod
    def mod_select():
        print("就Fabric和Forge可以选择，没什么好说的")


class MinixServer:
    @staticmethod
    def minix_select():
        print("选择你的服务器类型")
        generate_select([{"name": "Fabric端", "call": MinixServer.select_fabric},
                         {"name": "Forge端", "call": MinixServer.select_forge}])

    @staticmethod
    def select_fabric():
        print("Banner和ArcLight-Fabric都可以!")

    @staticmethod
    def select_forge():
        print("请选择服务器版本")
        generate_select([{"name": "1.7服务器", "call": MinixServer.select_17},
                         {"name": "1.12.2服务器", "call": MinixServer.select_1122},
                         {"name": "1.16.5以上服务器", "call": MinixServer.select_1165}])

    @staticmethod
    def select_17():
        print("Crucible是你的选择!")

    @staticmethod
    def select_1122():
        print("CatServer是你的选择!")

    @staticmethod
    def select_1165():
        print("Mohist和ArcLight都可以!")


def select_main():
    print("请选择服务器类型")
    generate_select(
        [{"name": "插件端", "call": PluginServer.plugin_select},
         {"name": "混合(插件+模组)端", "call": MinixServer.minix_select},
         {"name": "模组端", "call": ModServer.mod_select}])


if __name__ == "__main__":
    select_main()
    exit_()
