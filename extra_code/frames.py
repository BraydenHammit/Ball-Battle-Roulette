import random as ran

def frame(canvas, root, ball1, ball2, healthbar1, healthbar2, winner, checkforwinner, frm, dmg, splits=[]):
    frm += 1
    if ball1['type'] == 'healer':
        ball1['hp'] += ran.uniform(0.0,0.25)
    elif (not ball1['hp'] <= 0) and (not ball1['type'] == 'zombie'):
        ball1['hp'] += ran.uniform(0.0,0.05)
    if ball2['type'] == 'healer':
        ball2['hp'] += ran.uniform(0.0,0.25)
    elif (not ball2['hp'] <= 0) and (not ball2['type'] == 'zombie'):
        ball2['hp'] += ran.uniform(0.0,0.05)
    canvas.move(ball1['shape'], ball1['dx'], ball1['dy'])
    canvas.move(ball2['shape'], ball2['dx'], ball2['dy'])
    pos1 = canvas.coords(ball1['shape'])
    pos2 = canvas.coords(ball2['shape'])
    if ball1['type'] == 'duo':
        duoAttkPos = canvas.coords(ball1['extshape'])
    if ball2['type'] == 'duo':
        duoAttkPos = canvas.coords(ball2['extshape'])

    ball1Mult = ran.uniform(-0.5,0.5)
    ball2Mult = ran.uniform(-0.5,0.5)
    try:
        if pos1[2] >= canvas.winfo_width() or pos1[0] <= 0:
            ball1['dx'] = -ball1['dx'] - ball1Mult
            ball1['dy'] += ball1Mult
        if pos1[3] >= canvas.winfo_height() or pos1[1] <= 0:
            ball1['dy'] = -ball1['dy'] - ball1Mult
            ball1['dx'] += ball1Mult
    except IndexError: None
    try:
        if pos2[2] >= canvas.winfo_width() or pos2[0] <= 0:
            ball2['dx'] = -ball2['dx'] - ball2Mult
            ball2['dy'] += ball2Mult
        if pos2[3] >= canvas.winfo_height() or pos2[1] <= 0:
            ball2['dy'] = -ball2['dy'] - ball2Mult
            ball2['dx'] += ball2Mult
    except IndexError: None

    if (ball1['type'] == 'splitting' or ball2['type'] == 'splitting') and splits != []:
        for num, var in enumerate(splits):
            if var[1][2] <= 0:
                try:
                    canvas.delete(var[0])
                    splits.pop(num)
                except: None
                continue
            var[1][2] += ran.uniform(0.0,0.05)
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
                    ball2depletion = 2.5*(ran.uniform(0.05,2.5))*((frm/1200)+1)
                    tempdepletion = ball2['damage']*(ran.uniform(0.05,2.5))*((frm/1200)+1)
                    var[1][2] -= tempdepletion
                    ball2['hp'] -= ball2depletion

                    var[1][0] = -var[1][0]
                    var[1][1] = -var[1][1]
                    ball2['dx'] = -ball2['dx']
                    ball2['dy'] = -ball2['dy']

                    var[1][2] = var[1][2] / 2
                    if var[1][2] <= 0:
                        canvas.delete(var[0])
                    splits.append([canvas.create_oval(tempPos[0], tempPos[1], tempPos[2], tempPos[3], fill='red'),[-var[1][0],-var[1][1],var[1][2]]])

                    if ball2['type'] == 'duo':
                        if (tempPos[2] >= duoAttkPos[0] and tempPos[0] <= duoAttkPos[2] and tempPos[3] >= duoAttkPos[1] and tempPos[1] <= duoAttkPos[3]):
                            tempdepletion = 10*(ran.uniform(0.05,2.5))*((frm/1200)+1)
                            var[1][2] -= tempdepletion
    
                            var[1][0] = -var[1][0]
                            var[1][1] = -var[1][1]
                            ball2['edx'] = -ball2['edx']
                            ball2['edy'] = -ball2['edy']
    
                            var[1][2] = var[1][2] / 2
                            if var[1][2] <= 0:
                                canvas.delete(var[0])
                            splits.append([canvas.create_oval(tempPos[0], tempPos[1], tempPos[2], tempPos[3], fill='blue'),[-var[1][0],-var[1][1],var[1][2]]])

            elif ball2['type'] == 'splitting':
                if (tempPos[2] >= pos1[0] and tempPos[0] <= pos1[2] and tempPos[3] >= pos1[1] and tempPos[1] <= pos1[3]):
                    ball1depletion = 2.5*(ran.uniform(0.05,2.5))*((frm/1200)+1)
                    tempdepletion = ball1['damage']*(ran.uniform(0.05,2.5))*((frm/1200)+1)
                    var[1][2] -= tempdepletion
                    ball1['hp'] -= ball1depletion

                    var[1][0] = -var[1][0]
                    var[1][1] = -var[1][1]
                    ball1['dx'] = -ball1['dx']
                    ball1['dy'] = -ball1['dy']

                    var[1][2] = var[1][2] / 2
                    if var[1][2] <= 0:
                        canvas.delete(var[0])
                    splits.append([canvas.create_oval(tempPos[0], tempPos[1], tempPos[2], tempPos[3], fill='blue'),[-var[1][0],-var[1][1],var[1][2]]])

                if ball1['type'] == 'duo':
                    if (tempPos[2] >= duoAttkPos[0] and tempPos[0] <= duoAttkPos[2] and tempPos[3] >= duoAttkPos[1] and tempPos[1] <= duoAttkPos[3]):
                        tempdepletion = 10*(ran.uniform(0.05,2.5))*((frm/1200)+1)
                        var[1][2] -= tempdepletion

                        var[1][0] = -var[1][0]
                        var[1][1] = -var[1][1]
                        ball1['edx'] = -ball1['edx']
                        ball1['edy'] = -ball1['edy']

                        var[1][2] = var[1][2] / 2
                        if var[1][2] <= 0:
                            canvas.delete(var[0])
                        splits.append([canvas.create_oval(tempPos[0], tempPos[1], tempPos[2], tempPos[3], fill='red'),[-var[1][0],-var[1][1],var[1][2]]])

            if var[1][2] > 175:
                var[1][2] = 175

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
    elif ball2['type'] == 'duo':
        canvas.move(ball2['extshape'],ball2['edx'],ball2['edy'])
        duoAttkPos = canvas.coords(ball2['extshape'])
        tempMult = ran.uniform(-0.5,0.5)
        if duoAttkPos[2] >= canvas.winfo_width() or duoAttkPos[0] <= 0:
            ball2['edx'] = -ball2['edx'] - tempMult
            ball2['edy'] += tempMult
        if duoAttkPos[3] >= canvas.winfo_height() or duoAttkPos[1] <= 0:
            ball2['edy'] = -ball2['edy'] - tempMult
            ball2['edx'] += tempMult



    pos1 = canvas.coords(ball1['shape'])
    pos2 = canvas.coords(ball2['shape'])
    try:
        if (pos1[2] >= pos2[0] and pos1[0] <= pos2[2] and pos1[3] >= pos2[1] and pos1[1] <= pos2[3]):
            ball2depletion = ball1['damage']*(ran.uniform(0.05,2.5))*((frm/1200)+1)
            ball1depletion = ball2['damage']*(ran.uniform(0.05,2.5))*((frm/1200)+1)
            ball1['hp'] -= ball1depletion
            ball2['hp'] -= ball2depletion

            if ball1['type'] == 'vampire':
                ball1['hp'] += (0.25*ball2depletion)
            elif ball2['type'] == 'vampire':
                ball2['hp'] += (0.25*ball1depletion)

            if ball1['type'] == 'splitting':
                ball1['hp'] = ball1['hp'] / 2
                if ball1['hp'] <= 0:
                    canvas.delete(ball1['shape'])
                splits.append([canvas.create_oval(pos1[0], pos1[1], pos1[2], pos1[3], fill='red'),[-ball1['dx'],-ball1['dy'],ball1['hp']]])
            if ball2['type'] == 'splitting':
                ball2['hp'] = ball2['hp'] / 2
                if ball2['hp'] <= 0:
                    canvas.delete(ball2['shape'])
                splits.append([canvas.create_oval(pos2[0], pos2[1], pos2[2], pos2[3], fill='blue'),[-ball2['dx'],-ball2['dy'],ball2['hp']]])

            ball1['dx'] = -ball1['dx']
            ball1['dy'] = -ball1['dy']
            ball2['dx'] = -ball2['dx']
            ball2['dy'] = -ball2['dy']

        if ball1['type'] == 'duo':
            if (pos2[2] >= duoAttkPos[0] and pos2[0] <= duoAttkPos[2] and pos2[3] >= duoAttkPos[1] and pos2[1] <= duoAttkPos[3]):
                ball2depletion = 10*(ran.uniform(0.05,2.5))*((frm/1200)+1)
                ball2['hp'] -= ball2depletion

                if ball2['type'] == 'splitting':
                    ball2['hp'] = ball2['hp'] / 2
                    if ball2['hp'] <= 0:
                        canvas.delete(ball2['shape'])
                    splits.append([canvas.create_oval(pos2[0], pos2[1], pos2[2], pos2[3], fill='blue'),[-ball2['dx'],-ball2['dy'],ball2['hp']]])

                ball2['dx'] = -ball2['dx']
                ball2['dy'] = -ball2['dy']
                ball1['edx'] = -ball1['edx']
                ball1['edy'] = -ball1['edy']

        elif ball2['type'] == 'duo':
            if (pos1[2] >= duoAttkPos[0] and pos1[0] <= duoAttkPos[2] and pos1[3] >= duoAttkPos[1] and pos1[1] <= duoAttkPos[3]):
                ball1depletion = 10*(ran.uniform(0.05,2.5))*((frm/1200)+1)
                ball1['hp'] -= ball1depletion
        
                if ball1['type'] == 'splitting':
                    ball1['hp'] = ball1['hp'] / 2
                    if ball1['hp'] <= 0:
                        canvas.delete(ball1['shape'])
                    splits.append([canvas.create_oval(pos1[0], pos1[1], pos1[2], pos1[3], fill='red'),[-ball1['dx'],-ball1['dy'],ball1['hp']]])
        
                ball1['dx'] = -ball1['dx']
                ball1['dy'] = -ball1['dy']
                ball2['edx'] = -ball2['edx']
                ball2['edy'] = -ball2['edy']
    except IndexError: None


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



    if (ball1['hp'] <= 0) and (splits == [] or (ball1['type'] != 'splitting' or ball2['type'] == 'splitting')) and (ball2['hp'] <= 0) and (
    splits == [] or (ball2['type'] != 'splitting' or ball1['type'] == 'splitting')):
        winner = "draw"
        canvas.delete('all')
        checkforwinner(winner)
    elif (ball1['hp'] <= 0) and (splits == [] or (ball1['type'] != 'splitting' or ball2['type'] == 'splitting')):
        winner = "ball2"
        healthbar1.configure(text=f'0/{ball1["max hp"]}')
        canvas.delete('all')
        checkforwinner(winner)
    elif (ball2['hp'] <= 0) and (splits == [] or (ball2['type'] != 'splitting' or ball1['type'] == 'splitting')):
        winner = "ball1"
        healthbar2.configure(text=f'0/{ball2["max hp"]}')
        canvas.delete('all')
        checkforwinner(winner)
    else:
        root.after(16, lambda: frame(canvas, root, ball1, ball2, healthbar1, healthbar2, winner, checkforwinner, frm, dmg, splits=splits))