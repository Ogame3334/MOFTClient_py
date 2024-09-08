from tkinter import Tk, Text, Label, Button, constants
from tkinter.ttk import Frame
from scenes.main_scene import MainScene
from scenes.error import ErrorScreen
from functions.others.ogm import error_output
from functions.others.system_finish import SystemInterruption

from classes.OSCClient import OSCClient
from classes.WSClient import WSClient

from time import sleep

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title('MOFTClient')
        self.root.geometry('1280x720')
        self.root.resizable(False, False)
        self.root.iconbitmap(default='.\\moft.ico')
        # self.root.protocol("WM_DELETE_WINDOW", lambda: SystemInterruption(self.root).click_close())

        self.osc_client = OSCClient()

        self.ws_client = WSClient()
        self.ws_client.set_on_message(lambda ws, message: print(message))

        self.is_running = False

    def __osc_run(self, ip: str, port: int):
        self.osc_client.run(ip, port)

    def __send_jump(self):
        self.osc_client.send("/input/Jump", 1)
        sleep(1)
        self.osc_client.send("/input/Jump", 0)

    def __send_alarm(self, i: int):
        self.osc_client.send("/avatar/parameters/Internal_" + str(i), True)
        sleep(1)
        self.osc_client.send("/avatar/parameters/Internal_" + str(i), False)

    def run(self):
        # MainScene(self.root, now_scene=None).make()

        # frame = Frame(self.root)
        # frame.place(width=640, height=720)

        label_title = Label(self.root, text='MOFT', font=('Arial', 40))
        label_title.place(relx=0.5, rely=0.1, anchor=constants.CENTER)

        label_osc_ip = Label(self.root, text='IPアドレス', font=('Arial', 20))
        label_osc_ip.place(relx=0.2, rely=0.2, anchor=constants.E)
        textbox_osc_ip = Text(self.root, font=('Arial', 20), height=1, width=30)
        textbox_osc_ip.insert('1.0', '127.0.0.1')
        textbox_osc_ip.place(relx=0.21, rely=0.2, anchor=constants.W)

        label_osc_port = Label(self.root, text='PORT番号', font=('Arial', 20))
        label_osc_port.place(relx=0.2, rely=0.3, anchor=constants.E)
        textbox_osc_port = Text(self.root, font=('Arial', 20), height=1, width=30)
        textbox_osc_port.insert('1.0', '9000')
        textbox_osc_port.place(relx=0.21, rely=0.3, anchor=constants.W)

        button = Button(
            self.root, 
            text='開始', 
            font=('Arial', 20),
            command=lambda: self.__osc_run(textbox_osc_ip.get(0., constants.END).replace('\n', ''), int(textbox_osc_port.get(0., constants.END).replace('\n', '')))
        )
        button.place(relx=0.5, rely=0.9, anchor=constants.CENTER)
        internal2_button = Button(
            self.root, 
            text='Internal 0', 
            font=('Arial', 20),
            command=lambda: self.__send_alarm(0)
        )
        internal2_button.place(relx=0.9, rely=0.2, anchor=constants.CENTER)
        internal3_button = Button(
            self.root, 
            text='Internal 1', 
            font=('Arial', 20),
            command=lambda: self.__send_alarm(1)
        )
        internal3_button.place(relx=0.9, rely=0.3, anchor=constants.CENTER)
        internal4_button = Button(
            self.root, 
            text='Internal 2', 
            font=('Arial', 20),
            command=lambda: self.__send_alarm(2)
        )
        internal4_button.place(relx=0.9, rely=0.4, anchor=constants.CENTER)
        internal5_button = Button(
            self.root, 
            text='Internal 3', 
            font=('Arial', 20),
            command=lambda: self.__send_alarm(3)
        )
        internal5_button.place(relx=0.9, rely=0.5, anchor=constants.CENTER)
        internal6_button = Button(
            self.root, 
            text='Internal 4', 
            font=('Arial', 20),
            command=lambda: self.__send_alarm(4)
        )
        internal6_button.place(relx=0.9, rely=0.6, anchor=constants.CENTER)
        internal7_button = Button(
            self.root, 
            text='Internal 5', 
            font=('Arial', 20),
            command=lambda: self.__send_alarm(5)
        )
        internal7_button.place(relx=0.9, rely=0.7, anchor=constants.CENTER)
        # # internal_buttons = []
        # for i in range(2, 8):
        #     button = Button(
        #         self.root,
        #         text="Internal" + str(i),
        #         font=('Arial', 20),
        #         command=lambda: self.__send_alarm(i)
        #     )
        #     button.place(relx=0.9, rely=i/10, anchor=constants.CENTER)
        temp_button = Button(
            self.root, 
            text='ジャンプ', 
            font=('Arial', 20),
            command=lambda: self.__send_jump()
        )
        temp_button.place(relx=0.7, rely=0.9, anchor=constants.CENTER)

        # text = Text(frame)
        # text.place(x=10, y=10, width=230, height=130)

        # self.ws_client.run('wss://api-realtime-sandbox.p2pquake.net/v2/ws')
        self.is_running = True

        self.root.mainloop()

        return True
    
if __name__ == '__main__':
    main_progress = Main()
    try:
        main_progress.run()
    except:
        error_text = error_output()
        ErrorScreen.output(main_progress.root, error_text)
    