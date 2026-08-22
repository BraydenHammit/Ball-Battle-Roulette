import tkinter as tk

class toolTip:
    def __init__(self, object, text):
        self.object = object
        self.text = text
        self.tooltip = None
        
        self.object.bind("<Enter>", self.show)
        self.object.bind("<Leave>", self.hide)

    def show(self, event=None):
        if self.tooltip or not self.text:
            return
        x = self.object.winfo_rootx() + 20
        y = self.object.winfo_rooty() + self.object.winfo_height() + 5
        self.tooltip = tk.Toplevel(self.object)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        
        self.label = tk.Label(self.tooltip, text=self.text, justify=tk.LEFT, background="#4A4A4A", relief=tk.SOLID, borderwidth=1, font=("Arial", "9", "normal"))
        self.label.pack(ipadx=4, ipady=2)

    def hide(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

def stats(type):
    if type == 'default':
        text = 'HP: 100, Damage: 10, Velocity: 10,\nSpecial: N/A'
    elif type == 'big':
        text = 'HP: 150, Damage: 7.5, Velocity: 5,\nSpecial: Double Size Circle'
    elif type == 'fast':
        text = 'HP: 75, Damage: 12, Velocity: 25,\nSpecial: N/A'
    elif type == 'hyperspeed':
        text = 'HP: 25, Damage: 20, Velocity: 100,\nSpecial: N/A'
    elif type == 'vampire':
        text = 'HP: 100, Damage: 10, Velocity: 10,\nSpecial: Spawn at 75 Health, Lifesteal 25% of Damage.'
    elif type == 'splitting':
        text = 'HP: 175, Damage: 2.5, Velocity:10,\nSpecial: Splits in Two Every Hit'
    elif type == 'healer':
        text = 'HP: 30, Damage: 6.75, Velocity:10,\nSpecial: 5x Passive Regen Speed'
    elif type == 'duo':
        text = 'HP: 100, Damage: 10, Velocity: 10,\nSpecial: One Attacking Ball With Infinite Health\n& One Defensive Ball That Deals No Damage\nLighter Color is Attack, Darker is Defense'
    return text