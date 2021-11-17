
if True == True:
    
    import os
    from tkinter import *
    from tkinter import filedialog


            # XXX Add the defs here
    def clearscr():
        os.system("cls")
    clearscr()
    print("Set defs")
    def blankline(Lines):
        for a in Lines:
            print("")
    def Readptb(PYBOYTE):
        Fileread = open(PYBOYTE, "r")
        for x in Fileread:
            print(x)
            blankline("1")
            input("Press enter")
            clearscr()
    def homescr():
        clearscr()
        print("PTR V2.5")
    # Defs here
    





    clearscr() # Do not do defs after Clearscr()
    SettingsYN = input("Settings Y/N ")
    clearscr() 
    if SettingsYN == "Y":
        clearscr()
        print("1 Color")
        print("2 Choose file from GUI")
        Setting = input("Setting  ") # asking for color
        clearscr()
    # Color set
        if Setting == "2":
            import tkinter
            from tkinter import filedialog
            filepath = filedialog.askopenfilename()
            Buffer = filepath
            skipask = "Y"

        if Setting == "1": # if it is 1 then run 
            color = input("color 1, 2, 3, 4, 5, 6, 7, A, B, C, D, E, F. pick one")
            if color == "1":
                os.system("color 1")
            if color == "2":
                os.system("color 2")
            if color == "3":
                os.system("color 3")
            if color == "4":
                os.system("color 4")
            if color == "5":
                os.system("color 5")
            if color == "6":
                os.system("color 6")
            if color == "7":
                os.system("color 7")
            if color == "A":
                os.system("color A")
            if color == "B":
                os.system("color B")
            if color == "C":
                os.system("color C")
            if color == "D":
                os.system("color D")
            if color == "E":
                os.system("color E")
            if color == "F":
                os.system("color F")


    if SettingsYN == "N":
            skipask = "N"
    



    clearscr()
    if skipask == "N":
        Buffer = input("drop file here:")
        clearscr()
    Readptb(Buffer)
# The code here will be run
clearscr()
