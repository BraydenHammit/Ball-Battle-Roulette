import random as ran

def create_balls(canvas, root):
    ball1type = 0
    ball2type = 0
    while ball1type == ball2type:
        ball1type = ran.choice(['default', 'big', 'fast', 'hyperspeed', 'vampire','splitting','healer','duo','zombie'])
        ball2type = ran.choice(['default', 'big', 'fast', 'hyperspeed', 'vampire','splitting','healer','duo','zombie'])







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
        temp_dx = ran.uniform(0.0, 100.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='red'),
            'hp': 25,
            'max hp': 25,
            'damage': 20,
            'dx': temp_dx,
            'dy': 100 - temp_dx,
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
            'hp': 30,
            'max hp': 30,
            'damage': 6.75,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'healer'
        }
    elif ball1type == 'duo':
        temp_dx = ran.uniform(0.0, 10.0)
        ball1 = {
            'shape': canvas.create_oval(10, 10, 50, 50, fill='dark red'),
            'extshape': canvas.create_oval(10, 10, 50, 50, fill='pink'),
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
            'hp': 10,
            'max hp': 10,
            'damage': 15,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'zombie'
        }







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
        temp_dx = ran.uniform(0.0, 100.0)
        ball2 = {
            'shape': canvas.create_oval(850, 550, 890, 590, fill='blue'),
            'hp': 25,
            'max hp': 25,
            'damage': 20,
            'dx': temp_dx,
            'dy': 100 - temp_dx,
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
            'hp': 30,
            'max hp': 30,
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
            'max hp': 10,
            'damage': 15,
            'dx': temp_dx,
            'dy': 10 - temp_dx,
            'type': 'zombie'
        }


    
    return ball1, ball2
