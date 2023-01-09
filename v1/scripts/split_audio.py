import pydub
from pydub import AudioSegment
from pydub.silence import split_on_silence
from scripts.constants import sound_names

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