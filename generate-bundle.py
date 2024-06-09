import os
import shutil
import urllib.request
import zipfile
import platform
if platform.system() == 'Windows':
    os.system("python3 -m pip install pyyaml install-jdk tqdm psutil requests pygithub "
              "rtoml-0.10.0-cp311-none-win_amd64.whl pyinstaller")
else:
    os.system("python3 -m pip install pyyaml install-jdk tqdm psutil requests pygithub rtoml pyinstaller")


import PyInstaller.__main__
import platform
if platform.system() == 'Windows':
    urllib.request.urlretrieve("https://github.com/upx/upx/releases/download/v4.2.4/upx-4.2.4-win64.zip",
                               "upx.zip")
    zip = zipfile.ZipFile("upx.zip")
    zip.extract("upx-4.2.4-win64/upx.exe", path=os.getcwd())
    shutil.move("upx-4.2.4-win64/upx.exe", os.path.join(os.getcwd(), "upx.exe"))
os.mkdir("dist")
for file in os.listdir(os.getcwd()):
    if file != "utils.py" and file != "generate-bundle.py" and file.endswith(".py") and not os.path.isdir(file):
        print(f"build {file}", flush=True)
        flag = ["-F", file, "--optimize", "2", "-i", "favicon.ico" ]
        if platform.system() != 'Windows':
            flag.append("--strip")
        PyInstaller.__main__.run(flag)
# 傻逼
# 狗屎代碼
