import random as ran

def create_balls(canvas, root):
    #Random Classes:
    ball1type = 0
    ball2type = 0
    tries = 0
    while (ball1type == ball2type) or ((ball1type == 'splitting' and ball2type == 'sentry') or (ball1type =='sentry' and ball2type == 'splitting')) or ((ball1type == 'ghost' and ball2type == 'sentry') or (ball1type =='sentry' and ball2type == 'ghost')) or ((ball1type == 'splitting' and ball2type == 'chaser') or (ball1type =='chaser' and ball2type == 'splitting')):
        tries += 1
        if tries >= 50:
            ball1type = 'default'
            ball2type = 'big'
        else:
            ball1type = ran.choice(['default','big','fast','hyperspeed','vampire','splitting','healer','duo','zombie','sentry','black hole','echo','chaser','ghost','looper','grower','atom'])      #Classes
            ball2type = ran.choice(['default','big','fast','hyperspeed','vampire','splitting','healer','duo','zombie','sentry','black hole','echo','chaser','ghost','looper','grower','atom'])



#---------------------------------------------------------------------------------------------------


    #Ball 1 Defining:
    if ball1type == 'default':
        temp_dx = ran.uniform(0.0, 10.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='red'),
            'hp': 100,
            'max hp': 100,
            'damage': 10,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'default'
        }
    elif ball1type == 'big':
        temp_dx = ran.uniform(0.0, 5.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 100, 100, fill='red'),
            'hp': 150,
            'max hp': 150,
            'damage': 7.5,
            'dx': temp_dx,
            'dy': 5 - temp_dx,
            'type': 'big'
        }
    elif ball1type == 'fast':
        temp_dx = ran.uniform(0.0, 25.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='red'),
            'hp': 75,
            'max hp': 75,
            'damage': 12,
            'dx': temp_dx,
            'dy': 25 - temp_dx,
            'type': 'fast'
        }
    elif ball1type == 'hyperspeed':
        temp_dx = ran.uniform(0.0, 25.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='red'),
            'hp': 50,
            'max hp': 50,
            'damage': 22.5,
            'dx': temp_dx,
            'dy': 25 - temp_dx,
            'type': 'hyperspeed'
        }
    elif ball1type == 'vampire':
        temp_dx = ran.uniform(0.0, 10.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='red'),
            'hp': 75,
            'max hp': 100,
            'damage': 10,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'vampire'
        }
    elif ball1type == 'splitting':
        temp_dx = ran.uniform(0.0, 10.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='red'),
            'hp': 175,
            'max hp': 175,
            'damage': 2.5,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'splitting'
        }
    elif ball1type == 'healer':
        temp_dx = ran.uniform(0.0, 10.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='red'),
            'hp': 50,
            'max hp': 50,
            'damage': 6.75,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'healer'
        }
    elif ball1type == 'duo':
        temp_dx = ran.uniform(0.0, 10.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='dark red'),
            'extshape': canvas.create_oval(10, 10, 50, 50, fill="#ff6464"),
            'hp': 100,
            'max hp': 100,
            'damage': 0,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'edx': temp_dx,
            'edy': 10 - temp_dx,
            'type': 'duo'
        }
    elif ball1type == 'zombie':
        temp_dx = ran.uniform(0.0, 10.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='red'),
            'hp': 5,
            'max hp': 5,
            'damage': 10,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'zombie'
        }
    elif ball1type == 'sentry':
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='red'),
            'extshape': canvas.create_oval(20, 20, 40, 40, fill='red'),
            'hp': 15,
            'max hp': 15,
            'damage': 0,
            'dx': 0,
            'dy': 0,
            'edx': 0,
            'edy': 0,
            'type': 'sentry'
        }
    elif ball1type == 'black hole':
        temp_dx = ran.uniform(0.0, 1.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 150, 150, fill="#1c0000"),
            'hp': 5,
            'max hp': 5,
            'damage': 1000000000000,
            'dx': temp_dx,
            'dy': 1 - temp_dx,
            'type': 'black hole'
        }
    elif ball1type == 'echo':
        temp_dx = ran.uniform(0.0, 10.0)
        ball1 = {
            'extshape': canvas.create_oval(10, 10, 50, 50, fill="black"),
            'shape': canvas.create_oval(10, 10, 50, 50, fill="red"),
            'prevpos': [10,10,50,50,temp_dx,10-temp_dx],
            'hp': 100,
            'max hp': 100,
            'damage': 7.5,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'timer': 0,
            'type': 'echo'
        }
    if ball1type == 'chaser':
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='red'),
            'hp': 100,
            'max hp': 100,
            'damage': 10,
            'dx': 0,
            'dy': 0,
            'type': 'chaser'
        }
    if ball1type == 'ghost':
        temp_dx = ran.uniform(0.0, 10.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='red'),
            'hp': 100,
            'max hp': 100,
            'damage': 10,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'ghost'
        }
    if ball1type == 'looper':
        temp_dx = ran.uniform(0.0, 10.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='red'),
            'hp': 100,
            'max hp': 100,
            'damage': 10,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'looper'
        }
    if ball1type == 'grower':
        temp_dx = ran.uniform(0.0, 10.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 40, 40, fill='red'),
            'hp': 75,
            'max hp': 75,
            'damage': 7.5,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'grower'
        }
    if ball1type == 'atom':
        temp_dx = ran.uniform(0.0, 10.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 11, 11, fill='red'),
            'hp': 1,
            'max hp': 1,
            'damage': 0,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'timer': 240,
            'type': 'atom'
        }



#---------------------------------------------------------------------------------------------------


    #Ball 2 Defining:
    if ball2type == 'default':
        temp_dx = ran.uniform(0.0, 10.0)
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='blue'),
            'hp': 100,
            'max hp': 100,
            'damage': 10,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'default'
        }
    elif ball2type == 'big':
        temp_dx = ran.uniform(0.0, 5.0)
        ball2 = {
            'shape': canvas.create_oval(800, 500, 890, 590, fill='blue'),
            'hp': 150,
            'max hp': 150,
            'damage': 7.5,
            'dx': temp_dx,
            'dy': 5 - temp_dx,
            'type': 'big'
        }
    elif ball2type == 'fast':
        temp_dx = ran.uniform(0.0, 25.0)
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='blue'),
            'hp': 75,
            'max hp': 75,
            'damage': 12,
            'dx': temp_dx,
            'dy': 25 - temp_dx,
            'type': 'fast'
        }
    elif ball2type == 'hyperspeed':
        temp_dx = ran.uniform(0.0, 25.0)
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='blue'),
            'hp': 50,
            'max hp': 50,
            'damage': 22.5,
            'dx': temp_dx,
            'dy': 25 - temp_dx,
            'type': 'hyperspeed'
        }
    elif ball2type == 'vampire':
        temp_dx = ran.uniform(0.0, 10.0)
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='blue'),
            'hp': 75,
            'max hp': 100,
            'damage': 10,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'vampire'
        }
    elif ball2type == 'splitting':
        temp_dx = ran.uniform(0.0, 10.0)
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='blue'),
            'hp': 175,
            'max hp': 175,
            'damage': 2.5,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'splitting'
        }
    elif ball2type == 'healer':
        temp_dx = ran.uniform(0.0, 10.0)
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='blue'),
            'hp': 50,
            'max hp': 50,
            'damage': 6.75,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'healer'
        }
    elif ball2type == 'duo':
        temp_dx = ran.uniform(0.0, 10.0)
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='navy'),
            'extshape': canvas.create_oval(850, 550, 890, 590, fill='cyan'),
            'hp': 100,
            'max hp': 100,
            'damage': 0,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'edx': temp_dx,
            'edy': 10 - temp_dx,
            'type': 'duo'
        }
    elif ball2type == 'zombie':
        temp_dx = ran.uniform(0.0, 10.0)
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='blue'),
            'hp': 10,
            'max hp': 5,
            'damage': 5,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'zombie'
        }
    elif ball2type == 'sentry':
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='blue'),
            'extshape': canvas.create_oval(860, 560, 880, 580, fill='blue'),
            'hp': 15,
            'max hp': 15,
            'damage': 0,
            'dx': 0,
            'dy': 0,
            'edx': 0,
            'edy': 0,
            'type': 'sentry'
        }
    elif ball2type == 'black hole':
        temp_dx = ran.uniform(0.0, 1.0)
        ball2 = {
            'shape': canvas.create_oval(750, 450, 890, 590, fill="#00071c"),
            'hp': 5,
            'max hp': 5,
            'damage': 1000000000000,
            'dx': temp_dx,
            'dy': 1 - temp_dx,
            'type': 'black hole'
        }
    elif ball2type == 'echo':
        temp_dx = ran.uniform(0.0, 10.0)
        ball2 = {
            'extshape': canvas.create_oval(850, 550, 890, 590, fill="black"),
            'shape': canvas.create_oval(850, 550, 890, 590, fill="blue"),
            'prevpos': [850, 550, 890, 590, temp_dx, 10-temp_dx],
            'hp': 100,
            'max hp': 100,
            'damage': 7.5,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'timer': 0,
            'type': 'echo'
        }
    if ball2type == 'chaser':
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='blue'),
            'hp': 100,
            'max hp': 100,
            'damage': 10,
            'dx': 0,
            'dy': 0,
            'type': 'chaser'
        }
    if ball2type == 'ghost':
        temp_dx = ran.uniform(0.0, 10.0)
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='blue'),
            'hp': 100,
            'max hp': 100,
            'damage': 10,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'ghost'
        }
    if ball2type == 'looper':
        temp_dx = ran.uniform(0.0, 10.0)
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='blue'),
            'hp': 100,
            'max hp': 100,
            'damage': 10,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'looper'
        }
    if ball2type == 'grower':
        temp_dx = ran.uniform(0.0, 10.0)
        ball2 = {
            'shape': canvas.create_oval(860, 560, 890, 590, fill='blue'),
            'hp': 75,
            'max hp': 75,
            'damage': 7.5,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'grower'
        }
    if ball2type == 'atom':
        temp_dx = ran.uniform(0.0, 10.0)
        ball2 = {
            'shape': canvas.create_oval(889, 589, 890, 590, fill='blue'),
            'hp': 1,
            'max hp': 1,
            'damage': 0,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'timer': 240,
            'type': 'atom'
        }



    
    return ball1, ball2
