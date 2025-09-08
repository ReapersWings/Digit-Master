import random
import tkinter
from tkinter import messagebox
import re
import tkinter.messagebox

class number :
    def __init__(self):
        self.arraylabel=[]
        self.mainpage=tkinter.Tk()
        self.totalmark=0
        self.checkanswertime=0
        
    def functionstart(self):
        for w in self.mainpage.winfo_children() :
            w.destroy()
        if self.checkanswertime > 0:
            self.checkanswertime+=1
        else:
            self.checkanswertime=3
            
        self.randomnumber=random.randint(1000,100000)
        self.arrayrandomnumber=re.findall('[0-9]',str(self.randomnumber))
        self.entryvalue=[]
        for i in range(0,len(self.arrayrandomnumber)):
            entry=tkinter.Entry(justify='center')
            entry.grid(row=1,column=i)
            self.entryvalue.append(entry)
            
        self.changelabel=tkinter.Label(self.mainpage,text=f'Change : {self.checkanswertime}')
        self.changelabel.grid(row=0,column=1 ,)
        tkinter.Label(self.mainpage,text=f'Total mark : {self.totalmark}').grid(row=0,column=len(self.arrayrandomnumber)-2)
        tkinter.Button(self.mainpage,text='Guest',command=class1.check_answer).grid(row=3,column=0 ,columnspan=len(self.arrayrandomnumber))
        self.mainpage.mainloop()
        
    def check_answer(self):
        try:
            if self.checkanswertime > 0:
                timecheck=self.checkanswertime-1
                self.checkanswertime=timecheck
                self.changelabel.config(text=f'Change : {self.checkanswertime}')
                self.everyentryvalue=(input.get() for input in self.entryvalue)
                self.arrayentryvalue=[*self.everyentryvalue]
                self.currectanswer=0 ; 
                if len(self.arraylabel) > 0 :
                    for i in self.arraylabel :
                        i.destroy()
                    self.arraylabel.clear()
                for i in range(0,len(self.arrayentryvalue)) :
                    if int(self.arrayentryvalue[i]) < 10:
                        if self.arrayentryvalue[i]==self.arrayrandomnumber[i] :
                            label=tkinter.Label(self.mainpage,bg="green",fg='white',text='This number is currect !')
                            label.grid(row=2,column=i)
                            self.arraylabel.append(label)
                            self.currectanswer+=1
                            if int(self.currectanswer) == 5:
                                self.totalmark+=1
                                class1.functionstart()
                            # print(self.currectanswer)
                        else :
                            if self.arrayentryvalue[i] in self.arrayrandomnumber :
                                label=tkinter.Label(self.mainpage,bg='yellow',text='This number wrong plece!')
                                label.grid(row=2,column=i)
                                self.arraylabel.append(label)
                            else :
                                if self.arrayrandomnumber[i] > self.arrayentryvalue[i] :
                                    answer=int(self.arrayrandomnumber[i])-int(self.arrayentryvalue[i])
                                else :
                                    answer=int(self.arrayentryvalue[i])-int(self.arrayrandomnumber[i])
                                label=tkinter.Label(self.mainpage,bg='yellow',text=f'This number between answer is {answer} !')
                                label.grid(row=2,column=i)
                                self.arraylabel.append(label)
                    else:
                        label=tkinter.Label(self.mainpage,bg='red',fg='white',text="The number can't more 9")
                        label.grid(row=2,column=i)
                        self.arraylabel.append(label)
            else:
                tkinter.messagebox.showerror('Game Over',f'chenge is used finish! Your mark : {self.totalmark}')
                self.totalmark=0
                class1.functionstart()
        except ValueError as answer:
            tkinter.Label(self.mainpage,bg='red',fg='white',text='Only can input number').grid(row=4,column=0 ,columnspan=len(self.arrayrandomnumber))
                
class1=number()
class1.functionstart()

#cd path
#python -m PyInstaller --onefile filename.py