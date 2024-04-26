from textwrap import dedent as _
from utils import *
import subprocess

print("Minecraft自动AntiSeedCracker")
print("作者:lilingfeng")
print("此向导将会自动为你生成启动脚本!")


def detect_jar():
    for i in os.listdir(os.getcwd()):
        if not os.path.isdir(i) and i.endswith(".jar"):
            print(f"找到服务端核心{i}!!")
            return i
    print("没有发现服务端核心")
    return


def ask(title):
    select = input(title + "(y/n):")
    if select.lower().startswith("y"):
        return True
    return False


def get_memory():
    output = subprocess.check_output(["wmic", "ComputerSystem", "get", "TotalPhysicalMemory"]).decode('utf-8')
    return int(int(output.strip().split('\n')[1]) / (1024 * 1024))  # to MB


def generate_script(server: str):
    if ask("自动检测使用内存"):
        memory = get_memory() - 100  # to MB
        if memory / 1024 > 20:
            memory = 20 * 1024
        print(f"自动使用内存{memory}MB")
    else:
        memory = int(input("内存(至少1024MB,不建议为服务器分配少于2048MB的内存)(单位为MB,输入时不带单位):"))
        if memory / 1024 > 20:
            print("不建议为您的服务器分配超过 16-20GB 的内存,给 Java 太多的内存可能会损害服务器的性能")

    if not ask("使用优化参数(推荐使用)?"):
        return f"java -Xms1024M -Xmx{memory}M -jar {server}"

    base = f"java -Xms1024M -Xmx{memory}M -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 "

    if ask("使用的是Pufferfish或下游(Purpur,Gale,Leaf,Leaves)?"):
        base += "--add-modules=jdk.incubator.vector "

    if ask("使用的是Leaf?"):
        base += "-DLeaf.library-download-repo=https://maven.aliyun.com/repository/public "

    base += f"-jar {server} "

    if ask("关闭GUI(GUI没啥用)(推荐关闭)"):
        base += "--nogui"

    return base


if __name__ == "__main__":
    server = detect_jar()
    if server is None:
        exit_()
    command = generate_script(server)
    with open("start.bat", "w", encoding="utf8") as fp:
        if ask("开启自动重启?"):
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
    exit_()
