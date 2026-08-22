import tkinter as tk
from extra_code.create_balls import create_balls
from extra_code.frames import frame
from extra_code.tooltips import toolTip, stats

root = tk.Tk()
root.title("Ball Battle Roulette")
root.geometry("900x800")
root.minsize(900, 800)
try:
    root.state('zoomed')
except: None
root.configure(bg="#393939")
money = 100
winner = None
bet = [None,None]#       [Ball#,$$$] 


images = {
    'title': tk.PhotoImage(file='assets/images/title.png')
}





def start_bet():
    global ball2, ball1, textbox1, textbox2, textboxM, textboxW, tooltip1, tooltip2
    start_button.configure(highlightbackground="#494949")
    root.configure(bg="#494949")
    start_button.pack_forget()
    title.pack_forget()
    try:
        textboxW.destroy()
    except: None
    canvas.delete('all')
    ball1, ball2 = create_balls(canvas, root)
    textbox1.configure(text=f'Ball 1 will be: {ball1["type"].title()}', fg='red', bg="#494949")
    textbox2.configure(text=f'Ball 2 will be: {ball2["type"].title()}', fg='blue', bg="#494949")
    tooltip1.text=stats(ball1['type'])
    tooltip2.text=stats(ball2['type'])
    textboxM = tk.Label(text=f'You have: ${money}\n\nWhat would you like to bet?', bg="#494949")
    textboxW = tk.Label(text='Who would you like to bet on?', bg="#494949")
    textbox1.pack(pady = 5)
    textbox2.pack(pady = 5)
    textboxM.pack(pady = 5)
    betting_enter.pack(pady = 15)
    textboxW.pack(pady = 10)
    betting_ok1.pack(pady = 5)
    betting_ok2.pack(pady = 5)

    root.update_idletasks()



def check_for_winner(winner):
    global money, textboxW, canvas
    prevmoney = money

    if winner == 'ball1':
        if bet[0] == 'ball1':
            money += bet[1]
        else:
            money -= bet[1]
    elif winner == 'ball2':
        if bet[0] == 'ball2':
            money += bet[1]
        else:
            money -= bet[1]


    healthbar1.pack_forget()
    canvas.destroy()
    canvas = tk.Canvas(root, width=900, height=600, bg="gray50", highlightbackground="gray10")
    healthbar2.pack_forget()
    if winner == 'draw':
        textboxW = tk.Label(text=f'It was a draw.\nNo money was changed.',bg="#494949")
    else:
        textboxW = tk.Label(text=f'Ball {winner[4]} won.\nYou made ${money-prevmoney}, and are now at ${money}.',bg="#494949")
    start_button.configure(text='Ok')
    textboxW.pack(pady = 10)
    start_button.pack(pady = 5)
    winner = None
    root.update_idletasks()
     


def start(betNONGLOBAL):
    global money, bet, winner
    try:
        if (int(betting_enter.get()) >= 0) and (int(betting_enter.get()) <= money):
                bet = [betNONGLOBAL,int(betting_enter.get())]
                textbox1.pack_forget()
                textbox2.pack_forget()
                textboxM.destroy()
                textboxW.destroy()
                betting_enter.pack_forget()
                betting_ok1.pack_forget()
                betting_ok2.pack_forget()
                healthbar1.pack(pady=20)
                canvas.pack(expand=True, fill='none')
                healthbar2.pack(pady=20)
                

                frame(canvas, root, ball1, ball2, healthbar1, healthbar2, winner, check_for_winner, 0)
    except: None



canvas = tk.Canvas(root, width=900, height=600, bg="gray50", highlightbackground="gray10")
start_button = tk.Button(root, text="Start", highlightbackground="#393939", command=lambda: start_bet())
title = tk.Label(root, image=images['title'], borderwidth=0, highlightthickness=0)
betting_enter = tk.Entry(root, highlightbackground="#494949", width=30)
betting_ok1 = tk.Button(root, highlightbackground="#494949", text='Ball 1', command = lambda: start('ball1'))
betting_ok2 = tk.Button(root, highlightbackground="#494949", text='Ball 2', command = lambda: start('ball2'))
healthbar1 = tk.Label(text=None,fg='red', bg="#494949")
healthbar2 = tk.Label(text=None,fg='blue', bg="#494949")
textbox1 = tk.Label(text=f'Ball 1 will be: None', fg='red', bg="#494949")
textbox2 = tk.Label(text=f'Ball 2 will be: None', fg='blue', bg="#494949")
tooltip1 = toolTip(textbox1,None)
tooltip2 = toolTip(textbox2,None)
title.pack(pady=10)
start_button.pack(pady=20)

root.mainloop()