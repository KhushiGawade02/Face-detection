from logging import root
from tkinter import*
from PIL import Image,ImageTk
from student_details import Student_Details
import os
from train import Train
from face_recognition import Face_Recognization
from attendance import Attendance
import tkinter as tk
from tkinter import messagebox

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #student detail button
        b1=Button(text="Student Details",command= self.student_details,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=200,y=100,width=220,height=220)
        
        #detect face button
        b2=Button(text="Face Detector",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=500,y=100,width=220,height=220)
        
        #attendance
        b3=Button(text="Attendance",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3.place(x=800,y=100,width=220,height=220)
        
        #train data
        b4=Button(text="Train Data",cursor="hand2",command=self.train_data, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4.place(x=200,y=400,width=220,height=220)
        
        
        #photos face
        b5=Button(text="Photos",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5.place(x=500,y=400,width=220,height=220)
        
        #exit
        b6=Button(text="Exit",command=self.exitApp, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6.place(x=800,y=400,width=220,height=220)
        
    def open_img(self):
        os.startfile("Data")
        
    def exitApp(self):
        self.exitApp = tk.messagebox.askyesno("Face Recognition","Are you sure?", parent= self.root)
        if self.exitApp>0:
            self.root.destroy()
        else:
            return
        
      
    # =========function button============
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_Details(self.new_window)
            
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognization(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

