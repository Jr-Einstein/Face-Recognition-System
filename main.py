from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("VTOP Face Attendance System")
        #blue bar pic in header
        img=Image.open(r"C:\Users\amans\OneDrive\Desktop\face_recognition system\college_images\collegepic.jpg")
        img=img.resize((1370,190),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1370,height=90)
        #logo image
        img1=Image.open(r"C:\Users\amans\OneDrive\Desktop\face_recognition system\college_images\logo.jpg")
        img1=img1.resize((155,90),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=155,height=90)
        
        #bg image
        img2=Image.open(r"C:\Users\amans\OneDrive\Desktop\face_recognition system\college_images\bg.jpg")
        img2=img2.resize((1530,710),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=90,width=1530,height=610)
        #title i am hiding it for now as i have text on image only
        title_lbl=Label(f_lbl,text="VIT BHOPAL FACE ATTENDANCE SYSTEM               ",font=("times new roman",20,"bold"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        title_lbl=Label(f_lbl,text="Crafted by a team of VIT students, our Face Attendance System unifies Faculty, Staff, Students, Parents, and Alumni on a single platform.                                        ",font=("times new roman",9,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=40,width=1530,height=45)
        
        # student button
        img3=Image.open(r"C:\Users\amans\OneDrive\Desktop\face_recognition system\college_images\student.jpg")
        img3=img3.resize((210,150),Image.ADAPTIVE)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        b1=Button(f_lbl,image=self.photoimg3,command=self.student_details,cursor="hand2")
        b1.place(x=130,y=100,width=190,height=150)
        
        b1_1=Button(f_lbl,text="Student Details",command=self.student_details,cursor="hand2",font=("gineva",11,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=130,y=250,width=190,height=40)
        
        # detect face button
        img4=Image.open(r"C:\Users\amans\OneDrive\Desktop\face_recognition system\college_images\detectface.jpg")
        img4=img4.resize((210,150),Image.ADAPTIVE)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(f_lbl,image=self.photoimg4,cursor="hand2",command=self.face_data)
        b1.place(x=430,y=100,width=190,height=150)
        
        b1_1=Button(f_lbl,text="Face Detector",command=self.face_data,cursor="hand2",font=("gineva",11,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=430,y=250,width=190,height=40)
        
        # Attedance  button
        img5=Image.open(r"C:\Users\amans\OneDrive\Desktop\face_recognition system\college_images\attendance.jpg")
        img5=img5.resize((210,150),Image.ADAPTIVE)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(f_lbl,image=self.photoimg5,cursor="hand2")
        b1.place(x=730,y=100,width=190,height=150)
        
        b1_1=Button(f_lbl,text="Attendance",cursor="hand2",font=("gineva",11,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=730,y=250,width=190,height=40)

        # Help  button
        img6=Image.open(r"C:\Users\amans\OneDrive\Desktop\face_recognition system\college_images\help.jpg")
        img6=img6.resize((210,150),Image.ADAPTIVE)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(f_lbl,image=self.photoimg6,cursor="hand2")
        b1.place(x=1030,y=100,width=190,height=150)
        
        b1_1=Button(f_lbl,text="Help Desk",cursor="hand2",font=("gineva",11,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=1030,y=250,width=190,height=40)

        # Train Face  button
        img7=Image.open(r"C:\Users\amans\OneDrive\Desktop\face_recognition system\college_images\traindata.jpg")
        img7=img7.resize((210,150),Image.ADAPTIVE)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(f_lbl,image=self.photoimg7,command=self.train_data,cursor="hand2")
        b1.place(x=130,y=310,width=190,height=150)
        
        b1_1=Button(f_lbl,text="Train Data",command=self.train_data,cursor="hand2",font=("gineva",11,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=130,y=450,width=190,height=40)

        # Photos button
        img8=Image.open(r"C:\Users\amans\OneDrive\Desktop\face_recognition system\college_images\photos.jpg")
        img8=img8.resize((210,150),Image.ADAPTIVE)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(f_lbl,image=self.photoimg8,cursor="hand2",command=self.open_img)
        b1.place(x=430,y=310,width=190,height=150)
        
        b1_1=Button(f_lbl,text="Photos",cursor="hand2",command=self.open_img,font=("gineva",11,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=430,y=450,width=190,height=40)
      
        # Developer Info button
        img9=Image.open(r"C:\Users\amans\OneDrive\Desktop\face_recognition system\college_images\developerinfo.jpg")
        img9=img9.resize((210,150),Image.ADAPTIVE)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(f_lbl,image=self.photoimg9,cursor="hand2")
        b1.place(x=730,y=310,width=190,height=150)
        
        b1_1=Button(f_lbl,text="Developer's Info",cursor="hand2",font=("gineva",11,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=730,y=450,width=190,height=40)

        # exit Info button
        img10=Image.open(r"C:\Users\amans\OneDrive\Desktop\face_recognition system\college_images\exit.jpg")
        img10=img10.resize((210,150),Image.ADAPTIVE)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(f_lbl,image=self.photoimg10,cursor="hand2")
        b1.place(x=1030,y=310,width=190,height=150)
        
        b1_1=Button(f_lbl,text="Exit",cursor="hand2",font=("gineva",11,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=1030,y=450,width=190,height=40)
        
        
        
        
    #    copyright
    
        title_lbl=Label(f_lbl,text="Copyright © 2024 Project Exhibition - II Team 34                                              ",font=("times new roman",9,"bold"),bg="white",fg="black")
        title_lbl.place(x=410,y=560,width=670,height=45)
        
        
        
        
    def open_img(self):
        os.startfile("data")
        
        
        
        
        
        
        
        
    # =============Function Buttons==================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)   
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window) 
          
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window) 
        
        
        
        
        

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()     
    