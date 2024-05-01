@echo off
chcp 65001
rem SBFactory.newInstance()
echo 开始下载Python
curl -L -o python-installer.exe https://mirrors.huaweicloud.com/python/3.8.10/python-3.8.10.exe
echo 下载完成
echo 开始安装
python-installer.exe /quiet CompileAll=1 SimpleInstallDescription="笨蛋脚本Python自动安装程序" Include_test=0 PrependPath=1
echo 安装完成
echo 清理安装文件
del /Q python-installer.exe
echo 清理完成
pause