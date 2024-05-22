from pytube import YouTube
import os
from threading import Thread

only_audio = True
urls = [
    "https://www.youtube.com/watch?v=9vpBLmZeCwU",
]

    
for url in urls:
    def funct():
        streams = YouTube(url).streams
        file = streams.get_audio_only() if only_audio else streams.get_by_resolution("720p")
        path = file.download()

        if only_audio:
            os.rename(path, path.replace(".mp4", ".mp3"))
        print("Download realizado", path.split("/")[-1].split(".")[0])

    thread = Thread(target=funct)
    thread.start()