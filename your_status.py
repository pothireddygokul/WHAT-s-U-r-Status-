from selenium import webdriver   #module for selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time  #used for pausing program
import os    #used for file handling
import random 
from tkinter import * # GUI
root1=Tk()

root1.geometry("300x300")
lab1=Label(root1,text="NAME",bg="grey",font=("Adorable",9))
ent1=Entry(root1)
but1=Button(root1,text="LOGIN")
lab2=Label(root1,text="PASSWORD",bg="grey",font=("Adorable",9))
ent2=Entry(root1,show="*")
fram=Frame(root1,height=150)
fram1=Frame(root1,width=50)
fram.grid(row=0,column=0)
fram1.grid(row=0,column=0)
lab1.grid(row=0,column=1)
lab2.grid(row=1,column=1)
ent1.grid(row=0,column=2)
ent2.grid(row=1,column=2)
root1.configure(background="black")
root1.title("LOGIN PAGE")
global im
im=1
   

def func2(event):
    
    if(len(ent2.get())>0):  #if details entered
        u1=ent1.get()   #id
        p1=ent2.get()   #passord
        root=Tk()
       
        while(1):  #infinite loop to run whole time
            def func1(a,im):  #fun after selecting your area of intrest
                ar=[]
                def ran():  #image id
                    im=random.randint(1,11)
                    if im not in ar:
                        ar.append(im)
                        return(im)
                    else:
                        ran()
                k=ran()
                search_queries =['best gym quotes','best love quotes','best education quotes','best friends quotes']  #files name of each area of intrest already defined
                global b,ipath
                b=a.upper()
                dic={'GYM':0,'LOVE':1,'EDUCATION':2,'FRIENDS':3}  # change this we buttons changed and also search_queris list too
                query=dic[b]
                print(query)
                ipath="D://codes//downloads//"+search_queries[query]+"//"+str(k)+'.jpg'  #image path
            
            
                o=Options()
                o.add_argument("--disable-infobars")
                o.add_argument("start-maximized")
                o.add_argument("--disable-extensions")
                o.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1}) #used for stoping alert(allow/decline) on chrome
                
                
                driver = webdriver.Chrome(options=o, executable_path='D:\codes\chromedriver.exe')   # opens a chrome window
                driver.get('https://www.facebook.com')  #request for facebook
                uid=u1
                pas=p1
                
                username_box = driver.find_element_by_id('email')  #searches for id box
                username_box.send_keys(uid)
                
                password_box = driver.find_element_by_id('pass')    #searches for password box
                password_box.send_keys(pas)
                
                login_btn = driver.find_element_by_id('loginbutton')   #finds login button
                login_btn.submit()
                
                def func1():
                    return("<RETURN>")
                n=func1()
                print(4)
                
                x=driver.find_element_by_class_name('_7h4p')           # finds new status box 
               
                print(3)
                x.click()
                time.sleep(5)                  
                l=driver.find_elements_by_tag_name('input')           
                time.sleep(1)
                for g in l:
                    if g==driver.find_element_by_xpath("//input[@type='file'][@class='_n _5f0v']"):  #finds photo/video file to upload photo frm image path
                        g.send_keys(ipath)  #image path on ur disk
                        print('image loaded')
                        
                print(2)
               
                time.sleep(10)
                print(1)
                f=driver.find_elements_by_tag_name('button')   #post button locator
                time.sleep(5)
                for button in f:
                    if button.text=='Post':    
                        button.click()  # for post button
                print(0)
                print('POSTED!!')
                driver.close()
                time.sleep(30)
                
                print('NEXT DAY')
                
           
                
            def skip():
                print('Skiped!')
                time.sleep(30)
                
            def ex():
                print('ByE!!!')
                exit()
                
            frame=Frame(root,height=80,bg="Gold")
            lab=Label(root,text="wHat'S YOUR STATUS?",bg="black",fg="White",font=("Helvetica", 10))
            frame1=Frame(root,width=100,bg="blue")
            but1=Button(root,text="GyM",bg="Grey",fg="White")
            but2=Button(root,text="LoVE",bg="Grey",fg="White")
            but3=Button(root,text="EdUCATION",bg="Grey",fg="White")
            but4=Button(root,text="FrIENDS",bg="Grey",fg="White")
            but1['command'] = lambda arg1=but1.cget("text") : func1(arg1,im)
            but2['command'] = lambda arg1=but2.cget("text") : func1(arg1,im)
            but3['command'] = lambda arg1=but3.cget("text") : func1(arg1,im)
            but4['command'] = lambda arg1=but4.cget("text") : func1(arg1,im)
            frame.grid(row=1,column=0)
            frame1.grid(row=2,column=0)
            but1.grid(row=3,column=1)
            but2.grid(row=4,column=1)
            but3.grid(row=5,column=1)
            but4.grid(row=6,column=1)
            root.geometry("300x300")
            root.configure(background="black")
            root.title("MENU")
            but5=Button(root,text="SKIP!",bg="Grey")
            but6=Button(root,text="STOP!",bg="Grey")
            lab.grid(row=0,column=1)
            but5.grid(row=7,column=0)
            but6.grid(row=7,column=5)
            
            but5['command'] = lambda : skip()
            but6['command'] = lambda : ex()
            root.mainloop()  
    
        
        
    
    else:
        root2=Tk()
        lab3=Label(root2,text="ENTER SOMETHING ",bg="black",fg="White",font=("Helvetica", 10))
        lab3.pack()
        root2.mainloop()
        
but1.bind("<Button-1>",func2)
but1.grid(row=3,column=2)
root1.mainloop()           
exit()        

