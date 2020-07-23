import os
import pickle
from tkinter import *

l2 = []
G = []


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


class Hotel_Management_Checkout:
    r = ""

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
        font11 = "-family {Segoe UI} -size 23 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 24 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant " \
                "roman -underline 0 -overstrike 0"

        root.geometry("1011x750")
        root.title("HOTEL MANAGEMENT")
        root.configure(background="#ffffff")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="black")

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.04, rely=0.04, relheight=0.91, relwidth=0.91)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.14, rely=0.12, height=46, width=442)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#bfbfbf")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#ffffff")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''ENTER THE ROOM NO       : ''')

        self.Entry1 = Entry(self.Frame1)
        self.data = StringVar()
        self.Entry1.place(relx=0.67, rely=0.12, height=44, relwidth=0.07)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#bfbfbf")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#ffffff")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#e6e6e6")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=self.data)

        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.05, rely=0.54, relheight=0.4, relwidth=0.89)
        self.Text1.configure(background="white")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#ffffff")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#e6e6e6")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=824)
        self.Text1.configure(wrap=WORD)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.34, rely=0.28, height=93, width=286)
        self.Button1.configure(activebackground="#ffffff")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(font=font12)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#ffffff")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''CHECK OUT''')
        self.Button1.configure(command=self.check_out)
        root.mainloop()

    def check_out(self):
        self.r = str(self.data.get())
        if self.r.isdigit() is True and len(self.r) != 0:
            self.Text1.insert(INSERT, " valid room number ""\n")
            file = open("hotel.data", "rb")
            old_list = pickle.load(file)
            file.close()
            os.remove("hotel.data")

            new_list = []
            found = False
            for item in old_list:
                if item.room_no == int(self.r):
                    found = True
                    name = item.name
                else:
                    new_list.append(item)
            if found is True:
                self.Text1.insert(INSERT, "THANK YOU  " + name.upper() + " FOR VISITING US""\n")
            else:
                self.Text1.insert(INSERT, "NO GUEST FOUND""\n")
            new_file = open("new_hotel.data", "wb")
            pickle.dump(new_list, new_file)
            new_file.close()
            os.rename("new_hotel.data", "hotel.data")
        else:
            self.Text1.insert(INSERT, "invalid input please input a valid ROOM NO.""\n")


if __name__ == '__main__':
    check_out = Hotel_Management_Checkout()
