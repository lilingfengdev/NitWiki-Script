from textwrap import dedent as _
from utils import *
from psutil import virtual_memory
import platform


script_license()
print("此向导将会自动为你生成启动脚本!")


def detect_jar():
    for i in os.listdir(os.getcwd()):
        if not os.path.isdir(i) and i.endswith(".jar"):
            print(f"找到服务端核心{i}!!")
            return i
    print("没有发现服务端核心")
    return


class VersionMeta:
    pufferfish: bool = False
    leaf: bool = False
    minecraft_version: int = 0


def detect_brand(name):
    meta = VersionMeta()
    a = name.rsplit(".", 1)[0].split("-")
    if len(a) >= 2:
        meta.minecraft_version = int(a[1].split(".")[1])
    else:
        meta.minecraft_version = int(input("您使用的Minecraft版本(格式:1.x或1.x.x)?").split(".")[1])

    if a[0].lower() == "leaf":
        meta.leaf = True
        meta.pufferfish = True
        return meta

    if a[0] in ["pufferfish", "purpur", "leaves", "gale"]:
        meta.pufferfish = True
        return meta

    if a[0] == "paper":
        return meta

    if ask("使用的是Leaf?"):
        meta.leaf = True
        meta.pufferfish = True
        return meta

    if ask("使用的是Pufferfish或下游(Purpur,Gale,Leaves)(不包含Paper)?"):
        meta.pufferfish = True
        return meta


def ask(title):
    select = input(title + "(y/n):")
    if select.lower().startswith("y"):
        return True
    return False


def get_memory():
    return int(virtual_memory().available / (1024 * 1024))  # to MB


def generate_command(server: str, meta: VersionMeta):
    if ask("自动检测使用内存"):
        memory = get_memory() - 1000  # to MB
        if memory / 1024 > 20:
            memory = 20 * 1024
        print(f"自动使用内存{memory}MB")
    else:
        memory = int(input("内存(至少1024MB,不建议为服务器分配少于2048MB的内存)(单位为MB,输入时不带单位):"))
        if memory / 1024 > 20:
            print("不建议为您的服务器分配超过 16-20GB 的内存,给 Java 太多的内存可能会损害服务器的性能")

    if not ask("使用优化参数(推荐使用)?"):
        return f"java -Xms{memory}M -Xmx{memory}M -jar {server}"

    base = f"java -Xms1024M -Xmx{memory}M -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 "

    if meta.pufferfish and meta.minecraft_version >= 18:
        base += "--add-modules=jdk.incubator.vector "

    if meta.leaf:
        base += "-DLeaf.library-download-repo=https://maven.aliyun.com/repository/public "

    base += f"-jar {server} "

    if ask("关闭GUI(GUI没啥用)(推荐关闭)"):
        base += "--nogui"

    return base


def generate_batch(command, restart):
    os_name = platform.system()
    if os_name == "Windows":
        with open("start.bat", "w", encoding="utf8") as fp:
            if restart:
                fp.write(_(f"""
                    @echo off
                    chcp 65001
                    :start
                    echo 开始启动MC服务器
                    {command}
                    echo MC服务器已关闭
                    echo 服务器正在重新启动..。
                    echo 按 CTRL + C 停止。
                    goto :start
                """))
            else:
                fp.write(_(f"""
                    @echo off
                    chcp 65001
                    echo 开始启动MC服务器
                    {command}
                    echo MC服务器已关闭
                    pause
                """))
    elif os_name == "Linux":
        with open("start.sh", "w", encoding="utf8") as fp:
            if restart:
                fp.write(_(f"""
                    #!/bin/bash
                    echo "开始启动MC服务器"
                    {command}
                    echo "MC服务器已关闭"
                    while true; do
                        echo "按 CTRL + C 停止。"
                        {command}
                        sleep 1
                    done
                """))
            else:
                fp.write(_(f"""
                    #!/bin/bash
                    echo "开始启动MC服务器"
                    {command}
                    echo "MC服务器已关闭"
                """))
    else:
        raise OSError("Unsupported operating system")


if __name__ == "__main__":
    server = detect_jar()
    if server is None:
        exit_()
    command = generate_command(server, detect_brand(server))
    generate_batch(command, ask("开启自动重启?"))
    exit_()
