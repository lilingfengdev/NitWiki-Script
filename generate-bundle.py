import os

# 傻逼
# 狗屎代碼
with open("utils.py", "r", encoding="utf8") as util:
    util_context = util.read()
for file in os.listdir(os.getcwd()):
    if file != "utils.py" and file != "generate-bundle.py" and file.endswith(".py") and not os.path.isdir(file):
        with open(file, "r+", encoding="utf8") as raw:
            raw = raw.read()
        raw = raw.replace("from utils import *", util_context)
        with open(file, "w+", encoding="utf8") as new:
            new.write(raw)
