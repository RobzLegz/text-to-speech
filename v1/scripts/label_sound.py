from scripts.constants import sound_names

def label_sounds():
    label_sounds = {}

    for sn in sound_names:
        label_sounds[sn] = f"/sounds/{sn}.mp3"

    return label_sounds
