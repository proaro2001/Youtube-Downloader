import tkinter as tk
from pytube import YouTube
# create a class to handle the UI
class UI:
    def __init__(self, master):
        # param master is the root window
        self.master = master
        self.master.title("Hello World")
        self.master.geometry("500x500")
        self.master.resizable(False, False)

        self.label = tk.Label(self.master, text="Input the youtube link below:")
        self.label.pack()

        # input box for youtube link
        self.entry = tk.Entry(self.master)
        self.entry.pack()

        # download video buttom
        self.button = tk.Button(self.master, text="Click Me to Download Video!", command=self.video)
        self.button.pack()

        # download mp3 buttom
        self.buttom = tk.Button(self.master, text="Click Me to Download MP3!", command=self.mp3)
        self.buttom.pack()

    def video(self):
        print("Video")
        # extract the youtube link from the input box
        link = self.entry.get()
        print(f"Downloading from link: {link}")
        yt = YouTube(link)
        # download the video with the highest resolution
        yt.streams.get_highest_resolution().download()
    
    def mp3(self):
        print("MP3")
        # extract the youtube link from the input box
        link = self.entry.get()
        print(f"Downloading from link: {link}")
        yt = YouTube(link)
        # download the audio only with specifi
        yt.streams.filter(only_audio=True).first().download()



if __name__ == "__main__":
    root = tk.Tk()
    app = UI(root)
    root.mainloop()