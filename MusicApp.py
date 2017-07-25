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

        # Entry_frame design
        ttk.Label(self.entry_frame, text='Song').grid(
            row=0, column=0, padx=75, sticky='w')
        ttk.Label(self.entry_frame, text='Artist').grid(
            row=0, column=2, padx=75, sticky='w')
        ttk.Label(self.entry_frame).grid(
            row=0, column=1, padx=50, sticky='w')

        self.song = StringVar()
        self.artist = StringVar()

        ttk.Entry(self.entry_frame, width=20, textvariable=self.song).grid(row=1, column=0)
        ttk.Entry(self.entry_frame, width=20, textvariable=self.artist).grid(row=1, column=2)
        ttk.Button(self.master, text='Search',
                   command=lambda: self.callback(
                       self.song.get(), self.artist.get())).pack(pady=10)


        ttk.Checkbutton(self.entry_frame, text='Youtube', onvalue=True, offvalue=False,
                        style='1.TCheckbutton').grid(row=2, column=0, pady=10)
        ttk.Checkbutton(self.entry_frame, text='SoundCloud', onvalue=True, offvalue=False,
                        style='1.TCheckbutton').grid(row=2, column=1, pady=10)
        ttk.Checkbutton(self.entry_frame, text='Audiomack', onvalue=True, offvalue=False,
                        style='1.TCheckbutton').grid(row=2, column=2, pady=10)


        # Output_frame design
        self.yt_link = StringVar()
        self.sc_link = StringVar()
        self.am_link = StringVar()

        self.yt_img = PhotoImage(file='icons/youtube-icon.png').subsample(6, 6)
        ttk.Label(self.output_frame, image=self.yt_img).grid(row=0, column=0, pady=10)

        self.sc_img = PhotoImage(file='icons/soundcloud-icon.png').subsample(14, 14)
        ttk.Label(self.output_frame, image=self.sc_img).grid(row=1, column=0, pady=10)

        self.am_img = PhotoImage(file='icons/audiomack-icon.png').subsample(3, 3)
        ttk.Label(self.output_frame, image=self.am_img).grid(row=2, column=0, pady=10)
        self.yt = ttk.Label(self.output_frame, cursor='hand2',
                            wraplength=350,
                            textvariable=self.yt_link, style='Link.TLabel',
                            compound=LEFT)
        self.yt.grid(row=0, column=1, sticky='w', pady=10)

        self.sc = ttk.Label(self.output_frame, cursor='hand2',
                            wraplength=350,
                            textvariable=self.sc_link, compound=LEFT)

        self.sc.grid(row=1, column=1, sticky='w', pady=10)
        self.sc.bind('<Button-1>', lambda e: self.link_callback(e, self.sc_link))

        self.am = ttk.Label(self.output_frame, cursor='hand2',
                            wraplength=350,
                            textvariable=self.am_link, style='Link.TLabel',
                            compound=LEFT)
        self.am.grid(row=2, column=1, sticky='w', pady=10)
        self.am.bind('<Button-1>', lambda e: self.link_callback(e, self.am_link))

    def callback(self, song, artist, providers):
        for thing in providers:
            x = Link(provider='Youtube', song=song, artist=artist)
            thing.set(Web.search(x))
            if thing.get() != 'None':
                self.yt.bind('<Button-1>', lambda e: self.link_callback(e, self.yt_link))
                self.yt.configure(style='Link.TLabel')
        else:
            self.yt_link.set('SONG WAS NOT FOUND')

        self.sc_link.set(Web.soundcloud_search(song, artist))
        print(self.sc_link.get(), type(self.sc_link.get()))
        if self.sc_link.get() != 'None':
            self.sc.bind('<Button-1>', lambda e: self.link_callback(e, self.sc_link))
            self.sc.configure(style='Link.TLabel')
        else:
            self.sc_link.set('SONG WAS NOT FOUND')

        self.am_link.set(Web.audiomack_search(song, artist))
        if self.am_link.get() != 'None':
            self.am.bind('<Button-1>', lambda e: self.link_callback(e, self.am_link))
            self.am.configure(style='Link.TLabel')
        else:
            self.am_link.set('SONG WAS NOT FOUND')
        self.output_frame.pack()

    def link_callback(self, event, link):
        webbrowser.open_new(link.get())

def main():
    root = Tk()
    MusicApp(root)
    root.mainloop()

if __name__ == '__main__': main()