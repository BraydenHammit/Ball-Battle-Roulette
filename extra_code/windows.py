import tkinter as tk

class InternalWindow(tk.Frame):
    def __init__(self, parent, title, width=300, height=200, x=50, y=50, fncts=[]):
        super().__init__(parent, bg="#626262", bd=2, relief="groove")
        
        self.parent = parent
        self.place(x=x, y=y, width=width, height=height)
        
        self._title_bar(title)
        self._window_area()
        self._bindings()

    def _title_bar(self, title):
        self.title_bar = tk.Frame(self, bg="#3c3c3c", height=25)
        self.title_bar.pack(fill="x", side="top")
        title_label = tk.Label(self.title_bar, text=title, bg="#3c3c3c", fg="white", font=("Helvetica", 11, "bold"))
        title_label.pack(side="left", padx=8)
        close_btn = tk.Button(
            self.title_bar, text="✕", highlightbackground="#3c3c3c", fg="black", 
            bd=0, command=self.destroy, highlightthickness=0
        )
        close_btn.pack(side="right", padx=5)

    def _window_area(self):
        self.window = tk.Frame(self, bg="#626262")
        self.window.pack(fill="both", expand=True, padx=10, pady=10)
        if self.title == 'Shop':
            shop_setup(self)

    def _bindings(self):
        self.title_bar.bind("<Button-1>", self._sdrag)
        self.title_bar.bind("<B1-Motion>", self._drag)

    def _sdrag(self, event):
        self._drag_start_x = event.x
        self._drag_start_y = event.y

    def _drag(self, event):
        x = self.winfo_x() - self._drag_start_x + event.x
        y = self.winfo_y() - self._drag_start_y + event.y
        self.place(x=x, y=y)




#Shop Window Setup:
def shop_setup(shop):
    None