from pydub import AudioSegment
from scripts.label_sound import label_sounds, work_dir
from pydub.effects import speedup
from pydub.playback import play

labeled_sounds = label_sounds()

text = "ābols"

split_text = [*text]

ignore_index = None

sound_sequence = []

def check_next(index, lettr, letters):
    try:
        for letter in letters:
            if split_text[index + 1] == letter:
                sound_sequence.append("{lettr}{letter}".format(lettr=lettr, letter=letter))
                return True
        sound_sequence.append(lettr)
    except IndexError:
        sound_sequence.append(lettr)
        
def get_next_letter(index, lettr):
    if lettr == "a":
        return check_next(index, lettr, letters=["i", "u"])
    elif lettr == "d":
        return check_next(index, lettr, letters=["z", "ž"])
    elif lettr == "e":
        return check_next(index, lettr, letters=["i", "u"])
    elif lettr == "i":
        return check_next(index, lettr, letters=["e", "u"])
    elif lettr == "u":
        return check_next(index, lettr, letters=["e", "u"])
    else:
        sound_sequence.append(lettr)

for i, lettr in enumerate(split_text):
    if ignore_index != i:
        increment = get_next_letter(i, lettr)

        if increment == True:
            ignore_index = i + 1
        
full_sound = None    

for sound in sound_sequence:
    if sound == " ":
        continue

    new_sound = AudioSegment.from_file(labeled_sounds[sound], format="mp3")

    if full_sound != None:
        full_sound = full_sound + new_sound
    else:
        full_sound = AudioSegment.from_file(labeled_sounds[sound], format="mp3")

def optimal_name():
    return text.replace(" ", "")

opt_name = optimal_name()

sped_up_sound = speedup(full_sound, 1.2, 150)

output_file = f"{work_dir}\output\{opt_name}.mp3"

file_handle = sped_up_sound.export(output_file, format="mp3")

print(f"Saved audio to {output_file}")