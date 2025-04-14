from logging import root
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import tkinter as tk
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attenance")
        
        # ------------variables------------
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        
        
        
        
        
        title_lbl=Label(self.root ,text="ATTENDANCE",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # main frame
        main_frame=Frame(self.root ,bg="lightblue",bd=2)
        main_frame.place(x=0,y=50,width=1500,height=650)
        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=40,y=10,width=730,height=580)
        
        
        left_inside_frame=Frame(Left_frame,bg="lightblue",bd=2)
        left_inside_frame.place(x=10,y=50,width=700,height=500)
        
         # ==================label and entry========================================= 
         # attendance ID 
        AttendanceID_label=Label(left_inside_frame,text="AttendanceID",font=("times new roman",12,"bold"))
        AttendanceID_label.grid(row=0,column=0,padx=10,sticky=W) 
        
        AttendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        AttendanceID_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        # roll no
        roll_no_label=Label(left_inside_frame,text="Roll No:",font=("times new roman",12,"bold"))
        roll_no_label.grid(row=0,column=2,padx=10,pady=5,sticky=W) 
        
        roll_no_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        # name
        StudentName_label=Label(left_inside_frame,text="Student Name",font=("times new roman",12,"bold"))
        StudentName_label.grid(row=1,column=0,padx=10,pady=5,sticky=W) 
        
        StudentName_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",12,"bold"))
        StudentName_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        # department
        depLabel_label=Label(left_inside_frame,text="Department",font=("times new roman",12,"bold"))
        depLabel_label.grid(row=1,column=2,padx=10,pady=5,sticky=W) 
        
        depLabel_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",12,"bold"))
        depLabel_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        # time
        timeLabel_label=Label(left_inside_frame,text="Time",font=("times new roman",12,"bold"))
        timeLabel_label.grid(row=2,column=0,padx=10,pady=5,sticky=W) 
        
        timeLabel_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",12,"bold"))
        timeLabel_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        # Date
        dateLabel_label=Label(left_inside_frame,text="Date",font=("times new roman",12,"bold"))
        dateLabel_label.grid(row=2,column=2,padx=10,pady=5,sticky=W) 
        
        dateLabel_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",12,"bold"))
        dateLabel_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        # attendance status
        attendanceLabel_label=Label(left_inside_frame,text="Attendance Status",font=("times new roman",12,"bold"))
        attendanceLabel_label.grid(row=3,column=0,padx=10,pady=5,sticky=W) 
        
        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,width=20,font=("times new roman",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Abesnt")
        self.atten_status.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        self.atten_status.current(0)
        
        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=180,width=715,height=80)
        
       
        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)
        
        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv, width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)
        
        update_btn=Button(btn_frame,text="Update",command=self.updateCsv, width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3) 
        
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=660,height=580)
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=640,height=415)

        # -----scroll bar table-------
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("AttendanceId","roll_no","StudentName","Department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("AttendanceId",text="Attendance ID")
        self.AttendanceReportTable.heading("roll_no",text="Roll No")
        self.AttendanceReportTable.heading("StudentName",text="Student Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("AttendanceId",width=100)
        self.AttendanceReportTable.column("roll_no",width=100)
        self.AttendanceReportTable.column("StudentName",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    # ----------fetch data-------------------
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children()) #added ()
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    # --------import csv---------        
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
     
    # -------export csv--------
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
            messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent = self.root)
                    
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])   
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
      
    def updateCsv(self):
        global mydata
        fln = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        
        if fln:
            with open(fln, 'w', newline='') as myfile:
                csvwrite = csv.writer(myfile, delimiter=",")
                csvwrite.writerows(mydata)  
    

    




        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
