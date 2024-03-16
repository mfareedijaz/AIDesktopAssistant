import tkinter as tk
import fnmatch
import os
from pygame import mixer

def Music_Player():
    canvas = tk.Tk()
    canvas.title("Music Player")
    canvas.geometry("600x500")
    canvas.config(bg='black')

    rootpath = r"E:\WebProj\AudioSphere\Songs"
    pattern = "*.mp3"
    mixer.init()

    def select():
        selection = listBox.curselection()
        if selection:
            index = int(selection[0])
            label.config(text=listBox.get(index))
            mixer.music.load(os.path.join(rootpath, listBox.get(index)))
            mixer.music.play()

    def stop():
        mixer.music.stop()
        listBox.select_clear('active')

    def playNext():
        nextSong = listBox.curselection()
        if nextSong:
            nextSong = nextSong[0] + 1
            if nextSong < listBox.size():
                nextSongName = listBox.get(nextSong)
                label.config(text=nextSongName)

                mixer.music.load(os.path.join(rootpath, listBox.get(nextSong)))
                mixer.music.play()

                listBox.select_clear(0, 'end')
                listBox.activate(nextSong)
                listBox.select_set(nextSong)

    def playPrev():
        prevSong = listBox.curselection()
        if prevSong:
            prevSong = prevSong[0] - 1
            if prevSong >= 0:
                prevSongName = listBox.get(prevSong)
                label.config(text=prevSongName)

                mixer.music.load(os.path.join(rootpath, listBox.get(prevSong)))
                mixer.music.play()

                listBox.select_clear(0, 'end')
                listBox.activate(prevSong)
                listBox.select_set(prevSong)

    def pause():
        if pauseButton['text'] == "Pause":
            mixer.music.pause()
            pauseButton['text'] = "Play"
        else:
            mixer.music.unpause()
            pauseButton['text'] = "Pause"

    listBox = tk.Listbox(canvas, fg="cyan", bg="black", width=100)
    listBox.pack(padx=15, pady=15)

    label = tk.Label(canvas, text="", bg="black", fg="yellow")
    label.pack(pady=15)

    top = tk.Frame(canvas, bg="black")
    top.pack(padx=10, pady=5, anchor="center")

    prevButton = tk.Button(canvas, text="Prev", command=playPrev)
    prevButton.pack(pady=15, padx=8, in_= top, side="left")

    stopButton = tk.Button(canvas, text="Stop", command=stop)
    stopButton.pack(pady=15, padx=8, in_= top, side="left")

    playButton = tk.Button(canvas, text="Play", command=select)
    playButton.pack(pady=15, padx=8, in_= top, side="left")

    pauseButton = tk.Button(canvas, text="Pause", command=pause)
    pauseButton.pack(pady=15, padx=8, in_= top, side="left")

    nextButton = tk.Button(canvas, text="Next", command=playNext)
    nextButton.pack(pady=15, padx=8, in_= top, side="left")

    for root, dirs, files in os.walk(rootpath):
        for filename in fnmatch.filter(files, pattern):
            listBox.insert('end', filename)

    canvas.mainloop()
