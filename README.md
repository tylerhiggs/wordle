# Wordle

run with `python3 wordle.py` and when prompted, choose a word and then indicate how wordle responded. The response will be 10 words that could be the wordle of the day given your previous guesses. Type `q` to quit. Here is an example:

You guess "irate" in the wordle and it responds with 🟩⬜️⬜️⬜️🟨 that means that "i" is the first letter of the wordle and "e" is in the wordle but is not the last letter. "r", "a", and "t" are not in the wordle. My program will then create a list of five letter words that fit that description and return up to ten from that list or fewer if the list is shorter. When prompted to give the wordle responce (🟩⬜️⬜️⬜️🟨) you type "g" for green, "b" for black or "w" for white, or "y" for yellow. In this example you would type "gwwwy". 
