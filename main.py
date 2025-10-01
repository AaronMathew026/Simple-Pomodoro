from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Simple Pomodoro")
window.config(padx = 100,pady=50, bg = YELLOW)
fg = GREEN


canvas = Canvas(width =200 ,height =224, bg= YELLOW, highlightthickness=0)
tomato_image =  PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image = tomato_image)
canvas.grid(column=1,row=5)
canvas.create_text(103,130,text="00:00",fill = "white",font = (FONT_NAME,35,"bold"))


start_button = Button(text = "Start",command = None,font = (FONT_NAME,15,"bold"))
start_button.grid(column=0,row=6)



Reset_button = Button(text = "Reset",command = None, font =  (FONT_NAME,15,"bold"))
Reset_button.grid(column=2,row=6)



title_text = Label(text="Timer",font=(FONT_NAME,20,"bold"),bg = YELLOW,fg= GREEN)
title_text.grid(column=1,row=1)
window.mainloop()
