from tkinter import *
from tkinter import ttk
import os
from pytube import YouTube


def download_video():
    url = url_input.get()
    download_folder = os.path.join(os.path.expanduser('~'), 'Documents', 'Download Youtube Vídeos', 'Vídeos')

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    try:
        youtube = YouTube(url)

        video = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video_file_path = os.path.join(download_folder, video.title + ".mp4")

        if check_file_already_exist(video_file_path):
            show_file_already_exists("O vídeo já foi baixado!")
            return

        if video is not None:
            video.download(output_path=download_folder)
            show_completed_donwload("Download do vídeo concluído!")

        else:
            show_download_error("Não foi possível encontrar o vídeo no formato mp4!")

    except Exception as e:
        show_download_error("Ocorreu um erro durante o downoad: " + str(e))


def download_audio():
    url = url_input.get()
    download_folder = os.path.join(os.path.expanduser('~'), 'Documents', 'Download Youtube Vídeos', 'Áudios')

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    try:
        youtube = YouTube(url)

        audio = youtube.streams.filter(only_audio=True).first()
        audio_file_path = os.path.join(download_folder, audio.title + ".mp4")

        if check_file_already_exist(audio_file_path):
            show_file_already_exists("O áudio já foi baixado!")
            return

        if audio is not None:
            audio.download(output_path=download_folder)
            show_completed_donwload("Download do áudio concluído!")

        else:
            show_download_error("Não foi possível encontrar o áudio no formato mp4!")

    except Exception as e:
        show_download_error("Ocorreu um erro durante o downoad: " + str(e))


def show_completed_donwload(msg):
    status_label.config(text=msg, foreground="green")
    status_label.after(4000, hide_message)


def show_download_error(msg):
    status_label.config(text=msg, foreground="red")
    status_label.after(10000, hide_message)


def show_file_already_exists(msg):
    status_label.config(text=msg, foreground="orange")
    status_label.after(4000, hide_message)


def hide_message():
    status_label.config(text="")


def check_file_already_exist(file_path):
    return os.path.exists(file_path)


root = Tk()
root.title("Download Youtube Videos")
root.resizable(False, False)
root.iconbitmap(default="images/YOUTUBE_icon-icons.com_65487.ico")

frame = ttk.Frame(root, padding=20)
frame.grid()

ttk.Label(frame, text="Coloque a url do vídeo no campo abaixo ⬇️").grid(column=0, row=0, columnspan=2)

url_input = ttk.Entry(frame, width=60)
url_input.grid(column=0, row=1, columnspan=2)

download_video_button = ttk.Button(frame, text="Download vídeo", cursor="hand2", command=download_video)
download_video_button.grid(column=0, row=2, padx=(50, 0), pady=(10, 0))

download_audio_button = ttk.Button(frame, text="Download áudio", cursor="hand2", command=download_audio)
download_audio_button.grid(column=1, row=2, padx=(0, 50), pady=(10, 0))

status_label = ttk.Label(frame, text="")
status_label.grid(column=0, row=3, columnspan=2, pady=(10, 0))

root.mainloop()
