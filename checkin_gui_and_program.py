from subprocess import call
from tkinter import *
import os
import pickle

Delux_Room = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
Semi_Delux_Room = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
General_Room = (26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45)
Joint_Room = (46, 47, 48, 49, 50, 46, 47, 48, 49, 50)


class Hotel_Management_Checkin:
    name = ""
    address = ""
    mobile_no = 0
    no_of_days = 0
    room_type = ""
    room_no = 0
    payment_type = ""
    price = 0

    def __init__(self):
        root = Tk()
        '''This class configures and populates the toplevel window.
            top is the toplevel containing window.'''
        _bgcolor = '#ffffff'  # X11 color: 'white'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff'  # X11 color: 'white'
        _ana1color = '#ffffff'  # X11 color: 'white'
        _ana2color = '#ffffff'  # X11 color: 'white'
        font10 = "-family {Courier New} -size 10 -weight normal -slant" \
                 " roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 30 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 18 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 17 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font14 = "-family {Segoe UI} -size 16 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font15 = "-family {Segoe UI} -size 19 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font16 = "-family {Segoe UI} -size 15 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant " \
                "roman -underline 0 -overstrike 0"

        root.geometry("1069x742")
        root.title("HOTEL MANAGMENT")
        root.configure(background="#ffffff")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="black")

        self.Text1 = Text(root)
        self.Text1.place(relx=0.03, rely=0.65, relheight=0.29, relwidth=0.93)
        self.Text1.configure(background="white")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#ffffff")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#e6e6e6")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=994)
        self.Text1.configure(wrap=WORD)

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.03, rely=0.05, relheight=0.12, relwidth=0.93)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=995)

        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.04, rely=0.11, relheight=0.84, relwidth=0.9)
        self.Message1.configure(background="#ffffff")
        self.Message1.configure(font=font11)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#ffffff")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''YOU CLICKED ON CHECK INN''')
        self.Message1.configure(width=800)

        self.menubar = Menu(root, font=font9, bg=_bgcolor, fg=_fgcolor)
        root.configure(menu=self.menubar)

        self.Frame2 = Frame(root)
        self.Frame2.place(relx=0.03, rely=0.18, relheight=0.46, relwidth=0.93)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#ffffff")
        self.Frame2.configure(highlightbackground="#ffffff")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=995)

        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0.05, rely=0.03, height=47, width=289)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#bfbfbf")
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#ffffff")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''ENTER YOUR NAME''')

        self.Entry1 = Entry(self.Frame2)
        self.NAME = StringVar()
        self.Entry1.place(relx=0.47, rely=0.05, height=34, relwidth=0.43)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#bfbfbf")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#ffffff")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#e6e6e6")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=self.NAME)

        self.Button1 = Button(self.Frame2)
        self.Button1.place(relx=0.91, rely=0.05, height=33, width=43)
        self.Button1.configure(activebackground="#ffffff")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#ffffff")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''OK''')
        self.Button1.configure(command=self.check_name)

        self.Label2 = Label(self.Frame2)
        self.Label2.place(relx=0.045, rely=0.16, height=47, width=334)
        self.Label2.configure(activebackground="#ffffff")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#bfbfbf")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#ffffff")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''ENTER YOUR ADDRESS''')

        self.Entry2 = Entry(self.Frame2)
        self.ADDRESS = StringVar()
        self.Entry2.place(relx=0.47, rely=0.18, height=34, relwidth=0.43)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#bfbfbf")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#ffffff")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#e6e6e6")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.configure(textvariable=self.ADDRESS)

        self.Button2 = Button(self.Frame2)
        self.Button2.place(relx=0.91, rely=0.18, height=33, width=43)
        self.Button2.configure(activebackground="#ffffff")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#ffffff")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''OK''')
        self.Button2.configure(command=self.check_address)

        self.Label3 = Label(self.Frame2)
        self.Label3.place(relx=0.045, rely=0.29, height=47, width=329)
        self.Label3.configure(activebackground="#ffffff")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#bfbfbf")
        self.Label3.configure(font=font12)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#ffffff")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''ENTER YOUR NUMBER''')

        self.Entry3 = Entry(self.Frame2)
        self.MOBILE = StringVar()
        self.Entry3.place(relx=0.47, rely=0.31, height=34, relwidth=0.43)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#bfbfbf")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#ffffff")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#e6e6e6")
        self.Entry3.configure(selectforeground="black")
        self.Entry3.configure(textvariable=self.MOBILE)

        self.Button3 = Button(self.Frame2)
        self.Button3.place(relx=0.91, rely=0.31, height=33, width=43)
        self.Button3.configure(activebackground="#ffffff")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#ffffff")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#ffffff")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''OK''')
        self.Button3.configure(command=self.check_mobile)

        self.Label4 = Label(self.Frame2)
        self.Label4.place(relx=0.05, rely=0.43, height=44, width=260)
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#bfbfbf")
        self.Label4.configure(font=font13)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''NUMBER OF DAYS''')

        self.Entry4 = Entry(self.Frame2)
        self.DAYS = StringVar()
        self.Entry4.place(relx=0.47, rely=0.43, height=34, relwidth=0.43)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#bfbfbf")
        self.Entry4.configure(font=font10)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(width=424)
        self.Entry4.configure(textvariable=self.DAYS)

        self.Button4 = Button(self.Frame2)
        self.Button4.place(relx=0.91, rely=0.43, height=33, width=43)
        self.Button4.configure(activebackground="#ffffff")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#ffffff")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#ffffff")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''OK''')
        self.Button4.configure(command=self.check_day)

        self.Label5 = Label(self.Frame2)
        self.Label5.place(relx=0.32, rely=0.5, height=48, width=296)
        self.Label5.configure(activebackground="#ffffff")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#ffffff")
        self.Label5.configure(disabledforeground="#bfbfbf")
        self.Label5.configure(font=font13)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#ffffff")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''CHOOSE YOUR ROOM''')

        self.Label6 = Label(self.Frame2)
        self.Label6.place(relx=0.3, rely=0.79, height=48, width=300)
        self.Label6.configure(activebackground="#ffffff")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(disabledforeground="#bfbfbf")
        self.Label6.configure(font=font14)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#ffffff")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''CHOOSE PAYMENT METHOD''')

        self.Checkbutton1 = Checkbutton(self.Frame2)
        self.var1 = IntVar()
        self.Checkbutton1.place(relx=0.15, rely=0.58, relheight=0.17, relwidth=0.14)
        self.Checkbutton1.configure(activebackground="#ffffff")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#ffffff")
        self.Checkbutton1.configure(disabledforeground="#bfbfbf")
        self.Checkbutton1.configure(font=font14)
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#ffffff")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='''DELUXE''')
        self.Checkbutton1.configure(variable=self.var1)

        self.Checkbutton2 = Checkbutton(self.Frame2)
        self.var2 = IntVar()
        self.Checkbutton2.place(relx=0.15, rely=0.72, relheight=0.11, relwidth=0.21)
        self.Checkbutton2.configure(activebackground="#ffffff")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="#ffffff")
        self.Checkbutton2.configure(disabledforeground="#bfbfbf")
        self.Checkbutton2.configure(font=font13)
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#ffffff")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text='''SEMI-DELUXE''')
        self.Checkbutton2.configure(variable=self.var2)

        self.Checkbutton3 = Checkbutton(self.Frame2)
        self.var3 = IntVar()
        self.Checkbutton3.place(relx=0.5, rely=0.6, relheight=0.11, relwidth=0.16)
        self.Checkbutton3.configure(activebackground="#ffffff")
        self.Checkbutton3.configure(activeforeground="#000000")
        self.Checkbutton3.configure(background="#ffffff")
        self.Checkbutton3.configure(disabledforeground="#bfbfbf")
        self.Checkbutton3.configure(font=font13)
        self.Checkbutton3.configure(foreground="#000000")
        self.Checkbutton3.configure(highlightbackground="#ffffff")
        self.Checkbutton3.configure(highlightcolor="black")
        self.Checkbutton3.configure(justify=LEFT)
        self.Checkbutton3.configure(text='''GENERAL''')
        self.Checkbutton3.configure(variable=self.var3)

        self.Checkbutton4 = Checkbutton(self.Frame2)
        self.var4 = IntVar()
        self.Checkbutton4.place(relx=0.5, rely=0.71, relheight=0.11, relwidth=0.12)
        self.Checkbutton4.configure(activebackground="#ffffff")
        self.Checkbutton4.configure(activeforeground="#000000")
        self.Checkbutton4.configure(background="#ffffff")
        self.Checkbutton4.configure(disabledforeground="#bfbfbf")
        self.Checkbutton4.configure(font=font13)
        self.Checkbutton4.configure(foreground="#000000")
        self.Checkbutton4.configure(highlightbackground="#ffffff")
        self.Checkbutton4.configure(highlightcolor="black")
        self.Checkbutton4.configure(justify=LEFT)
        self.Checkbutton4.configure(text='''JOINT''')
        self.Checkbutton4.configure(variable=self.var4)

        self.Checkbutton5 = Checkbutton(self.Frame2)
        self.var5 = IntVar()
        self.Checkbutton5.place(relx=0.153, rely=0.89, relheight=0.1, relwidth=0.15)
        self.Checkbutton5.configure(activebackground="#ffffff")
        self.Checkbutton5.configure(activeforeground="#000000")
        self.Checkbutton5.configure(background="#ffffff")
        self.Checkbutton5.configure(disabledforeground="#bfbfbf")
        self.Checkbutton5.configure(font=font16)
        self.Checkbutton5.configure(foreground="#000000")
        self.Checkbutton5.configure(highlightbackground="#ffffff")
        self.Checkbutton5.configure(highlightcolor="black")
        self.Checkbutton5.configure(justify=LEFT)
        self.Checkbutton5.configure(text='''By cash''')
        self.Checkbutton5.configure(variable=self.var5)

        self.Checkbutton6 = Checkbutton(self.Frame2)
        self.var6 = IntVar()
        self.Checkbutton6.place(relx=0.485, rely=0.89, relheight=0.1, relwidth=0.3)
        self.Checkbutton6.configure(activebackground="#ffffff")
        self.Checkbutton6.configure(activeforeground="#000000")
        self.Checkbutton6.configure(background="#ffffff")
        self.Checkbutton6.configure(disabledforeground="#bfbfbf")
        self.Checkbutton6.configure(font=font16)
        self.Checkbutton6.configure(foreground="#000000")
        self.Checkbutton6.configure(highlightbackground="#ffffff")
        self.Checkbutton6.configure(highlightcolor="black")
        self.Checkbutton6.configure(justify=LEFT)
        self.Checkbutton6.configure(text='''By credit/debit card''')
        self.Checkbutton6.configure(variable=self.var6)

        self.Button5 = Button(self.Frame2)
        self.Button5.place(relx=0.76, rely=0.66, height=83, width=156)
        self.Button5.configure(activebackground="#ffffff")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#ffffff")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(font=font16)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#ffffff")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''SUBMIT''')
        self.Button5.configure(command=self.submit_clicked)

        root.mainloop()

    def check_name(self):
        if len(str(self.NAME.get())) != 0:
            self.name = str(self.NAME.get())
            self.Text1.insert(INSERT, "name has been inputted""\n")
        else:
            self.Text1.insert(INSERT, "invalid input please input a valid name""\n")

    def check_address(self):
        if len(str(self.ADDRESS.get())) != 0:
            self.address = str(self.ADDRESS.get())
            self.Text1.insert(INSERT, "address has been inputted""\n")
        else:
            self.Text1.insert(INSERT, "invalid input please input a valid address""\n")

    def check_mobile(self):
        mb = str(self.MOBILE.get())
        if mb.isdigit() is True and len(mb) == 10:
            self.mobile_no = int(mb)
            self.Text1.insert(INSERT, "mobile number has been inputted""\n")
        else:
            self.Text1.insert(INSERT, "invalid input please input a valid mobile number""\n")

    def check_day(self):
        d = str(self.DAYS.get())
        if d.isdigit() is True and len(d) != 0:
            self.no_of_days = int(d)
            self.Text1.insert(INSERT, "days has been inputted""\n")
        else:
            self.Text1.insert(INSERT, "invalid input please input valid no of days""\n")

    def submit_clicked(self):
        if self.var1.get() == 1 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 0\
                and self.var5.get() == 1 and self.var6.get() == 0:
            self.room_type = "Delux"
            self.payment_type = "Cash"
            self.tor()
            self.payment_option()
            self.bill()
        elif self.var1.get() == 1 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 0\
                and self.var5.get() == 0 and self.var6.get() == 1:
            self.room_type = "Delux"
            self.payment_type = "Credit/Debit"
            self.tor()
            self.payment_option()
            self.bill()
        elif self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 0 and self.var4.get() == 0\
                and self.var5.get() == 1 and self.var6.get() == 0:
            self.room_type = "Semi-Delux"
            self.payment_type = "Cash"
            self.tor()
            self.payment_option()
            self.bill()
        elif self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 0 and self.var4.get() == 0\
                and self.var5.get() == 0 and self.var6.get() == 1:
            self.room_type = "Semi-Delux"
            self.payment_type = "Credit/Debit"
            self.tor()
            self.payment_option()
            self.bill()
        elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 1 and self.var4.get() == 0\
                and self.var5.get() == 1 and self.var6.get() == 0:
            self.room_type = "General"
            self.payment_type = "Cash"
            self.tor()
            self.payment_option()
            self.bill()
        elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 1 and self.var4.get() == 0\
                and self.var5.get() == 0 and self.var6.get() == 1:
            self.room_type = "General"
            self.payment_type = "Credit/Debit"
            self.tor()
            self.payment_option()
            self.bill()
        elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 1\
                and self.var5.get() == 1 and self.var6.get() == 0:
            self.room_type = "Joint"
            self.payment_type = "Cash"
            self.tor()
            self.payment_option()
            self.bill()
        elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 1\
                and self.var5.get() == 0 and self.var6.get() == 1:
            self.room_type = "Joint"
            self.payment_type = "Credit/Debit"
            self.tor()
            self.payment_option()
            self.bill()
        else:
            self.Text1.insert(INSERT, "invalid choice please input a valid choice""\n")

    def tor(self):
        G = []
        try:
            file = open("hotel.data", "rb")
            mylist = pickle.load(file)
            file.close()
        except FileNotFoundError:
            mylist = []
        for item in mylist:
            G.append(item.room_no)
        if self.room_type == "Delux":
            self.price = self.price + (2000 * self.no_of_days)
            for i in Delux_Room:
                if i in G:
                    continue
                else:
                    self.room_no = i
                    break
        elif self.room_type == "Semi-Delux":
            self.price = self.price + (1500 * self.no_of_days)
            for i in Semi_Delux_Room:
                if i in G:
                    continue
                else:
                    self.room_no = i
                    break
        elif self.room_type == "General":
            self.price = self.price + (1000 * self.no_of_days)
            for i in General_Room:
                if i in G:
                    continue
                else:
                    self.room_no = i
                    break
        elif self.room_type == "Joint":
            self.price = self.price + (1700 * self.no_of_days)
            for i in Joint_Room:
                if i in G:
                    continue
                else:
                    self.room_no = i
                    break

    def payment_option(self):
        if self.payment_type == "Cash":
            self.Text1.insert(INSERT, "no discount""\n")
        elif self.payment_type == "Credit/Debit":
            self.price = self.price - ((self.price * 10) / 100)
            self.Text1.insert(INSERT, "10% discount""\n")

    def bill(self):
        try:
            file = open("hotel.data", "rb")
            old_list = pickle.load(file)
            file.close()
            os.remove("hotel.data")
        except FileNotFoundError:
            old_list = []
        a = save(self.name, self.address, self.mobile_no, self.no_of_days, self.room_type, self.room_no,
                 self.payment_type, self.price)
        old_list.append(a)
        new_file = open("new_hotel.data", "wb")
        pickle.dump(old_list, new_file)
        new_file.close()
        os.rename("new_hotel.data", "hotel.data")

        mylist = [str(self.name), str(self.mobile_no), str(self.room_no), str(self.price)]
        text_file = open("receipt.txt", "w+")
        for i in range(0, 4):
            text_file.write(mylist[i] + "\n")
        text_file.close()
        call(["python", "receipt.py"])
        restart_program()


class save:
    name = ""
    address = ""
    mobile_no = 0
    no_of_days = 0
    room_type = ""
    room_no = 0
    payment_type = ""
    price = 0

    def __init__(self, NAME_PRO, ADDRESS_PRO, MOBILE_NO_PRO, DAYS, ROOM_TYPE_PRO, ROOM_NO_PRO, PAYMENT_TYPE_PRO, PRICE_PRO):
        self.name = NAME_PRO
        self.address = ADDRESS_PRO
        self.mobile_no = MOBILE_NO_PRO
        self.no_of_days = DAYS
        self.room_type = ROOM_TYPE_PRO
        self.room_no = ROOM_NO_PRO
        self.payment_type = PAYMENT_TYPE_PRO
        self.price = PRICE_PRO


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, *sys.argv)


if __name__ == '__main__':
    hotel = Hotel_Management_Checkin()
