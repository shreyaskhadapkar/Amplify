import tkinter as tk
from PIL import ImageTk, Image


class PlayButton(tk.Button):
    def __init__(self, master, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)

        self.playing = False

        self.music_icon = self.prepare_image('music_icon.png', 16)
        self.green_music_icon = self.prepare_image('green_music_icon.png', 16)
        self.pause_icon = self.prepare_image('pause_icon.png', 25)
        self.play_icon = self.prepare_image('play_icon.png', 25)
        self.volume_icon = self.prepare_image('volume_icon.png', 25)

        self['background'] = '#181818'
        self['activebackground'] = '#333333'
        self['bd'] = 0
        self['image'] = self.music_icon
        self['height'] = 23
        self['width'] = 23
        self['command'] = lambda: self.click()

        self.bind('<Button-1>', self.master.master.click)
        self.bind('<Enter>', self.enter)
        self.bind('<Leave>', self.leave)

    @staticmethod
    def prepare_image(filename, size):
        icon = Image.open('images/'+filename)
        icon = icon.resize((size, size), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        return icon

    def enter(self, event):
        if self.playing:
            self['image'] = self.play_icon
        else:
            self['image'] = self.pause_icon

    def leave(self, event):
        if self.playing:
            self['image'] = self.volume_icon
        else:
            from Base.listOfPage import current_playing
            if len(current_playing) > 0:
                if current_playing[0] == self.master.master:
                    self['image'] = self.green_music_icon

    def click(self):
        if self.playing:
            self['image'] = self.pause_icon
            self.playing = False
            self.master.master.master.master.master.master.master.head.text_frame.play_button.isPlaying = False
            self.master.master.master.master.master.master.master.head.text_frame.play_button.ifPlaying()
        else:
            self.playing = True
            self.master.master.double_click(event='')
            self['image'] = self.play_icon