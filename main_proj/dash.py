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
