# Imports
from tkinter import *
from tkinter import messagebox
import subprocess, sys

# Testing, enables useless features
testing = True

# Window
window = Tk()
window.title("Pixel Draw")
window.resizable(0, 0)
window.geometry(f'1140x492+{int((window.winfo_screenwidth() / 2) - (1187 / 2))}+{int((window.winfo_screenheight() / 2) - (568 / 2))}')

colors = {
    "Brown": "#914710",
    "Red": "#e28383",
    "Red Orange": "#e29b83",
    "Orange": "#e2b383",
    "Yellow Orange": "#e2ca83",
    "Yellow": "#e2e283",
    "Lighter Green": "#cae283",
    "Light Green": "#b3e283",
    "Green": "#9be283",
    "Greener": "#83e283",
    "Turquoise": "#83e29b",
    "Turquoise-ish": "#83e2b3",
    "Light Blue": "#83e2ca",
    "Another Blue": "#83cae2",
    "Blue": "#83b3e2",
    "Purplish Blue": "#839be2",
    "Purple": "#8383e2",
    "Violet": "#9b83e2",
    "Mostly Pink": "#b383e2",
    "Saturated Pink": "#ca83e2",
    "Reddish Pink": "#e283b3",
    "Black": 'black',
    "Grey": 'grey',
    "White": "White",
}

# Colors
ROWS = 0
ROW_2 = 0
TAG = 0

# Testing fe    ature
if testing == True:

    # Color row 
    color_row = Frame(window)
    color_row.pack(side=LEFT, fill='y')

    for color in colors:
        ROWS += 1

        batan = Button(
                color_row, bg=colors.get(color), height=2, width=4, activebackground=colors.get(color)
            )
        batan["command"] = lambda colorr=colors.get(color): set_block(colorr)

        if ROWS <= 12: batan.grid(row=ROWS, column=0)
        else:
            ROW_2 += 1
            batan.grid(row=ROW_2, column=1)

# Create main frame
root = Frame(window)
root.pack(fill='both', expand=1)

# Variables
r,c = 0,0
__width = 28
current_block = colors["Green"]

tags = []
tag = 0

def set_block(color):
    global current_block
    current_block = color

    if color == "black" or color == colors.get("Brown"): cc.config(fg='white')
    else: cc.config(fg='black')

    cb.config(bg=color)

    cc.config(bg=color)
    window.config(bg=color)

def placeb(btn):
    btn["bg"] = current_block
    btn["activebackground"] = current_block

# Itterate a bunch of tons
for x in range(1,299):
    tag += 1
    tags.append(tag)
    b = Button(root, bg=colors["Another Blue"], width=4, height=2, highlightbackground='black', activebackground=colors["Another Blue"])
    b.grid(row=r, column=c, sticky=N+S+E+W)
    b["command"] = lambda b=b: placeb(b)
    c+=1

    if c==__width:
        r+=1
        c=0

# Build some grass
r_, c_ = 0, 0
_width = 18,0
fake_tags = 126

for x in range(1, 29):
    fake_tags += 1
    tags.append(fake_tags)
    b = Button(root, bg=colors["Green"], width=4, height=2, highlightbackground='black', activebackground=colors["Green"])
    b.grid(row=10, column=c_, sticky=N+S+E+W)
    b["command"] = lambda b=b: placeb(b)
    c_+=1

    if c_==_width:
        r_+=1
        c_=0

# Execute
if __name__ == '__main__':
    cb = Frame(root, height=45, bg=current_block)
    cb.grid(row=11, columnspan=28, sticky="nsew")

    cc = Label(cb, text="Control+C > Clear all | Useless Python App", font=("Product Sans", 21), bg=current_block)
    cc.pack()

    def reopen():
        ee = messagebox.askyesno("Are you sure you want to exit", "Are you sure you want to exit, you will loose all your work", icon='warning')

        if ee == True:
            root.quit()
            subprocess.Popen(f"{sys.executable} main.py")

    window.bind("<Control-c>", lambda event: reopen())

    window.mainloop()
