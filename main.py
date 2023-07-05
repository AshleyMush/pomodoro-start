from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = f"00: 00")
    timer_label.config(text="Timer",bg=YELLOW, fg=GREEN,  font=(FONT_NAME, 50, "bold"))
    check_mark.config(text="")
    global  REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS

    REPS += 1

    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    #If it's the 1st/3rd/5th/7th rep
    if REPS % 8 == 0 :
        timer_label.config(text="Break",bg=YELLOW, fg=RED,  font=(FONT_NAME, 50, "bold"))
        count_down(LONG_BREAK_MIN)

    elif REPS %2 == 0:
        timer_label.config(text="Break",bg=YELLOW, fg=PINK,  font=(FONT_NAME, 50, "bold"))
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work",bg=YELLOW, fg=GREEN,  font=(FONT_NAME, 50, "bold"))

        count_down(work_sec)
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}: {count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)

    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Domasi")
window.config(padx=100, pady=150, bg= YELLOW)





canvas = Canvas(width=200 , height= 224, bg= YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00: 00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)





#Buttons


#calls action() when pressed
start_button = Button(text="Start",highlightthickness=0,  command=start_timer)
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3)




#Check Mark
check_mark = Label(text="✔",fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
check_mark.grid(column=1, row=5)




#Labels
timer_label = Label(text="Timer",bg=YELLOW, fg=GREEN,  font=(FONT_NAME, 50, "bold"))
# label.config(text="This is new text")

timer_label.grid(column=1, row=0)




window.mainloop()