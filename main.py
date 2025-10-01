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
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    print(reps)
    if reps % 2 > 0 and reps != 7:
        print("Short Break")
        time_to_count = SHORT_BREAK_MIN
    elif reps % 2 > 0 and reps == 7:
        print("Long Break")
        time_to_count = LONG_BREAK_MIN
    elif reps % 2 == 0:
        print("Work Time")
        time_to_count = WORK_MIN
    if reps > 7:
        reps = 0 
        checkmark.config(text="")
    checkmark.config(text="✅" * (reps // 2))
    reps += 1
    countdown(time_to_count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):

    minutes = count // 60
    if minutes < 10:
        minutes = "0" + str(minutes)
        int(minutes)
    seconds = count % 60
    if seconds < 10:
        seconds = "0" + str(seconds)
        int(seconds)

    time =f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text =time)
    if count > 0:
        window.after(100,countdown,count - 1)
    else:
        start_timer()

    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Simple Pomodoro")
window.config(padx = 100,pady=50, bg = YELLOW)
fg = GREEN



canvas = Canvas(width =200 ,height =224, bg= YELLOW, highlightthickness=0)
tomato_image =  PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image = tomato_image)
canvas.grid(column=1,row=5)
timer_text = canvas.create_text(103,130,text="00:00",fill = "white",font = (FONT_NAME,35,"bold"))


start_button = Button(text = "Start",command = start_timer,font = (FONT_NAME,15,"bold"))
start_button.grid(column=0,row=6)

Reset_button = Button(text = "Reset",command = None, font =  (FONT_NAME,15,"bold"))
Reset_button.grid(column=2,row=6)

checkmark = Label(text="✅",font=(FONT_NAME,10,"bold"),bg = YELLOW,)
checkmark.grid(column = 1, row =6 )

title_text = Label(text="Timer",font=(FONT_NAME,20,"bold"),bg = YELLOW,fg= GREEN)
title_text.grid(column=1,row=1)
window.mainloop()
