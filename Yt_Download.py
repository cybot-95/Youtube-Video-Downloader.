from tkinter import *
from pytube import YouTube

# Creating API Window
root = Tk()
root.geometry("600x400")  # note: use x instead of * !!
root.title('Cloud-load')


# Creating Elements
t1 = Label(root, text="YouTube Video Downloader", font=('Courier', 16, 'bold'))
t1.pack()
t2 = Label(root, text="Link Here: ", font=('Arial', 12))
t2.place(x=50, y=55)
link = StringVar()
link_ent = Entry(root, width=70, textvariable=link)
link_ent.place(x=140, y=58)

# Creating Download Function
def download():
    dls = 0
    yt = YouTube(link_ent.get())
    vid = yt.streams.get_highest_resolution()
    try:
        vid.download()
    except:
        dls = 1
    # conditions for error status
    if dls == 0:
        t3 = Label(root, text="Download Complete !!", font=('Arial', 14))
        t3.place(x=200, y=100)
    else:
        t4 = Label(root, text="An Unknown Error Occurred", font=('Arial', 14))
        t4.place(x=200, y=100)


# Creating Button for Download ! (note place after calling function)
b1 = Button(root, text='Download', font=('Arial', 14), bg='beige', padx=2, command=download)
b1.place(x=250, y=150)


root.mainloop()
