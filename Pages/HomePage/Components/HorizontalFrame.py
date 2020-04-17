import tkinter as tk
import pyglet
import tkinter.font as tkfont
from Pages.Resource.HorizontalScrollableFrame import HorizontalScrollableFrame


def wid():
    global w
    return w


class HorizontalFrame(tk.Frame):
    def __init__(self, master, controller, data, text, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#181818'
        self['padx'] = 20
        self['pady'] = 20

        self.upper = Upper(self, text)
        self.line = tk.Frame(self, background='#ffffff')
        self.lower = Lower(self, controller, data)

        self.upper.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.line.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.lower.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

    def right(self):
        self.lower.scrollable.right()

    def left(self):
        self.lower.scrollable.left()


class Upper(tk.Frame):
    def __init__(self, master, text, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#181818'
        self.master = master

        pyglet.font.add_file('fonts/Play/Play-Bold.ttf')
        play = tkfont.Font(family="Play", size=15, weight="bold")

        self.left = tk.PhotoImage(file=r'.\images\left_arrow.png')
        self.right = tk.PhotoImage(file=r'.\images\right_arrow.png')

        self.label = tk.Label(self,
                              text=text,
                              font=play,
                              anchor=tk.W,
                              background='#181818',
                              foreground='white')

        self.left_button = ArrowButton(self, image=self.left, command=master.left)
        self.right_button = ArrowButton(self, image=self.right, command=master.right)

        self.left_button.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)
        self.right_button.grid(row=0, column=2, sticky=tk.N + tk.S + tk.E + tk.W)

        self.label.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=100)
        self.grid_columnconfigure((1, 2), weight=1)


class Lower(tk.Frame):
    def __init__(self, master, controller, data, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#181818'
        self['pady'] = 10
        self.bind('<Configure>', self.size)
        self.Ed_sheeran = tk.PhotoImage(file='images/Ed_sheeran.png')

        self.scrollable = HorizontalScrollableFrame(self)
        self.frame = tk.Frame(self.scrollable.scrollable_frame, bg='#181818')
        self.name = [x for x in range(len(data))]
        self.value = [x for x in range(len(data))]

        for i, j in enumerate(data):
            self.button = CardButton(self.frame, text=j['text'],
                                     image=self.Ed_sheeran,
                                     url=j['url'],
                                     command=lambda d=self.value[i]: controller.show_frame_Main(data=d)
                                     )
            self.button.grid(row=0, column=i, padx=(0, 10))

        self.frame.grid(row=0, column=0, sticky='nsew')

        self.scrollable.grid(row=0, column=0, sticky=tk.W + tk.E)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def size(self, event):
        global width
        global w
        width = event.width
        w = event.width / 5 - 14


class ArrowButton(tk.Button):
    def __init__(self, master, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)
        self['relief'] = tk.FLAT
        self['background'] = '#181818'
        self['foreground'] = 'white'
        self['activebackground'] = '#181818'
        self['activeforeground'] = 'white'
        self['borderwidth'] = 0


class CardButton(tk.Button):
    def __init__(self, master, url, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)
        self.url = url

        self.bind('<Configure>', self.size)

        pyglet.font.add_file('fonts/Play/Play-Bold.ttf')
        play = tkfont.Font(family="Play", size=15, weight="bold")
        # print(width)
        self['background'] = '#181818'
        self['height'] = 300
        self['border'] = 0
        self['font'] = play
        self['compound'] = tk.TOP
        self['activebackground'] = '#181818'
        self['foreground'] = 'white'
        self['activeforeground'] = 'white'

    def size(self, event):
        global width
        w = width / 5 - 14
        self.configure(width=w)
        # print(self.url)

    # image = io.imread(url)
    # image = cv2.resize(image, (w,250), interpolation = cv2.INTER_AREA)
    # image = Image.fromarray(image)
    # image = ImageTk.PhotoImage(image)
    # self.configure(image = image)
