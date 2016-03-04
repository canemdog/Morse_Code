import string
from tkinter import *
from tkinter import ttk


Morse_Code = {"A":(0,1), "B":(1,0,0,0), "C":(1,0,1,0), "C":(1,0,1,0), "D":(1,0,0), "E":(0,), 
"F":(0,0,1,0), "G":(1,1,0), "H":(0,0,0,0), "I":(0,0), "J":(0,1,1,1), "K":(1,0,1), "L":(0,1,0,0), 
"M":(1,1), "N":(1,0), "O":(1,1,1), "P":(0,1,1,0), "Q":(1,1,0,1), "R":(0,1,0), "S":(0,0,0), "T":(1), 
"U":(0,0,1), "V":(0,0,0,1), "W":(0,1,1), "X":(1,0,0,1), "Y":(1,0,1,1,), "Z":(1,1,0,0), "0":(1,1,1,1,1)
, "1":(0,1,1,1,1), "2":(0,0,1,1,1), "3":(0,0,0,1,1), "4":(0,0,0,0,1), "5":(0,0,0,0,0), "6":(1,0,0,0,0)
, "7":(1,1,0,0,0), "8":(1,1,1,0,0), "9":(1,1,1,1,0), ".":(0,1,0,1,0,1), ",":(1,1,0,0,1,1), 
":":(1,1,1,0,0,0), "?":(0,0,1,1,0,0), "'":(0,1,1,1,1,0), "-":(1,0,0,0,0,1), "/":(1,0,0,1,0), 
"(":(1,0,1,1,0,1), ")":(1,0,1,1,0,1), "\"":(0,1,0,0,1,0), "@":(0,1,1,0,1,0), "=":(1,0,0,0,1)}


def encode(*args):
    try:
        # e_message is the Encoded Message, Post More Code Translation
        e_message = ""
        # nessage is the message to be encoded into Morse
        message = str(Decode.get())

        for char in message:
        	char = str.upper(char)
        	#print ("char is:", char)
        	tuple_len = int(len(Morse_Code[char]))
        	x = 0
        	int(x)
        	while x < tuple_len:
        		e_message = e_message + str((Morse_Code[char][x]))
        		x = x + 1
        # Code is the Variable in Tkinter that you set and display back to the user
        Code.set (e_message)
    except ValueError:
        pass
    
root = Tk()
root.title("Morse Code")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Defining variables in tkinter gui. Decode is for Entry of the string to Decode
# Code is for the result of coding the message
Decode = StringVar()
Code = StringVar()

#Section of the GUI defining the Decode Entry window.  Decdoe is the variable that takes
# the string that the user wishes to change from text into Morse
Decode_Entry = ttk.Entry(mainframe, width=40, textvariable=Decode)
Decode_Entry.grid(column=2, row=1, sticky=(W, E))
#Defining Buttoms, Encode to change the message into Morse.  Quit to exit application
ttk.Label(mainframe, textvariable=Code).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Encode", command=encode).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="Quit", command=root.destroy).grid(column=3, row=3, sticky=E)
#Defining the output of the conversion to Morese
ttk.Label(mainframe, text="Covert").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="to Morse Code.").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="In Morse Code:").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

Decode_Entry.focus()
root.bind('<Return>', encode)

root.mainloop()