from tkinter import *
from tkinter import ttk

class ErrorScreen:
    def output(root: Tk, error_text: str) -> None:
        root.title('MOFTClient : Error')
        root.protocol("WM_DELETE_WINDOW", root.destroy)
        frame = ttk.Frame(root, width=1280, height=720)
        frame.propagate(False)
        frame.place(x=0, y=0)
        label = ttk.Label(frame, text=error_text, font=('Consolas', 10))
        label.place(x=0, y=0)
        root.mainloop()
