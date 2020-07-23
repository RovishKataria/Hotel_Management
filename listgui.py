import pickle
from tkinter import *

l2 = []
G = []


class Hotel_Management_List:
    def __init__(self):
        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff'  # X11 color: 'white'
        _ana1color = '#ffffff'  # X11 color: 'white'
        _ana2color = '#ffffff'  # X11 color: 'white'
        font11 = "-family {Segoe UI} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Times New Roman} -size 16 -weight bold " \
                 "-slant roman -underline 0 -overstrike 0"

        root.geometry("780x541+504+123")
        root.title("HOTEL MANAGEMENT")
        root.configure(background="#ffffff")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="black")

        self.Labelframe1 = LabelFrame(root)
        self.Labelframe1.place(relx=0.01, rely=0.04, relheight=0.95, relwidth=0.97)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=font11)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''LIST OF ALL GUEST''')
        self.Labelframe1.configure(background="#ffffff")
        self.Labelframe1.configure(highlightbackground="#ffffff")
        self.Labelframe1.configure(highlightcolor="black")
        self.Labelframe1.configure(width=760)

        self.Frame1 = Frame(self.Labelframe1)
        self.Frame1.place(relx=0.03, rely=0.1, relheight=0.86, relwidth=0.47, y=-31, h=15)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=355)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.28, rely=0.02, height=37, width=117)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#ffffff")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''NAMES''')

        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.06, rely=0.16, relheight=0.8, relwidth=0.88)
        self.Text1.configure(background="white")
        self.Text1.configure(font=font14)
        self.Text1.configure(foreground="#000000")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=314)
        self.Text1.configure(wrap=WORD)

        self.Frame2 = Frame(self.Labelframe1)
        self.Frame2.place(relx=0.51, rely=0.1, relheight=0.86, relwidth=0.47, y=-31, h=15)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#ffffff")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=355)

        self.Label2 = Label(self.Frame2)
        self.Label2.place(relx=0.37, rely=0.02, height=44, width=152)
        self.Label2.configure(activebackground="#ffffff")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#ffffff")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''ROOM NO.''')

        self.Text2 = Text(self.Frame2)
        self.Text2.place(relx=0.06, rely=0.16, relheight=0.8, relwidth=0.88)
        self.Text2.configure(background="white")
        self.Text2.configure(font=font14)
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(width=314)
        self.Text2.configure(wrap=WORD)

        for i in range(0, len(G)):
            self.Text1.insert(INSERT, str(l2[i])+"\n")
            self.Text2.insert(INSERT, str(G[i])+"\n")
        root.mainloop()


class save:
    def __init__(self, NAME_PRO, ADDRESS_PRO, MOBILE_NO_PRO, DAYS, ROOM_TYPE_PRO, ROOM_NO_PRO, PAYMENT_TYPE_PRO, PRICE_PRO):
        self.name = NAME_PRO
        self.address = ADDRESS_PRO
        self.mobile_no = MOBILE_NO_PRO
        self.no_of_days = DAYS
        self.room_type = ROOM_TYPE_PRO
        self.room_no = ROOM_NO_PRO
        self.price_type = PAYMENT_TYPE_PRO
        self.price = PRICE_PRO


if __name__ == '__main__':
    file = open('hotel.data', 'rb')
    mylist = pickle.load(file)
    file.close()
    for item in mylist:
        l2.append(item.name)
        G.append(item.room_no)
    hotel = Hotel_Management_List()
