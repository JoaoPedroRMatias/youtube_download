from pytube import YouTube
import moviepy.editor as mp
import re
import os

def directory():
    try:
        dir = './songs'    
        os.makedirs(dir)
    except:
        pass

def converter():
    path = "./songs"

    for file in os.listdir(path):               
        if re.search('mp4', file):                                
            mp4_path = os.path.join(path , file)  
            mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3') 
            new_file = mp.AudioFileClip(mp4_path)  
            new_file.write_audiofile(mp3_path)     
            os.remove(mp4_path)                    
    print("Download Completo!")

def download_music():
    directory()

    while True:
        link = input('LINK YOUTUBE: ')
        yt = YouTube(link)

        ys = yt.streams.filter(only_audio=True).first().download("./songs")

        converter()

download_music()