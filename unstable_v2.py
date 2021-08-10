import os
import PySimpleGUI as sg
import time
from pytube import YouTube

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Link do video do youtube'), sg.Input()],
            [sg.Button('Baixar Música')],
            [sg.Output(size=(70, 10))]
        ]

        janela = sg.Window("Dados do usuário").layout(layout)

        self.button, self.values = janela.Read()

    def Iniciar(self):
        link_youtube = self.values[0]
        video = YouTube(link_youtube)
        print(f'Título do vídeo: {video.title}')
        print(f'Duração: {video.length / 60:.2f} minutos')
        print(f'Número de views: {video.views}\n')
        print("Aguarde...")
        
        if link_youtube[:24] == "https://www.youtube.com/":
            link_is_valid = True

        elif link_youtube[:17] == "https://youtu.be/":
            link_is_valid = True

        else:
            print("Link Inválido!")
            time.sleep(10)
            link_is_valid = False

        if link_is_valid == True:
            start_time = time.time()
            musica = YouTube(link_youtube).streams.filter(only_audio=True).first().download('Youtube_Downloader/Músicas')
            base, ext = os.path.splitext(musica)
            new_file = base + '.mp3'
            os.rename(musica, new_file)
            print("\nSua música se encontra no diretório: {}\Youtube_Downloader\Músicas".format(os.getcwd()))
            seconds = time.time() - start_time
            print('Tempo total:', time.strftime("%H:%M:%S",time.gmtime(seconds)))
            time.sleep(10)

tela = TelaPython()
tela.Iniciar()
