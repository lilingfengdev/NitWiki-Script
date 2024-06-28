import os
import shutil
import subprocess
import urllib.request
import zipfile
import platform

if platform.system() == 'Windows':
    os.system("python3 -m pip install pyyaml install-jdk tqdm psutil requests pygithub imageio "
              "rtoml-0.10.0-cp311-none-win_amd64.whl nuitka")
    urllib.request.urlretrieve("https://github.com/upx/upx/releases/download/v4.2.4/upx-4.2.4-win64.zip",
                               "upx.zip")
    zip = zipfile.ZipFile("upx.zip")
    zip.extract("upx-4.2.4-win64/upx.exe", path=os.getcwd())
    shutil.move("upx-4.2.4-win64/upx.exe", os.path.join(os.getcwd(), "upx.exe"))
else:
    os.system("python3 -m pip install pyyaml install-jdk tqdm psutil requests imageio pygithub rtoml nuitka")

os.mkdir("dist")
for file in os.listdir(os.path.join(os.getcwd(), "src")):
    filepath = os.path.join(os.getcwd(), "src", file)
    print(f"build {file}", flush=True)
    args = ["python3", "-m", "nuitka", "--lto=yes", "--onefile", filepath, "--output-dir=dist"]
    if platform.system() == 'Windows':
        args.append("--windows-icon-from-ico=favicon.png")
    if platform.system() == 'MacOS':
        args.append("--macos-app-icon=favicon.png")
    subprocess.call(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if platform.system() == 'Windows':
        subprocess.call(["upx.exe", os.path.join(os.getcwd(), "dist", file + ".exe"), "-o",
                         os.path.join(os.getcwd(), "dist", file + ".exe"), "-9", "-q"])
    break
# 傻逼
# 狗屎代碼
