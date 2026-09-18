#Imports:
import tkinter as tk
from extra_code.create_balls import create_balls
from extra_code.frames import frame
from extra_code.tooltips import toolTip, stats
from extra_code.damage import dmg
from extra_code.windows import InternalWindow
import random as ran

def main(L=False, q=None):
    global money, rounds, winner, donations, bet, images, cos, cosset, ucos, roundNum, ball1, ball2, textbox1, textbox2, textboxM, textboxW, tooltip1, tooltip2, canvas, start_button, betting_enter, betting_frame, betting_ok1, betting_ok2, healthbar1, healthbar2, classtextbox1, classtextbox2, textbox_frame, shop_open, shop
    if L:
        q.destroy()
    #Basic Variables:
    root = tk.Tk()
    root.title("Ball Battle Roulette")
    root.geometry("900x800")
    root.minsize(900, 800)
    try: root.attributes('-fullscreen',True)
    except: 
        try: root.state('zoomed')
        except: None
    root.configure(bg="#393939")
    money = 100
    rounds = 0
    winner = None
    donations = 0
    bet = [None,None]#       [Ball#,$$$] 

    images = {
        'title': tk.PhotoImage(file='assets/images/title.png')
    }

    cos = []
    cosset = {}
    ucos = []

    #---------------------------------------------------------------------------------------------------


    #Open Betting Screen:
    def start_bet():
        global ball2, ball1, textbox1, textbox2, textboxM, textboxW, tooltip1, tooltip2, roundNum, rounds
        rounds += 1
        start_button.configure(highlightbackground="#494949")
        root.configure(bg="#494949")
        start_button.pack_forget()
        title.pack_forget()
        try:
            textboxW.destroy()
        except: None
        canvas.delete('all')
        ball1, ball2 = create_balls(canvas, root)
        roundNum.configure(text=f'Round {rounds}:')
        textbox1.configure(text=f'(i) Ball 1: {ball1["type"].title()}', fg='red', bg="#494949")
        textbox2.configure(text=f'(i) Ball 2: {ball2["type"].title()}', fg='blue', bg="#494949")
        tooltip1.text=stats(ball1['type'])
        tooltip2.text=stats(ball2['type'])
        textboxM = tk.Label(text=f'You have: ${money}\n\nWhat would you like to bet?', bg="#494949")
        textboxW = tk.Label(text='Who would you like to bet on?', bg="#494949")
        roundNum.pack(pady = 7)
        textbox_frame.pack(pady = 5)
        textbox1.pack(side=tk.LEFT, padx = 5)
        textbox2.pack(side=tk.LEFT, padx = 5)
        textboxM.pack(pady = 5)
        betting_enter.pack(pady = 5)
        textboxW.pack(pady = 10)
        betting_frame.pack(pady = 5)
        betting_ok1.pack(side=tk.LEFT, padx=5)
        betting_ok2.pack(side=tk.LEFT, padx=5)
        shop_open.pack(pady=20,side=tk.BOTTOM)

        root.update_idletasks()


    #After Round Finished:
    def round_won(winner):
        global money, textboxW, canvas
        prevmoney = money

        if winner == 'ball1':
            if bet[0] == 'ball1':
                money += bet[1]
                canvas.wins += 1
            else:
                money -= bet[1]
        elif winner == 'ball2':
            if bet[0] == 'ball2':
                money += bet[1]
                canvas.wins += 1
            else:
                money -= bet[1]


        healthbar1.pack_forget()
        wins = canvas.wins
        canvas.destroy()
        canvas = tk.Canvas(root, width=900, height=600, bg="gray50", highlightbackground="gray10")
        canvas.wins = wins
        canvas.mx = 0
        canvas.my = 0
        canvas.ghostinvince = None
        canvas.echotp = False
        healthbar2.pack_forget()
        classtextbox1.pack_forget()
        classtextbox2.pack_forget()
        new = None
        if winner == 'draw':
            textboxW = tk.Label(text=f'It was a draw.\n\nNo money was changed.',bg="#494949")
        else:
            textboxW = tk.Label(text=f'Ball {winner[4]} won.\n\nYou made ${money-prevmoney}, and are now at ${money}.',bg="#494949")
        if money <= 0:
            textboxW.configure(text=f'Ball {winner[4]} won.\n\nYou made ${money-prevmoney}, and are now at ${money}.\n\nYou ran out of money and made some terrible gambling decisions.\n\nGoodbye.')
            start_button.configure(text='Exit', command=lambda: root.destroy())
            new = tk.Button(root, text='Restart', highlightbackground="#494949", command=lambda: main(L=True, q=root))
        else:
            start_button.configure(text='Ok')
        textboxW.pack(pady = 10)
        if new != None:
            new.pack(pady = 10)
        start_button.pack(pady = 10)
        winner = None
        root.update_idletasks()
        

    #Start Round:
    def start(betNONGLOBAL):
        global bet
        try:
            if (int(betting_enter.get()) >= 0) and (int(betting_enter.get()) <= money):
                    bet = [betNONGLOBAL,int(betting_enter.get())]
                    if bet[0] == 'ball1':
                        classtextbox1.configure(text=f'{ball1["type"].title()}\n\nBetting: FOR')
                        classtextbox2.configure(text=f'Betting: AGAINST\n\n{ball2["type"].title()}')
                    elif bet[0] == 'ball2':
                        classtextbox1.configure(text=f'{ball1["type"].title()}\n\nBetting: AGAINST')
                        classtextbox2.configure(text=f'Betting: FOR\n\n{ball2["type"].title()}')
                    if shop.winfo_exists():
                        shop.destroy()
                    roundNum.pack_forget()
                    textbox_frame.pack_forget()
                    textbox1.pack_forget()
                    textbox2.pack_forget()
                    textboxM.destroy()
                    textboxW.destroy()
                    betting_enter.pack_forget()
                    betting_frame.pack_forget()
                    betting_ok1.pack_forget()
                    betting_ok2.pack_forget()
                    shop_open.pack_forget()
                    healthbar1.pack(pady=2)
                    classtextbox1.pack(pady=2)
                    canvas.pack(expand=True, fill='none')
                    classtextbox2.pack(pady=2)
                    healthbar2.pack(pady=2)
                    

                    root.after(0,lambda: frame(canvas, root, ball1, ball2, healthbar1, healthbar2, winner, round_won, 0, dmg, [classtextbox1, classtextbox2], cos, cosset, splits=[]))
        except: None

    #---------------------------------------------------------------------------------------------------

    #TKinter Object Variables:
    canvas = tk.Canvas(root, width=900, height=600, bg="gray50", highlightbackground="gray10")
    canvas.ghostinvince = None
    canvas.wins = 0
    canvas.echotp = False
    start_button = tk.Button(root, text="Start", highlightbackground="#393939", command=lambda: start_bet())
    roundNum = tk.Label(root, text=f'Round {rounds}', font=("Arial", 30, "bold"), bg="#494949", fg='#363636')
    title = tk.Label(root, image=images['title'], borderwidth=0, highlightthickness=0)
    betting_enter = tk.Entry(root, highlightbackground="#494949", width=30)
    betting_frame = tk.Frame(root, bg="#494949")
    betting_ok1 = tk.Button(betting_frame, highlightbackground="#494949", text='Ball 1', command = lambda: start('ball1'))
    betting_ok2 = tk.Button(betting_frame, highlightbackground="#494949", text='Ball 2', command = lambda: start('ball2'))
    healthbar1 = tk.Label(text=None,fg='red', bg="#494949",font=(None,30))
    healthbar2 = tk.Label(text=None,fg='blue', bg="#494949",font=(None,30))
    classtextbox1 = tk.Label(text=None,fg='red', bg="#494949")
    classtextbox2 = tk.Label(text=None,fg='blue', bg="#494949")
    textbox_frame = tk.Frame(root, bg="#494949")
    textbox1 = tk.Label(textbox_frame,text=f'Ball 1 will be: N/A', fg='red', bg="#494949")
    textbox2 = tk.Label(textbox_frame,text=f'Ball 2 will be: N/A', fg='blue', bg="#494949")
    tooltip1 = toolTip(textbox1,None)
    tooltip2 = toolTip(textbox2,None)
    shop_open = tk.Button(root, highlightbackground="#494949", text='Shop', command = lambda: openShop())
    shop = tk.Label(root,text=None)
    shop.destroy()

    #---------------------------------------------------------------------------------------------------

    #Shop Window Functions:
    def openShop():
        global shop, cosbutt, donbutt, bldbutt, cosset
        if not shop.winfo_exists():
            shop = InternalWindow(root,'Shop')
            #if ucos == []:
            #    cosbutt = tk.Button(shop,text='Cosmetics Have Not\nBeen Added Yet',highlightbackground="#494949",fg='black') #'All Cosmetics Unlocked,\nGreat Job I Suppose'
            #else:
            #    cosbutt = tk.Button(shop,text='Purchase Cosmetic\n$150',highlightbackground="#494949",fg='black',command=roll)
            #cosbutt.pack(expand=True)
            if 'bloodbath' in cos:
                bldbutt = tk.Button(shop,text='Secret Cosmetic Unlocked:\nBloodbath Endscreen\n10 Won Bets',highlightbackground="#494949",fg='black',command=lambda:setting('bloodbath',bldbutt))
            elif canvas.wins >= 10:
                bldbutt = tk.Button(shop,text='Secret Cosmetic Unlocked:\nBloodbath Endscreen\n10 Won Bets',highlightbackground="#494949",fg='black',command=lambda:setting('bloodbath',bldbutt))
                cos.append('bloodbath')
                cosset['bloodbath'] = True
            if 'donate' in cos:
                donbutt = tk.Button(shop,text='Secret Cosmetic Unlocked:\nGolden Round Number\n100 Donations',highlightbackground="#494949",fg='black',command=lambda:setting('donate',donbutt))
            else:
                donbutt = tk.Button(shop,text='Donate\n$1',highlightbackground="#494949",fg='black',command=donate)
            donbutt.pack(expand=True)

    def roll():
        global money, ucos, cos, cosset
        if money > 150:
            money -= 150
            rollNum = ran.randint(0,(len(ucos))-1)
            rolll = ucos[rollNum]
            cos.append(rolll)
            cosset[rolll] = True
            ucos.pop(rollNum)
            cosbutt.configure(text=f'Rolled:\n{rolll.title()}')
            textboxM.configure(text=f'You have: ${money}\n\nWhat would you like to bet?')
            root.after(1000,resetRollTxt)
            if ucos == []:
                cosbutt.configure(command=None)
            root.update_idletasks()
        else:
            cosbutt.configure(text='Cannot\nPurchase!',fg='red')
            root.update_idletasks()
            root.after(1000,resetRollTxt)

    def donate():
        global money, donations, cos, cosset
        if money > 1:
            money -= 1
            donations += 1
            if donations >= 100 and 'donate' not in cos:
                cos.append('donate')
                cosset['donate'] = True
                roundNum.configure(fg="#7c820e")
                donbutt.configure(text='Secret Cosmetic Unlocked:\nGolden Round Number\n100 Donations',bg='#3C5F0C',command=lambda:setting('donate',donbutt))
            textboxM.configure(text=f'You have: ${money}\n\nWhat would you like to bet?')
            root.update_idletasks()
        else:
            donbutt.configure(text='Cannot\nPurchase!',fg='red')
            root.update_idletasks()
            root.after(1000,resetDonTxt)


    def resetRollTxt():
        cosbutt.configure(text='Purchase Cosmetic\n$150',fg='black')
        if ucos == []:
            cosbutt.configure(text='All Cosmetics Unlocked,\nGreat Job I Suppose')
        root.update_idletasks()

    def resetDonTxt():
        if 'donate' not in cos:
            donbutt.configure(text='Donate\n$1',fg='black')

    def setting(cosmetic,button):
        global cosset
        if cosset[cosmetic] == True: 
            cosset[cosmetic] = False
            button.configure(bg="#CA1818")
            if cosmetic == 'donate':
                roundNum.configure(fg='#363636')
        elif cosset[cosmetic] == False:
            cosset[cosmetic] = True
            button.configure(bg="#3C5F0C")
            if cosmetic == 'donate':
                roundNum.configure(fg='#7c820e')
        
    #---------------------------------------------------------------------------------------------------

    #Start Game:
    title.pack(pady=10)
    start_button.pack(pady=20)
    root.mainloop()

main()