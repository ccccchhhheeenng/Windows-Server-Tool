import tkinter as tk
import time
import threading
import os

root = tk.Tk()
root.title('Windows Server Setup')
root.geometry('500x500')

#-----<DHCP>-----

    #-----<DHCP_Install>-----
def DHCP_Install_Click():
    DHCP_install_thread = threading.Thread(target=installing_DHCP)
    DHCP_install_thread.start()
    DHCP_Install.config(text='Installing')

def installing_DHCP():
    os.system("powershell.exe Install-WindowsFeature -Name 'DHCP' –IncludeManagementTools")
    DHCP_complete_thread = threading.Thread(target=Func_DHCP_complete)
    DHCP_complete_thread.start()


def Func_DHCP_complete():
    DHCP_Install.config(text="Finished")  
    time.sleep(3)
    DHCP_Install.config(text="Install DHCP Feature")  
    
    #-----</DHCP_Install>-----

    #-----<DHCP_Setup>-----

def DHCP_Setup_Click():
        #-----<Read、Setup and close>-----
    def DHCP_Finish_Button():
        DHCP_Setup_thread = threading.Thread(target=read_DHCP_input)
        DHCP_Setup_thread.start()
        read_input.config(text="Please Wait")

    def read_DHCP_input():
        StartRange=StartRangeentry.get()
        EndRange=EndRangeentry.get()
        SubnetMask=SubnetMaskentry.get()
        ScopeName=ScopeNameentry.get()
        DNS_Address=DNS_Addressentry.get()
        Router=Routerentry.get()
        #<Scope id calculate>
        r=StartRange.split(".")
        ScopeID=""
        for i in range(3):
            ScopeID+=r[i]
            ScopeID+="."
        ScopeID+="0"
        #</Scope id calculate>
        AddScope="Add-DhcpServerV4Scope -Name "+ScopeName+" -StartRange "+StartRange+" -EndRange "+EndRange+" -Subnetmask "+SubnetMask
        tmp="powershell.exe "+AddScope
        os.system(tmp)
        SetDHCPDNS="Set-DhcpServerv4OptionValue -ScopeId "+ScopeID+" -OptionId 6 -Value "+DNS_Address
        tmp="powershell.exe "+SetDHCPDNS
        os.system(tmp)
        SetDHCPRouter="Set-DhcpServerv4OptionValue -ScopeId "+ScopeID+" -Router "+Router
        tmp="powershell.exe "+SetDHCPRouter
        os.system(tmp)
        DHCP_Setup_Window.destroy()
        DHCP_Setup_Window.update()
        #-----</Read、Setup and close>-----

        #-----<Just close>-----
    def DHCP_Setup_Exit():
        DHCP_Setup_Window.destroy()
        DHCP_Setup_Window.update()
        #-----</Just close>-----

    DHCP_Setup_Window = tk.Toplevel(root)
    DHCP_Setup_Window.geometry("200x200")

    #<Entrys>
    StartRangelabel = tk.Label(DHCP_Setup_Window, text='StartRange:')
    StartRangelabel.grid(row=0, column=0)
    StartRangeentry = tk.Entry(DHCP_Setup_Window)
    StartRangeentry.grid(row=0, column=1)
    EndRangelabel = tk.Label(DHCP_Setup_Window, text='EndRange:')
    EndRangelabel.grid(row=1, column=0)
    EndRangeentry = tk.Entry(DHCP_Setup_Window)
    EndRangeentry.grid(row=1, column=1)
    SubnetMasklabel = tk.Label(DHCP_Setup_Window, text='SubnetMask:')
    SubnetMasklabel.grid(row=2, column=0)
    SubnetMaskentry = tk.Entry(DHCP_Setup_Window)
    SubnetMaskentry.grid(row=2, column=1)
    ScopeNamelabel = tk.Label(DHCP_Setup_Window, text='ScopeName:')
    ScopeNamelabel.grid(row=3, column=0)
    ScopeNameentry = tk.Entry(DHCP_Setup_Window)
    ScopeNameentry.grid(row=3, column=1)
    DNS_Addresslabel = tk.Label(DHCP_Setup_Window, text='DNS Address:')
    DNS_Addresslabel.grid(row=4, column=0)
    DNS_Addressentry = tk.Entry(DHCP_Setup_Window)
    DNS_Addressentry.grid(row=4, column=1)
    Routerlabel = tk.Label(DHCP_Setup_Window, text='Router IP:')
    Routerlabel.grid(row=5, column=0)
    Routerentry = tk.Entry(DHCP_Setup_Window)
    Routerentry.grid(row=5, column=1)
    #</Entrys>

    Exit=tk.Button(DHCP_Setup_Window,text="Exit",command=DHCP_Setup_Exit)
    Exit.grid(row=6,column=0)
    read_input=tk.Button(DHCP_Setup_Window,text="Finish",command=DHCP_Finish_Button)
    read_input.grid(row=6,column=1)   
    #-----</DHCP_Setup>-----

DHCP_Install = tk.Button(root, text='Install DHCP Feature', command=DHCP_Install_Click)
DHCP_Install.pack()
Setup_DHCP=tk.Button(root,text="Setup DHCP",command=DHCP_Setup_Click)
Setup_DHCP.pack()
#----</DHCP>-----

root.mainloop()