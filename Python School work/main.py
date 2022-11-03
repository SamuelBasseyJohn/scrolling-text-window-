from tkinter import *


def shift():
    x1, y1, x2, y2 = canvas.bbox("sam")
    if (x2 < 0 or y1 < 0):  # reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("sam", x1, y1)
    else:
        canvas.move("sam", -2, 0)
    canvas.after(1000//fps, shift)


root = Tk()
root.title('Assignment')
canvas = Canvas(root, bg='blue')
canvas.pack(fill=BOTH, expand=1)
text_var = "Welcome to computer science department"
text = canvas.create_text(0, -2000, text=text_var, font=('Times New Roman',
                          20, 'bold'), fill='black', tags=("sam",), anchor='w',)
x1, y1, x2, y2 = canvas.bbox("sam")
width = x2-x1
height = y2-y1
canvas['width'] = 300
canvas['height'] = 200
fps = 24  # Change the fps to make the animation faster/slower.
shift()
root.mainloop()
