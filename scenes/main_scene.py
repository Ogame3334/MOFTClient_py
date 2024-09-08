from tkinter import *
from tkinter import ttk


class MainScene:
    def __init__(self, root: Tk, now_scene: Frame) -> None:
        self.root = root
        self.now_scene = now_scene

    def make(self) -> None:
        #destroyメソッドだとエラーが出るのでNoneにした
        if self.now_scene != None:
            self.now_scene = None

        self.now_scene = ttk.Frame(self.root)
        self.now_scene.place(width=1280, height=720)
        
        label_title = ttk.Label(self.now_scene, text='PrimeFactorizationGame', font=('Arial', 40))
        width, height = self.now_scene.size()
        print(width)
        label_title.place(relx=0.5, rely=0.1, anchor=CENTER)

        # MenuButton(self.root, self.now_scene, self.config).create(TITLE, [button_next_scene])
