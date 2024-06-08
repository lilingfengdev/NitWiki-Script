import json
from github import Github
import typing

from utils import *

script_license()


class SelectNode:
    def __init__(self, desc, version_map, skip=False):
        self.desc = desc
        self.map = version_map
        self.skip = skip

    def get_version_list(self):
        return list(self.map.keys())

    def get_url_by_version(self, ver):
        return self.map[ver]


class SkipSelectNode(SelectNode):
    def __init__(self, desc, url):
        super().__init__(desc, {}, True)
        self.url = url

    def get_url(self):
        return self.url


class SelectTree:
    def __init__(self, desc):
        self.desc = desc
        self.children: typing.List[typing.Union[SelectNode, SelectTree]] = []


class Purpur(SelectNode):
    def __init__(self):
        super().__init__("最常用的插件核心(Purpur)(1.16.5+)", {})

    def get_version_list(self):
        return json.loads(requests.get("https://api.purpurmc.org/v2/purpur/").content)["versions"]

    def get_url_by_version(self, ver):
        return f"https://api.purpurmc.org/v2/purpur/{ver}/latest/download"


class Leaves(SelectNode):
    def __init__(self):
        super().__init__("生电红石插件核心(Leaves)(1.18.2/1.19+)(其他版本请选择Purpur)", {})

    def get_version_list(self):
        return ["1.18.2"] + json.loads(requests.get("https://api.leavesmc.org/projects/leaves/versions/").content)[
            "versions"]

    def get_url_by_version(self, ver):
        if ver == "1.18.2":
            return "https://qcymc.cloud/f/xG5Cx/Leaves-paperclip-1.18.2-R0.1-SNAPSHOT-reobf.jar"
        id = json.loads(requests.get(f"https://api.leavesmc.org/projects/leaves/versions/{ver}").content)["builds"][-1]
        return f"https://api.leavesmc.org/projects/leaves/versions/{ver}/builds/{id}/downloads/ghproxy"


class Leaf(SelectNode):
    def __init__(self):
        super().__init__("超高性能插件核心(Leaf)(1.19+)", {})

    def get_version_list(self):
        version = []
        github = Github()
        repo = github.get_repo("Winds-Studio/Leaf")
        tags = repo.get_tags()
        for t in tags:
            if t.name.startswith("ver-"):
                version.append(t.name[4:])
        return version

    def get_url_by_version(self, ver):
        github = Github()
        repo = github.get_repo("Winds-Studio/Leaf")
        release = repo.get_release(f"ver-{ver}")
        assets = release.get_assets()
        for a in assets:
            if a.name.lower().startswith("leaf"):
                return a.browser_download_url


class Mohist(SelectNode):
    def __init__(self):
        super().__init__("MC 版本 1.16.5+", {})

    def get_version_list(self):
        jobs = json.loads(requests.get("https://ci.codemc.io/job/MohistMC/api/json").content)["jobs"]
        version_list = []
        for job in jobs:
            if job["name"].startswith("Mohist-") and job["name"][-1].isdigit():
                version_list.append(job["name"][7:])
        return version_list

    def get_url_by_version(self, ver):
        path = json.loads(
            requests.get(f"https://ci.codemc.io/job/MohistMC/job/Mohist-{ver}/lastCompletedBuild/api/json").content)[
            "artifacts"][0]["relativePath"]
        return f"https://ci.codemc.io/job/MohistMC/job/Mohist-{ver}/lastCompletedBuild/artifact/{path}"


root = SelectTree("")

# 插件

plugin = SelectTree("插件服")
plugin1165 = SelectTree("MC 版本1.16.5+")

plugin1165.children = [Purpur(), Leaves(), Leaf()]

plugin1122 = SkipSelectNode("MC 版本1.12.2", "https://qcymc.cloud/f/G6ziA/beast-1.12.2.jar")

plugin188 = SelectTree("MC 版本1.8.8")

panda = SkipSelectNode("PVP服务器", "https://vip.123pan.cn/1821558579/Lingyi/core/pandaspigot-116-mcres.cn.jar")
sport = SkipSelectNode("生存服务器", "https://qcymc.cloud/f/ERGcp/sportpaper-1.8.8-R0.1-SNAPSHOT.jar")

plugin188.children = [panda, sport]

plugin.children = [plugin1165, plugin1122, plugin188]

# 混合

mix = SelectTree("混合服(插件+MOD)")

forge = SelectTree("Forge混合")

forge1710 = SkipSelectNode("MC 版本 1.7.10", "https://qcymc.cloud/f/gJRFG/Crucible-1.7.10-staging-0c25d250-server.jar")
forge1122 = SkipSelectNode("MC 版本 1.12.2", "https://catserver.moe/download/universal")

forge.children = [forge1710, forge1122, Mohist()]

fabric = SelectTree("Fabric混合")

mix.children = [forge, fabric]

root.children = [plugin, mix]

while True:
    if isinstance(root, SelectTree):
        for index, node in enumerate(root.children):
            print(f"\033[92m{index + 1}\033[0m,{node.desc}")
        i = int(input("\033[33m你的选择：\033[0m"))
        root = root.children[i - 1]
    elif isinstance(root, SkipSelectNode):
        url = root.get_url()
        break
    elif isinstance(root, SelectNode):
        print("\033c\033[3J", end='')
        print("\033[92m支持的版本(可能会加载一段时间）：\033[0m")
        for ver in root.get_version_list():
            print(f"\033[96m{ver}\033[0m")
        i = input("\033[33m你的选择：\033[0m")
        url = root.get_url_by_version(i)
        break
print(url)
