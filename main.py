from pytube import YouTube
from pytube.cli import on_progress 
import time
import os

isMovie = None
isLink = None
loop = True

def separatePhrase(nameFile):
    file = open(nameFile, "r", encoding='utf-8')
    linesPhrase = file.readlines()
    listPhrases = []
    for lines in linesPhrase:
        lines = lines.rstrip('\n')
        if not (lines.isnumeric()) and lines:
            listPhrases.append(lines)
    file.close()
    return listPhrases

print('*'*100) 
logo = """
 __   _____  _   _ _____ _   _ ___ ___   ___   _____      ___  _ _    ___   _   ___  ___ ___   _____   __
 \ \ / / _ \| | | |_   _| | | | _ ) __| |   \ / _ \ \    / / \| | |  / _ \ /_\ |   \| __| _ \ | _ \ \ / /
  \ V / (_) | |_| | | | | |_| | _ \ _|  | |) | (_) \ \/\/ /| .` | |_| (_) / _ \| |) | _||   /_|  _/\ V / 
   |_| \___/ \___/  |_|  \___/|___/___|_|___/ \___/ \_/\_/ |_|\_|____\___/_/ \_\___/|___|_|_(_)_|   |_|  
                                     |___|                                                               
"""
print('\033[1;31m' + logo + '\033[0m') 

while(loop):
        linkIsValid = False
        while linkIsValid == False:
                linkVideo = input("Enter the video or song link: ")
                linkVideo = str(linkVideo)
                if linkVideo[:24] == "https://www.youtube.com/":
                        linkIsValid = True
                        isLink = False

                elif linkVideo[:17] == "https://youtu.be/":
                        linkIsValid = True
                        isLink = False

                elif linkVideo == "link":
                        linkSeparados = separatePhrase('link.txt')
                        isLink = True
                        linkIsValid = True

                else:
                        print("Invalid Link!")
                        linkIsValid = False
                        isLink = False
        if linkIsValid:
                try:
                        isVideoError = False
                        if isLink == False:
                                video = YouTube(linkVideo,on_progress_callback = on_progress)
                                print(f'Video Title: {video.title}')
                                print(f'Duration: {video.length / 60:.2f} minutes')
                                print(f'Number of views: {video.views}\n')

                except:
                        print("Video unavailable!")
                        isVideoError = True


                if isLink == False:
                        escolha = int(input("1 - to download as video\n2 - to download as song\nChoose: "))
                        if escolha == 1:
                                isMovie = True
                                video = video.streams.get_highest_resolution()
                                print('For the video to have sound and image, it is necessary to download the resolution: {}'.format(video.resolution))
                                video.download('Youtube_Downloader\Video')
                                print("(:")
                                print('*'*100) 

                        elif escolha == 2:
                                isMovie = False
                                musica = YouTube(linkVideo,on_progress_callback=on_progress).streams.filter(only_audio=True).first().download('Youtube_Downloader\Music')
                                print("(:")
                                print('*'*100) 
                                base, ext = os.path.splitext(musica)
                                newFile = base + '.mp3'

                                if not os.path.exists(newFile):
                                        os.rename(musica, newFile)
                                else:
                                        print("This file already exists.")
                                        os.remove(musica)
                        else:
                                print("choose a valid number")
                else:
                        for i in range(len(linkSeparados)):
                                nome = YouTube(linkSeparados[i])
                                print("Starting music download {}/{}: {}".format(i+1, len(linkSeparados), nome.title))
                                try:
                                        musica = YouTube(linkSeparados[i]).streams.filter(only_audio=True).first().download('Youtube_Downloader\Music\Links')
                                        base, ext = os.path.splitext(musica)
                                        newFile = base + '.mp3'

                                        if not os.path.exists(newFile):
                                                os.rename(musica, newFile)
                                        else:
                                                print('This file already exists. trying the next')
                                                os.remove(musica)
                                        
                                except():
                                        print("An unexpected error has occurred.")

                        print("Completed, your music is: {}\Youtube_Downloader\Music\Links".format(os.getcwd()))
                        print("Thanks for using!")
                        print('*'*100)
