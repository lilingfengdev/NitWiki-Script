import json
import subprocess
import sys

import requests
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

    def download(self, version):
        return lambda: download(self.get_url_by_version(version), "server.jar")


class SkipSelectNode(SelectNode):
    def __init__(self, desc, url):
        super().__init__(desc, {}, True)
        self.url = url

    def get_url(self):
        return self.url

    def download(self, version=""):
        return lambda: download(self.get_url(), "server.jar")


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
            return "https://dl.imc.rip/plugins/Leaves-paperclip-1.18.2.jar"
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


class CardBoard(SelectNode):
    def __init__(self):
        super().__init__("Fabric混合", {})

    def get_version_list(self):
        vers = json.loads(requests.get("https://api.modrinth.com/v2/project/cardboard/version").content)
        for ver in vers:
            for game in ver["game_versions"]:
                if game not in self.map.keys():
                    self.map[game] = ver["files"][0]["url"]
        return list(self.map.keys())


class Forge(SelectNode):
    def __init__(self):
        super().__init__("Forge", {})

    def download(self, version):
        def _download():
            build = json.loads(requests.get(f"https://bmclapi2.bangbang93.com/forge/minecraft/{version}").content)[0][
                "build"]
            print("开始下载")
            download(f"https://bmclapi2.bangbang93.com/forge/download/{build}", f"forge-installer.jar")
            download(f"https://bmclapi2.bangbang93.com/version/{version}/server", f"minecraft_server.{version}.jar")
            try:
                subprocess.run(["java", "-jar", "forge-installer.jar", "--installServer"], stdout=subprocess.PIPE,
                               stderr=sys.stderr, check=True)
            except subprocess.CalledProcessError:
                print("安装失败")
            else:
                print("安装完成,开始清理")
            finally:
                os.remove("forge-installer.jar")
                os.remove(f"minecraft_server.{version}.jar")

        return _download


class NeoForge(SelectNode):
    def __init__(self):
        super().__init__("NeoForge", {})

    def download(self, version):
        def _download():
            build: str = \
                json.loads(requests.get(f"https://bmclapi2.bangbang93.com/neoforge/list/{version}").content)[-1][
                    "rawVersion"]
            download(f"https://bmclapi2.bangbang93.com/neoforge/version/{build[9:]}/download/installer.jar",
                     "neoforge-installer.jar")
            download(f"https://bmclapi2.bangbang93.com/version/{version}/server", f"minecraft_server.{version}.jar")
            print("开始安装")
            try:
                subprocess.run(["java", "-jar", "neoforge-installer.jar", "--installServer"], stdout=subprocess.PIPE,
                               stderr=sys.stderr, check=True)
            except subprocess.CalledProcessError:
                print("安装失败")
            else:
                print("安装完成,开始清理")
            finally:
                os.remove("neoforge-installer.jar")
                os.remove(f"minecraft_server.{version}.jar")

        return _download


root = SelectTree("")

# 插件

plugin = SelectTree("插件服")
plugin1165 = SelectTree("MC 版本1.16.5+")

plugin1165.children = [Purpur(), Leaves(), Leaf()]

plugin1122 = SkipSelectNode("MC 版本1.12.2", "https://vip.123pan.cn/1821558579/6492155")

plugin188 = SelectTree("MC 版本1.8.8")

panda = SkipSelectNode("PVP服务器", "https://vip.123pan.cn/1821558579/Lingyi/core/pandaspigot-116-mcres.cn.jar")
sport = SkipSelectNode("生存服务器", "https://vip.123pan.cn/1821558579/6492156")

plugin188.children = [panda, sport]

plugin.children = [plugin1165, plugin1122, plugin188]

# 混合

hybird = SelectTree("混合服(插件+MOD)")

forge = SelectTree("Forge混合")

forge1710 = SkipSelectNode("MC 版本 1.7.10", "https://vip.123pan.cn/1821558579/6492157")
forge1122 = SkipSelectNode("MC 版本 1.12.2", "https://catserver.moe/download/universal")

forge.children = [forge1710, forge1122, Mohist()]

hybird.children = [forge, CardBoard()]

mod = SelectTree("mod服")

mod.children = [Forge(), NeoForge(), SkipSelectNode("Fabric(不要选择这个)", "")]

root.children = [plugin, hybird, mod]

while True:
    if isinstance(root, SelectTree):
        for index, node in enumerate(root.children):
            print(f"\033[92m{index + 1}\033[0m,{node.desc}")
        i = int(input("\033[33m你的选择：\033[0m"))
        root = root.children[i - 1]
    elif isinstance(root, SkipSelectNode):
        d = root.download()
        break
    elif isinstance(root, SelectNode):
        print("\033c\033[3J", end='')
        print("\033[92m支持的版本(可能会加载一段时间）：\033[0m")
        for ver in root.get_version_list():
            print(f"\033[96m{ver}\033[0m")
        i = input("\033[33m你的选择：\033[0m")
        d = root.download(i)
        break

if ask("自动下载?"):
    d()
    print("下载完成")
exit_()
