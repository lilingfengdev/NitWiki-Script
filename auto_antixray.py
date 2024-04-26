from utils import *
print("Minecraft自动AntiXray")
print("开始配置!")


def antixray_config(config):
    if "anticheat" not in config.keys():
        config["anticheat"] = {"anti-xray": {}}
    if "antixray" not in config["anticheat"].keys():
        config["anticheat"]["antixray"] = {}


@handler(r'config/paper-world-defaults.yml')
def config_paper_world(paper):
    antixray_config(paper)
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
    antixray_config(paper)
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
    antixray_config(paper)
    paper["anticheat"]["anti-xray"]["enabled"] = False


if __name__ == "__main__":
    config_paper_world()
    config_paper_nether()
    config_paper_end()
    exit_()
