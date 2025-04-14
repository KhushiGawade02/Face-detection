from logging import root
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import tkinter as tk
import cv2
import os
import numpy as np





class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Training Data")
        
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #img_top=Image.open(".png")
        #img_top=img_top.resize((1530,325),Image.Resampling.LANCZOS)
        #self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        #f_lbl=Label(self.root,image=self.photoimg_top)
        #f_lbl.place(x=0,y=55,width=1530,height=325)
        
        # button
        b1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=200,y=100,width=220,height=220)
        
    def train_classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')    #Gray Scale Image
            imageNp=np.array(img,'uint8') #uint is a data type
            id=int(os.path.split(image)[1].split('.')[1]) 
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13 #13=Enter
        ids = np.array(ids)  
        
        #--------------Train classifier----------------
        
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset completed!")
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=tk.Tk()
    obj=Train(root)
    root.mainloop()
