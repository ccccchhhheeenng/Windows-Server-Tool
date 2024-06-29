import tkinter as tk
import time
import threading
import subprocess
from tkinter import ttk

root = tk.Tk()
root.title('Windows Server Setup')
root.geometry('400x400')
current_interface = list()

def setup_main_interface():
  # DHCP_Install = ttk.Button(root, text='Install DHCP Feature', command=DHCP_Install_Click, style='Custom.TButton')
  # DHCP_Install.pack()
  # DHCP_Uninstall = ttk.Button(root, text='Uninstall DHCP Feature', command=DHCP_Uninstall_Click, style='Custom.TButton')
  # DHCP_Uninstall.pack()
  Setup_DHCP = ttk.Button(root, text="Setup DHCP", command=DHCP_Setup_Click, style='Custom.TButton')
  Setup_DHCP.pack()
def setup_dhcp_interface():
    StartRangelabel = tk.Label(root, text='StartRange:')
    StartRangelabel.grid(row=0, column=0)
    StartRangeentry = tk.Entry(root)
    StartRangeentry.grid(row=0, column=1)
    EndRangelabel = tk.Label(root, text='EndRange:')
    EndRangelabel.grid(row=1, column=0)
    EndRangeentry = tk.Entry(root)
    EndRangeentry.grid(row=1, column=1)
    SubnetMasklabel = tk.Label(root, text='SubnetMask:')
    SubnetMasklabel.grid(row=2, column=0)
    SubnetMaskentry = tk.Entry(root)
    SubnetMaskentry.grid(row=2, column=1)
    ScopeNamelabel = tk.Label(root, text='ScopeName:')
    ScopeNamelabel.grid(row=3, column=0)
    ScopeNameentry = tk.Entry(root)
    ScopeNameentry.grid(row=3, column=1)
    DNS_Addresslabel = tk.Label(root, text='DNS Address:')
    DNS_Addresslabel.grid(row=4, column=0)
    DNS_Addressentry = tk.Entry(root)
    DNS_Addressentry.grid(row=4, column=1)
    Routerlabel = tk.Label(root, text='Router IP:')
    Routerlabel.grid(row=5, column=0)
    Routerentry = tk.Entry(root)
    Routerentry.grid(row=5, column=1)
    Exit = ttk.Button(root, text="Back", command=back, style='Red.TButton')
    Exit.grid(row=6, column=0, padx=20)
def back():
  current_interface.pop()
  for widget in root.winfo_children():
    widget.destroy()
  setup_main_interface()
def DHCP_Setup_Click():
    global current_interface
    current_interface.append("DHCP")
    for widget in root.winfo_children():
        widget.destroy()
    setup_dhcp_interface()
setup_main_interface()
root.mainloop()