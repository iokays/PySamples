#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from moviepy.editor import *
import os


def mp4_to_mp3(path: str):
    if os.path.exists('./mp3'):
        os.mkdir('./mp3')  # 将歌曲mp3格式存储在mp3这个文件夹中

    for x in [x for x in os.listdir(path) if x.endswith(".MP4") or x.endswith(".mp4")]:
        print("\nFile is", x)
        videofile = VideoFileClip(path + x)
        filename = os.path.splitext(x)[0]  # 获得mp4文件的名称
        print("     Open file:", filename)
        audio = videofile.audio
        audio.write_audiofile('../mp3/' + filename + ".mp3")  # 保存mp3的名称
        print("     Write mp3 sucessfully!")


mp4_to_mp3('./')
