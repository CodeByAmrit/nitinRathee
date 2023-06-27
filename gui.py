from customtkinter import *
from alexa2 import *
from tkinter import PhotoImage


def gui():
    win = CTk()

    win.geometry("300x300")
    win.title("Alexa")
    img = PhotoImage(file="alexalogo.png")
    Btn1 = CTkButton(master=win, 
                    image=img, 
                    height=100,
                    text="",
                    width=100,
                    command=start
                    )
    Btn1.pack(padx=20, pady=80)

    win.mainloop()

def start():
    
    process1 = Process(target=run1)  
    process1.start()




if __name__ == "__main__":
    GUI = Process(target=gui)  
    GUI.start() 

    

