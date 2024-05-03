from utils import *

try:
    import jdk
except ModuleNotFoundError:
    install_package("jdk")
    import jdk
import os, ctypes

script_license()


def java_install(add_path=False):
    try:
        jdk.install("8", vendor="Zulu") if ask("服务器版本是否小于等于 1.16.5? ") else jdk.install("19", vendor="Zulu")
    except Exception as e:
        print(f"安装失败: {e}")
        exit_()

    path = os.path.expanduser("~") + "\\.jdk"
    java_path = os.path.join(path, os.listdir(path)[0])
    if add_path:
        os.system(f'chcp 65001&setx JAVA_HOME {java_path}&setx "Path" "%Path%;%JAVA_HOME%\\bin" /m')
    print("安装完成")


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if __name__ == "__main__":
    add_path = ask("添加到环境变量(需要管理员)")
    if not is_admin() and add_path:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit(0)
    java_install()
    exit_()
