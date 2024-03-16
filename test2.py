import os
import tkinter as tk
import time
import threading
import subprocess
from tkinter import ttk

root = tk.Tk()
root.title('Windows Server Setup')
root.geometry('500x500')
def powershell(command):
    subprocess.run(["powershell.exe", command])

def DHCP_Install_Click():
    DHCP_install_thread = threading.Thread(target=installing_DHCP)
    DHCP_install_thread.start()
    DHCP_Install.config(text='Installing')

def installing_DHCP():
    code="powershell.exe Install-WindowsFeature -Name 'DHCP' –IncludeManagementTools"
    powershell(code)
    DHCP_complete_thread = threading.Thread(target=Func_DHCP_complete)
    DHCP_complete_thread.start()


def Func_DHCP_complete():
    DHCP_Install.config(text="Finished")  
    time.sleep(3)
    DHCP_Install.config(text="Install DHCP Feature")
def aaaaa():
    print(aaa.get())
DHCP_Install = tk.Button(root, text='Install DHCP Feature', command=DHCP_Install_Click)
DHCP_Install.pack()
aaa=ttk.Combobox(root,values=["January", "February", "March", "April"])
aaa.pack()
aaa_Install = tk.Button(root, text='Install DHCP Feature', command=aaaaa)
aaa_Install.pack()
root.mainloop()