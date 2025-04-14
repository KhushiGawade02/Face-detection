from logging import root
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import tkinter as tk
import cv2





class Student_Details:
        def __init__(self,root):
            self.root=root
            self.root.geometry("1530x790+0+0")
            self.root.title("Student Details")
            
            
        
            
            #-------------------Variables-------------
        
            self.var_dep=StringVar()
            self.var_course=StringVar()
            self.var_year=StringVar()
            self.var_semester=StringVar()
            self.var_std_id=StringVar()
            self.var_std_name=StringVar()
            self.var_div=StringVar()
            self.var_roll=StringVar()
            self.var_gender=StringVar()
            self.var_dob=StringVar()
            self.var_email=StringVar()
            self.var_phone=StringVar()
            
            
        
            title_lbl=Label(self.root, text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
            title_lbl.place(x=0,y=0,width=1530,height=45)
            
            #frame
            main_frame=Frame(self.root, bg="lightblue",bd=2)
            main_frame.place(x=0,y=50,width=1500,height=650)
            
            #left label frame
            Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
            Left_frame.place(x=40,y=10,width=730,height=580)   
                
            #current course
            Current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",15,"bold"))
            Current_course_frame.place(x=3,y=10,width=710,height=200) 
            
            #department
            dep_label=Label(Current_course_frame,text="Department",font=("times new roman",12,"bold"))
            dep_label.grid(row=0,column=0) 
            dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="read only")
            dep_combo['values']=("Select Department","CS","IT","EXTC","MECH")
            dep_combo.current(0)
            dep_combo.grid(row=0,column=1,padx=2,pady=10)           
            
            #course
            course_label=Label(Current_course_frame,text="Course",font=("times new roman",12,"bold"))
            course_label.grid(row=0,column=2,padx=10,sticky=W) 
            course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="read only")
            course_combo['values']=("Select Course","FE","SE","TE","BE")
            course_combo.current(0)
            course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)           
            
            #year
            year_label=Label(Current_course_frame,text="Year",font=("times new roman",12,"bold"))
            year_label.grid(row=1,column=0,padx=10,sticky=W) 
            year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")
            year_combo['values']=("Select Year","2020-21","2021-22","2022-23","2023-24")
            year_combo.current(0)
            year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W) 
            
            #semester
            semester_label=Label(Current_course_frame,text="Semester",font=("times new roman",12,"bold"))
            semester_label.grid(row=1,column=2,padx=10,sticky=W) 
            semester_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="read only")
            semester_combo['values']=("Select Semester","Semester-1","Semester-2")
            semester_combo.current(0)
            semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W) 
            
            #class student information
            Class_Student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",15,"bold"))
            Class_Student_frame.place(x=3,y=230,width=710,height=300) 
            
            #studentID
            StudentID_label=Label(Class_Student_frame,text="StudentID",font=("times new roman",12,"bold"))
            StudentID_label.grid(row=0,column=0,padx=10,sticky=W) 
            
            StudentID_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
            StudentID_entry.grid(row=0,column=1,padx=10,sticky=W)
            
            #student name
            StudentName_label=Label(Class_Student_frame,text="Student Name",font=("times new roman",12,"bold"))
            StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W) 
            
            StudentName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
            StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
            
            #class division
            class_division_label=Label(Class_Student_frame,text="Class Division",font=("times new roman",12,"bold"))
            class_division_label.grid(row=1,column=0,padx=10,pady=5,sticky=W) 
            
            class_division_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
            class_division_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
            
            div_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="read only")
            div_combo['values']=("A","B","C","D","E")
            div_combo.current(0)
            div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
            
            #roll no
            roll_no_label=Label(Class_Student_frame,text="Roll No:",font=("times new roman",12,"bold"))
            roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W) 
            
            roll_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
            roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
            
            #gender
            gender_label=Label(Class_Student_frame,text="Gender:",font=("times new roman",12,"bold"))
            gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W) 
            
            gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="read only")
            gender_combo['values']=("Male","Female","Other")
            gender_combo.current(0)
            gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
            
            #DOB
            dob_label=Label(Class_Student_frame,text="DOB:",font=("times new roman",12,"bold"))
            dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W) 
            
            dob_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
            dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
            
            #Email
            email_label=Label(Class_Student_frame,text="Email:",font=("times new roman",12,"bold"))
            email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W) 
            
            email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
            email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
            
            #phone no
            phone_label=Label(Class_Student_frame,text="Phone No:",font=("times new roman",12,"bold"))
            phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W) 
            
            phone_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
            phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
            
            #radio button
            self.var_radio1=StringVar()
            radiobtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
            radiobtn1.grid(row=6,column=0)
            
            self.var_radio2=StringVar()
            radiobtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No photo sample",value="No")
            radiobtn2.grid(row=6,column=1)
            
            #button frame
            btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE)
            btn_frame.place(x=0,y=180,width=715,height=80)
            
        
            save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
            save_btn.grid(row=0,column=0)
            
            update_btn=Button(btn_frame,text="Update",command=self.update_data, width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
            update_btn.grid(row=0,column=1)
            
            delete_btn=Button(btn_frame,text="Delete",command=self.delete_data, width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
            delete_btn.grid(row=0,column=2)
            
            
            reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
            reset_btn.grid(row=0,column=3) 
            
            take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Photo Sample",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
            take_photo_btn.grid(row=1,column=0)
            
            update_photo_btn=Button(btn_frame,command=self.generate_dataset, text="Update Photo Sample",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
            update_photo_btn.grid(row=1,column=1)

            back_button = Button(btn_frame, command=self.goBack, text="Back",  width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
            back_button.grid(row=1, column=3, pady=10)
                
            #right label frame
            Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
            Right_frame.place(x=780,y=10,width=660,height=580)   

            
        
            
            #----------search system-----------      
            Search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",15,"bold"))
            Search_frame.place(x=1,y=10,width=650,height=70) 
        
            search_label=Label(Search_frame,text="Search By",font=("times new roman",12,"bold"),bg="red",fg="white")
            search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W) 
        
            search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=17,state="read only")
            search_combo['values']=("Select","Roll_No","phone_No")
            search_combo.current(0)
            search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)  
                
            search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold"))
            search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
                
            search_btn=Button(Search_frame,text="Search",width=9,font=("times new roman",12,"bold"),bg="blue",fg="white")
            search_btn.grid(row=0,column=3,padx=4)
            
            showAll_btn=Button(Search_frame,text="Show All",width=9,font=("times new roman",12,"bold"),bg="blue",fg="white")
            showAll_btn.grid(row=0,column=4)  
            
            #----------table frame-----------
            table_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE)
            table_frame.place(x=1,y=80,width=650,height=250)  
            
            scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
            scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
            
            self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","semester","studentID","studentName","div","roll_no","gender","dob","email","phone_no","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)        
        
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.student_table.xview)
            scroll_y.config(command=self.student_table.yview)
            
            self.student_table.heading("dep",text="Department")
            self.student_table.heading("course",text="Course")
            self.student_table.heading("year",text="Year")
            self.student_table.heading("semester",text="Semester")
            self.student_table.heading("studentID",text="StudentID")
            self.student_table.heading("studentName",text="StudentName")
            self.student_table.heading("div",text="Class Division")
            self.student_table.heading("roll_no",text="Roll No")
            self.student_table.heading("gender",text="Gender")
            self.student_table.heading("dob",text="DOB")
            self.student_table.heading("email",text="Email")
            self.student_table.heading("phone_no",text="Phone No")
            self.student_table.heading("photo",text="PhotoSampleStatus")
            self.student_table["show"]="headings"
            
            self.student_table.pack(fill=BOTH,expand=1)
            self.student_table.bind("<ButtonRelease>", self.get_cursor)
            self.fetch_data()
            
        
        
        #---------------Function Declaration---------------
        def add_data(self):
            if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        
                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_semester.get(),
                                                                                        self.var_std_id.get(),
                                                                                        self.var_std_name.get(),
                                                                                        self.var_div.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_radio1.get()
                                                                                        
                                                                                ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details have been added succesfully")
                except Exception as es:
                    messagebox("Error", f"Due To:{str(es)}", parent= self.root)
            
    
                
        #------------------------fetch data-----------------------
        def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student")
            data = my_cursor.fetchall()
            
            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()
            conn.close()   
        
    #------------------------get cursor----------------------
        def get_cursor(self, event=""): 
            cursor_focus = self.student_table.focus()
            content=self.student_table.item(cursor_focus)
            data = content["values"]
            self.var_dep.set(data[0]),
            self.var_course.set(data[1]),
            self.var_year.set(data[2]),
            self.var_semester.set(data[3]),
            self.var_std_id.set(data[4]),
            self.var_std_name.set(data[5]),
            self.var_div.set(data[6]),
            self.var_roll.set(data[7]),
            self.var_gender.set(data[8]),
            self.var_dob.set(data[9]),
            self.var_email.set(data[10]),
            self.var_phone.set(data[11]),
            self.var_radio1.set(data[12])
            
        # update function
        def update_data(self):
            if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                try:
                    Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                    if Update>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update student set Department=%s, course=%s, year=%s, semester=%s, student_name=%s, class_division=%s, roll_no=%s, gender=%s, dob=%s, email=%s, phone_no=%s, photo_sample=%s where student_id=%s",(

                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                        self.var_std_id.get()     
                                                                                                                                                                                                                    ))
                    else:
                        if not Update:
                            return
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error", f"Due To:{str(es)}", parent = self.root)
        
        #---------delete function--------------
        def delete_data(self):
            if self.var_std_id.get() == "":
                messagebox.showerror("Error", "Student ID required", parent=self.root)
            else:
                try:
                    delete = messagebox.askyesno("Student delete page", "Do you want to delete this student", parent=self.root)
                    if delete>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                        my_cursor=conn.cursor()
                        sql = "delete from student where student_id=%s"
                        val = (self.var_std_id.get(), )
                        my_cursor.execute(sql, val)
                    else:
                        if not delete:
                            return
                        
                    conn.commit()
                    self.fetch_data()
                    conn.close()

                    messagebox.showinfo("Delete", "Successfully deleted student details", parent = self.root)
                
                except Exception as es:
                    messagebox.showerror("Error", f"Due To:{str(es)}", parent = self.root)
                        
        # -------------reset-------------
        def reset_data(self):
            self.var_dep.set("Select Department")
            self.var_course.set("Select Course")
            self.var_year.set("Select Year")
            self.var_semester.set("Select semester")
            self.var_std_id.set("")
            self.var_std_name.set("")
            self.var_div.set("Select Division")
            self.var_roll.set("")
            self.var_gender.set("Male")
            self.var_dob.set("")
            self.var_email.set("")
            self.var_phone.set("")
            self.var_radio1.set("")
            
        # -----------generate data set or take a photo samples------------
        def generate_dataset(self):
            if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Select * from student")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                        id+=1
                    my_cursor.execute("update student set Department=%s, course=%s, year=%s, semester=%s, student_name=%s, class_division=%s, roll_no=%s, gender=%s, dob=%s, email=%s, phone_no=%s, photo_sample=%s where student_id=%s",(

                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                        self.var_std_id.get()==id+1
                                                                                                                                                                                                                        
                                                                                                                                                                                                                    ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()
                    
                    # ---------load predefine data on face frontals from opencv---------
                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
                    
                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling factor=1.3
                        #minimum neighbour=5
                        
                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped
                        
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="C:/Users/HP/Documents/pd/face detection/Data/."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped Face",face)
                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data set completed!!")
                except Exception as es:
                    messagebox.showerror("Error", f"Due To:{str(es)}", parent = self.root)

        
        def goBack(self):
            self.root.destroy()

                    
    
    

if __name__ == "__main__":
        root=tk.Tk()
        obj=Student_Details(root)
        root.mainloop()
