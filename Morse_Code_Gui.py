
import string, re
from tkinter import *
from tkinter import ttk


Morse_Code = {"A":(0,1), "B":(1,0,0,0), "C":(1,0,1,0), "C":(1,0,1,0), "D":(1,0,0), "E":(0,), 
"F":(0,0,1,0), "G":(1,1,0), "H":(0,0,0,0), "I":(0,0), "J":(0,1,1,1), "K":(1,0,1), "L":(0,1,0,0), 
"M":(1,1), "N":(1,0), "O":(1,1,1), "P":(0,1,1,0), "Q":(1,1,0,1), "R":(0,1,0), "S":(0,0,0), "T":(1), 
"U":(0,0,1), "V":(0,0,0,1), "W":(0,1,1), "X":(1,0,0,1), "Y":(1,0,1,1,), "Z":(1,1,0,0), "0":(1,1,1,1,1)
, "1":(0,1,1,1,1), "2":(0,0,1,1,1), "3":(0,0,0,1,1), "4":(0,0,0,0,1), "5":(0,0,0,0,0), "6":(1,0,0,0,0)
, "7":(1,1,0,0,0), "8":(1,1,1,0,0), "9":(1,1,1,1,0), ".":(0,1,0,1,0,1), ",":(1,1,0,0,1,1), 
":":(1,1,1,0,0,0), "?":(0,0,1,1,0,0), "'":(0,1,1,1,1,0), "-":(1,0,0,0,0,1), "/":(1,0,0,1,0), 
"(":(1,0,1,1,0,1), ")":(1,0,1,1,0,1), "\"":(0,1,0,0,1,0), "@":(0,1,1,0,1,0), "=":(1,0,0,0,1), " ":()}



class ConstrainedEntry(ttk.Entry):
    def __init__(self, *args, **kwargs):
        ttk.Entry.__init__(self, *args, **kwargs)
        #Recursively call itself on each key stroke of the message Entry field to validate if an invalid key press is detected
        vcmd = (self.register(self.on_validate),"%P")
        self.configure(validate="key", validatecommand=vcmd)

    def disallow(self):
        self.bell()

    def on_validate(self, message):
        try:
            # Check that the input string is allowed using Relational Expressions
            # First strip it of white chars at front and end vis .strip() command
            if message.strip() == "": return True
            message_1 = str(message)
            #use striped string to check if valid
            if re.match(r"^[A-Za-z0-9\.,:\?'\-\/\(\)\\@=\s]*$", message_1) == None:
            #Invalid input. Only charactors defined in the dictionary are allowed

                self.disallow()
                return False
        # handle exceptions        
        except ValueError:
            self.disallow()
            return False

        return True

    def encode(self, *args):
        try:
            # e_message is the Encoded Message, Post Morse code translation
            e_message = ""
            # nessage is the message to be encoded into Morse
            message = str(Input_Str.get())

            for char in message:
                #Convert each character into upper case only
                char = str.upper(char)
                #Determien the length of the tuple to know how many dit or dah you expect to append to the string
                tuple_len = int(len(Morse_Code[char]))
                x = 0
                int(x)
                # while your position x is less than the length of the word apend the next dit or dah to make up the word in Morse
                while x < tuple_len:
                    e_message = e_message + str((Morse_Code[char][x]))
                    x = x + 1
                #Add a space after each encoded letter
                e_message = e_message + str(" ")
            # Ouput_Str is the Variable in Tkinter Tex field that you set and display back to the user
            Output_Str.set (e_message)
        except ValueError:
            pass
        return

root = Tk()
#Define global varialble for the clear and encoded messages
Input_Str = StringVar()
Output_Str = StringVar()

#Define the Tkinter Frame
content = ttk.Frame(root)
root.title("Morse Code")
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100) 
#Define the widgets that will make up the frame
#Button for Encoding and Quitting   
button1 = ttk.Button(content, text="Encode", command= lambda: ConstrainedEntry.encode(content, Input_Str))
button2 = ttk.Button(content, text="Quit", command=root.destroy)
#Defining the output of the conversion to Morese
label1 = ttk.Label(content, text="Message:", anchor="w")
# Calls the ContrainedEntry method to check that values entered are valid
Encode_Entry = ConstrainedEntry(content, width=40, textvariable=Input_Str)
label2 = ttk.Label(content, text="Morse Code:", anchor="w")
# Result display of coded result
Coded_Result = ttk.Entry(content, width=40, textvariable=Output_Str)
#Construct the window

#Draw the frame and the widgets that make up the GUi
content.grid (column=0 , row=0)
frame.grid (column=0, row=0, columnspan=2, rowspan=3)
label1.grid(column=1, row=1, sticky=(N,W))
Encode_Entry.grid(column=2, row=1, sticky=(N,W))
label2.grid(column=1, row=2, sticky=(N,W))
Coded_Result.grid(column=2, row=2, sticky=(N,W))
button1.grid(column=3, row=3, sticky=W)
button2.grid(column=2, row=3, sticky=W)

#After drawing the Frame and its widgets set the focus on the Entry box for the message to be encoded
Encode_Entry.focus()

#Set the main loop for the program to run
root.mainloop()


