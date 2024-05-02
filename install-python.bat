@echo off
chcp 65001
echo SBFactory.newInstance()
echo 开始下载Python
curl -L -o python-installer.exe https://mirrors.huaweicloud.com/python/3.8.10/python-3.8.10.exe
echo 下载完成
echo 开始安装
python-installer.exe /quiet CompileAll=1 SimpleInstallDescription="笨蛋脚本Python自动安装程序" Include_test=0 PrependPath=1
echo 安装完成
echo 清理安装文件
del /Q /S "python-installer.exe"
echo 清理完成
echo 下载前置库
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyyaml psutil
echo 前置库下载完成
pause