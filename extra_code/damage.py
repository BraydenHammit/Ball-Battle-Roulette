import random as ran

def dmg(canvas, splits, frm, o1, o1t, o1d, o1dx, o1dy, o1hp, o2, o2t, o2d, o2dx, o2dy, o2hp, splitNum=None, duoAttk=None, sentryProj=None, sentryBase=None):
    o1depletion = o2d*(ran.uniform(0.05,2.5))*((frm/1200)+1)
    o2depletion = o1d*(ran.uniform(0.05,2.5))*((frm/1200)+1)
    if o1t == 'zombie' and ((o2t != 'duo') or (duoAttk == 2)):
        o1hp -= 1
    elif duoAttk != 1 and sentryProj != 1 and (o2t != 'duo' or duoAttk == 2):
        o1hp -= o1depletion
    if o2t == 'zombie' and ((o1t != 'duo') or (duoAttk == 1)):
        o2hp -= 1
    elif duoAttk != 2 and sentryProj != 2 and (o1t != 'duo' or duoAttk == 1):
        o2hp -= o2depletion

    if o1t == 'vampire' and duoAttk != 2 and sentryProj != 2:
        o1hp += 0.25*o2depletion
    if o2t == 'vampire' and duoAttk != 1 and sentryProj != 1:
        o2hp += 0.25*o1depletion

    if o1t == 'splitting' and len(splits) <= 15:
        tempPos = canvas.coords(o1)
        if o1hp <= 0:
            canvas.delete(o1)
            if splitNum != None and 0 <= splitNum < len(splits):
                splits.pop(splitNum)
        else:
            o1hp = o1hp / 2
            splits.append([canvas.create_oval(tempPos[0], tempPos[1], tempPos[2], tempPos[3], fill='red'),[-o1dx,-o1dy,o1hp]])
    if o2t == 'splitting' and len(splits) <= 15:
        tempPos = canvas.coords(o2)
        if o2hp <= 0:
            canvas.delete(o2)
            if splitNum != None and 0 <= splitNum < len(splits):
                splits.pop(splitNum)
        else:
            o1hp = o1hp / 2
            splits.append([canvas.create_oval(tempPos[0], tempPos[1], tempPos[2], tempPos[3], fill='blue'),[-o2dx,-o2dy,o2hp]])


    if o1t == 'sentry' or o2t == 'sentry':
        if o1t == 'sentry':
            o2dx = -o2dx
            o2dy = -o2dy
            x = [ran.uniform(0.0,canvas.winfo_width()),ran.uniform(0.0,canvas.winfo_height())]
            y = [x[0] - 40, x[1] -40]
            canvas.coords(o1,x[0],x[1],y[0],y[1])
        if o2t == 'sentry':
            o1dx = -o1dx
            o1dy = -o1dy
            x = [ran.uniform(0.0,canvas.winfo_width()),ran.uniform(0.0,canvas.winfo_height())]
            y = [x[0] - 40, x[1] -40]
            canvas.coords(o2,x[0],x[1],y[0],y[1])
    else:
        try:
            pos1 = canvas.coords(o1)
            pos2 = canvas.coords(o2)
            dx = ((pos2[0] + pos2[1]) / 2) - ((pos1[0] + pos1[1]) / 2)
            dy = ((pos2[2] + pos2[3]) / 2) - ((pos1[2] + pos1[3]) / 2)
            preDir = [o1dx, o1dy, o2dx, o2dy]
            if ((o1dx * dx) + (o1dy * dy)) > 0:
                o1dx = preDir[2]
                o1dy = preDir[3]
            else:
                o1dx = -o1dx
                o1dy = -o1dy
            if ((o2dx * (-dx)) + (o2dy * (-dy))) > 0:
                o2dx = preDir[0]
                o2dy = preDir[1]
            else:
                o2dx = -o2dx
                o2dy = -o2dy
        except IndexError: None

    if sentryProj == 1:
        xy = canvas.coords(sentryBase)
        canvas.coords(o1,xy[0]+10,xy[1]+10,xy[2]-10,xy[3]-10)

    return splits, o1dx, o1dy, o1hp, o2dx, o2dy, o2hp