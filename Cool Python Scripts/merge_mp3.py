import ffmpeg, os

mp3s = [a for a in os.listdir() if a.endswith(".mp3")]
mp3s = sorted(mp3s)

def concat_mp3s(mp3s, output):
    input_args = []
    for mp3 in mp3s:
        input_args.append(ffmpeg.input(mp3))
    ffmpeg.concat(*input_args, v=0, a=1).output(output).run()

concat_mp3s(mp3s, "./Cristus Lucifer - Semana Santa 2005 - VM Lakhsmi Daimon.mp3")