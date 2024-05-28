@echo off
chcp 65001
echo 开始下载Python
curl -L -o python-installer.exe https://raw.githubusercontent.com/adang1345/PythonWin7/master/3.11.9/python-3.11.9-amd64-full.exe
echo 下载完成
echo 开始安装
python-installer.exe /quiet CompileAll=1 SimpleInstallDescription="笨蛋脚本Python自动安装程序" Include_test=0 PrependPath=1
echo 安装完成
