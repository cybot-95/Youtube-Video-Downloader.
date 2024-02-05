from tkinter import *
from tkinter.ttk import Combobox

from pytube import YouTube

# Creating API Window
root = Tk()
root.geometry("600x400")  # note: use x instead of * !!
root.title('Cloud-load')


# Creating Elements starting with a Title
t1 = Label(root, text="YouTube Video Downloader", font=('Courier', 16, 'bold'), bg='yellow', fg='red')
t1.pack()
# For Link Entry
t2 = Label(root, text="Link Here: ", font=('Arial', 12))
t2.place(x=50, y=55)
link = StringVar()
link_ent = Entry(root, width=70, textvariable=link)
link_ent.place(x=140, y=58)
# For Resolution Selection
t5 = Label(root, text="Resolution: ", font=('Arial', 12))
t5.place(x=50, y=80)
res_ent = Combobox(root, font=('Arial', 16), width=15, height=5)
res_ent['values'] = ("720p", "480p", "360p", "240p", "144p")
res_ent.current(0)
res_ent.place(x=140, y=80)

# Creating Download Function
def download():
    dls = 0
    yt = YouTube(link_ent.get())
    vid = yt.streams.get_by_resolution(str(res_ent.get()))
    try:
        vid.download()
    except:
        dls = 1
    # conditions for error status
    if dls == 0:
        t3 = Label(root, text="Download Complete !!", font=('Arial', 14))
        t3.place(x=200, y=250)
    else:
        t4 = Label(root, text="An Unknown Error Occurred", font=('Arial', 14))
        t4.place(x=200, y=250)


# Creating Button for Download ! (note place after calling function)
b1 = Button(root, text='Download',font=('Arial', 14), bg='blue', fg='yellow', padx=2, command=download)
b1.place(x=250, y=150)


root.mainloop()
