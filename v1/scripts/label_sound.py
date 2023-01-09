import os
from scripts.constants import sound_names

work_dir = os.path.dirname(os.path.dirname(__file__))

def label_sounds():
    label_sounds = {}

    for sn in sound_names:
        label_sounds[sn] = f"{work_dir}/sounds/{sn}.mp3"

    return label_sounds
