def ragam():
    while True:
        a = input(f"\n\nPlease enter a (2 digit) number : \n\n")
        numbere = a.replace(' ', "", )
        if (numbere.isdecimal()) == 0:
            print(F"no!!'{numbere}' is not a number")
        elif len(numbere) < 2:
            print(F"(no!!{numbere} it is smaller than 2 digits")
        elif len(numbere) > 2:
            print(F"(no!!{numbere} it is bigger than 2 digits")
        elif numbere[1] > numbere[0]:
            benevis = int(numbere[1]) - int(numbere[0])
            print(F"({numbere[1]}-{numbere[0]})={benevis}\n The second number is larger.")
        elif numbere[0] > numbere[1]:
            benevis = int(numbere[0]) - int(numbere[1])
            print(F"({numbere[0]}-{numbere[1]})={benevis}\n The first number is larger.")
        elif numbere[1] == numbere[0]:
            print(F"({numbere[1]}-{numbere[0]})=0\n The numbers are equal.")
        while True:
            soval = input("\nDDO YOU CONTINUE AGAIN? y / n\n")
            if soval.lower() == "n":
                start()
            elif soval.lower() == "y":
                ragam()
            else:
                print("The character entered is invalid!!\nPlease enter(n) to exit and(y) to continue")
# --------------------------------------------------------
def mashin_hesab():
    while True:
        nbr = (input("\n\nENTER NUMBER 1 :"))
        nbr_1 = nbr.replace(' ', "", )
        if (nbr_1.isdecimal()) == 0:
            print(F"no!!'{nbr_1}' is not a number")
            mashin_hesab()
        while True:
            mshs_space = input("ENTER TYPE : ( / , * , + , - )")
            moshakhas = mshs_space.replace(' ', "", )
            # نا بهینه
            if moshakhas == "*":
                break
            elif moshakhas == "/":
                break
            elif moshakhas == "+":
                break
            elif moshakhas == "-":
                break
            else:
                print("no!! ENTER: / or * or + or - ")
        while True:
            nbrd = (input("ENTER NUMBER 2 :"))
            nbr_2 = nbrd.replace(' ', "", )
            if (nbr_2.isdecimal()) == 0:
                print(F"no!!'{nbr_2}' is not a number")
            elif (nbr_2.isdecimal()) == 1:
                break
        if moshakhas == "+":
            hasel = int(nbr_1) + int(nbr_2)
            print(f"({nbr_1}+{nbr_2})={hasel}")
        elif moshakhas == "-":
            hasel = int(nbr_1) - int(nbr_2)
            print(f"({nbr_1}-{nbr_2})={hasel}")
        elif moshakhas == "*":
            hasel = int(nbr_1) * int(nbr_2)
            print(f"({nbr_1}*{nbr_2})={hasel}")
        elif moshakhas == "/":
            try:
                hasel = int(nbr_1) / int(nbr_2)
            except ZeroDivisionError:
                print("NO!! You cannot divide a number by 0!")
                break
            else:
                print(f"({nbr_1}/{nbr_2})={hasel}")
        while True:
            soval = input("\nDDO YOU CONTINUE AGAIN? y / n\n")
            if soval.lower() == "n":
                start()
            elif soval.lower() == "y":
                mashin_hesab()
            else:
                print("The character entered is invalid!!\nPlease enter(n) to exit and(y) to continue")
# ---------------------------------------------------
def start():
    while True:
        moshakhas = input("\n\nENTE TYPE : 1=tafazol | 2=calculator \n\n")
        if moshakhas == "1":
            ragam()
        elif moshakhas == "2":
            mashin_hesab()
        else:
            print("please ENTER A NUMBER TRUE!! ")
start()