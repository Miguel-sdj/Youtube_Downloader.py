from pytube import YouTube
import sys
import itertools
import threading
import time
import os
import sys
import time

is_movie = None
is_link = None
done = False

def separate_phrase(name_file):
    file = open(name_file, "r", encoding='utf-8')
    lines_phrase = file.readlines()
    list_phrases = []
    for lines in lines_phrase:
        lines = lines.rstrip('\n')
        if not (lines.isnumeric()) and lines:
            list_phrases.append(lines)
    file.close()
    return list_phrases

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDownload Completed!')
    
    if is_movie == True:
        print("\nYour video is in the directory: {}\Youtube_Downloader\Video".format(os.getcwd()))
    else:
        print("\nYour music is in the directory: {}\Youtube_Downloader\Music".format(os.getcwd()))
    print('*'*100)
    time.sleep(20)

t = threading.Thread(target=animate)
print('*'*100)

link_is_valid = False
while link_is_valid == False:
    link_video = input("Enter the video or song link: ")
    link_video = str(link_video)
    if link_video[:24] == "https://www.youtube.com/":
        link_is_valid = True
        is_link = False

    elif link_video[:17] == "https://youtu.be/":
        link_is_valid = True
        is_link = False

    elif link_video == "link":
        links_separados = separate_phrase('link.txt')
        is_link = True
        link_is_valid = True

    else:
        print("Invalid Link!")
        link_is_valid = False
        is_link = False

if link_is_valid:
    try:
        video_error = False
        if is_link == False:
            video = YouTube(link_video)
            print(f'Video Title: {video.title}')
            print(f'Duration: {video.length / 60:.2f} minutes')
            print(f'Number of views: {video.views}\n')

    except:
        print("Video unavailable!")
        video_error = True

    if is_link == False:
        escolha = int(input("1 - to download as video\n2 - to download as song\nChoose: "))
        if escolha == 1:
            is_movie = True
            video = video.streams.get_highest_resolution()
            print('For the video to have sound and image, it is necessary to download the resolution: {}'.format(video.resolution))
            t.start()
            video.download('Youtube_Downloader\Video')
            

        elif escolha == 2:
            is_movie = False
            t.start()

            musica = YouTube(link_video).streams.filter(only_audio=True).first().download('Youtube_Downloader\Music')
            base, ext = os.path.splitext(musica)
            new_file = base + '.mp3'

            if not os.path.exists(new_file):
                os.rename(musica, new_file)
            else:
                print("This file already exists.")
                os.remove(musica)
                os._exit(0)

        else:
            print("choose a valid number")

    else:
        for i in range(len(links_separados)):
            nome = YouTube(links_separados[i])
            print("Starting music download {}/{}: {}".format(i+1, len(links_separados), nome.title))
            try:
                musica = YouTube(links_separados[i]).streams.filter(only_audio=True).first().download('Youtube_Downloader\Music\Links')
                base, ext = os.path.splitext(musica)
                new_file = base + '.mp3'

                if not os.path.exists(new_file):
                    os.rename(musica, new_file)
                else:
                    print('This file already exists. trying the next')
                    os.remove(musica)
                    
            except():
                print("An unexpected error has occurred.")
            
        
        print("Completed, your music is: {}\Youtube_Downloader\Music\Links".format(os.getcwd()))
        print("Thanks for using!")
        print('*'*100)
        time.sleep(10)


done = True
