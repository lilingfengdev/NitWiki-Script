from utils import *
import jdk
import os, ctypes

script_license()


def java_install(add_path=False):
    try:
        if ask("安装Java21(推荐在Leaf,Beast上启用)(不支持1.16.5以下"):
            jdk.install("21")
        elif ask("服务器版本是否大于 1.16.5 "):
            jdk.install("19")
        else:
            jdk.install("8")
    except Exception as e:
        print(f"安装失败: {e}")
        exit_()

    path = os.path.expanduser("~") + "\\.jdk"
    java_path = os.path.join(path, os.listdir(path)[0])
    if add_path:
        try:
            kernel32 = ctypes.windll.kernel32
            kernel32.SetEnvironmentVariableW("JAVA_HOME", java_path)
            current_path = os.environ.get('PATH', '')
            new_path = f"{java_path}\\bin;{current_path}"
            kernel32.SetEnvironmentVariableW("Path", new_path)
        except Exception as e:
            print(f"设置环境变量失败: {e}")
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
