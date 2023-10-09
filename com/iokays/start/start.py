#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import subprocess
import platform

sys_platform = platform.platform().lower()
print(sys_platform)

if "windows" in sys_platform:
    subprocess.Popen(r'cmd /k start Snipaste.exe', cwd='D:/App/Snipaste-2.8.3')
    # subprocess.Popen(r'cmd /k start shutdown.cmd', cwd='D:/App/Nacos/nacos-server-2.1.0/bin')
    subprocess.Popen(r'cmd /k start startup.cmd -m standalone', cwd='D:/App/Nacos/nacos-server-2.1.0/bin')
    subprocess.Popen(r'cmd /k start redis-server.exe', cwd='D:/App/Redis')

if "mac" in sys_platform:
    os.system("brew install ffmpeg")







