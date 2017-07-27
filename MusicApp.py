# Ameen Ahmed
# 7/13/17

from tkinter import *
from tkinter import ttk
import webbrowser
import Web
import Link


class MusicApp:
    def __init__(self, master):
        self.master = master
        self.createGUI()

    def createGUI(self):
        # Configure master window
        bkgrnd = '#AE2D58'
        self.master.configure(background=bkgrnd)
        self.master.title('MusicApp.py')
        self.master.resizable(False, False)

        # Style
        style = ttk.Style(self.master)
        style.configure('.', background=bkgrnd, font=('Arial Black', 8))
        style.configure('Link.TLabel', font=('Arial', 8, 'bold'), foreground='#0B00AB')
        style.configure('1.TCheckbutton', font=('Arial', 8))

        # Frame creation
        self.entry_frame = ttk.Frame(self.master)
        self.entry_frame.pack()
        self.output_frame = ttk.Frame(self.master)

        self.song = StringVar()
        self.artist = StringVar()

        # Entry Fields
        ttk.Label(self.entry_frame, text='Song').grid(
            row=0, column=0, padx=75, sticky='w')
        ttk.Label(self.entry_frame, text='Artist').grid(
            row=0, column=2, padx=75, sticky='w')
        ttk.Label(self.entry_frame).grid(
            row=0, column=1, padx=50, sticky='w')
        ttk.Entry(self.entry_frame, width=20,
                  textvariable=self.song).grid(row=1, column=0)
        ttk.Entry(self.entry_frame, width=20,
                  textvariable=self.artist).grid(row=1, column=2)

        # Check buttons
        self.youtube = Link.Link(provider='Youtube', priority=0)
        self.soundcloud = Link.Link(provider='SoundCloud', status=BooleanVar(), priority=2)
        self.audiomack = Link.Link(provider='Audiomack', status=BooleanVar(), priority=1)
        self.my_dict = {'Youtube': self.youtube,
                        'SoundCloud': self.soundcloud,
                        'Audiomack': self.audiomack}

        for key, value in self.my_dict.items():
            ttk.Checkbutton(self.entry_frame, text=key,
                        variable=value.status, onvalue=True, offvalue=False,
                        style='1.TCheckbutton').grid(row=2, column=value.priority, pady=10)

        ttk.Button(self.master, text='Search',
                   command=lambda: self.callback(
                       self.song.get(), self.artist.get(), self.my_dict)).pack(pady=10)

        #Images
        self.youtube.image = PhotoImage(file='icons/youtube-icon.png').subsample(6, 6)
        self.soundcloud.image = PhotoImage(file='icons/soundcloud-icon.png').subsample(14, 14)
        self.audiomack.image = PhotoImage(file='icons/audiomack-icon.png').subsample(3, 3)

        for key, value in self.my_dict.items():
            ttk.Label(self.output_frame, image=value.image).grid(row=value.priority, column=0, pady=10)

        #Output/ Links
        for key, value in self.my_dict.items():
            value.label = ttk.Label(self.output_frame, cursor='hand2',
                                           wraplength=350, textvariable=value.link,
                                           style='Link.TLabel', compound=LEFT)
            value.label.grid(row=value.priority, column=1, sticky='w', pady=10)
            value.label.bind('<Button-1>', lambda e: self.link_callback(e, value.link))


    def callback(self, song, artist, providers):
        for key, value in providers.items():
            if value.status.get():
                if value.link is None:
                    value.link.set('SONG WAS NOT FOUND')
                else:
                    value.link.set(Web.search(value, song, artist))
        self.output_frame.pack()

    def link_callback(self, event, link):
        webbrowser.open_new(link.get())


def main():
    root = Tk()
    MusicApp(root)
    root.mainloop()

if __name__ == '__main__': main()