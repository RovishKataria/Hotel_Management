import os
import pickle

u = list()
Delux = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
Semi_Delux = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
General = (26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45)
Joint_Room = (46, 47, 48, 49, 50, 46, 47, 48, 49, 50)
m = [9]
G = []


def check_name():
    while True:
        name = input("ENTER GUEST NAME: ")
        if len(name) != 0:
            return name
        else:
            print("invalid input please input a valid name")


def check_address():
    while True:
        address = input("ENTER GUEST ADDRESS: ")
        if len(address) != 0:
            return address
        else:
            print("invalid input ")


def check_mobile():
    while True:
        mobile_no = input("ENTER MOBILE/PHONE NUMBER: ")
        if mobile_no.isdigit() is True and len(mobile_no) == 10:
            return mobile_no
        else:
            print("invalid input")


def check_day():
    while True:
        days = int(input("ENTER NO. OF DAYS GUEST WANT TO STAY: "))
        if days != 0:
            return days
        else:
            print("invalid input")


class GUEST:
    def __init__(self):
        self.name = " "
        self.address = " "
        self.mobile_no = 0
        self.room = 0
        self.no_of_days = 0
        self.price = 0

    def enter(self):
        self.name = check_name()
        self.address = check_address()
        self.mobile_no = check_mobile()
        self.no_of_days = check_day()

    def type_of_room(self):
        print("\nWhich type of room guest want")
        print("1. Delux")
        print("2. Semi-Delux")
        print("3. General")
        print("4. Joint Room")
        while True:
            choice = int(input("Enter guest's choice: "))
            if choice == 1:
                self.price = self.price + (2000 * self.no_of_days)
                m[0] = 1
                break
            elif choice == 2:
                self.price = self.price + (1500 * self.no_of_days)
                m[0] = 2
                break
            elif choice == 3:
                self.price = self.price + (1000 * self.no_of_days)
                m[0] = 3
                break
            elif choice == 4:
                self.price = self.price + (1700 * self.no_of_days)
                m[0] = 4
                break
            else:
                print("invalid choice")

    def payment_option(self):
        print("\nEnter mode of payment")
        print("1. By cash")
        print("2. By credit/debit card")
        while True:
            option = int(input("Enter guest's choice: "))
            if option == 1:
                print("No discount.")
                break
            elif option == 2:
                self.price = self.price - ((self.price * 10) / 100)
                print("Discount of 10%.")
                break
            else:
                print("Invalid option.")

    def bill(self):
        print("\nNAME -", self.name)
        print("ADDRESS -", self.address)
        print("MOBILE NO. -", self.mobile_no)
        print("Your total bill is Rs.", self.price)
        if m[0] == 1:
            a = Delux
        elif m[0] == 2:
            a = Semi_Delux
        elif m[0] == 3:
            a = General
        elif m[0] == 4:
            a = Joint_Room

        G = []
        f2 = open("hotel.data", "rb")
        try:
            while True:
                s = pickle.load(f2)
                k = s.room
                G.append(k)
                continue
        except EOFError:
            pass

        for r in a:
            if r not in G:
                print(self.name, " - room", r, "is alloted to you")
                self.room = r
                break
            else:
                continue
        self.room = r


# main
while True:
    print("1. Check in")
    print("2. Show Guest List")
    print("3. Check out")
    print("4. Get info of any guest")
    print("5. Exit")
    k = int(input("Enter choice: "))
    if k == 1:
        a = GUEST()
        f = open("hotel.data", "ab")
        a.enter()
        a.type_of_room()
        a.payment_option()
        a.bill()
        pickle.dump(a, f, protocol=2)
        f.close()
    elif k == 2:
        f1 = open("hotel.data", "rb")
        print("NAME", "\t", "\t", "ROOM NO.")
        try:
            while True:
                s = pickle.load(f1)
                print(s.name, "\t", "\t", s.room)
        except EOFError:
            pass
        f1.close()
    elif k == 3:
        while True:
            a = int(input("ENTER ROOM NO: "))
            if a != 0:
                break
            else:
                print("no input found")
                continue
        v = a
        f = open("hotel.data", "rb")
        f1 = open("hote.dat", "ab")
        n = 0
        try:
            while True:
                s = pickle.load(f)
                if s.room == v:
                    n = 1
                    name1 = s.name
                    print(" ")
                else:
                    pickle.dump(s, f1)
        except EOFError:
            if n == 0:
                print("NO GUEST IN ROOM ", v)
            elif n == 1:
                print("THANK YOU", name1, "2 FOR VISTING US")
                print("HOPE YOU LIKE OUR SERVICE")
                print("\n")
            pass
        f.close()
        f1.close()
        os.remove("hotel.data")
        os.rename("hote.dat", "hotel.data")
    elif k == 4:
        f2 = open("hotel.data", "rb")
        while True:
            v = input("ENTER ROOM NO.")
            if len(v) != 0:
                break
            else:
                print("no input found")
                continue
        v = int(v)
        try:
            n = 0
            while True:
                s = pickle.load(f2)
                a = s.room
                if v == a:
                    n = 1
                    print("NAME-", "\t", "\t", s.name)
                    print("\n")
                    print("ADDRESS-", "\t", s.address)
                    print("\n")
                    print("MOBILE NO.-", "  ", s.mobile_no)
                    print("\n")
                    print("HIS TOTAL BILL IS Rs.", s.price)
                elif EOFError:
                    if n == 0:
                        print("NO GUEST IN ROOM ", v)
                else:
                    n = 0
                    continue
        except EOFError:
            pass
        f2.close()
    elif k == 5:
        break
    else:
        print("invalid choice")
        continue
