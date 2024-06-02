import os
import shutil
import urllib.request
import zipfile

import PyInstaller.__main__

urllib.request.urlretrieve("https://github.com/upx/upx/releases/download/v4.2.4/upx-4.2.4-win64.zip",
                           "upx.zip")
zip = zipfile.ZipFile("upx.zip")
zip.extract("upx-4.2.4-win64/upx.exe", path=os.getcwd())
shutil.move("upx-4.2.4-win64/upx.exe", os.path.join(os.getcwd(), "upx.exe"))
os.mkdir("dist")
for file in os.listdir(os.getcwd()):
    if file != "utils.py" and file != "generate-bundle.py" and file.endswith(".py") and not os.path.isdir(file):
        print(f"build {file}", flush=True)
        PyInstaller.__main__.run(["-F", file, "--optimize", "2", "-i", "favicon.ico", "--exclude-module",
                                  "charset_normalizer,_ctypes,_decimal,_hashlib,_bz2,_lzma,pyexpat,decimal,ctypes,"
                                  "hashlib,bz2,lzma", ])

# 傻逼
# 狗屎代碼
