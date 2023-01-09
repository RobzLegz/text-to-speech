import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from constants import sound_names

work_dir = os.path.dirname(os.path.dirname(__file__))

sound = AudioSegment.from_mp3(f"{work_dir}/scripts/allsounds.mp3")

audio_chunks = split_on_silence(sound, min_silence_len=100, silence_thresh=-40 )

for i, chunk in enumerate(audio_chunks):
   soundn = sound_names[i]
   output_file = f"{work_dir}/sounds/{soundn}.mp3"

   print("Exporting file", output_file)
   chunk.export(output_file, format="mp3")