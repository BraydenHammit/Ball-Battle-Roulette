import random as ran
import tkinter as tk
import math as m
import time as t
import platform as plt

#Looper Function:
def wrap_ball(canvas, shape):
    x1, y1, x2, y2 = canvas.coords(shape)
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    r = (x2 - x1) / 2
    w = canvas.winfo_width()
    h = canvas.winfo_height()

    if cx > w + r:
        cx = -r
    elif cx < -r:
        cx = w + r
    if cy > h + r:
        cy = -r
    elif cy < -r:
        cy = h + r

    canvas.coords(shape, cx - r, cy - r, cx + r, cy + r)



def frame(canvas, root, ball1, ball2, healthbar1, healthbar2, winner, checkforwinner, frm, dmg, clstxtbx, cos, splits=[]):
    prps = None
    frm += 1

    #Sentry Starting Random Position:
    if frm == 2:
        if ball1['type'] == 'sentry':
            x = [ran.uniform(0.0,canvas.winfo_width()),ran.uniform(0.0,canvas.winfo_height())]
            y = [x[0] - 40, x[1] -40]
            canvas.coords(ball1['shape'],x[0],x[1],y[0],y[1])
        if ball2['type'] == 'sentry':
            x = [ran.uniform(0.0,canvas.winfo_width()),ran.uniform(0.0,canvas.winfo_height())]
            y = [x[0] - 40, x[1] -40]
            canvas.coords(ball2['shape'],x[0],x[1],y[0],y[1])

    #Echo Teleport Set:
    if ball1['type'] == 'echo':
        if frm % 313 == 0:
            ball1['prevpos'] = canvas.coords(ball1['shape'])
            ball1['prevpos'].append(ball1['dx'])
            ball1['prevpos'].append(ball1['dy'])
            canvas.coords(ball1['extshape'],ball1['prevpos'][0],ball1['prevpos'][1],ball1['prevpos'][2],ball1['prevpos'][3])
        prps = ball1['prevpos']
    if ball2['type'] == 'echo':
        if frm % 313 == 0:
            ball2['prevpos'] = canvas.coords(ball2['shape'])
            ball2['prevpos'].append(ball2['dx'])
            ball2['prevpos'].append(ball2['dy'])
            canvas.coords(ball2['extshape'],ball2['prevpos'][0],ball2['prevpos'][1],ball2['prevpos'][2],ball2['prevpos'][3])
        prps = ball2['prevpos']

    #Chaser Movement:
    if ball1['type'] == 'chaser':
        pos = canvas.coords(ball1['shape'])
        pos_ = canvas.coords(ball2['shape'])
        cx = (pos[0] + pos[2]) / 2
        cy = (pos[1] + pos[3]) / 2
        cx2 = (pos_[0] + pos_[2]) / 2
        cy2 = (pos_[1] + pos_[3]) / 2
        dx = cx2 - cx
        dy = cy2 - cy
        dis = m.sqrt(dx*dx + dy*dy)
        if dis > 0:
            step = min(10, dis)
            ball1['dx'] = (dx / dis) * step
            ball1['dy'] = (dy / dis) * step
        else:
            ball1['dx'] = 0
            ball1['dy'] = 0
        canvas.move(ball1['shape'], ball1['dx'], ball1['dy'])
    elif ball2['type'] == 'chaser':
        pos = canvas.coords(ball2['shape'])
        pos_ = canvas.coords(ball1['shape'])
        cx = (pos[0] + pos[2]) / 2
        cy = (pos[1] + pos[3]) / 2
        cx2 = (pos_[0] + pos_[2]) / 2
        cy2 = (pos_[1] + pos_[3]) / 2
        dx = cx2 - cx
        dy = cy2 - cy
        dis = m.sqrt(dx*dx + dy*dy)
        if dis > 0:
            step = min(10, dis)
            ball2['dx'] = (dx / dis) * step
            ball2['dy'] = (dy / dis) * step
        else:
            ball2['dx'] = 0
            ball2['dy'] = 0
        canvas.move(ball2['shape'], ball2['dx'], ball2['dy'])

    #Ghost Invincibility:
    if ball1['type'] == 'ghost':
        if canvas.ghostinvince == None:
            canvas.ghostinvince = 0
        if canvas.ghostinvince > 0:
            canvas.ghostinvince -= 1
            canvas.itemconfigure(ball1['shape'],fill="#9d7474")
        else:
            canvas.itemconfigure(ball1['shape'],fill='red')
    if ball2['type'] == 'ghost':
        if canvas.ghostinvince == None:
            canvas.ghostinvince = 0
        if canvas.ghostinvince > 0:
            canvas.ghostinvince -= 1
            canvas.itemconfigure(ball2['shape'],fill="#74799d")
        else:
            canvas.itemconfigure(ball2['shape'],fill='blue')

    #Grower Growth:
    if ball1['type'] == 'grower':
        if (frm % 124) == 0:
            ball1['damage'] += ball1['damage']*0.01
            ball1['max hp'] += int(round(ball1['max hp']*0.01,0))
            ball1['hp'] += round(ball1['hp']*0.1,10)
            crds = canvas.coords(ball1['shape'])
            canvas.coords(ball1['shape'],crds[0]-1,crds[1]-1,crds[2]+1,crds[3]+1)
    if ball2['type'] == 'grower':
        if (frm % 123) == 0:
            ball2['damage'] += ball2['damage']*0.01
            ball2['max hp'] += int(round(ball2['max hp']*0.01,0))
            ball2['hp'] += ball2['hp']*0.01
            crds = canvas.coords(ball2['shape'])
            canvas.coords(ball2['shape'],crds[0]-1,crds[1]-1,crds[2]+1,crds[3]+1)

    #Healing:
    if ball1['type'] == 'healer':
        ball1['hp'] += ran.uniform(0.0,0.25)
    elif ball1['type'] == 'black hole':
        ball1['hp'] -= ran.uniform(0.0,0.025)
    elif (not ball1['hp'] <= 0) and (not ball1['type'] == 'zombie'):
        ball1['hp'] += ran.uniform(0.0,0.05)
    if ball2['type'] == 'healer':
        ball2['hp'] += ran.uniform(0.0,0.25)
    elif ball2['type'] == 'black hole':
        ball2['hp'] -= ran.uniform(0.0,0.025)
    elif (not ball2['hp'] <= 0) and (not ball2['type'] == 'zombie'):
        ball2['hp'] += ran.uniform(0.0,0.05)

    #Movement:
    if ball1['type'] not in ('sentry','chaser'):
        canvas.move(ball1['shape'], ball1['dx'], ball1['dy'])
    if ball2['type'] not in ('sentry','chaser'):
        canvas.move(ball2['shape'], ball2['dx'], ball2['dy'])
    pos1 = canvas.coords(ball1['shape'])
    pos2 = canvas.coords(ball2['shape'])
    if ball1['type'] == 'duo':
        duoAttkPos = canvas.coords(ball1['extshape'])
    if ball2['type'] == 'duo':
        duoAttkPos = canvas.coords(ball2['extshape'])
    if ball1['type'] == 'sentry':
        sentryProjPos = canvas.coords(ball1['extshape'])
    if ball2['type'] == 'sentry':
        sentryProjPos = canvas.coords(ball2['extshape'])

    #Wall Bouncing:
    ball1Mult = ran.uniform(-0.5,0.5)
    ball2Mult = ran.uniform(-0.5,0.5)
    try:
        if pos1[2] >= canvas.winfo_width() or pos1[0] <= 0:
            if ball1['type'] == 'hyperspeed':
                ball1['dx'] = -ball1['dx'] * 1.05
                ball1['dy'] *= 1.05
            elif ball1['type'] == 'looper':
                wrap_ball(canvas, ball1['shape'])
            elif ball1['type'] != 'chaser':
                ball1['dx'] = -ball1['dx'] - ball1Mult
                ball1['dy'] += ball1Mult
        if pos1[3] >= canvas.winfo_height() or pos1[1] <= 0:
            if ball1['type'] == 'hyperspeed':
                ball1['dy'] = -ball1['dy'] * 1.05
                ball1['dx'] *= 1.05
            elif ball1['type'] == 'looper':
                wrap_ball(canvas,ball1['shape'])
            elif ball1['type'] != 'chaser':
                ball1['dy'] = -ball1['dy'] - ball1Mult
                ball1['dx'] += ball1Mult
    except IndexError: None
    try:
        if pos2[2] >= canvas.winfo_width() or pos2[0] <= 0:
            if ball2['type'] == 'hyperspeed':
                ball2['dx'] = -ball2['dx'] * 1.05
                ball2['dy'] *= 1.05
            elif ball2['type'] == 'looper':
                wrap_ball(canvas, ball2['shape'])
            elif ball2['type'] != 'chaser':
                ball2['dx'] = -ball2['dx'] - ball2Mult
                ball2['dy'] += ball2Mult
        if pos2[3] >= canvas.winfo_height() or pos2[1] <= 0:
            if ball2['type'] == 'hyperspeed':
                ball2['dy'] = -ball2['dy'] * 1.05
                ball2['dx'] *= 1.05
            elif ball2['type'] == 'looper':
                wrap_ball(canvas,ball2['shape'])   
            elif ball2['type'] != 'chaser':
                ball2['dy'] = -ball2['dy'] - ball2Mult
                ball2['dx'] += ball2Mult
    except IndexError: None

    #Terminal Velocity:
    for d in [ball1['dx'],ball2['dx'],ball1['dy'],ball2['dy']]:
        if d > 100:
            d = 100

    #Too far out of bounds = DEATH:
    for c in canvas.coords(ball1['shape']):
        if abs(c) >= 3000:
            ball1['hp'] = 0
    for c in canvas.coords(ball2['shape']):
        if abs(c) >= 3000:
            ball2['hp'] = 0

#---------------------------------------------------------------------------------------------------

    #Splitting Loop:
    if (ball1['type'] == 'splitting' or ball2['type'] == 'splitting') and splits != []:
        for num, var in enumerate(splits):
            if var[1][2] <= 0:
                try:
                    canvas.delete(var[0])
                    splits.pop(num)
                except: None
                continue
            var[1][2] = min(var[1][2] + ran.uniform(0.0,0.05), 175)
            canvas.move(var[0],var[1][0],var[1][1])
            tempPos = canvas.coords(var[0])
            tempMult = ran.uniform(-0.5,0.5)
            if tempPos[2] >= canvas.winfo_width() or tempPos[0] <= 0:
                var[1][0] = -var[1][0] - tempMult
                var[1][1] += tempMult
            if tempPos[3] >= canvas.winfo_height() or tempPos[1] <= 0:
                var[1][1] = -var[1][1] - tempMult
                var[1][0] += tempMult

            if ball1['type'] == 'splitting':
                if (tempPos[2] >= pos2[0] and tempPos[0] <= pos2[2] and tempPos[3] >= pos2[1] and tempPos[1] <= pos2[3]):
                    splits, var[1][0], var[1][1], var[1][2], ball2['dx'], ball2['dy'], ball2['hp'] = dmg(root, canvas, prps, splits, frm,
                    var[0], 'splitting', 2.5, var[1][0], var[1][1], var[1][2],
                    ball2['shape'], ball2['type'], ball2['damage'], ball2['dx'], ball2['dy'], ball2['hp'], splitNum=num)
                if ball2['type'] == 'duo':
                    if (tempPos[2] >= duoAttkPos[0] and tempPos[0] <= duoAttkPos[2] and tempPos[3] >= duoAttkPos[1] and tempPos[1] <= duoAttkPos[3]):
                        splits, var[1][0], var[1][1], var[1][2], ball2['edx'], ball2['edy'], ball2['hp'] = dmg(root, canvas, prps, splits, frm,
                        var[0], 'splitting', 2.5, var[1][0], var[1][1], var[1][2],
                        ball2['extshape'], 'duo', 10, ball2['edx'], ball2['edy'], ball2['hp'], splitNum=num, duoAttk=2)

            if ball2['type'] == 'splitting':
                if (tempPos[2] >= pos1[0] and tempPos[0] <= pos1[2] and tempPos[3] >= pos1[1] and tempPos[1] <= pos1[3]):
                    splits, ball1['dx'], ball1['dy'], ball1['hp'], var[1][0], var[1][1], var[1][2] = dmg(root, canvas, prps, splits, frm,
                    ball1['shape'], ball1['type'], ball1['damage'], ball1['dx'], ball1['dy'], ball1['hp'],
                    var[0], 'splitting', 2.5, var[1][0], var[1][1], var[1][2], splitNum=num)
                if ball1['type'] == 'duo':
                    if (tempPos[2] >= duoAttkPos[0] and tempPos[0] <= duoAttkPos[2] and tempPos[3] >= duoAttkPos[1] and tempPos[1] <= duoAttkPos[3]):
                        splits, ball1['edx'], ball1['edy'], ball1['hp'], var[1][0], var[1][1], var[1][2] = dmg(root, canvas, prps, splits, frm,
                        ball1['extshape'], 'duo', 10, ball1['edx'], ball1['edy'], ball1['hp'],
                        var[0], 'splitting', 2.5, var[1][0], var[1][1], var[1][2], splitNum=num, duoAttk=1)


            if var[1][2] > 175:
                var[1][2] = 175

#---------------------------------------------------------------------------------------------------

    #Duo Attacking Ball:
    if ball1['type'] == 'duo':
        canvas.move(ball1['extshape'],ball1['edx'],ball1['edy'])
        duoAttkPos = canvas.coords(ball1['extshape'])
        tempMult = ran.uniform(-0.5,0.5)
        if duoAttkPos[2] >= canvas.winfo_width() or duoAttkPos[0] <= 0:
            ball1['edx'] = -ball1['edx'] - tempMult
            ball1['edy'] += tempMult
        if duoAttkPos[3] >= canvas.winfo_height() or duoAttkPos[1] <= 0:
            ball1['edy'] = -ball1['edy'] - tempMult
            ball1['edx'] += tempMult
    if ball2['type'] == 'duo':
        canvas.move(ball2['extshape'],ball2['edx'],ball2['edy'])
        duoAttkPos = canvas.coords(ball2['extshape'])
        tempMult = ran.uniform(-0.5,0.5)
        if duoAttkPos[2] >= canvas.winfo_width() or duoAttkPos[0] <= 0:
            ball2['edx'] = -ball2['edx'] - tempMult
            ball2['edy'] += tempMult
        if duoAttkPos[3] >= canvas.winfo_height() or duoAttkPos[1] <= 0:
            ball2['edy'] = -ball2['edy'] - tempMult
            ball2['edx'] += tempMult


    #Sentry Projectile:
    if ball1['type'] == 'sentry':
        sentryProjPos = canvas.coords(ball1['extshape'])
        dx = ((pos2[0] + pos2[2]) / 2) - ((sentryProjPos[0] + sentryProjPos[2]) / 2)
        dy = ((pos2[1] + pos2[3]) / 2) - ((sentryProjPos[1] + sentryProjPos[3]) / 2)
        dis = m.sqrt(dx*dx + dy*dy)
        ball1['edx'] = (dx / dis) * 10
        ball1['edy'] = (dy / dis) * 10
        canvas.move(ball1['extshape'],ball1['edx'],ball1['edy'])
        sentryProjPos = canvas.coords(ball1['extshape'])

        if (sentryProjPos[2] >= pos2[0] and sentryProjPos[0] <= pos2[2] and sentryProjPos[3] >= pos2[1] and sentryProjPos[1] <= pos2[3]):
            splits, ball1['edx'], ball1['edy'], __, ball2['dx'], ball2['dy'], ball2['hp'] = dmg(root, canvas, prps, splits, frm,
            ball1['extshape'], 'sentry', 3, ball1['edx'], ball1['edy'], ball1['hp'],
            ball2['shape'], ball2['type'], ball2['damage'], ball2['dx'], ball2['dy'], ball2['hp'], sentryProj=1, sentryBase=ball1['shape'])
        elif ball2['type'] == 'duo' and (sentryProjPos[2] >= duoAttkPos[0] and sentryProjPos[0] <= duoAttkPos[2] and sentryProjPos[3] >= duoAttkPos[1] and sentryProjPos[1] <= duoAttkPos[3]):
            splits, ball1['edx'], ball1['edy'], __, ball2['edx'], ball2['edy'], _ = dmg(root, canvas, prps, splits, frm,
            ball1['extshape'], 'sentry', 3, ball1['edx'], ball1['edy'], ball1['hp'],
            ball2['extshape'], 'duo', 10, ball2['edx'], ball2['edy'], None, sentryProj=1, sentryBase=ball1['shape'], duoAttk=2)
    if ball2['type'] == 'sentry':
        sentryProjPos = canvas.coords(ball2['extshape'])
        dx = ((pos1[0] + pos1[2]) / 2) - ((sentryProjPos[0] + sentryProjPos[2]) / 2)
        dy = ((pos1[1] + pos1[3]) / 2) - ((sentryProjPos[1] + sentryProjPos[3]) / 2)
        dis = m.sqrt(dx*dx + dy*dy)
        ball2['edx'] = (dx / dis) * 10
        ball2['edy'] = (dy / dis) * 10
        canvas.move(ball2['extshape'],ball2['edx'],ball2['edy'])
        sentryProjPos = canvas.coords(ball2['extshape'])

        if (sentryProjPos[2] >= pos1[0] and sentryProjPos[0] <= pos1[2] and sentryProjPos[3] >= pos1[1] and sentryProjPos[1] <= pos1[3]):
            splits, ball1['dx'], ball1['dy'], ball1['hp'], ball2['edx'], ball2['edy'], _ = dmg(root, canvas, prps, splits, frm,
            ball1['shape'], ball1['type'], ball1['damage'], ball1['dx'], ball1['dx'], ball1['hp'],
            ball2['extshape'], 'sentry', 3, ball2['edx'], ball2['edy'], None, sentryProj=2, sentryBase=ball2['shape'])
        elif ball1['type'] == 'duo' and (sentryProjPos[2] >= duoAttkPos[0] and sentryProjPos[0] <= duoAttkPos[2] and sentryProjPos[3] >= duoAttkPos[1] and sentryProjPos[1] <= duoAttkPos[3]):
            splits, ball1['edx'], ball1['edy'], __, ball2['edx'], ball2['edy'], _ = dmg(root, canvas, prps, splits, frm,
            ball1['extshape'], 'duo', 10, ball1['edx'], ball1['edx'], None,
            ball2['extshape'], 'sentry', 3, ball2['edx'], ball2['edy'], None, duoAttk=1, sentryProj=2, sentryBase=ball2['shape'])

#---------------------------------------------------------------------------------------------------

    #Basic Ball Collisions:
    pos1 = canvas.coords(ball1['shape'])
    pos2 = canvas.coords(ball2['shape'])
    try:
        if (pos1[2] >= pos2[0] and pos1[0] <= pos2[2] and pos1[3] >= pos2[1] and pos1[1] <= pos2[3]):
            splits, ball1['dx'], ball1['dy'], ball1['hp'], ball2['dx'], ball2['dy'], ball2['hp'] = dmg(root, canvas, prps, splits, frm,
            ball1['shape'], ball1['type'], ball1['damage'], ball1['dx'], ball1['dy'], ball1['hp'],
            ball2['shape'], ball2['type'], ball2['damage'], ball2['dx'], ball2['dy'], ball2['hp'])

        if ball1['type'] == 'duo':
            if (pos2[2] >= duoAttkPos[0] and pos2[0] <= duoAttkPos[2] and pos2[3] >= duoAttkPos[1] and pos2[1] <= duoAttkPos[3]):
                splits, ball1['edx'], ball1['edy'], ball1['hp'], ball2['dx'], ball2['dy'], ball2['hp'] = dmg(root, canvas, prps, splits, frm,
                ball1['extshape'], 'duo', 10, ball1['edx'], ball1['edy'], ball1['hp'],
                ball2['shape'], ball2['type'], ball2['damage'], ball2['dx'], ball2['dy'], ball2['hp'], duoAttk=1)

        elif ball2['type'] == 'duo':
            if (pos1[2] >= duoAttkPos[0] and pos1[0] <= duoAttkPos[2] and pos1[3] >= duoAttkPos[1] and pos1[1] <= duoAttkPos[3]):
                splits, ball1['dx'], ball1['dy'], ball1['hp'], ball2['edx'], ball2['edy'], ball2['hp'] = dmg(root, canvas, prps, splits, frm,
                ball1['shape'], ball1['type'], ball1['damage'], ball1['dx'], ball1['dy'], ball1['hp'],
                ball2['extshape'], 'duo', 10, ball2['edx'], ball2['edy'], ball2['hp'], duoAttk=2)
    except IndexError: None


    #HP Bar Updates:
    if ball1['hp'] > ball1['max hp']:
        ball1['hp'] = ball1['max hp']
    if ball2['hp'] > ball2['max hp']:
        ball2['hp'] = ball2['max hp']
    healthbar1.configure(text=f"{round(ball1['hp'],1)}/{ball1['max hp']}")
    healthbar2.configure(text=f"{round(ball2['hp'],1)}/{ball2['max hp']}")
    if ball1['hp'] <= 0:
        healthbar1.configure(text=f'0/{ball1["max hp"]}')
    elif ball2['hp'] <= 0:
        healthbar2.configure(text=f'0/{ball2["max hp"]}')


    #Check For Winner / Continue:
    if (ball1['hp'] <= 0) and (splits == [] or (ball1['type'] != 'splitting' or ball2['type'] == 'splitting')) and (ball2['hp'] <= 0) and (
    splits == [] or (ball2['type'] != 'splitting' or ball1['type'] == 'splitting')):
        winner = "draw"
        healthbar1.configure(text=f'0/{ball1["max hp"]}')
        healthbar2.configure(text=f'0/{ball2["max hp"]}')
    elif (ball1['hp'] <= 0) and (splits == [] or (ball1['type'] != 'splitting' or ball2['type'] == 'splitting')):
        winner = "ball2"
        healthbar1.configure(text=f'0/{ball1["max hp"]}')
    elif (ball2['hp'] <= 0) and (splits == [] or (ball2['type'] != 'splitting' or ball1['type'] == 'splitting')):
        winner = "ball1"
        healthbar2.configure(text=f'0/{ball2["max hp"]}')
    else: 
        winner = None
    if winner is not None:
        cont = tk.Button(root, text='Continue', highlightbackground="#494949", command=lambda: won(canvas, checkforwinner, winner, cont))
        if plt.system() == 'Linux':  
            clstxtbx[0].pack_forget()
            clstxtbx[1].pack_forget()
        cont.pack(side=tk.BOTTOM, pady=10)
        root.update_idletasks()
        if winner == 'ball1':
            canvas.configure(bg="blue")
            canvas.delete(ball2['shape'])
            try:
                if ball2['extshape'] is not None:
                    canvas.delete(ball2['extshape'])
            except KeyError: None
        if winner == 'ball2':
            canvas.configure(bg="red")
            canvas.delete(ball1['shape'])
            try:
                if ball1['extshape'] is not None:
                    canvas.delete(ball1['extshape'])
            except KeyError: None
        elif winner == 'draw':
            canvas.delete('all')
            canvas.configure(bg='purple')
    else:
        root.after(16, lambda: frame(canvas, root, ball1, ball2, healthbar1, healthbar2, winner, checkforwinner, frm, dmg, clstxtbx, cos, splits=splits))

def won(canvas,checkforwinner,winner,self):
    self.destroy()
    canvas.delete('all')
    checkforwinner(winner)