import os
import shutil
import subprocess
import sys
import urllib.request
import zipfile
import platform

if platform.system() == 'Windows':
    os.system("pip install rtoml-0.10.0-cp311-none-win_amd64.whl ")
    urllib.request.urlretrieve("https://github.com/upx/upx/releases/download/v4.2.4/upx-4.2.4-win64.zip",
                               "upx.zip")
    zip = zipfile.ZipFile("upx.zip")
    zip.extract("upx-4.2.4-win64/upx.exe", path=os.getcwd())
    shutil.move("upx-4.2.4-win64/upx.exe", os.path.join(os.getcwd(), "upx.exe"))
else:
    os.system("pip install rtoml")

os.system("python3 -m pip install pyyaml install-jdk tqdm psutil requests imageio pygithub rtoml nuitka")

import nuitka.__main__

if os.path.exists("dist"):
    shutil.rmtree("dist")
os.mkdir("dist")
for file in os.listdir(os.path.join(os.getcwd(), "src")):
    filepath = os.path.join(os.getcwd(), "src", file)
    print(f"build {file}", flush=True)
    args = ["nuitka", "--onefile", filepath, "--output-dir=dist", "--quiet", "--pgo", "--remove-output",
            "--assume-yes-for-downloads"]
    if platform.system() == 'Windows':
        args.append("--windows-icon-from-ico=favicon.png")
        args.append("--enable-plugins=upx")
    if platform.system() == 'MacOS':
        args.append("--macos-app-icon=favicon.png")
    if platform.system() == 'Linux':
        args.append("--linux-icon=favicon.png")
    print(" ".join(args))
    sys.argv = args
    nuitka.__main__.main()

# 傻逼
# 狗屎代碼
