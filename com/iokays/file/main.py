#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import os


def rename(path: str):
    for x in [x for x in os.listdir(path) if (x.endswith(".MP4") or x.endswith(".mp4"))]:
        print(x + '::::::' + x[0:x.find('-')] + '.mp4')
        os.renames(path+x, path+x+'.mp4')


rename('/Users/pengyuanbin/OneDrive/英文文档/雅思英语基础语法/')

