print("Minecraft自动AntiXray")
print("作者:lilingfeng")
import os, sys

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


def antixray_config(config):
    if "anticheat" not in config.keys():
        config["anticheat"] = {"anti-xray": {}}
    if "antixray" not in config["anticheat"].keys():
        config["anticheat"]["antixray"] = {}


def handler(filename):
    def a(func):
        def b():
            print(f"开始配置{filename}")
            if not os.path.exists(filename):
                print(f"{filename}不存在,跳过")
            try:
                with open(filename, 'r+', encoding="utf8") as fp:
                    config = yaml.load(fp, Loader=Loader)
                antixray_config(config)
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
    paper["anticheat"]["anti-xray"] = {
        "enabled": True,
        "engine-mode": 1,
        "hidden-blocks": [
            "chest",
            "coal_ore",
            "deepslate_coal_ore",
            "copper_ore",
            "deepslate_copper_ore",
            "raw_copper_block",
            "diamond_ore",
            "deepslate_diamond_ore",
            "emerald_ore",
            "deepslate_emerald_ore",
            "gold_ore",
            "deepslate_gold_ore",
            "iron_ore",
            "deepslate_iron_ore",
            "raw_iron_block",
            "lapis_ore",
            "deepslate_lapis_ore",
            "redstone_ore",
            "deepslate_redstone_ore"
        ],
        "lava-obscures": False,
        "max-block-height": 64,
        "replacement-blocks": [],
        "update-radius": 2,
        "use-permission": False
    }


@handler(r'world_nether/paper-world.yml')
def config_paper_nether(paper):
    paper["anticheat"]["anti-xray"] = {
        "enabled": True,
        "engine-mode": 1,
        "hidden-blocks": [
            "ancient_debris",
            "nether_gold_ore",
            "nether_quartz_ore"
        ],
        "lava-obscures": False,
        "max-block-height": 128,
        "replacement-blocks": [],
        "update-radius": 2,
        "use-permission": False
    }


@handler(r'world_the_end/paper-world.yml')
def config_paper_end(paper):
    paper["anticheat"]["anti-xray"]["enabled"] = False


if __name__ == "__main__":
    config_paper_world()
    config_paper_nether()
    config_paper_end()
