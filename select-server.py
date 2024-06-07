import requests
import json
import lxml
import typing

from utils import *

script_license()


class SelectNode:
    def __init__(self, desc, version_map):
        self.desc = desc
        self.map = version_map

    def get_version_list(self):
        return list(self.map.keys())

    def get_url_by_version(self, ver):
        return self.map[ver]


class SelectTree:
    def __init__(self, desc):
        self.desc = desc
        self.children: typing.List[SelectNode] = []

    def register(self, node: SelectNode):
        self.children.append(node)


class Purpur(SelectNode):
    def __init__(self):
        super().__init__("最常用的插件核心(Purpur)(1.16.5+)", {})

    def get_version_list(self):
        return json.loads(requests.get("https://api.purpurmc.org/v2/purpur/").content)["versions"]


class Leaves(SelectNode):
    def __init__(self):
        super().__init__("生电红石插件核心(Leaves)(1.18.2/1.19+)(其他版本请选择Purpur)", {})

    def get_version_list(self):
        return ["1.18.2"] + json.loads(requests.get("https://api.leavesmc.org/projects/leaves/versions/").content)[
            "versions"]


root = SelectTree("")

# 插件

plugin = SelectTree("插件服")
plugin.register(Purpur())
plugin.register(Leaves())

root.register(plugin)

while True:
    if isinstance(root, SelectTree):
        for index, node in enumerate(root.children):
            print(f"{index + 1},{node.desc}")
        i = int(input("你的选择："))
        root = root.children[i - 1]
    else:
        print("支持的版本(可能会加载一段时间）：")
        for ver in root.get_version_list():
            print(ver)
        i = int(input("你的选择："))
        url = root.get_url_by_version(i)
        break
