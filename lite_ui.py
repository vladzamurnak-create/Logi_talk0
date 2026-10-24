import threading
from socket import *
from customtkinter import *


class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.label = None

        self.menu_frame = CTkFrame(self, width=30, height=300)
        self.menu_frame.pack_propagate(False)
        self.menu_frame.place(x=0, y=0)
        self.is.show_menu = False
        self.speed_animate_menu = -5
        self.btn = CTkButton(self, text='',
        command=self.toggle_show_menu, width=30)
        self.btn.place(x=0, y=0)

        self.chat_field = CTkTextbox(self, font=('Arial', 14, 'bold'), state='disable')
        self.chat_field.place(x=0, y=0)
        self.message_entry = CTkEntry(self, placeholder_text='Введіть повідомлення:', height=40)
        self.message_entry.place(x=0, y=0)
        self.send_button = CTkButton(self, text='>', width=50, height=40, command=self.send_message)
        self.send_button.place(x=0, y=0)

        self.username = 'Vlad'
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect(('localhost', 8000))
