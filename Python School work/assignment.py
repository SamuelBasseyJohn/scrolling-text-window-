from tkinter import *


def buttonPressed():
    print("Done")


window = Tk()
label = Label(window, text="CSC 212 Assignment", bg="red")
label.pack(fill="both")
button = Button(window, text="Done", foreground='blue',
                bg='red', command=buttonPressed)
button.pack()
window.mainloop()
