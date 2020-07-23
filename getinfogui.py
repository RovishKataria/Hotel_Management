import pickle
from tkinter import *


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


class Hotel_Management_Info:
    r = ""

    def __init__(self):
        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font10 = "-family {Segoe UI} -size 17 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 28 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 23 -weight bold -slant roman" \
                " -underline 0 -overstrike 0"

        root.geometry("881x582+249+104")
        root.title("HOTEL MANAGEMENT")
        root.configure(background="#d9d9d9")

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.94)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=825)

        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.04, rely=0.46, relheight=0.48, relwidth=0.93)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=764)
        self.Text1.configure(wrap=WORD)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.12, rely=0.15, height=48, width=377)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''ENTER THE ROOM NO.   :''')

        self.Entry1 = Entry(self.Frame1)
        self.data = StringVar()
        self.Entry1.place(relx=0.65, rely=0.17, height=40, relwidth=0.1)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=84)
        self.Entry1.configure(textvariable=self.data)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.39, rely=0.29, height=74, width=197)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font10)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''SUBMIT''')
        self.Button1.configure(width=197)
        self.Button1.configure(command=self.get_info)

        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.22, rely=0.02, relheight=0.12, relwidth=0.56)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(font=font11)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''GET INFO HERE ..!!''')
        self.Message1.configure(width=460)
        root.mainloop()

    def get_info(self):
        self.r = str(self.data.get())
        if self.r.isdigit() is True and len(self.r) != 0:
            self.Text1.insert(INSERT, "\nvalid room number ""\n")
            file = open("hotel.data", "rb")
            old_list = pickle.load(file)
            file.close()
            found = False
            for item in old_list:
                if item.room_no == int(self.r):
                    found = True
                    self.Text1.insert(INSERT, "NAME : " + item.name.upper() + "\n")
                    self.Text1.insert(INSERT, "ADDRESS : " + item.address + "\n")
                    self.Text1.insert(INSERT, "MOBILE NO : " + str(item.mobile_no) + "\n")
                    self.Text1.insert(INSERT, "ROOM NO : " + str(item.room_no) + "\n")
                    self.Text1.insert(INSERT, "TOTAL BILL : " + str(item.price) + "\n")
            if found is False:
                self.Text1.insert(INSERT, "No guest found""\n")
        else:
            self.Text1.insert(INSERT, "invalid room number""\n")
            
            
if __name__ == '__main__':
    get_info = Hotel_Management_Info()
