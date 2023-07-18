
# Imports
from time import sleep
import random, os
from subprocess import call

# Song Class
class Song:
    def __init__(self):
        self.path = ""

    def randomizeSong(self):
        path = os.getcwd()
        path = os.path.dirname(path)
        song_files_path = path + "/" + "Song_WAV_Files"
        random_song_path = song_files_path + "/" + random.choice(os.listdir(song_files_path))
        self.path = random_song_path

    # Starts playing a random song from the path asynchronously
    def startRandomSong(self):
        self.randomizeSong()
        call(["aplay",self.path])

test = Song()
test.startRandomSong()
sleep(10)
