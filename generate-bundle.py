import os
import urllib.request, zipfile, shutil

urllib.request.urlretrieve("https://github.com/upx/upx/releases/download/v4.2.3/upx-4.2.3-win32.zip",
                           "upx-4.2.3-win32.zip")
zip = zipfile.ZipFile("upx-4.2.3-win32.zip")
zip.extract("upx-4.2.3-win32/upx.exe", path=os.getcwd())
shutil.move("upx-4.2.3-win32/upx.exe", os.path.join(os.getcwd(), "upx.exe"))
os.mkdir("dist")
with open("utils.py", "r", encoding="utf8") as util:
    util_context = util.read()
for file in os.listdir(os.getcwd()):
    if file != "utils.py" and file != "generate-bundle.py" and file.endswith(".py") and not os.path.isdir(file):
        print(f"build {file}", flush=True)
        os.system(f"pyinstaller -F {file} ")
        name = os.path.splitext(file)[0]
        shutil.move(os.path.join("build", name, name + ".exe"), 'dist')

# 傻逼
# 狗屎代碼
