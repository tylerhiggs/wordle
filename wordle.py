import string
file = open("words.txt", "r")
lines = file.readlines()
lines = [line.strip() for line in lines]
forbidden = ""
lowercase = string.ascii_lowercase

print("type in the word, press enter, then for each letter of that word write g (green), y (yellow), or b (black) depending on wordle results")

for _ in range(6):
    word = input("guess a word: ").lower()
    if word == "q":
        break
    assert len(word) == 5, "word length must be 5"
    colors = input("wordle results: ")
    assert len(colors) == 5, "wordle results must be length 5"
    if colors == "q":
        break
    if colors == "ggggg":
        print("good job!!!")
        break

    # deal with duplicate letters
    green_freq = {}
    yellow_freq = {}
    for l in range(len(word)):
        if colors[l] == "g":
            if word[l] in green_freq:
                green_freq[word[l]] += 1
            else:
                green_freq[word[l]] = 1
        elif colors[l] == "y":
            if word[l] in yellow_freq:
                yellow_freq[word[l]] += 1
            else:
                yellow_freq[word[l]] = 1
    for letter in green_freq:
        if letter in yellow_freq:
            lines = [line for line in lines if line.count(letter) > green_freq[letter]]

    for l in range(len(word)):
        if colors[l].lower() == "g":
            lines = [line for line in lines if line[l] == word[l]]
        elif colors[l].lower() == "y":                
            lines = [line for line in lines if line[l] != word[l] and word[l] in line]
        elif colors[l].lower() == "b" or colors[l].lower() == "w":
            lines = [line for line in lines if word[l] not in line]
        else:
            print("invalid wordle results (must be g, y, or b")
    print(lines[0:10])

