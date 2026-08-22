import random as ran

def dmg(canvas, splits, frm, o1, o1t, o1d, o1dx, o1dy, o1hp, o2, o2t, o2d, o2dx, o2dy, o2hp, num=None, duoAttk=None):
    o1depletion = o2d*(ran.uniform(0.05,2.5))*((frm/1200)+1)
    o2depletion = o1d*(ran.uniform(0.05,2.5))*((frm/1200)+1)
    if duoAttk != 1 and o1t == 'zombie':
        o1hp -= 1
    elif duoAttk != 1:
        o1hp -= o1depletion
    if duoAttk != 2 and o2t == 'zombie':
        o2hp -= 1
    elif duoAttk != 2:
        o2hp -= o2depletion

    if o1t == 'vampire' and duoAttk != 2:
        o2hp += 0.25*o2depletion
    elif o1t == 'vampire' and duoAttk != 1:
        o2hp += 0.25*o1depletion

    if o1t == 'splitting':
        tempPos = canvas.coords(o1)
        o1hp = o1hp / 2
        if o1hp <= 0:
            canvas.delete(o1)
            if num != None:
                splits.pop(num)
        splits.append([canvas.create_oval(tempPos[0], tempPos[1], tempPos[2], tempPos[3], fill='red'),[-o1dx,-o1dy,o1hp]])
    elif o2t == 'splitting':
        tempPos = canvas.coords(o2)
        o2hp = o2hp / 2
        if o2hp <= 0:
            canvas.delete(o2)
            if num != None:
                splits.pop(num)
        splits.append([canvas.create_oval(tempPos[0], tempPos[1], tempPos[2], tempPos[3], fill='blue'),[-o2dx,-o2dy,o2hp]])


    o1dx = -o1dx
    o1dy = -o1dy
    o2dx = -o2dx
    o2dy = -o2dy

    return splits, o1dx, o1dy, o1hp, o2dx, o2dy, o2hp