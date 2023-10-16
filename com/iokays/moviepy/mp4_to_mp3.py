#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from moviepy.editor import *
import os


def mp4_to_mp3(path: str):
    mp3_dir = path + '/mp3/'
    os.mkdir(mp3_dir)  # 将歌曲mp3格式存储在mp3这个文件夹中

    for x in [x for x in os.listdir(path) if x.endswith(".MP4") or x.endswith(".mp4")]:
        print("\nFile is", x)
        videofile = VideoFileClip(path + x)
        filename = os.path.splitext(x)[0]  # 获得mp4文件的名称
        print("     Open file:", filename, filename[0:filename.find(' ')])
        audio = videofile.audio
        audio.write_audiofile(mp3_dir + filename + ".mp3")  # 保存mp3的名称
        print("     Write mp3 sucessfully!")


mp4_to_mp3('/Users/pengyuanbin/OneDrive/英文文档/新概念英语/新概念英语第二册/教程讲解/')
