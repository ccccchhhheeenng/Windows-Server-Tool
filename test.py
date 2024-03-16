import asyncio
import os
import tkinter as tk
import time

async def DHCP_Install_Click():
    await installing_DHCP()

async def installing_DHCP():
    os.system("powershell.exe Install-WindowsFeature -Name 'DHCP' –IncludeManagementTools")
    await Func_DHCP_complete()

async def Func_DHCP_complete():
    DHCP_Install.config(text="Finished")
    await asyncio.sleep(3)
    DHCP_Install.config(text="Install DHCP Feature")

root = tk.Tk()
DHCP_Install = tk.Button(root, text='Install DHCP Feature', command=DHCP_Install_Click)
DHCP_Install.pack()
root.mainloop()
