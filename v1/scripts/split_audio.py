import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

#reading from audio mp3 file
sound = AudioSegment.from_mp3("D:/links/code/speech-synthesiser/v1/scripts/allsounds.mp3")
# spliting audio files
# audio_chunks = split_on_silence(sound, min_silence_len=200, silence_thresh=-40 )
# #loop is used to iterate over the output list
# for i, chunk in enumerate(audio_chunks):
#    output_file = "/content/Audio/output/chunk{0}.mp3".format(i)
#    print("Exporting file", output_file)
#    chunk.export(output_file, format="mp3")