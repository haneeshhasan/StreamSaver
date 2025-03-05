from tkinter import *
from pytube import YouTube
from moviepy.editor import VideoFileClip

root = Tk()

root.title('Youtube Video Downloader ')
root.geometry('450x550+400+50')
root.configure(bg='#d8d9e5')
root.resizable(False,False)

def download():
    v_link = link.get('1.0','end')
    
    # download 
    Y_tube = YouTube(v_link)
    root.title('downloading....')
    stream = Y_tube.streams.filter(progressive="True", res="720p")
    video = stream.first().download()
    root.title('Success')
    clip = VideoFileClip(video)
    clip.close()

def audio():
    v_link = link.get('1.0','end')
    
    # download audio only
    Y_tube = YouTube(v_link)
    root.title('downloading....')
    stream = Y_tube.streams.filter( mime_type="audio/mp4", abr="128kbps" )
    video = stream.first().download()
    root.title('Success')
    clip = VideoFileClip(video)
    clip.close()

def video():
    v_link = link.get('1.0','end')
    
    # download video only
    Y_tube = YouTube(v_link)
    root.title('downloading....')
    stream = Y_tube.streams.filter(progressive="False", res="720p")
    video = stream.first().download()
    root.title('Success')
    clip = VideoFileClip(video)
    clip.close()

# load image
img = PhotoImage(file='youtube-logo-2.png')
Label(image=img,bd=1,bg='#d8d9e5').place(x=70,y=20)

#Create a frame where we provie our fields 
frame = Frame(root,width=400,height=350,bg='#d8d9e5') #size of frame and bg color
frame.place(x=25,y=190) #passing location of frame

#passing text with in a frame
heading = Label(frame,text='Youtube Video Downloader',fg='#57a1f8',bg='#F8EBE7',font=('Microsoft yahie UI Light',22,'bold'))
heading.place(x=10,y=10)

#passing text with in a frame
Label(frame,text="Link :-> ",fg='#019f90',bg='#F8EBE7',font=('Microsoft yahie UI Light',14,'bold')).place(x=10,y=80)

# Taking Link
link = Text(frame,fg='black', bd=1, height=1, width=30,bg = "light yellow",font=('Microsoft yahie UI Light',13))
link.place(x=95,y=83)

# Download Button
Button(frame,width=10,padx=1,pady=3,text='Download',bg='#57a1f8',fg='white',border=2,command=download,font=('Microsoft yahie UI Light',14,'bold')).place(x=140,y=155)

# for Audio
Button(frame,width=10,padx=1,pady=3,text='Audio',bg='#57a1f8',fg='white',border=2,command=audio,font=('Microsoft yahie UI Light',14,'bold')).place(x=30,y=250)

# for video only
Button(frame,width=10,padx=1,pady=3,text='Video',bg='#57a1f8',fg='white',border=2,command=video,font=('Microsoft yahie UI Light',14,'bold')).place(x=230,y=250)


root.mainloop()
