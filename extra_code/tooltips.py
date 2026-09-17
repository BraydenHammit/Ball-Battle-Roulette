import tkinter as tk

#Class:
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



#Class Tooltip Text:
def stats(t):
    if t == 'default':
        text = 'HP: 100, Damage: 10, Velocity: 10,\nSpecial: N/A'
    elif t == 'big':
        text = 'HP: 150, Damage: 7.5, Velocity: 5,\nSpecial: Double Size Circle'
    elif t == 'fast':
        text = 'HP: 75, Damage: 12, Velocity: 25,\nSpecial: N/A'
    elif t == 'hyperspeed':
        text = 'HP: 25, Damage: 22.5, Velocity: 25,\nSpecial: Speeds Up After Every Wall Bounce'
    elif t == 'vampire':
        text = 'HP: 100, Damage: 10, Velocity: 10,\nSpecial: Spawn at 75 Health, Lifesteal 25% of Damage.'
    elif t == 'splitting':
        text = 'HP: 175, Damage: 2.5, Velocity:10,\nSpecial: Splits in Two Every Hit'
    elif t == 'healer':
        text = 'HP: 50, Damage: 6.75, Velocity:10,\nSpecial: 5x Passive Regen Speed'
    elif t == 'duo':
        text = 'HP: 100, Damage: 10, Velocity: 10,\nSpecial: One Attacking Ball With Infinite Health\n& One Defensive Ball That Deals No Damage\nLighter Color is Attack, Darker is Defense'
    elif t == 'zombie':
        text = 'HP: 5, Damage: 10, Velocity: 10,\nSpecial: Always Takes 1 Damage,\nBut Cannot Regen'
    elif t == 'sentry':
        text = 'HP: 15, Damage: 3, Velocity: 0,\nSpecial: Stationary, Teleports When Hit, Shoots Projectiles'
    elif t == 'black hole':
        text = 'HP: 5, Damage: ∞, Velocity: 1,\nSpecial: Immune To Damage,\nSlowly Loses Health,\nLarger & Darker Circle'
    elif t == 'echo':
        text = 'HP: 100, Damage: 7.5, Velocity: 10,\nSpecial: Rewinds To Echo When Hit,\nSets Echo Every 5 Seconds,\nDouble Damage For 1 Second After Echo'
    elif t == 'chaser':
        text = 'HP: 100, Damage: 10, Velocity: 10,\nSpecial: Moves Directly To Other Ball'
    elif t == 'ghost':
        text = 'HP: 100, Damage: 10, Velocity: 10,\nSpecial: Invincible For 3 Seconds\nWhen Hit'
    elif t == 'looper':
        text = 'HP: 100, Damage: 10, Velocity: 10,\nSpecial: Loops To Other Side Of Arena'
    elif t == 'grower':
        text = 'HP: 75, Damage: 7.5, Velocity: 10,\nHP, Damage, and Size Increase Over Time'
    return text