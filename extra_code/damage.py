import random as ran

def dmg(canvas, splits, frm, o1, o1t, o1d, o1dx, o1dy, o1hp, o2, o2d, o2t, o2dx, o2dy, o2hp):
    o1depletion = o2d*(ran.uniform(0.05,2.5))*((frm/1200)+1)
    o2depletion = o1d*(ran.uniform(0.05,2.5))*((frm/1200)+1)
    o1hp -= o1depletion
    o2hp -= o2depletion

    if o1t == 'splitting':
        tempPos = canvas.coords(o1)
        o1hp = o1hp / 2
        if o1hp <= 0:
            canvas.delete(o1)
        splits.append([canvas.create_oval(tempPos[0], tempPos[1], tempPos[2], tempPos[3], fill='red'),[-o1dx,-o1dy,o1hp]])
    elif o2t == 'splitting':
        tempPos = canvas.coords(o2)
        o2hp = o2hp / 2
        if o2hp <= 0:
            canvas.delete(o2)
        splits.append([canvas.create_oval(tempPos[0], tempPos[1], tempPos[2], tempPos[3], fill='blue'),[-o2dx,-o2dy,o2hp]])


    o1dx = -o1dx
    o1dy = -o1dy
    o2dx = -o2dx
    o2dx = -o2dy