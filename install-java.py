from utils import *
install_package("install-jdk")
import jdk
import os

try:
    jdk.install("8") if ask("服务器版本是否小于等于 1.16.5? ") else jdk.install("19")
except Exception as e:
    print(f"安装失败: {e}")
    exit_()

path = os.path.expanduser("~") + "\\.jdk"
java_path = os.path.join(path, os.listdir(path)[0])

# os.system(f"setx JAVA_HOME {java_path}")
os.system(f'setx "Path" "%Path%;%JAVA_HOME%\\bin" /m')

print("安装完成")
exit_()