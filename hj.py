#! usr/bin/python

#<28/12/18>
#Created base GUI for radio controller

#CONSIDER ROWCONFIGURE AND COLUMNCONFIGURE for resize responsivity
#Determine a way for the application to resize on start 


from omxplayer.player import OMXPlayer
from sys import exit
from Tkinter import *

def newlineStrip(x):
    
    y = ''
    
    for i in x:
        if i != '\n':
            y += i
    
    return y

def getStationList(fileName):

    stations = []

    statFile = open(fileName)
 
    for line in statFile:
        row = line.split(': ')
	retRow = []
        for x in row:
		retRow.append(newlineStrip(x))
        stations.append(retRow)

    statFile.close()

    return stations

rad_urls = getStationList("radio_stations.txt")

#cur_url = 'http://5.63.151.52:7032/hd#.mp3'
cur_index = 0
#cur_url = rad_urls[cur_index][1]

try:
    player = OMXPlayer(rad_urls[cur_index][1])
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
img1 = PhotoImage(file="images/previous.png")
img2 = PhotoImage(file="images/next.png")
img3 = PhotoImage(file="images/play.png")
img4 = PhotoImage(file="images/stop.png")
img5 = PhotoImage(file="images/VInc.png")
img6 = PhotoImage(file="images/VDec.png")
img7 = PhotoImage(file="images/list.png")
img8 = PhotoImage(file="images/exit.png")
img9 = PhotoImage(file="images/pause.png")

lab1 = StringVar()
lab1.set(rad_urls[cur_index][0])

def changeDropdown(*args):
	lab1.set(" "+lab1.get())

#Creating dropdown for stations
choices = []
for i in range (0, len(rad_urls)):
	choices.append(rad_urls[i][0])

statOpt = OptionMenu(topFrame, lab1, *choices)
statOpt.configure(indicatoron=0,compound='left',image=img7,bg='white',borderwidth=0,relief="flat", highlightthickness=0, font=('Verdana',24))
statOpt.grid(row=0, column=1, padx=20)
lab1.trace('w',changeDropdown)


#Middle frame
midFrame = Frame(bg='white',width=w,height=100)

#change station
def nextStation():
	global cur_index
	if cur_index != (len(rad_urls) - 1):
		cur_index += 1
		lab1.set(rad_urls[cur_index][0])	
		player.load(rad_urls[cur_index][1])
		#player.load('http://pureplay.cdnstream1.com/6043_128.mp3')
		
	else:
		pass

def prevStation():
	global cur_index
	if cur_index >= 1:
		cur_index -= 1
		lab1.set(rad_urls[cur_index][0])
		player.load(rad_urls[cur_index][1])
		#player.load('http://pureplay.cdnstream1.com/6033_128.mp3')
	else:
		pass

togglePrev = Button(midFrame, image=img1, bg='white',borderwidth=0, relief="flat", highlightthickness=0, command=prevStation)
toggleNext = Button(midFrame, image=img2, bg='white',borderwidth=0,relief="flat", highlightthickness=0, command=nextStation)
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

#Volume control
def incVol():
   tmpv = player.volume()
   if(tmpv < 10):
        player.set_volume(tmpv + 0.1)
    

def decVol():
    tmpv = player.volume()
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
