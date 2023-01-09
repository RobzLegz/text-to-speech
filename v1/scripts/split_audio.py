import os
import pydub
from pydub import AudioSegment
from pydub.silence import split_on_silence

sound_names = [
   "a",
   "ā",
   "e",
   "ē",
   "i",
   "ī",
   "u",
   "ū",
   "o",
   "ai",
   "au",
   "ei",
   "ie",
   "eu",
   "uo",
   "iu",
   "ui",
   "oi",
   "ou",
   "b",
   "c",
   "č",
   "d",
   "f",
   "g",
   "ģ",
   "h",
   "j",
   "k",
   "ķ",
   "l",
   "ļ",
   "m",
   "n",
   "ņ",
   "p",
   "r",
   "s",
   "š",
   "t",
   "v",
   "z",
   "ž",
   "dz",
   "dž",
]

#reading from audio mp3 file
pydub.AudioSegment.ffmpeg = r"D:\Downloads\ffmpeg-2023-01-04-git-4a80db5fc2-essentials_build\ffmpeg-2023-01-04-git-4a80db5fc2-essentials_build\bin\ffmpeg.exe"
sound = AudioSegment.from_mp3("allsounds.mp3")
# spliting audio files
audio_chunks = split_on_silence(sound, min_silence_len=200, silence_thresh=-40 )
#loop is used to iterate over the output list
for i, chunk in enumerate(audio_chunks):
   output_file = "sounds/{0}.mp3".format(sound_names[i])
   print("Exporting file", output_file)
   chunk.export(output_file, format="mp3")