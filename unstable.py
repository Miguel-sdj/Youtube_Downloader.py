from pytube import YouTube
import sys
import itertools
import threading
import time
import os
import sys
import time
from sentence_handling import separate_phrase

is_movie = None
is_link = None
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rCarregando ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDownload Finalizado!')
    if is_movie == True:
        print("\nSeu vídeo se encontra no diretório: {}\Youtube_Downloader\Vídeos".format(os.getcwd()))
    else:
        print("\nSua música se encontra no diretório: {}\Youtube_Downloader\Músicas".format(os.getcwd()))
    print('*'*100)
    time.sleep(20)

t = threading.Thread(target=animate)
print('*'*100)

link_is_valid = False
while link_is_valid == False:
    link_video = input("Digite o link do video: ")
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
        print("Link Inválido!")
        link_is_valid = False
        is_link = False

try:
    if link_is_valid:
        try:
            video_error = False
            if is_link == False:
                video = YouTube(link_video)
                print(f'Título do vídeo: {video.title}')
                print(f'Duração: {video.length / 60:.2f} minutos')
                print(f'Número de views: {video.views}\n')

        except:
            print("Vídeo indisponível!")
            video_error = True

        if is_link == False:
            escolha = int(input("1 - para baixar como vídeo\n2 - para baixar a música\nEscolha: "))
            if escolha == 1:
                is_movie = True
                video = video.streams.get_highest_resolution()
                print('Para que o vídeo tenha som e imagem é necessário baixar na resolução: {}'.format(video.resolution))
                video.download('Youtube_Downloader/Vídeos')
                t.start()

            elif escolha == 2:
                is_movie = False
                t.start()
                musica = YouTube(link_video).streams.filter(only_audio=True).first().download('Youtube_Downloader/Músicas')
                base, ext = os.path.splitext(musica)
                new_file = base + '.mp3'
                os.rename(musica, new_file)

            else:
                print("escolhe um número válido")

        else:
            for i in range(len(links_separados)):
                nome = YouTube(links_separados[i])
                print("Iniciando download da música {}/{}: {}".format(i+1, len(links_separados), nome.title))
                musica = YouTube(links_separados[i]).streams.filter(only_audio=True).first().download('Youtube_Downloader/Músicas/Links')
                base, ext = os.path.splitext(musica)
                new_file = base + '.mp3'
                os.rename(musica, new_file)
                
            print("Concluído, sua musica se encontra: {}\Youtube_Downloader\Músicas\Links".format(os.getcwd()))
            print("Obrigado por usar!")
            print('*'*100)
            time.sleep(10)
except:
    print("Ocorreu um erro, reinicie e tente novamente!")
    time.sleep(5)

done = True