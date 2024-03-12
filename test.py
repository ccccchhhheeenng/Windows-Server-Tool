import tkinter as tk
import time
import threading
root = tk.Tk()
import os
root.title('my window')
root.geometry('200x150')
#-----<DHCP>-----
def DHCP_Install_Click():
    DHCP_install_thread = threading.Thread(target=installing_DHCP)
    DHCP_install_thread.start()
    DHCP_Install.config(text='installing')

def installing_DHCP():
    os.system("powershell.exe Install-WindowsFeature -Name 'DHCP' –IncludeManagementTools")
    DHCP_complete_thread = threading.Thread(target=Func_DHCP_complete)
    DHCP_complete_thread.start()


def Func_DHCP_complete():
    time.sleep(3)  
    DHCP_Install.config(text="Finished")  
    time.sleep(3)
    DHCP_Install.config(text="Install DHCP Feature")  

DHCP_Install = tk.Button(root, text='Install DHCP Feature', command=DHCP_Install_Click)
DHCP_Install.pack()

#----</DHCP>-----

root.mainloop()