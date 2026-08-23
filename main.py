import tkinter as tk
import platform as plt
import subprocess as sp
from extra_code.create_balls import create_balls
from extra_code.frames import frame
from extra_code.tooltips import toolTip, stats
from extra_code.damage import dmg

if plt.system() == 'Darwin':
    syst = 'm' #MacBook
elif plt.system() == 'Windows':
    syst = 'w' #Windows
else:
    syst = 'o' #Other

root = tk.Tk()
root.title("Ball Battle Roulette")
root.geometry("900x800")
root.minsize(900, 800)
root.configure(bg="#393939")
if syst != 'o':
    try:
        root.attributes('-fullscreen', True)
    except:
        root.state('zoomed')
else: #Using codespace
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")


money = 100
winner = None
bet = [None,None]#       [Ball#,$$$] 


images = {
    'title': tk.PhotoImage(file='assets/images/title.png')
}

sounds = {
    'bonk': 'assets/audio/bonk.mp3',
    'pop': 'assets/audio/pop.mp3',
    'click': 'assets/audio/click.mp3'
}

soundsPlaying = {
    'bonk': None,
    'pop': None,
    'click': None
}


def play(f, t, v=1.0):  # (file, type, volume)
    global soundsPlaying
    if syst == "w":
        cmd = f'(New-Object Media.SoundPlayer "{f}").Play();'
        soundsPlaying[t] = sp.Popen(["powershell", "-WindowStyle", "Hidden", "-Command", cmd], stdout=sp.DEVNULL, stderr=sp.DEVNULL)
    elif syst == "m":
        appS = f'play alias (POSIX file "{f}")'
        soundsPlaying[t] = sp.Popen(["afplay", "-v", str(v), appS], stdout=sp.DEVNULL, stderr=sp.DEVNULL, close_fds=True)

def stopPlaying(t):
    if t:            
        t.terminate()
    t = None         


def start_bet():
    global ball2, ball1, textbox1, textbox2, textboxM, textboxW, tooltip1, tooltip2
    play(sounds['click'],soundsPlaying['click'])
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
                play(sounds['click'],'click')
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
                

                frame(canvas, root, ball1, ball2, healthbar1, healthbar2, winner, check_for_winner, 0, dmg, play, sounds, splits=[])
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
stopPlaying(soundsPlaying['bonk'])
stopPlaying(soundsPlaying['click'])
stopPlaying(soundsPlaying['pop'])