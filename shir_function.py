import os
import tkinter as tk
from tkinter import ttk
import pygame

from shir_file_names import SONGS, SONGS_DIR

class ShirShelPamApp:
    def __init__(self, root):
        self.root = root
        self.root.title("שיר של פעם 🎶")
        self.root.geometry("400x200")

        pygame.mixer.init()

        self.selected_song = tk.StringVar(value=list(SONGS.keys())[0])

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="בחר שיר:", font=("Arial", 14)).pack(pady=10)
        ttk.Combobox(self.root, textvariable=self.selected_song, values=list(SONGS.keys())).pack()

        tk.Button(self.root, text="🎵 נגן גרסה קלאסית", command=self.play_classic).pack(pady=5)
        tk.Button(self.root, text="🎧 נגן גרסה מודרנית", command=self.play_modern).pack(pady=5)

    def play_song(self, version):
        song_name = self.selected_song.get()
        filename = SONGS[song_name][version]
        path = os.path.join(SONGS_DIR, filename)
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

    def play_classic(self):
        self.play_song("classic")

    def play_modern(self):
        self.play_song("modern")