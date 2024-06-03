import os
import PyInstaller.__main__
os.mkdir("dist")
for file in os.listdir(os.getcwd()):
    if file != "utils.py" and file != "generate-bundle.py" and file.endswith(".py") and not os.path.isdir(file):
        print(f"build {file}", flush=True)
        PyInstaller.__main__.run(["-F", file, "--optimize", "2", "-i", "favicon.ico", "--exclude-module",
                                  "charset_normalizer,_ctypes,_decimal,_hashlib,_bz2,_lzma,pyexpat,decimal,ctypes,"
                                  "hashlib,bz2,lzma", ])

# 傻逼
# 狗屎代碼
