import mysql.connector as sqlcon
import tkinter as tin
import webbrowser
import requests
import time
                if not hdlLink in categHeadlineLinks:
                    categHeadlines.append(h)
                    categHeadlineLinks.append(hdlLink)
        elif searchStr in hdlLink:
            if not hdlLink in categHeadlineLinks:


                categHeadlines.append(h)
                categHeadlineLinks.append(hdlLink)

    def openHeadlineLink(link):
        webbrowser.open_new(link)
   
    unwanted = ['BBC World News TV', 'BBC World Service Radio','News daily newsletter', 'Mobile app', 'Get in touch']

    ycoord=150  
    for i in range(0,len(categHeadlines)):
        hdl = categHeadlines[i]
        hdlLink = categHeadlineLinks[i]
        if hdl.text.strip() not in unwanted:
            categHead=tin.Button(
                win4,
                text=hdl.text.strip(),
                font=("Courier",13),
                fg='black',
                bg='#C19FB3',
                width=100,
                height=1,
                command = partial(openHeadlineLink,hdlLink),
            )
            categHead.pack()
            categHead.place(x=250,y=ycoord)
        ycoord+=32

    def read():        
        for i in list(dict.fromkeys(categHeadlines)):
            if i.text.strip() not in unwanted:
                voice.Speak(i.text.strip())
           
    read=tin.Button(
        win4,
        text='READ',
        font=("Courier",15),
        fg='white',
        bg='red',
        width=10,
        height=2,
        command=read,
        )
    read.pack()
    read.place(x=50,y=100)

    win4back=tin.Button(
        win4,
        text='BACK',
        font=("Courier",15),
        fg='white',
        bg='red',
        width=6,
        height=1,
        command=win4.destroy,
    )
    win4back.pack()
    win4back.place(y=0, x=0)
   
    win4.mainloop()

def indnews():
    webbrowser.open_new("https://www.indiatoday.in/india")
def weathernews():
    webbrowser.open_new("https://www.timeanddate.com/weather/@12022490")
   
def newswin():
    win3= tin.Toplevel(win1)
    win3.attributes('-fullscreen', True)
    win3.configure(bg="#C19FB3")
   
    topicslbl=tin.Label(
        win3,
        text='TOPICS: ',
        font=("Courier",50),
        fg='black',
        bg='#C19FB3',
        width=20,
        height=4,
    )
    topicslbl.pack()
    topicslbl.place(x=400, y=5)
   
    sportsbtn=tin.Button(
        win3,
        text='SPORTS',
        font=("Courier",30),
        fg='black',
        bg='#4C7486',
        width=20,
        height=2,
        command= partial(openCategHeadlines,'SPORTS','/sport',None),
    )
    sportsbtn.pack()
    sportsbtn.place(y=250, x=200)
   
    entertainmentbtn=tin.Button(
        win3,
        text='ENTERTAINMENT',
        font=("Courier",30),
        fg='black',
        bg='#4C7486',
        width=20,
        height=2,
        command = partial(openCategHeadlines,'ENTERTAINMENT','/entertainment-arts',None),
    )
    entertainmentbtn.pack()
    entertainmentbtn.place(y=250, x=850)
   
    worldbtn=tin.Button(
        win3,
        text='WORLD',
        font=("Courier",30),
        fg='black',
        bg='#4C7486',
        width=20,
        height=2,
        command = partial(openCategHeadlines,'WORLD','/world',None),
    )
    worldbtn.pack()
    worldbtn.place(y=400, x=200)
   
    businessbtn=tin.Button(
        win3,
        text='BUSINESS',
        font=("Courier",30),
        fg='black',
        bg='#4C7486',
        width=20,
        height=2,
        command=partial(openCategHeadlines,'BUSINESS','/business',None),
    )
    businessbtn.pack()
    businessbtn.place(y=400, x=850)
   
    techbtn=tin.Button(
        win3,
        text='TECHNOLOGY',
        font=("Courier",30),
        fg='black',
        bg='#4C7486',
        width=20,
        height=2,
        command = partial(openCategHeadlines,'TECHNOLOGY','/technology',None),
    )
    techbtn.pack()
    techbtn.place(y=550, x=200)
   
    othersbtn=tin.Button(
        win3,
        text='OTHERS',
        font=("Courier",30),
        fg='black',
        bg='#4C7486',
        width=20,
        height=2,
        command = partial(openCategHeadlines,'OTHERS','',['/sport','/entertainment-arts','/world','/business','/technology']),
    )
    othersbtn.pack()
    othersbtn.place(y=700, x=850)
   
    weatherbtn=tin.Button(
        win3,
        text='WEATHER',
      font=("Courier",30),
        fg='black',
        bg='#4C7486',
        width=20,
        height=2,
        command=weathernews,
    )
    weatherbtn.pack()
    weatherbtn.place(y=700, x=200)

    indiabtn=tin.Button(
        win3,
        text='INDIA',
        font=("Courier",30),
        fg='black',
        bg='#4C7486',
        width=20,
        height=2,
        command = indnews,
    )
    indiabtn.pack()
    indiabtn.place(y=550, x=850)
   
    win3back=tin.Button(
        win3,
        text='BACK',
        font=("Courier",15),
        fg='white',
        bg='red',
        width=6,
        height=1,
        command=win3.destroy,
    )
    win3back.pack()
    win3back.place(y=0, x=0)
   
    win3.mainloop()


win1.mainloop()
mycon.close()
