#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import subprocess

subprocess.Popen(r'cmd /k start Snipaste.exe', cwd='D:/App/Snipaste-2.8.3')
# subprocess.Popen(r'cmd /k start shutdown.cmd', cwd='D:/App/Nacos/nacos-server-2.1.0/bin')
subprocess.Popen(r'cmd /k start startup.cmd -m standalone', cwd='D:/App/Nacos/nacos-server-2.1.0/bin')
subprocess.Popen(r'cmd /k start redis-server.exe', cwd='D:/App/Redis')
