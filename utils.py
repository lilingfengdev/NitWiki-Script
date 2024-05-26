import sys, os
import yaml, requests, tqdm

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def script_license():
    print("\033[92mMinecraft笨蛋脚本\033[0m")
    print("\033[92m作者:lilingfeng\033[0m")
    print("\033[92m仓库地址:https://github.com/lilingfengdev/NitWiki-Script\033[0m")
    print("\033[91m未经许可,禁止用于商业用途\033[0m")


def handler(filename):
    def a(func):
        def b(*args, **kwargs):
            print(f"开始配置{filename}")
            if not os.path.exists(filename):
                print(f"{filename}不存在,跳过")
                return
            try:
                with open(filename, 'r+', encoding="utf8") as fp:
                    config = yaml.load(fp, Loader=Loader)

                func(config, *args, **kwargs)
                with open(filename, 'w+', encoding="utf8") as fp:
                    yaml.dump(config, fp, Dumper=Dumper)
            except Exception as e:
                print(f"错误:{e}")
            else:
                print(f"完成配置{filename}")

        return b

    return a


def ask(title):
    YELLOW = '\033[33m'
    RESET = '\033[0m'
    title = f"{YELLOW}{title}{RESET}"
    select = input(f"{title}(y/n): ")
    if select.lower().startswith("y"):
        return True
    return False


def exit_():
    print("回车退出")
    input()
    sys.exit(0)


class ServerPropLoader:

    def __init__(self):
        self.data = {}
        with open("server.properties", "r") as fp:
            for line in fp.readlines():
                if not line.startswith("#"):
                    k, v = line.split("=", 1)
                    self.data[k] = v.strip()

    def save(self):
        with open("server.properties", "w") as fp:
            for key in self.data.keys():
                fp.write(key + "=" + str(self.data[key]) + "\n")


def download(url, local_filepath):
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/111.0.0.0 Safari/537.36"
    }
    try:
        with requests.get(url, stream=True, headers=headers) as r:
            r.raise_for_status()
            size = int(r.headers["Content-Length"])
            chunk_size = 8192
            with tqdm.tqdm(
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024,
                    miniters=1,
                    desc=f"下载文件 {local_filepath}",
                    total=size,
            ) as pbar:
                with open(local_filepath, "wb") as f:
                    for chunk in r.iter_content(chunk_size=chunk_size):
                        f.write(chunk)
                        pbar.update(len(chunk))
    except Exception as e:
        print(f"下载错误:{e}")
