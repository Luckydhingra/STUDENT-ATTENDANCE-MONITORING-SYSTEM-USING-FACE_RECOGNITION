import webbrowser
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x790+0+0")
        self.root.title("FaceCheck Attendance")
        self.root.iconbitmap('assets/logo_PI6_icon.ico')
        
        
        
        title_lbl = Label(self.root,text="DEVELOPERS",font=("times new roman",25,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1540,height=45)
        
        Back_Button = Button(title_lbl, text="Back", command=self.root.destroy, font=("times new roman",11,"bold"),width=17,bg="darkblue",fg="white")
        Back_Button.pack(side=RIGHT)

        img_top = Image.open(r".\assets\Bg.png")
        img_top = img_top.resize((1540,780),Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1540,height=740)
        
        # Contributor 1
        # Main Frame
        main_frame1 = Frame(f_lbl, bd=2, bg="skyblue")
        main_frame1.place(x=285, y=100, width=400, height=450)
        
        img1 = Image.open(r".\assets\Kunal.png")
        img1 = img1.resize((200,200),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(main_frame1, image=self.photoimg1)
        f_lbl1.place(x=100,y=10,width=200,height=200)
        
        # Developer1 info
        name_label1 = Label(main_frame1, text="Kunal Kathpal", font=("times new roman", 20, "bold"),fg="blue", bg="skyblue")
        name_label1.place(x=100,y=220)
        
        w_label1 = Label(main_frame1, text="Full Stack Developer", font=("times new roman", 20, "bold"),fg="blue", bg="skyblue")
        w_label1.place(x=100,y=260)
        
        p_label1 = Label(main_frame1, text="Student", font=("times new roman", 14, "bold"),fg="black", bg="skyblue")
        p_label1.place(x=100,y=300)
        
        c_label1 = Label(main_frame1, text="CRS-SIET, Jhajjar", font=("times new roman", 14, "bold"),fg="black", bg="skyblue")
        c_label1.place(x=100,y=320)
        
        aboutme_btn2 = Button(main_frame1, text="About me",width=18, font=("times new roman",16,"bold"), bg="blue", fg="white", cursor="hand2")
        aboutme_btn2.place(x=100, y=350)
        aboutme_btn2.bind ('<Button-1>',
                   lambda x:webbrowser.open_new("https://www.linkedin.com/in/kunal-kathpal"))
        
              

        # Contributor 2
        # Main Frame
        main_frame2 = Frame(f_lbl, bd=2, bg="skyblue")
        main_frame2.place(x=855, y=100, width=400, height=450)
        
        img2 = Image.open(r".\assets\Lucky.jpg")
        img2 = img2.resize((200,200),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(main_frame2, image=self.photoimg2)
        f_lbl2.place(x=100,y=10,width=200,height=200)
        
        # Developer2 info
        name_label2 = Label(main_frame2, text="Lucky (Rudra0_0)", font=("times new roman", 20, "bold"),fg="blue", bg="skyblue")
        name_label2.place(x=90,y=220)
        
        w_label2 = Label(main_frame2, text="Open-Source-Evangelist", font=("times new roman", 20, "bold"),fg="blue", bg="skyblue")
        w_label2.place(x=90,y=260)
        
        p_label2 = Label(main_frame2, text="Student", font=("times new roman", 14, "bold"),fg="black", bg="skyblue")
        p_label2.place(x=90,y=300)
        
        c_label2 = Label(main_frame2, text="CRS-SIET, Jhajjar", font=("times new roman", 14, "bold"),fg="black", bg="skyblue")
        c_label2.place(x=90,y=320)
        
        aboutme_btn2 = Button(main_frame2, text="About me",width=18, font=("times new roman",16,"bold"), bg="blue", fg="white", cursor="hand2")
        aboutme_btn2.place(x=100, y=350)
        aboutme_btn2.bind('<Button-1>',
                   lambda x:webbrowser.open_new("https://rudra0_0.bio.link/"))
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()