from scripts.label_sound import label_sounds

labeled_sounds = label_sounds()

text = "dzintara siers"

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
        
print(sound_sequence)


