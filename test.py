import tkinter as tk
import time
import threading
root = tk.Tk()
import os
root.title('my window')
root.geometry('200x150')

def button_event():
    os.system("powershell.exe Get-Process")  
    mybutton.config(text='complete') 
    after_thread.start()

def run_after_completion():
    time.sleep(3)  
    mybutton.config(text="run cmd")  

mybutton = tk.Button(root, text='run cmd', command=button_event)
mybutton.pack()


after_thread = threading.Thread(target=run_after_completion)

root.mainloop()