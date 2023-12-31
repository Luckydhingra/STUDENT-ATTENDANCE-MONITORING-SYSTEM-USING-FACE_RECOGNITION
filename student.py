from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x790+0+0")
        self.root.title("Face Recognition System")
        self.root.iconbitmap('assets/logo_PI6_icon.ico')

        # variables
        self.var_dep= StringVar()
        self.var_course= StringVar()
        self.var_year= StringVar()
        self.var_sem= StringVar()
        self.var_Student_id= StringVar()
        self.var_name= StringVar()
        self.var_div= StringVar()
        self.var_roll= StringVar()
        self.var_gender= StringVar()
        self.var_dob= StringVar()
        self.var_email= StringVar()
        self.var_phone= StringVar()
        self.var_address= StringVar()
        self.var_teacher= StringVar()


        # Header Image
        img = Image.open(r".\assets\Header.png")
        img = img.resize((1540,130),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1540,height=130)
       

        # Background Image
        img1 = Image.open(r".\assets\Background.jpg")
        img1 = img1.resize((1540,710),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0,y=130,width=1540,height=710)

        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1540,height=45)
        Back_Button = Button(title_lbl, text="Back", command=self.root.destroy, font=("times new roman",11,"bold"),width=17,bg="darkblue",fg="white")
        Back_Button.pack(side=RIGHT)

        # Main Frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1490, height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 13, "bold"))
        Left_frame.place(x=15, y=10, width=760, height=580)

        img_left = Image.open(r".\assets\collegestudents.jpg")
        img_left = img_left.resize((750,130),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=750,height=130)

        # current course information
        currentCourse_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 13, "bold"))
        currentCourse_frame.place(x=5, y=135, width=750, height=115)

        # Department
        dep_label = Label(currentCourse_frame, text="Department:", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(currentCourse_frame, textvariable=self.var_dep, font=("times new roman", 13, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department","CSE","CSE (AI & ML)","Civil","Mechanical", "Electrical","ECE")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(currentCourse_frame, text="Course:", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(currentCourse_frame, textvariable=self.var_course, font=("times new roman", 13, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course","B.Tech")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #  Year
        year_label = Label(currentCourse_frame, text="Year:", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(currentCourse_frame, textvariable=self.var_year, font=("times new roman", 13, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year","2023-24","2024-25","2025-26","2026-27")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(currentCourse_frame, text="Semester:", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(currentCourse_frame, textvariable=self.var_sem, font=("times new roman", 13, "bold"), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # class student information
        classStudent_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 13, "bold"))
        classStudent_frame.place(x=5, y=250, width=750, height=300)

        # Student ID
        Student_id_label = Label(classStudent_frame, text="Student ID:", font=("times new roman", 13, "bold"), bg="white")
        Student_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        Student_id_entry = ttk.Entry(classStudent_frame, textvariable=self.var_Student_id, width=20, font=("times new roman", 13, "bold"))
        Student_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_label = Label(classStudent_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(classStudent_frame, textvariable=self.var_name, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        classDiv_label = Label(classStudent_frame, text="Class Division:", font=("times new roman", 13, "bold"), bg="white")
        classDiv_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        classDiv_combo = ttk.Combobox(classStudent_frame, textvariable=self.var_div, font=("times new roman", 13, "bold"), state="readonly", width=18)
        classDiv_combo["values"] = ("Select Division","A","B","C")
        classDiv_combo.current(0)
        classDiv_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No.
        rollNo_label = Label(classStudent_frame, text="Roll No:", font=("times new roman", 13, "bold"), bg="white")
        rollNo_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        rollNo_entry = ttk.Entry(classStudent_frame, textvariable=self.var_roll, width=20, font=("times new roman", 13, "bold"))
        rollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(classStudent_frame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(classStudent_frame, textvariable=self.var_gender, font=("times new roman", 13, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_label = Label(classStudent_frame, text="DOB:", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(classStudent_frame, textvariable=self.var_dob, width=20, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(classStudent_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(classStudent_frame, textvariable=self.var_email, width=20, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No.
        phone_label = Label(classStudent_frame, text="Phone No:", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(classStudent_frame, textvariable=self.var_phone, width=20, font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(classStudent_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(classStudent_frame, textvariable=self.var_address, width=20, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        teacher_label = Label(classStudent_frame, text="Teacher Name:", font=("times new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(classStudent_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(classStudent_frame, variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2 = ttk.Radiobutton(classStudent_frame, variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        # buttons Frame 
        btn_frame = Frame(classStudent_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=745, height=35)

        save_btn = Button(btn_frame, text="Save", command=self.add_data,width=18, font=("times new roman",13,"bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=18, font=("times new roman",13,"bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=18, font=("times new roman",13,"bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=18, font=("times new roman",13,"bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # buttons Frame 1
        btn_frame1 = Frame(classStudent_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=745, height=35)

        takePhoto_btn = Button(btn_frame1, command=self.generate_dataset, text="Take Photo Sample",width=37, font=("times new roman",13,"bold"), bg="blue", fg="white")
        takePhoto_btn.grid(row=0, column=0)

        updatePhoto_btn = Button(btn_frame1, text="Update Photo Sample",width=37, font=("times new roman",13,"bold"), bg="blue", fg="white")
        updatePhoto_btn.grid(row=0, column=1)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 13, "bold"))
        Right_frame.place(x=790, y=10, width=670, height=580)

        img_right = Image.open(r".\assets\collegestudents1.jpg")
        img_right = img_right.resize((660,130),Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=660,height=130)

        # fetching Student details
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search student details", font=("times new roman", 13, "bold"))
        search_frame.place(x=5, y=135, width=660, height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select","Roll No.","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search",width=10, font=("times new roman",12,"bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(search_frame, text="Show All",width=10, font=("times new roman",12,"bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        # table frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=660, height=340)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student1 = ttk.Treeview(table_frame, columns=("dep","course","year","sem","Student_id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student1.xview)
        scroll_y.config(command=self.student1.yview)

        # "dep","course","year","sem","Student_id","name","div","roll","gender","dob","email","phone","address","teacher","photo"
        self.student1.heading("dep",text="Department")
        self.student1.heading("course",text="Course")
        self.student1.heading("year",text="Year")
        self.student1.heading("sem",text="Semester")
        self.student1.heading("Student_id",text="Student ID")
        self.student1.heading("name",text="Name")
        self.student1.heading("div",text="Division")
        self.student1.heading("roll",text="Roll No.")
        self.student1.heading("gender",text="Gender")
        self.student1.heading("dob",text="DOB")
        self.student1.heading("email",text="Email")
        self.student1.heading("phone",text="Phone No.")
        self.student1.heading("address",text="Address")
        self.student1.heading("teacher",text="Teacher")
        self.student1.heading("photo",text="Photo Sample Status")
        self.student1["show"]="headings"

        self.student1.column("dep",width=100)
        self.student1.column("course",width=100)
        self.student1.column("year",width=100)
        self.student1.column("sem",width=100)
        self.student1.column("Student_id",width=100)
        self.student1.column("name",width=100)
        self.student1.column("div",width=100)
        self.student1.column("roll",width=100)
        self.student1.column("gender",width=100)
        self.student1.column("dob",width=100)
        self.student1.column("email",width=100)
        self.student1.column("phone",width=100)
        self.student1.column("address",width=100)
        self.student1.column("teacher",width=100)
        self.student1.column("photo",width=150)

        self.student1.pack(fill=BOTH, expand=1)
        self.student1.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # function declaration
        
    # saving data into database
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester" or self.var_roll.get() == "" or self.var_Student_id.get() == "" or self.var_name.get() == "" or self.var_div.get() == "" or self.var_dob.get() == "" or self.var_gender.get() == "Select Gender" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "":
            messagebox.showerror("Error","All fields are required.",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="4321",database="student_database")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                                                                                                                                self.var_dep.get(),
                                                                                                                                self.var_course.get(),
                                                                                                                                self.var_year.get(),
                                                                                                                                self.var_sem.get(),
                                                                                                                                self.var_Student_id.get(),
                                                                                                                                self.var_name.get(),
                                                                                                                                self.var_div.get(),
                                                                                                                                self.var_roll.get(),
                                                                                                                                self.var_gender.get(),
                                                                                                                                self.var_dob.get(),
                                                                                                                                self.var_email.get(),
                                                                                                                                self.var_phone.get(),
                                                                                                                                self.var_address.get(),
                                                                                                                                self.var_teacher.get(),
                                                                                                                                self.var_radio1.get()
                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully.",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    # fetch data from database
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="4321",database="student_database")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student1.delete(*self.student1.get_children())
            for i in data:
                self.student1.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    # get cursor
    def get_cursor(self,event=""):
        cursor_focus= self.student1.focus()
        content = self.student1.item(cursor_focus)
        data= content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_Student_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # Update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester" or self.var_roll.get() == "" or self.var_Student_id.get() == "" or self.var_name.get() == "" or self.var_div.get() == "" or self.var_dob.get() == "" or self.var_gender.get() == "Select Gender" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "":
            messagebox.showerror("Error","All fields are required.",parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost",user="root",password="4321",database="student_database")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.var_Student_id.get()
                                                                                                                                                                                                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully updated.",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_Student_id.get() == "":
            messagebox.showerror("Error","Student ID No. must be required.",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete!","Do you want to delete this student?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",user="root",password="4321",database="student_database")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val = (self.var_Student_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Deleted","Student details successfully deleted.",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_Student_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # Generate data set or Take photo Samples
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester" or self.var_roll.get() == "" or self.var_Student_id.get() == "" or self.var_name.get() == "" or self.var_div.get() == "" or self.var_dob.get() == "" or self.var_gender.get() == "Select Gender" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "":
            messagebox.showerror("Error","All fields are required.",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="4321",database="student_database")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.var_Student_id.get()==id+1
                                                                                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on frontal face from opencv

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor = 1.3
                    # Minimum Neighbor = 5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Success","Data set is Generated successfully!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()