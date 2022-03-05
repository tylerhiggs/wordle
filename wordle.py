file = open("words.txt", "r")
lines = file.readlines()
lines = [line.strip() for line in lines]
forbidden = ""
##wordle = "*****"

print("type in the word, press enter, then for each letter of that word write g (green), y (yellow), or b (black) depending on wordle results")

while True: ## for i in range(len(5))??
    word = input("guess a word: ")
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
    for l in range(len(word)):
        if colors[l].lower() == "g":
            lines = [line for line in lines if line[l] == word[l]]
            ## wordle[l] = word[l]
        elif colors[l].lower() == "y":                
            lines = [line for line in lines if line[l] != word[l] and word[l] in line]
            
        elif colors[l].lower() == "b" or colors[l].lower() == "w":
            lines = [line for line in lines if word[l] not in line]
        else:
            print("invalid wordle results (must be g, y, or b")
    print(lines[0:10])

