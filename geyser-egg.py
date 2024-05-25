from utils import *

script_license()


def main():
    if not os.path.exists("plugins/Geyser-Spigot"):
        print("Geyser和Floodgate尚未安装")
        install_geyser()
        print("安装完成,启动服务器,在关闭后执行此脚本")
        exit_()
    print("已安装Geyser和Floodgate")
    setup_geyser()
    setup_floodgate()
    install_extend()


def install_geyser():
    download("https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/spigot",
             "plugins/Geyser-Spigot.jar")

    download("https://download.geysermc.org/v2/projects/floodgate/versions/latest/builds/latest/downloads/spigot",
             "plugins/floodgate.jar")


@handler("plugins/Geyser-Spigot/config.yml")
def setup_geyser(geyser):
    prop = ServerPropLoader()
    server_port = int(prop.data["port"])
    geyser["remote"]["port"] = server_port
    if ask("允许Geyser玩家在地狱上层(y>128)放置方块"):
        geyser["above-bedrock-nether-building"] = True

    if ask("开启XBox成绩获得"):
        geyser["xbox-achievements-enabled"] = True


@handler("plugins/floodgate/config.yml")
def setup_floodgate(floodgate):
    prefix = input("\033[33m基岩版玩家用户名前缀(默认为.,推荐BE_):\033[0m")
    floodgate["username-prefix"] = prefix


def install_extend():
    if ask("安装GeyserOptionalPack(推荐)"):
        download("https://download.geysermc.org/v2/projects/geyseroptionalpack/versions/latest/builds/latest"
                 "/downloads/geyseroptionalpack", "plugins/Geyser-Spigot/packs/geyseroptionalpack.mcpack")


if __name__ == "__main__":
    main()
