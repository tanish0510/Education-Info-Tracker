from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import datetime
import sqlite3
from tkinter import messagebox
import os
from math import sin, cos, radians
from course import courseClass
from student import studentClass
from result import resultClass
from report import reportClassfrom tkinter import *
from PIL import Image, ImageTk, ImageDraw  # pip install pillow
from datetime import *
import time
from math import *
import sqlite3
from tkinter import messagebox, ttk
import os

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1350x655+0+0")
        self.root.config(bg="#021e2f")

        left_lbl = Label(self.root, bg="#08A3D2", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=80, width=800, height=500)

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 20, "bold"), bg="white", fg="green").place(
            x=250, y=50)

        email = Label(login_frame, text="Enter Email Address", font=("times new roman", 15, "bold"), bg="white",
                      fg="gray").place(x=250, y=150)
        self.txt_email = Entry(login_frame, font=("times new roman", 15), bg="lightgray",fg="black")
        self.txt_email.place(x=250, y=180, width=350)

        password = Label(login_frame, text="Enter Password", font=("times new roman", 15, "bold"), bg="white",
                         fg="black").place(x=250, y=230)
        self.txt_password = Entry(login_frame, font=("times new roman", 15), bg="lightgray",fg="black")
        self.txt_password.place(x=250, y=260, width=350)

        btn_reg = Button(login_frame, text="Register new Account?", font=("times new roman", 14), bg="white", bd=0,
                         fg="green", cursor="hand2", command=self.register_window).place(x=250, y=290)

        btn_forget = Button(login_frame, text="Forget Password?", font=("times new roman", 14), bg="white", bd=0,
                            fg="red", cursor="hand2", command=self.forget_password_window).place(x=450, y=290)

        btn_login = Button(login_frame, text="Login", font=("times new roman", 18, "bold"),fg="black", bg="green",
                           cursor="hand2", command=self.login).place(x=250, y=350, width=180)

        self.lbl = Label(self.root, text="Clock", font=("\nBook Antiqua", 25, "bold"), fg="white", compound=BOTTOM,
                          bg="#081923", bd=0)
        self.lbl.place(x=90, y=105, height=450, width=350)

        self.working()

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_password.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_email.delete(0, END)

    def forget_password(self):
        if self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_new_password.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root2)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=?",
                            (self.txt_email.get(), self.cmb_quest.get(), self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error",
                                         "Please Select the Correct Security Question / Enter Answer", parent=self.root2)
                else:
                    cur.execute("update employee set password=? where email=?",
                                (self.txt_new_password.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Your password has been reset, Please login with new password",
                                        parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

    def forget_password_window(self):
        if self.txt_email.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset your password", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=?", (self.txt_email.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error",
                                         "Please enter the valid email address to reset your password", parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("400x410+450+140")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), bg="white",
                              fg="red").place(x=0, y=10, relwidth=1)

                    question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"),
                                     bg="white",fg="black").place(x=70, y=100)

                    self.cmb_quest = ttk.Combobox(self.root2, font=("times new roman", 13), state="readonly",
                                                  justify=CENTER)
                    self.cmb_quest["values"] = ("Select", "Your First Pet Name", "Your Birth Place",
                                                "Your Best Friend Name")
                    self.cmb_quest.place(x=70, y=130, width=250)
                    self.cmb_quest.current(0)

                    answer = Label(self.root2, text="Enter Answer", font=("times new roman", 15, "bold"), bg="white",
                                   fg="gray").place(x=70, y=180)
                    self.txt_answer = Entry(self.root2, font=("times new roman", 15), bg="lightgray",fg="black")
                    self.txt_answer.place(x=70, y=210, width=250)

                    new_password = Label(self.root2, text="Enter New Password", font=("times new roman", 15, "bold"),
                                         bg="white", fg="gray").place(x=70, y=260)
                    self.txt_new_password = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                    self.txt_new_password.place(x=70, y=290, width=250)

                    btn_change_password = Button(self.root2, text="Reset Password", bg="green", fg="white",
                                                 cursor="hand2", command=self.forget_password,
                                                 font=("times new roman", 15, "bold")).place(x=110, y=340, width=180)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.txt_email.get() == "" or self.txt_password.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and password=?",
                            (self.txt_email.get(), self.txt_password.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Username & Password", parent=self.root)
                else:
                    messagebox.showinfo("Success", f"Welcome: {self.txt_email.get()}", parent=self.root)
                    self.root.destroy()
                    os.system("python3 dashboard.py")
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)

        bg = Image.open("snapshots/c.png")
        bg = bg.resize((300, 300), Image.ANTIALIAS if hasattr(Image, "ANTIALIAS") else Image.BICUBIC)
        clock.paste(bg, (50, 50))

        origin = 200, 200
        draw.line((origin, 200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr))), fill="#DF005E", width=4)
        draw.line((origin, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill="white", width=3)
        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill="yellow", width=2)
        draw.ellipse((195, 195, 210, 210), fill="#1AD5D5")
        clock.save("snapshots/clock_new.png")

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h / 12) * 36
        min_ = (m / 60) * 360
        sec_ = (s / 60) * 360

        self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(file="snapshots/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)

root = Tk()
obj = Login_window(root)
root.mainloop()




class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x655+0+0")
        self.root.config(bg="white")

        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")

        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT, image=self.logo_dash,
                      font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1,
                                                                                            height=50)

        M_Frame = LabelFrame(self.root, text="Panel", font=(
            "times new roman", 15), bg="white", fg="black")
        M_Frame.place(x=10, y=70, width=1260, height=80)

        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="black",
                            cursor="hand2", command=self.add_course).place(x=10, y=5, width=200, height=40)

        btn_student = Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="black",
                             cursor="hand2", command=self.add_student).place(x=220, y=5, width=200, height=40)

        btn_result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="black",
                            cursor="hand2", command=self.add_result).place(x=430, y=5, width=200, height=40)

        btn_view = Button(M_Frame, text="View Student Result", font=("goudy old style", 15, "bold"), bg="#0b5377",
                          fg="black", cursor="hand2", command=self.add_report).place(x=640, y=5, width=200, height=40)

        btn_logout = Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="black",
                            cursor="hand2", command=self.logout).place(x=850, y=5, width=200, height=40)

        btn_exit = Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="black",
                          cursor="hand2", command=self.exit_).place(x=1060, y=5, width=180, height=40)

        self.bg_img_pil = Image.open("images/bg.png")
        self.bg_img_pil = self.bg_img_pil.resize(
            (920, 350), Image.ANTIALIAS if "ANTIALIAS" in dir(Image) else Image.BICUBIC)
        self.bg_img = ImageTk.PhotoImage(self.bg_img_pil)

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=330, y=180, width=920, height=350)

        # Initialize labels with default values
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20), bd=10,
                                relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=330, y=530, width=300, height=90)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20), bd=10,
                                 relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=640, y=530, width=300, height=90)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20), bd=10,
                                relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=950, y=530, width=300, height=90)

        self.lbl = Label(self.root, text="Clock", font=("\nBook Antiqua", 25, "bold"), fg="white", compound=BOTTOM,
                         bg="#081923", bd=0)
        self.lbl.place(x=10, y=170, height=450, width=310)

        self.working()

        footer = Label(self.root, text="SRMS - Student Result Management System ",
                       font=("goudy old style", 12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
        self.update_details()

    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            total_courses_text = f"Total Courses\n[{str(len(cr))}]"
            if hasattr(self, 'lbl_course'):
                self.lbl_course.config(text=total_courses_text)
            else:
                self.lbl_course = Label(self.root, text=total_courses_text, font=("goudy old style", 20), bd=10,
                                        relief=RIDGE, bg="#e43b06", fg="white")
                self.lbl_course.place(x=330, y=530, width=300, height=90)

            # ... (similar changes for other labels)

            self.lbl_course.after(200, self.update_details)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",)

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h / 12) * 360
        min_ = (m / 60) * 360
        sec_ = (s / 60) * 360

        self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)

    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)

        bg = Image.open("images/c.png")
        bg = bg.resize((300, 300), Image.ANTIALIAS if "ANTIALIAS" in dir(
            Image) else Image.BICUBIC)
        clock.paste(bg, (50, 50))

        origin = 200, 200
        draw.line((origin, 200 + 50 * sin(radians(hr)), 200 -
                  50 * cos(radians(hr))), fill="#DF005E", width=4)

        draw.line((origin, 200 + 80 * sin(radians(min_)), 200 -
                  80 * cos(radians(min_))), fill="white", width=3)

        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 -
                  100 * cos(radians(sec_))), fill="yellow", width=2)
        draw.ellipse((195, 195, 210, 210), fill="#1AD5D5")
        clock.save("images/clock_new.png")

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = courseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def logout(self):
        op = messagebox.askokcancel(
            "Confirm", "Do you really want to logout?", parent=self.root)
        if op:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op = messagebox.showwarning(
            "Confirm", "Do you really want to Exit?", parent=self.root)
        if op:
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import datetime
import sqlite3
from tkinter import messagebox
import os
from math import sin, cos, radians
from course import courseClass
from student import studentClass
from result import resultClass
from report import reportClass


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x655+0+0")
        self.root.config(bg="white")

        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")

        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT, image=self.logo_dash,
                      font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1,
                                                                                            height=50)

        M_Frame = LabelFrame(self.root, text="Panel", font=(
            "times new roman", 15), bg="white", fg="black")
        M_Frame.place(x=10, y=70, width=1260, height=80)

        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="black",
                            cursor="hand2", command=self.add_course).place(x=10, y=5, width=200, height=40)

        btn_student = Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="black",
                             cursor="hand2", command=self.add_student).place(x=220, y=5, width=200, height=40)

        btn_result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="black",
                            cursor="hand2", command=self.add_result).place(x=430, y=5, width=200, height=40)

        btn_view = Button(M_Frame, text="View Student Result", font=("goudy old style", 15, "bold"), bg="#0b5377",
                          fg="black", cursor="hand2", command=self.add_report).place(x=640, y=5, width=200, height=40)

        btn_logout = Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="black",
                            cursor="hand2", command=self.logout).place(x=850, y=5, width=200, height=40)

        btn_exit = Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="black",
                          cursor="hand2", command=self.exit_).place(x=1060, y=5, width=180, height=40)

        self.bg_img_pil = Image.open("images/bg.png")
        self.bg_img_pil = self.bg_img_pil.resize(
            (920, 350), Image.ANTIALIAS if "ANTIALIAS" in dir(Image) else Image.BICUBIC)
        self.bg_img = ImageTk.PhotoImage(self.bg_img_pil)

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=330, y=180, width=920, height=350)

        # Initialize labels with default values
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20), bd=10,
                                relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=330, y=530, width=300, height=90)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20), bd=10,
                                 relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=640, y=530, width=300, height=90)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20), bd=10,
                                relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=950, y=530, width=300, height=90)

        self.lbl = Label(self.root, text="Clock", font=("\nBook Antiqua", 25, "bold"), fg="white", compound=BOTTOM,
                         bg="#081923", bd=0)
        self.lbl.place(x=10, y=170, height=450, width=310)

        self.working()

        footer = Label(self.root, text="SRMS - Student Result Management System ",
                       font=("goudy old style", 12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
        self.update_details()

    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            total_courses_text = f"Total Courses\n[{str(len(cr))}]"
            if hasattr(self, 'lbl_course'):
                self.lbl_course.config(text=total_courses_text)
            else:
                self.lbl_course = Label(self.root, text=total_courses_text, font=("goudy old style", 20), bd=10,
                                        relief=RIDGE, bg="#e43b06", fg="white")
                self.lbl_course.place(x=330, y=530, width=300, height=90)

            # ... (similar changes for other labels)

            self.lbl_course.after(200, self.update_details)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",)

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h / 12) * 360
        min_ = (m / 60) * 360
        sec_ = (s / 60) * 360

        self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)

    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)

        bg = Image.open("images/c.png")
        bg = bg.resize((300, 300), Image.ANTIALIAS if "ANTIALIAS" in dir(
            Image) else Image.BICUBIC)
        clock.paste(bg, (50, 50))

        origin = 200, 200
        draw.line((origin, 200 + 50 * sin(radians(hr)), 200 -
                  50 * cos(radians(hr))), fill="#DF005E", width=4)

        draw.line((origin, 200 + 80 * sin(radians(min_)), 200 -
                  80 * cos(radians(min_))), fill="white", width=3)

        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 -
                  100 * cos(radians(sec_))), fill="yellow", width=2)
        draw.ellipse((195, 195, 210, 210), fill="#1AD5D5")
        clock.save("images/clock_new.png")

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = courseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def logout(self):
        op = messagebox.askokcancel(
            "Confirm", "Do you really want to logout?", parent=self.root)
        if op:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op = messagebox.showwarning(
            "Confirm", "Do you really want to Exit?", parent=self.root)
        if op:
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
