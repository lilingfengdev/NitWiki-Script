import sys, os

try:
    import yaml

    try:
        from yaml import CLoader as Loader, CDumper as Dumper
    except:
        from yaml import FullLoader as Loader, Dumper as Dumper
except ModuleNotFoundError:
    print("PyYaml尚未安装,开始自动安装")
    from pip._internal.cli.main import main as _main

    try:
        _main(["install", "pyyaml", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
    except Exception as e:
        print("安装失败!")
        sys.exit(0)
    import yaml

    try:
        from yaml import CLoader as Loader, CDumper as Dumper
    except:
        from yaml import FullLoader as Loader, Dumper as Dumper


def handler(filename):
    def a(func):
        def b():
            print(f"开始配置{filename}")
            if not os.path.exists(filename):
                print(f"{filename}不存在,跳过")
                return
            try:
                with open(filename, 'r+', encoding="utf8") as fp:
                    config = yaml.load(fp, Loader=Loader)

                func(config)
                with open(filename, 'w+', encoding="utf8") as fp:
                    yaml.dump(config, fp, Dumper=Dumper)
            except Exception as e:
                print(f"错误:{e}")
            else:
                print(f"完成配置{filename}")

        return b

    return a

def exit_():
    print("回车退出")
    input()
    sys.exit(0)