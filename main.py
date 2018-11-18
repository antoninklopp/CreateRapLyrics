from model import main
from create_lyrics import create
import sys
import os

MAX_SYLLABLES = 10
LINES = 20

FORCE_TRAINING = False

def create_song(artist):

    if os.path.isfile("lyrics_" + artist + ".txt") is False or FORCE_TRAINING:
        # create the lyrics
        create(artist)

    else:
        print("File with lyrics already exists, we use it")

    if os.path.isfile(artist + ".rap") is False or FORCE_TRAINING:

        # train the model
        main(5, True, artist, MAX_SYLLABLES, LINES)
    
    else:
        print("Model already trained")

    # write the lyrics
    main(5, False, artist, MAX_SYLLABLES, LINES)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use : python main.py artist")
        exit()

    create_song(sys.argv[1])
    
