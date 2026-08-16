import tkinter as tk

from pathlib import Path

import pygame
pygame.mixer.init()

music = pygame.mixer.Channel # to load and play music

song_path_list = [] # Stores the song path in a list

def select_song():
    """ Selecting song index and returning the path to the selected song """

    list_box_index = song_list_box.curselection() # stores the index of the selected song
    if list_box_index:
        song = list_box_index[0] # index of the selected song
        selected_song_path = song_path_list[song]
        return selected_song_path

    
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

previous_button = tk.Button(root, text="previous", command="") # "previous" button  goes to previous song on the list if there is
previous_button.pack(side=tk.LEFT, padx=5)

play_button = tk.Button(root, text="play", command="") # "play" button  plays a selected song
play_button.pack(side=tk.LEFT, padx=5)

next_button = tk.Button(root, text="next", command="") # "next"button  goes to next song on the list if there is
next_button.pack(side=tk.LEFT, padx=5)

root.mainloop() # keeps the app running on a loop and refreshes after user input