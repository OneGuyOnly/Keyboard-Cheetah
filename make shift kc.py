from tkinter import *
import ffdict
import random
from PIL import ImageTk,Image
import winsound
#from pygame import mixer
import sqlite3
import datetime

#mixer.init()

win=Tk()
win.title("FAST FINGERS")
win.state('zoomed')
win.configure(background="black") 
OneminuteMode=False
MarathonMode=False
SprintMode=False
StopTimer=False
disableMenu=False
PauseTimer=1
##mixer.music.load("crazyDrumming.mp3")
##mixer.music.play(-1)
##
##
##glass=mixer.Sound("glass.wav")



gameLogo=ImageTk.PhotoImage(Image.open("logo.png"))
CorrectedMistakes=0
def onenter(event):
    event.widget.config(fg="green")

def onleave(event):       
    event.widget.config(fg="yellow")
def show_stats():
    list_date=[]
    list_speed=[]
    list_keystrokes=[]
    conn=sqlite3.connect("typing.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM typing_stats")
    data=cur.fetchall()
    for data_list in data:
        list_date.append(data_list[0])
        list_speed.append(data_list[1])
        list_keystrokes.append(data_list[2])
    fastest_speed=max(list_speed)
    most_keystrokes=max(list_keystrokes)
    conn.close()
    try:
        root.destroy()
        
    except:
        pass
    try:
        timeupFrame.destroy()
    except:
        pass
    
    show_stats_Frame=Frame(mainframe,bg="black")
    show_stats_Frame.grid(row=1,column=2,columnspan=8)
    timeuplab3=Label(show_stats_Frame,text="FASTEST TYPING SPEED(WPM)" ,bg="#0e0e0e",fg="yellow",font=("Times New Roman",19,"bold"))
    timeuplab3.grid(row=2,column=0,columnspan=2,sticky="w")
    timeuplab3b=Label(show_stats_Frame,text=fastest_speed,bg="#0e0e0e",fg="yellow",font=("Times New Roman",19,"bold"))
    timeuplab3b.grid(row=2,column=2,columnspan=2,sticky="e",padx=50)       
        

def maingameframe(Sprint,Marathon):
    selection.destroy()
    
    global wrongkeystrokes,index,disableMenu,time,CorrectedMistakes,correct,root,wrong,text1,text2,text3,text4,text5,text6,text7,text8,text1b,text2b,text3b,text4b,text5b,text6b,text7b,text8b
    CorrectedMistakes=0
    ffdict.ffdictionary()
    text1=random.choice(ffdict.list1)
    text2=random.choice(ffdict.list2)
    text3=random.choice(ffdict.list3)
    text4=random.choice(ffdict.list4)
    text5=random.choice(ffdict.list5)
    text6=random.choice(ffdict.list6)
    text7=random.choice(ffdict.list7)
    text8=random.choice(ffdict.list8)

    text1b=random.choice(ffdict.list9)
    text2b=random.choice(ffdict.list10)
    text3b=random.choice(ffdict.list11)
    text4b=random.choice(ffdict.list12)
    text5b=random.choice(ffdict.list13)
    text6b=random.choice(ffdict.list14)
    text7b=random.choice(ffdict.list15)
    text8b=random.choice(ffdict.list16)


    sound="keysound"



    disableMenu=True
    disable(disableMenu)

    root=Frame(mainframe,bg="black")
    root.grid(row=1,column=2,columnspan=8)
        
    word1=Label(root,text=text1,fg="yellow",bg="black",font=("Times New Roman", 18, "bold"))
    word1.grid(row=2,column=0)
    word2=Label(root,text=text2,fg="yellow",bg="black",font=("Times New Roman", 18, "bold"))
    word2.grid(row=2,column=1)
    word3=Label(root,text=text3,fg="yellow",bg="black",font=("Times New Roman", 18,"bold"))
    word3.grid(row=2,column=2)
    word4=Label(root,text=text4,fg="yellow",bg="black",font=("Times New Roman", 18, "bold"))
    word4.grid(row=2,column=3)
    word5=Label(root,text=text5,fg="yellow",bg="black",font=("Times New Roman", 18, "bold"))
    word5.grid(row=2,column=4)
    word6=Label(root,text=text6,fg="yellow",bg="black",font=("Times New Roman", 18, "bold"))
    word6.grid(row=2,column=5)
    word7=Label(root,text=text7,fg="yellow",bg="black",font=("Times New Roman",18,"bold"))
    word7.grid(row=2,column=6)
    word8=Label(root,text=text8,fg="yellow",bg="black",font=("Times New Roman",18,"bold"))
    word8.grid(row=2,column=7)

    word1b=Label(root,text=text1b,fg="yellow",bg="black",font=("Times New Roman", 18, "bold"))
    word1b.grid(row=3,column=0)
    word2b=Label(root,text=text2b,fg="yellow",bg="black",font=("Times New Roman", 18, "bold"))
    word2b.grid(row=3,column=1)
    word3b=Label(root,text=text3b,fg="yellow",bg="black",font=("Times New Roman", 18,"bold"))
    word3b.grid(row=3,column=2)
    word4b=Label(root,text=text4b,fg="yellow",bg="black",font=("Times New Roman", 18, "bold"))
    word4b.grid(row=3,column=3)
    word5b=Label(root,text=text5b,fg="yellow",bg="black",font=("Times New Roman", 18, "bold"))
    word5b.grid(row=3,column=4)
    word6b=Label(root,text=text6b,fg="yellow",bg="black",font=("Times New Roman", 18, "bold"))
    word6b.grid(row=3,column=5)
    word7b=Label(root,text=text7b,fg="yellow",bg="black",font=("Times New Roman",18,"bold"))
    word7b.grid(row=3,column=6)
    word8b=Label(root,text=text8b,fg="yellow",bg="black",font=("Times New Roman",18,"bold"))
    word8b.grid(row=3,column=7)
    widList=[word1,word2,word3,word4,word5,word6,word7,word8]
    def winLabs():
        word1.configure(text=text1)
        word2.configure(text=text2)
        word3.configure(text=text3)
        word4.configure(text=text4)
        word5.configure(text=text5)
        word6.configure(text=text6)
        word7.configure(text=text7)
        word8.configure(text=text8)
        
        word1b.configure(text=text1b)
        word2b.configure(text=text2b)
        word3b.configure(text=text3b)
        word4b.configure(text=text4b)
        word5b.configure(text=text5b)
        word6b.configure(text=text6b)
        word7b.configure(text=text7b)
        word8b.configure(text=text8b)

    global index,correct,wrong
    index=0

    correct=0
    wrong=0    
    winLabs()
    inputText=Entry(root,fg="black",bg="yellow",width="50",font=("Times New Roman", 25, "bold"), bd=2)
    inputText.grid(row=4,column=0,ipady="20",padx="35",pady=(60,30),columnspan=8)
    WPM=0
    time=60
    TSlab=Label(root,fg="yellow",bg="black",text="TYPING SPEED ",width="30",font=("Times New Roman",20,"bold"),bd=2)
    TSlab.grid(row=5,column=0,columnspan=4)
    Tlab=Label(root,fg="yellow",bg="black",text="TIME REMAINING",width="30",font=("Times New Roman",20,"bold"),bd=2)
    Tlab.grid(row=5,column=4,columnspan=4)
    WPMlab=Label(root,fg="yellow",bg="black",text="",width="15",font=("Times New Roman",40,"bold"),bd=2)
    WPMlab.grid(row=6,column=0,pady=(40,0),columnspan=4)
    timelab=Label(root,fg="yellow",bg="black",text="",width="15",font=("Times New Roman",40,"bold"),bd=2)
    timelab.grid(row=6,column=4,pady=(40,0),columnspan=4)
    infolab=Label(root,fg="white",bg="black",text="Press Any Key To Start",font=("TImes New Roman",17,"bold"))
    infolab.grid(row=7,column=0,pady=(5,0),columnspan=8)
    exitlab=Button(root,fg="yellow",bg="black",text="QUIT CURRENT TEST",command=(HomeScreen),font=("TImes New Roman",17,"bold"))
    exitlab.grid(row=8,column=0,pady=(15,0),columnspan=8)

    def countdown():
        global time,speed,root,PauseTimer,speedvar4
        if Sprint==True or Marathon==True:
            time=0
            
            def countup():
                global time
                if PauseTimer%2==0:
                    time=time
                    infolab.config(text="Press Any Key To Restart")
                    
                else:
                    
                    time+=1
                    infolab.config(text="")
                if StopTimer==False:
                    speedvar1=time/60
                    speedvar2=length/5
                    speedvar3=wrongkeystrokes/5
                    speedvar4=speedvar2/speedvar1
                    speed=round(speedvar4-speedvar3,2)
              
                    timelab.configure(text=time)
                    if Marathon==True:
                        showTypingSpeed(speed)

                    timelab.after(1000,countup)
                    if speedvar2>=10 and Sprint==True:
                        timeup(root,speed,length,speedvar4,time)
                    elif speedvar2>=1000 and Marathon==True:
           
                        timeup(root,speed,length,speedvar4,time)
            countup()
        else:
            if time!=0:
                if PauseTimer%2==0:
                    time=time
                    infolab.config(text="Press Any Key To Restart")
                else:
                    time-=1
                    infolab.config(text="")
                if time>0:
                    speedtimer=60-time
                    speedvar2=speedtimer/60
                    speedvar1=length/5
                    speedvar3=wrongkeystrokes/5
                    speedvar4=speedvar1/speedvar2
                    speed=round(speedvar4-speedvar3)
                
                    timelab.configure(text="")
                timelab.after(1000,countdown)

            if time==0:
                
                time=60
                timeup(root,speed,length,speedvar4,time)
            
        
            
            
    keypressList=[]
    wrongkeystrokes=0
        
    def colorchangecorrect(wid):

        wid.configure(fg="black")
    def colorchangewrong(wid):

        wid.configure(fg="red")

    def returnDefaults():
        for widgets in widList:
            widgets.configure(fg="yellow")
        
    def click(keycode):
        global wrongkeystrokes,index,correct,wrong,text1,text2,text3,text4,text5,text6,text7,text8,text1b,text2b,text3b,text4b,text5b,text6b,text7b,text8b
        wordsList=[text1,text2,text3,text4,text5,text6,text7,text8]
        activewid=widList[index]
        activeword=wordsList[index]
        keystrokes=inputText.get()
        keypressList.append(keycode)
        
        if keystrokes.strip(" ")==activeword:
            correct+=1
            colorchangecorrect(activewid)
            try:
                glass.play()
                
            except:
                pass
        elif keystrokes.strip(" ")!=activeword:
            wrong+=1
            wrongkeystrokes+=len(activeword)
            colorchangewrong(activewid)

        inputText.delete(0,END)
        if index==7:
            try:
                
                winsound.PlaySound("explode",winsound.SND_ASYNC)
            except:
                pass
            returnDefaults()
            text1=text1b
            text2=text2b
            text3=text3b
            text4=text4b
            text5=text5b
            text6=text6b
            text7=text7b
            text8=text8b
            text1b=random.choice(ffdict.list9)
            text2b=random.choice(ffdict.list10)
            text3b=random.choice(ffdict.list11)
            text4b=random.choice(ffdict.list12)
            text5b=random.choice(ffdict.list13)
            text6b=random.choice(ffdict.list14)
            text7b=random.choice(ffdict.list15)
            text8b=random.choice(ffdict.list16)
            winLabs()
            
            index=-1
        index+=1
        

    def showTypingSpeed(speed):
        WPMlab.configure(text=speed)

    def startcountdown(keycode):
        global length,PauseTimer

        #mixer.music.pause()
        
        
        keypressList.append(keycode)
        length=len(keypressList)
        PauseTimer=1
        if length==1:
            countdown()
    def backspace(keycode):
        global CorrectedMistakes
        CorrectedMistakes+=1
        keypressList.pop()
               
        pass
    def PauseGame(keycode):
        global PauseTimer
        PauseTimer+=1
    inputText.bind("<space>",click)
    inputText.bind("<Key>",startcountdown)
    inputText.bind("<Return>",PauseGame)
    inputText.bind("<BackSpace>",backspace)




    
    
mainframe=Frame(win,bg="black",width=1000)
mainframe.grid(row=0,column=0,sticky="nswe")

heading=Label(mainframe,text="WHAT SHOULD YOUR FINGERS AND CHEETAHS HAVE IN COMMON?"
                  ,bg="black",fg="white",font=("Times New Roman",
                            21, "bold"))
heading.grid(row=0,column=0,columnspan=10,padx=(220,185),pady=(0,150))
menuframe=Frame(mainframe,bg="#0e0e0e",bd=20)
menuframe.grid(row=1,column=0,columnspan=2,sticky="w")




def StartSprintTyping():

    Sprint=True
    Marathon=False

    maingameframe(Sprint,Marathon)

def StartMarathonTyping():
   
    Marathon=True
    Sprint=False
   
    maingameframe(Sprint,Marathon)

def StartOneMinuteTyping():

    Sprint=False
    Marathon=False

    maingameframe(Sprint,Marathon)
    

    
menulab1=Label(menuframe,text="Select Typing Test Configuration",bg="black",fg="white",font=("Times New Roman",
                        14, "bold")).grid(row=1,column=0,sticky="w",pady=(15,15))
sprintTypingbtn=Button(menuframe,bg="black",fg="yellow",text="Sprint Typing (10 Words)",font=("Times New Roman",
                        14, "bold"),command=StartSprintTyping)
sprintTypingbtn.grid(row=2,column=0,sticky="w",pady=(15,15))
oneminutebtn=Button(menuframe,bg="black",fg="yellow",text="60 Seconds Flex Typing",font=("Times New Roman",
                        14, "bold"),command=StartOneMinuteTyping)
oneminutebtn.grid(row=3,column=0,sticky="w",pady=(15,15))
marathontypebtn=Button(menuframe,bg="black",fg="yellow",text="Marathon Typing(1000 words)",font=("Times New Roman",
                        14, "bold"),command=StartMarathonTyping)
marathontypebtn.grid(row=4,column=0,sticky="w",pady=(15,15))

otheroptionsLab=Label(menuframe,text="Other options",bg="black",fg="white",font=("Times New Roman",
                        14, "bold"))
otheroptionsLab.grid(row=5,column=0,sticky="w",pady=(30,15))
userstats=Button(menuframe,bg="black",fg="yellow",text="View statistics",font=("Times New Roman",
                        14, "bold"),command=show_stats)
userstats.grid(row=6,column=0,sticky="w",pady=(15,15))
def disable(disableMenu):
    if disableMenu==True:
        sprintTypingbtn.config(state=DISABLED)
        oneminutebtn.config(state=DISABLED)
        marathontypebtn.config(state=DISABLED)
        userstats.config(state=DISABLED)
    else:
        sprintTypingbtn.config(state=NORMAL)
        oneminutebtn.config(state=NORMAL)
        marathontypebtn.config(state=NORMAL)
        userstats.config(state=NORMAL)


def HomeScreen():
    global selection,root
    try:
        root.destroy()
    except:
        pass
    try:
        timeupFrame.destroy()
    except:
        pass
    selection=Frame(mainframe,bg="black")
    selection.grid(row=1,column=2,columnspan=8)
    GameLogoLabel=Label(selection,image=gameLogo,bd=0)
    GameLogoLabel.grid(row=0,column=0)
    disableMenu=False
    disable(disableMenu)
    
HomeScreen()


for button in [sprintTypingbtn,oneminutebtn,marathontypebtn,userstats]:
    
    
        button.bind("<Enter>",onenter)
        button.bind("<Leave>",onleave)


def timeup(root,speed,length,rawSpeed,time):
    global correct,wrong,disableMenu,timeupFrame
    
    root.destroy()
    day=datetime.date.today()
    formatted_day=str(day.strftime("%d %B %Y"))
    if wrong<=0.1*correct:
        conn=sqlite3.connect("typing.db")
        cur=conn.cursor()
        try:
            cur.execute("""CREATE TABLE typing_stats(date text, speed integer, keystrokes integer)""")
        except:
            pass
        cur.execute("INSERT INTO typing_stats VALUES(:date, :speed, :keystrokes)",{"date":formatted_day, "speed":speed, "keystrokes":length})
        conn.commit()
        cur.execute("DELETE FROM typing_stats WHERE speed<=40")
        conn.commit()
        conn.close()
    disableMenu=False
    disable(disableMenu)
    #mixer.music.unpause()
    timeupFrame=Frame(mainframe,bg="black")
    timeupFrame.grid(row=1,column=2,columnspan=8)

        
    timeuplab1=Label(timeupFrame,text="BRAVO, YOU COMPLETED THAT TEST"
                      ,bg="black",fg="white",font=("Times New Roman",
                                21, "bold"))
    timeuplab1.grid(row=0,column=0,columnspan=4,padx=(180,165),pady=(0,50))

        

    timeuplab2=Label(timeupFrame,text="STATISTICS:",bg="black",fg="yellow",font=("Times New Roman",
                            20, "bold"))
    timeuplab2.grid(row=1,column=0,columnspan=4,padx=(220,185))
    timeuplab3=Label(timeupFrame,text="AVERAGE TYPING SPEED(WPM)" ,bg="#0e0e0e",fg="yellow",font=("Times New Roman",19,"bold"))
    timeuplab3.grid(row=2,column=0,columnspan=2,sticky="w")
    timeuplab3b=Label(timeupFrame,text=speed,bg="#0e0e0e",fg="yellow",font=("Times New Roman",19,"bold"))
    timeuplab3b.grid(row=2,column=2,columnspan=2,sticky="e")

    timeuplab5=Label(timeupFrame,text="KEYSTROKES",bg="#0e0e0e",fg="yellow",font=("Times New Roman",19,"bold"))
    timeuplab5.grid(row=4,column=0,columnspan=2,sticky="w")
    timeuplab5b=Label(timeupFrame,text=length,bg="#0e0e0e",fg="yellow",font=("Times New Roman",19,"bold"))
    timeuplab5b.grid(row=4,column=2,columnspan=2,sticky="e")
    timeuplab6=Label(timeupFrame,text="CORRCT WORDS",bg="#0e0e0e",fg="yellow",font=("Times New Roman",19,"bold"))
    timeuplab6.grid(row=5,column=0,columnspan=2,sticky="w")
    timeuplab6b=Label(timeupFrame,text=correct,bg="#0e0e0e",fg="yellow",font=("Times New Roman",19,"bold"))
    timeuplab6b.grid(row=5,column=2,columnspan=2,sticky="e")
    timeuplab7=Label(timeupFrame,text="WRONG WORDS",bg="#0e0e0e",fg="yellow",font=("Times New Roman",19,"bold"))
    timeuplab7.grid(row=6,column=0,columnspan=2,sticky="w")
    timeuplab7b=Label(timeupFrame,text=wrong,bg="#0e0e0e",fg="yellow",font=("Times New Roman",19,"bold"))
    timeuplab7b.grid(row=6,column=2,columnspan=2,sticky="e")
    
    timeuplab8=Label(timeupFrame,text="NET TYPING SPEED",bg="#0e0e0e",fg="yellow",font=("Times New Roman",19,"bold"))
    timeuplab8.grid(row=7,column=0,columnspan=2,sticky="w")
    timeuplab8b=Label(timeupFrame,text=round(rawSpeed),bg="#0e0e0e",fg="yellow",font=("Times New Roman",19,"bold"))
    timeuplab8b.grid(row=7,column=2,columnspan=2,sticky="e")

    timeuplab9=Label(timeupFrame,text="CORRECTED MISTAKES",bg="#0e0e0e",fg="yellow",font=("Times New Roman",19,"bold"))
    timeuplab9.grid(row=8,column=0,columnspan=2,sticky="w")
    timeuplab9b=Label(timeupFrame,text=CorrectedMistakes,bg="#0e0e0e",fg="yellow",font=("Times New Roman",19,"bold"))
    timeuplab9b.grid(row=8,column=2,columnspan=2,sticky="e")
    infolab=Label(timeupFrame,text="CONGRATULATIONS!!!",bg="#0e0e0e",fg="green",font=("Times New Roman",19,"bold"))
    infolab.grid(row=9,column=0,columnspan=4)

    if wrong>0.1*correct:
        
        
        timeuplab1.config(text="FOCUS ON ACCURACY RATHER THAN SPEED")
        infolab.config(text="Data won't be saved", fg="red")

win.mainloop()
