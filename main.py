import tkinter as tk

from pathlib import Path

import pygame
pygame.mixer.init()

music = pygame.mixer_music # to load and play music

song_path_list = [] # Stores the song path in a list

current_index = None # tracks the index of the song currently loaded/playing

def play_song():
    """plays the song"""

    global current_index
    selection = song_list_box.curselection()
    if selection:
        current_index = selection[0]
        music.load(song_path_list[current_index])
        music.play()

def next_song():
    """plays next song"""

    global current_index ## whatever change is made within this func will be global and affect the current_index variable
    if current_index is None:
        return

    current_index += 1

    music.load(song_path_list[current_index])
    music.play()

def prev_song():
    """plays previous song"""

    global current_index
    if current_index is None:
        return
    
    current_index -= 1
    
    music.load(song_path_list[current_index])
    music.play()
    
def access_music_files(): 
    """ Used to access all mp3 files in the path """

    path = Path("c:/Users/OMEKO/Desktop/Music")

    return list((path.rglob("*.mp3")))


# All responsible for building the visual of the app
root = tk.Tk()
root.title("Music Player")

root.geometry("600x400")

# List box 
song_list_box = tk.Listbox(root, width=50, height=15)
song_list_box.pack(pady=10)


all_songs = access_music_files() # Stores all songs in this list
for songs in all_songs: # adds the songs to the list box and the list
    song_list_box.insert(tk.END, songs.name)
    song_path_list.append(songs)


# Buttons 
quit_button = tk.Button(root, text="quit", command=root.destroy) # "quit" button  Closes the app
quit_button.pack(side=tk.LEFT, padx=5)

previous_button = tk.Button(root, text="previous", command=prev_song) # "previous" button  goes to previous song on the list if there is
previous_button.pack(side=tk.LEFT, padx=5)

play_button = tk.Button(root, text="play", command=play_song) # "play" button  plays a selected song
play_button.pack(side=tk.LEFT, padx=5)

next_button = tk.Button(root, text="next", command=next_song) # "next"button  goes to next song on the list if there is
next_button.pack(side=tk.LEFT, padx=5)

pause_button = tk.Button(root, text="pause", command=pygame.mixer_music.pause) # "pause" button  pauses the song
pause_button.pack(side=tk.LEFT, padx=5)

unpause_button = tk.Button(root, text="unpause", command=pygame.mixer_music.unpause) # "unpause" button  unpauses the song
unpause_button.pack(side=tk.LEFT, padx=5)

root.mainloop() # keeps the app running on a loop and refreshes after user input
