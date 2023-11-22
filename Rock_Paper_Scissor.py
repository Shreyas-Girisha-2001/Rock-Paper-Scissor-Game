#Written by : Shreyas Girisha
#Date of creation : 22-November-2023

import tkinter as tk                #used to create GUI
import random                       #used to generate random number
from tkinter import messagebox      #used to create message box 
from PIL import Image,ImageTk       #used to make some modifications on image (resizing)

#function name: image_path
#function return type: list of strings
#function parameters: void
#function use: stores path for image file

def image_path():
    imglist=["image1.jpg","image2.jpg","image3.jpg"]
    return imglist

#function name: main
#function return type: void
#function parameters: void
#function use: used to create window with frame and GUI embedded to ask user his/her game name

def main():
    global askusergamename                      #Made window global as it needs to be accessible in other function to perform destroy on window.
    askusergamename=tk.Tk()
    askusergamename.title("Welcome user")
    askusergamename.geometry("420x130")
    askusergamename.resizable(False,False)                      #Making window non-resizable

    frame=tk.Frame(askusergamename,bg="#0d3b66")
    frame.place(x=0,y=0,height=130,width=420)

    label=tk.Label(frame,text="What is your game name : ",font=("Arial",15,"bold"),foreground="#faf0ca",background="#0d3b66")
    label.place(x=30,y=30)

    global textfield
    textfield=tk.Entry(frame,background="#faf0ca",foreground="#000000",font=("Arial",15))
    textfield.place(x=220,y=30)

    btnsubmit=tk.Button(frame,text="Submit",background="#faf0ca",foreground="#000000",font=("Arial",15),command=fetchGamename)
    btnsubmit.place(x=185,y=80)

    askusergamename.mainloop()
#function name: fetchGamename
#function return type: void
#function parameters: void
#function use: used to create window with frame and GUI which checks if username is entered or not and if entered creates mainscreen.
 
def fetchGamename():
    global usergamename
    usergamename=str(textfield.get())                   #Made usergamename global to make it accessible in different methods.
    if(usergamename==""):
        messagebox.showerror("Error","user's game name not entered ! Please enter and proceed")                     #error message shown when username is not entered                 
    else:
        imglist=image_path()
        askusergamename.destroy()                   #destroying old window used to askuser his game name
        global mainscreen                        #Made window global as it needs to be accessible in other function to perform destroy on window.
        
        mainscreen=tk.Tk()
        mainscreen.geometry("830x320")
        mainscreen.title("Rock Paper Scissor")
        mainscreen.resizable(False,False)

        frame=tk.Frame(mainscreen,bg="#0d3b66")
        frame.place(x=0,y=0,width=830,height=320) 

        label=tk.Label(frame,background="#0d3b66",foreground="#faf0ca",text="Select Rock , Paper or Scissors from below Images",font=("Arial",20,"bold"))
        label.place(x=180,y=10)

        #loading images using Image.open from Pillow library

        rockimg=Image.open(r""+imglist[0])
        paperimg=Image.open(r""+imglist[1])
        scissorimg=Image.open(r""+imglist[2])

        #resizing loaded image using Image.resize
        rockimg=rockimg.resize((150,150),Image.ANTIALIAS)
        paperimg=paperimg.resize((150,150),Image.ANTIALIAS)
        scissorimg=scissorimg.resize((150,150),Image.ANTIALIAS)

        #resizing image to fit in window
        rockimg=ImageTk.PhotoImage(rockimg)
        paperimg=ImageTk.PhotoImage(paperimg)
        scissorimg=ImageTk.PhotoImage(scissorimg)


        rock=tk.Label(mainscreen,image=rockimg,background="#0d3b66")
        rock.place(x=100,y=70,height=150,width=150)
        paper=tk.Label(mainscreen,image=paperimg,background="#0d3b66")
        paper.place(x=350,y=70,height=150,width=150)
        scissor=tk.Label(mainscreen,image=scissorimg,background="#0d3b66")
        scissor.place(x=600,y=70,height=150,width=150)

        global radioval
        radioval=tk.StringVar()

        #Radio button to make user make his choice.
        paperradiobtn=tk.Radiobutton(frame,variable=radioval,value="Paper",text="Paper",font=("Arial",20,"bold"),fg="#faf0ca",bg="#0d3b66")
        rockradiobtn=tk.Radiobutton(frame,variable=radioval,value="Rock",text="Rock",font=("Arial",20,"bold"),fg="#faf0ca",bg="#0d3b66")
        scissorradiobtn=tk.Radiobutton(frame,variable=radioval,value="Scissor",text="Scissor",font=("Arial",20,"bold"),fg="#faf0ca",bg="#0d3b66")
        
        paperradiobtn.place(x=380,y=220)
        rockradiobtn.place(x=135,y=220)
        scissorradiobtn.place(x=625,y=220)

        submitbtn=tk.Button(frame,text="Submit",background="#faf0ca",foreground="#000000",font=("Arial",15),command=confirmchoice)
        submitbtn.place(x= 370,y=270)

        mainscreen.mainloop()

#function name: confirmchoice
#function return type: void
#function parameters: void
#function use: used to create window with frame and GUI which checks if user picked a choice and call respective function if user did select

def confirmchoice():
    if(radioval.get() ==""):
        messagebox.showinfo("Selection","Please select any options of your choice from above !")
    else:
        res=messagebox.askyesno("Regarding your choice !","Are you sure with your choice as "+radioval.get())
        if(res==True):
            mainscreen.destroy()
            makecomputerchoose(radioval.get())
        else:
            pass

#function name: makecomputerchoose
#function return type: void
#function parameters: userchoice (String)
#function use: used to create window with frame and GUI which makes computer to make his choice 

def makecomputerchoose(userchoice):
    if(userchoice=="Rock"):
        userchoice=0
    if(userchoice=="Paper"):
        userchoice=1
    if(userchoice=="Scissor"):
        userchoice=2
    computerchoice=random.randint(0,2)
    show_result(userchoice,computerchoice)


#function name: show_result
#function return type: void
#function parameters: uc (userchoice, integer), cc (computerchoice, integer)
#function use: used to create window with frame and GUI which shows the choice made by both computer and user and dedices who is the winner

def show_result(uc,cc):
    imglist=image_path()
    global resultscreen
    resultscreen=tk.Tk()
    resultscreen.geometry("400x400")
    resultscreen.title("Results")
    resultscreen.resizable(False,False)
    frame=tk.Frame(resultscreen,bg="#0d3b66")
    frame.place(x=0,y=0,width=400,height=400)

    userimage=Image.open(r""+imglist[uc])
    userimage=userimage.resize((100,100),Image.ANTIALIAS)
    userphoto=ImageTk.PhotoImage(userimage)
    userchoicelbl=tk.Label(resultscreen,text=usergamename+"'s Move",font=("Arial",15,"bold"),background="#0d3b66",foreground="#faf0ca")
    userchoicelbl.place(x=150,y=10)
    userphotolbl=tk.Label(resultscreen,image=userphoto,background="#0d3b66")
    userphotolbl.place(x=150,y=40,width=100,height=100)

    computerimage=Image.open(r""+imglist[cc])
    computerimage=computerimage.resize((100,100),Image.ANTIALIAS)
    computerphoto=ImageTk.PhotoImage(computerimage)
    computerchoicelbl=tk.Label(resultscreen,text="Computer's Move",font=("Arial",15,"bold"),background="#0d3b66",foreground="#faf0ca")
    computerchoicelbl.place(x=140,y=145)
    computerphotolbl=tk.Label(resultscreen,image=computerphoto,background="#0d3b66")
    computerphotolbl.place(x=150,y=175,width=100,height=100)

    retrybtn=tk.Button(resultscreen,text="Retry",command=retry,font=("Arial",15))
    retrybtn.place(x=320,y=350)

    exitbtn=tk.Button(resultscreen,text="Exit",command=exit,font=("Arial",15))
    exitbtn.place(x=10,y=350)

    result=""
    if(uc==cc):
        result="It's a tie !"
    if(uc==0 and cc==1):
        result="Computer wins !"
    if(uc==0 and cc==2):
        result=usergamename+" wins !"
    if(uc==1 and cc==0):
        result=usergamename+" wins !"
    if(uc==1 and cc==2):
        result="Computer wins !"
    if(uc==2 and cc==0):
        result="Computer wins !"
    if(uc==2 and cc==1):
        result=usergamename+" wins !"

    resultlbl=tk.Label(resultscreen,text=result,font=("Arial",15,"bold"),background="#0d3b66",foreground="#faf0ca")
    resultlbl.place(x=150,y=300)
    
    resultscreen.mainloop()

#function name: retry
#function return type: void
#function parameters: void
#function use: used to destory result screen and redirects to start again

def retry():
    resultscreen.destroy()
    main()


main()