#! usr/bin/python

#<28/12/18>
#Created base GUI for radio controller

#CONSIDER ROWCONFIGURE AND COLUMNCONFIGURE for resize responsivity
#Determine a way for the application to resize on start 


from omxplayer.player import OMXPlayer
from sys import exit
from Tkinter import *

rad_urls = {
        'Power 103': 'http://5.63.151.52:7032/hd#.mp3'
        }

rad_urls_ids = {
        0 : 'Power 103'
        }

#cur_url = 'http://5.63.151.52:7032/hd#.mp3'
cur_index = 0;
cur_url = rad_urls[rad_urls_ids[cur_index]]

try:
    player = OMXPlayer(cur_url)
except:
    print 'OMXPlayer instance couldn\'t be created'
    exit(1)


root = Tk()
root.config(bg='white')
root.title("Radio Controller")

#Screen width and height
w = root.winfo_screenwidth()

#TOP FRAME(STATION NAME AND TOGGLE NEXT OR PREV. STAT.)
topFrame = Frame(height=100, width=w,bg='white')

#Loading images to be used later on
img1 = PhotoImage(file="previous.png")
img2 = PhotoImage(file="next.png")
img3 = PhotoImage(file="play.png")
img4 = PhotoImage(file="stop.png")
img5 = PhotoImage(file="VInc.png")
img6 = PhotoImage(file="VDec.png")
img7 = PhotoImage(file="list.png")
img8 = PhotoImage(file="exit.png")
img9 = PhotoImage(file="pause.png")

lab1 = StringVar()
lab1.set(rad_urls_ids[cur_index])

def changeDropdown(*args):
	lab1.set(" "+lab1.get())

#Creating dropdown for stations
choices = [" Star"," Mix"," Power"] #EDIT THIS TO CORESPOND W/ ID's of radio stations in rad_urls_id
statOpt = OptionMenu(topFrame, lab1, *choices)
statOpt.configure(indicatoron=0,compound='left',image=img7,bg='white',borderwidth=0,relief="flat", highlightthickness=0, font=('Verdana',24))
statOpt.grid(row=0, column=1, padx=20)
lab1.trace('w',changeDropdown)


#Middle frame
midFrame = Frame(bg='white',width=w,height=100)


togglePrev = Button(midFrame, image=img1, bg='white',borderwidth=0, relief="flat", highlightthickness=0)
toggleNext = Button(midFrame, image=img2, bg='white',borderwidth=0,relief="flat", highlightthickness=0)
togglePrev.grid(row=0, column=0, sticky="WE", padx=80)
toggleNext.grid(row=0, column=1, sticky="EW", padx=80)

topFrame.grid(row=0, pady=(20,0))
midFrame.grid(row=1, pady=(30,10))

#Bottom Frame
#RESEARCH THE trace function on the statOpt to trace value changes and adjust the station
lowFrame = Frame(width=w,height=200, bg='white',borderwidth=0)

#changeState
def changeState():
    if (player.playback_status() == "Playing"):
        player.play_pause()
        b1.configure(image=img3)
    elif(player.playback_status() == "Paused"):
        player.play_pause()
        b1.configure(image=img9)
    else:
        pass
    lab1.set(rad_urls_ids[cur_index])

tmpv = player.volume()

#Volume control
def incVol():
    tmpv = player.volume()
    if(tmpv < 10):
        player.set_volume(tmpv + 0.1)
    

def decVol():
    if(tmpv > 0):
        player.set_volume(tmpv - 0.1)

def killStream():
    player.stop()
    root.destroy()

#play
b1 = Button(lowFrame, image=img9, bg='white',borderwidth=0,relief="flat", highlightthickness=0,command=changeState)
b1.grid(row=0, column=1,padx=60,sticky="EW")
#stop
#b2 = Button(lowFrame, image=img4, bg='white',borderwidth=0,relief="flat", highlightthickness=0, command=changeState)
#b2.grid(row=0, column=2, padx=30,sticky="EW")
#Volume increase
b3 = Button(lowFrame, image=img5, bg='white',borderwidth=0,relief="flat", highlightthickness=0, command=incVol)
b3.grid(row=0, column=3, padx=30,sticky="EW")
#volume decrease
b4 = Button(lowFrame, image=img6, bg='white',borderwidth=0,relief="flat", highlightthickness=0, command=decVol)
b4.grid(row=0, column=4, padx=30,sticky="EW")
#exit
b5 = Button(lowFrame, image=img8, bg='white',borderwidth=0,relief="flat",highlightthickness=0,command=killStream)
b5.grid(row=0, column=5, padx=30, sticky="EW")


lowFrame.grid(row=2, pady=(45,20))

root.attributes('-fullscreen',True)
#root.geometry('300x400')
root.mainloop()
