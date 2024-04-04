import tkinter as tk
import time
import threading
import subprocess
from tkinter import ttk

root = tk.Tk()
root.title('Windows Server Setup')
root.geometry('400x400')
# root.iconbitmap(".\icon.ico")
# 添加自定義樣式來美化按鈕
style = ttk.Style()
style.configure('Custom.TButton', font=('Helvetica', 12), foreground='blue', padding=5)
style.configure('Red.TButton', font=('Helvetica', 12), foreground='red', padding=5)
style.configure('Green.TButton', font=('Helvetica', 12), foreground='green', padding=5)

def powershell(command):
    subprocess.run(["powershell.exe", command])

#-----<DHCP>-----

#-----<DHCP_Install>-----
def DHCP_Install_Click():
    DHCP_install_thread = threading.Thread(target=installing_DHCP)
    DHCP_install_thread.start()
    DHCP_Install.config(text='Installing')

def installing_DHCP():
    powershell("Install-WindowsFeature -Name 'DHCP' –IncludeManagementTools")
    DHCP_complete_thread = threading.Thread(target=Func_DHCP_complete)
    DHCP_complete_thread.start()

def Func_DHCP_complete():
    DHCP_Install.config(text="Finished")  
    time.sleep(3)
    DHCP_Install.config(text="Install DHCP Feature")  

#-----</DHCP_Install>-----
    
#-----<DHCP_Uninstall>-----
def DHCP_Uninstall_Click():
    DHCP_Uninstall_thread = threading.Thread(target=Uninstalling_DHCP)
    DHCP_Uninstall_thread.start()
    DHCP_Uninstall.config(text='Uninstalling')

def Uninstalling_DHCP():
    powershell("Uninstall-WindowsFeature -Name 'DHCP' –IncludeManagementTools")
    DHCP_complete_thread = threading.Thread(target=Func_UnDHCP_complete)
    DHCP_complete_thread.start()

def Func_UnDHCP_complete():
    DHCP_Uninstall.config(text="Finished")  
    time.sleep(3)
    DHCP_Uninstall.config(text="Uninstall DHCP Feature")  
#-----</DHCP_Uninstall>-----
    
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
        powershell(AddScope)
        SetDHCPDNS="Set-DhcpServerv4OptionValue -ScopeId "+ScopeID+" -OptionId 6 -Value "+DNS_Address
        powershell(SetDHCPDNS)
        SetDHCPRouter="Set-DhcpServerv4OptionValue -ScopeId "+ScopeID+" -Router "+Router
        powershell(SetDHCPRouter)
        DHCP_Setup_Window.destroy()
        DHCP_Setup_Window.update()
    
    #-----</Read、Setup and close>-----

    #-----<Just close>-----
    def DHCP_Setup_Exit():
        DHCP_Setup_Window.destroy()
        DHCP_Setup_Window.update()
    #-----</Just close>-----

    DHCP_Setup_Window = tk.Toplevel(root)
    DHCP_Setup_Window.title("DHCP Setup Window")
    DHCP_Setup_Window.geometry("320x200")
    # 設置窗口邊框樣式
    DHCP_Setup_Window.attributes('-topmost', 'true')

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
 
    Exit=ttk.Button(DHCP_Setup_Window, text="Exit", command=DHCP_Setup_Exit, style='Red.TButton')
    Exit.grid(row=6,column=0,padx=20)
    read_input=ttk.Button(DHCP_Setup_Window, text="Finish", command=DHCP_Finish_Button, style='Green.TButton')
    read_input.grid(row=6,column=1)    
    #-----</DHCP_Setup>-----

#----</DHCP>-----
def Remove_DHCP_Scope_Click():

    def DHCP_Setup_Exit():
        Remove_DHCP_Scope_Window.destroy()
        Remove_DHCP_Scope_Window.update()

    def DHCP_Finish_Button():
        ScopeID=ScopeIDentry.get()
        command="Remove-DhcpServerv4Scope -ScopeId "+ScopeID
        powershell(command)

    Remove_DHCP_Scope_Window = tk.Toplevel(root)
    Remove_DHCP_Scope_Window.title("Remove DHCP Scope")
    Remove_DHCP_Scope_Window.geometry("320x200")
    ScopeIDlabel = tk.Label(Remove_DHCP_Scope_Window, text='ScopeID:')
    ScopeIDlabel.grid(row=0, column=0)
    ScopeIDentry = tk.Entry(Remove_DHCP_Scope_Window)
    ScopeIDentry.grid(row=0, column=1)
    Exit=ttk.Button(Remove_DHCP_Scope_Window, text="Exit", command=DHCP_Setup_Exit, style='Red.TButton')
    Exit.grid(row=6,column=0,padx=20)
    read_input=ttk.Button(Remove_DHCP_Scope_Window, text="Finish", command=DHCP_Finish_Button, style='Green.TButton')
    read_input.grid(row=6,column=1) 
#----<DNS>-----
    #-----<DNS_Install>

def DNS_Install_Click():
    DNS_install_thread = threading.Thread(target=installing_DNS)
    DNS_install_thread.start()
    DNS_Install.config(text='Installing')

def installing_DNS():
    powershell("Install-WindowsFeature -Name 'DNS' –IncludeManagementTools")
    DNS_complete_thread = threading.Thread(target=Func_DNS_complete)
    DNS_complete_thread.start()


def Func_DNS_complete():
    DNS_Install.config(text="Finished")  
    time.sleep(3)
    DNS_Install.config(text="Install DNS Feature")  
    
    #-----</DNS_Install>-----

    #-----<DNS_Uninstall>

def DNS_Uninstall_Click():
    DNS_Uninstall_thread = threading.Thread(target=Uninstalling_DNS)
    DNS_Uninstall_thread.start()
    DNS_Uninstall.config(text='Uninstalling')

def Uninstalling_DNS():
    powershell("Uninstall-WindowsFeature -Name 'DNS' –IncludeManagementTools")
    DNS_complete_thread = threading.Thread(target=Func_UnDNS_complete)
    DNS_complete_thread.start()


def Func_UnDNS_complete():
    DNS_Uninstall.config(text="Finished")  
    time.sleep(3)
    DNS_Uninstall.config(text="Uninstall DNS Feature")  

    #-----</DNS_Uninstall>-----

    #-----<DNS_Main_Window>-----
def DNS_Setup_click():

        #-----<Foward lookup zone>-----
    def Foward_Lookup_Zone_Click():
            #-----<Primary Zone Setting>-----
        def Add_Primary_Button_Click():
                #-----<Add>-----
            def Add_Primary_Zone_Click():
                DNS_install_thread = threading.Thread(target=Adding_Zone)
                DNS_install_thread.start()
                Add_Primart_Zone_input.config(text="Please Wait")
            def Adding_Zone():
                ZoneName=ZoneNameEntry.get()
                ZoneFile=ZoneName+".dns"
                command="Add-DnsServerPrimaryZone -Name "+ZoneName+" -ZoneFile "+ZoneFile
                powershell(command)
                Add_Primary_Button_Window.destroy()
                #-----</Add>-----
            def Exit_Window():
                Add_Primary_Button_Window.destroy()  
            Add_Primary_Button_Window=tk.Toplevel(Foward_Lookup_Zone_Window)
            Add_Primary_Button_Window.title("Add Primary Button") 
            Add_Primary_Button_Window.geometry("320x200")
            ZoneNamelabel=tk.Label(Add_Primary_Button_Window,text="Zone Name")
            ZoneNamelabel.grid(row=0,column=0)
            ZoneNameEntry=tk.Entry(Add_Primary_Button_Window)
            ZoneNameEntry.grid(row=0,column=1)
            Exit=ttk.Button(Add_Primary_Button_Window,text="Exit",command=Exit_Window, style='Red.TButton')
            Exit.grid(row=1,column=0,padx=20)
            Add_Primart_Zone_input=ttk.Button(Add_Primary_Button_Window,text="Finish",command=Add_Primary_Zone_Click, style='Green.TButton')
            Add_Primart_Zone_input.grid(row=1,column=1)
            #-----</Primary Zone Setting>-----

            #----<DNS Record>----
        def Add_DNS_Record_Click():
                #----<ADD DNS Record>----
            def DNS_Record_input_Click():
                tmp=Set_Record_Type.get()
                if tmp=="A":
                    def A_input_Click():
                        DNS_install_thread = threading.Thread(target=installing_DNS_A)
                        DNS_install_thread.start()
                        A_input.config(text="Please Wait")
                    def installing_DNS_A():
                        zone=Set_Zone_Entry.get()
                        name=Name_Entry.get()
                        IPv4Address=IPv4Address_Entry.get()
                        command="Add-DnsServerResourceRecordA -Name "+name+" -ZoneName "+zone+" -IPv4Address "+IPv4Address
                        powershell(command)
                        Add_DNS_Record_Window.destroy()
                    Add_A_Record_Window=tk.Toplevel(Add_DNS_Record_Window)
                    Add_A_Record_Window.title("Add A Record") 
                    Add_A_Record_Window.geometry("320x200")
                    Name_Label=tk.Label(Add_A_Record_Window,text="Name:")
                    Name_Label.grid(row=0,column=0)
                    Name_Entry=tk.Entry(Add_A_Record_Window)
                    Name_Entry.grid(row=0,column=1)
                    IPv4Address_Label=tk.Label(Add_A_Record_Window,text="IPv4Address:")
                    IPv4Address_Label.grid(row=1,column=0)
                    IPv4Address_Entry=tk.Entry(Add_A_Record_Window)
                    IPv4Address_Entry.grid(row=1,column=1)
                    A_input=ttk.Button(Add_A_Record_Window,text="Finish",command=A_input_Click, style='Green.TButton')
                    A_input.grid(row=2,column=1)
                elif tmp=="AAAA":
                    def AAAA_input_Click():
                        DNS_install_thread = threading.Thread(target=installing_DNS_AAAA)
                        DNS_install_thread.start()
                        AAAA_input.config(text="Please Wait")
                    def installing_DNS_AAAA():
                        zone=Set_Zone_Entry.get()
                        name=Name_Entry.get()
                        IPv6Address=IPv6Address_Entry.get()
                        command="Add-DnsServerResourceRecordAAAA -Name "+name+" -ZoneName "+zone+" -IPv6Address "+IPv6Address
                        powershell(command)
                        Add_DNS_Record_Window.destroy()
                    Add_AAAA_Record_Window=tk.Toplevel(Add_DNS_Record_Window)
                    Add_AAAA_Record_Window.title("Add AAAA Record") 
                    Add_AAAA_Record_Window.geometry("320x200")
                    Name_Label=tk.Label(Add_AAAA_Record_Window,text="Name:")
                    Name_Label.grid(row=0,column=0)
                    Name_Entry=tk.Entry(Add_AAAA_Record_Window)
                    Name_Entry.grid(row=0,column=1)
                    IPv6Address_Label=tk.Label(Add_AAAA_Record_Window,text="IPv6Address:")
                    IPv6Address_Label.grid(row=1,column=0)
                    IPv6Address_Entry=tk.Entry(Add_AAAA_Record_Window)
                    IPv6Address_Entry.grid(row=1,column=1)
                    AAAA_input=ttk.Button(Add_AAAA_Record_Window,text="Finish",command=AAAA_input_Click, style='Green.TButton')
                    AAAA_input.grid(row=2,column=1)
                else:
                    def CName_input_Click():
                        DNS_install_thread = threading.Thread(target=installing_DNS_CName)
                        DNS_install_thread.start()
                        CName_input.config(text="Please Wait")
                    def installing_DNS_CName():
                        zone=Set_Zone_Entry.get()
                        name=Name_Entry.get()
                        HostNameAlias=HostNameAlias_Entry.get()
                        command="Add-DnsServerResourceRecordCName -Name "+name+" -ZoneName "+zone+" -HostNameAlias "+HostNameAlias
                        powershell(command)
                        Add_DNS_Record_Window.destroy()
                    Add_CName_Record_Window=tk.Toplevel(Add_DNS_Record_Window)
                    Add_CName_Record_Window.title("Add CNAME Record") 
                    Add_CName_Record_Window.geometry("320x200")
                    Name_Label=tk.Label(Add_CName_Record_Window,text="Name:")
                    Name_Label.grid(row=0,column=0)
                    Name_Entry=tk.Entry(Add_CName_Record_Window)
                    Name_Entry.grid(row=0,column=1)
                    HostNameAlias_Label=tk.Label(Add_CName_Record_Window,text="HostNameAlias:")
                    HostNameAlias_Label.grid(row=1,column=0)
                    HostNameAlias_Entry=tk.Entry(Add_CName_Record_Window)
                    HostNameAlias_Entry.grid(row=1,column=1)
                    CName_input=ttk.Button(Add_CName_Record_Window,text="Finish",command=CName_input_Click, style='Green.TButton')
                    CName_input.grid(row=2,column=1)
            def Exit_Window():
                Add_DNS_Record_Window.destroy()
            Add_DNS_Record_Window=tk.Toplevel(Foward_Lookup_Zone_Window)
            Add_DNS_Record_Window.title("Add DNS Record") 
            Add_DNS_Record_Window.geometry("340x200")
            Set_Zone_Label=tk.Label(Add_DNS_Record_Window,text="Set Zone:")
            Set_Zone_Label.grid(row=0,column=0,)
            Set_Zone_Entry=tk.Entry(Add_DNS_Record_Window)
            Set_Zone_Entry.grid(row=0,column=1)
            #---<!!!!!!!需合併column!!!!!>---
            Set_Record_Type_Label = ttk.Label(Add_DNS_Record_Window, text="Record Type:")
            Set_Record_Type_Label.grid(row=1, column=0)
            Set_Record_Type=ttk.Combobox(Add_DNS_Record_Window,values=["A","AAAA","CName"])
            Set_Record_Type.grid(row=1, column=1)
            Exit=ttk.Button(Add_DNS_Record_Window,text="Exit",command=Exit_Window, style='Red.TButton')
            Exit.grid(row=2,column=0,padx=20)
            DNS_Record_input=ttk.Button(Add_DNS_Record_Window,text="Next",command=DNS_Record_input_Click, style='Green.TButton')
            DNS_Record_input.grid(row=2,column=1)
                #----</ADD DNS Record>----
        def Remove_DNS_Zone_Click():
            def DNS_Finish_Button():
                DNS_Remove_thread=threading.Thread(target=Remove_Start)
                DNS_Remove_thread.start()
                read_input.config(text="Please Wait")
            def Remove_Start():
                Zone=ZoneNameentry.get()
                command="Remove-DnsServerZone -Name "+Zone+" -Force"
                powershell(command)
                Remove_DNS_Zone_Window.destroy()                
            def DNS_Setup_Exit():
                Remove_DNS_Zone_Window.destroy()
            Remove_DNS_Zone_Window=tk.Toplevel(Foward_Lookup_Zone_Window)
            Remove_DNS_Zone_Window.title("Remove DNS Zone") 
            Remove_DNS_Zone_Window.geometry("320x200")
            ZoneNamelabel = tk.Label(Remove_DNS_Zone_Window, text='ZoneName:')
            ZoneNamelabel.grid(row=0, column=0)
            ZoneNameentry = tk.Entry(Remove_DNS_Zone_Window)
            ZoneNameentry.grid(row=0, column=1)
            Exit=ttk.Button(Remove_DNS_Zone_Window, text="Exit", command=DNS_Setup_Exit, style='Red.TButton')
            Exit.grid(row=6,column=0,padx=20)
            read_input=ttk.Button(Remove_DNS_Zone_Window, text="Finish", command=DNS_Finish_Button, style='Green.TButton')
            read_input.grid(row=6,column=1)            
        def Remove_DNS_Record_Click():
            def DNS_Finish_Button():
                DNS_Remove_thread=threading.Thread(target=Remove_Start)
                DNS_Remove_thread.start()
                read_input.config(text="Please Wait")
            def Remove_Start():
                Zone=ZoneNameentry.get()
                Record=RecordNameentry.get()
                type=str(Set_Record_Type.get())
                command="Remove-DnsServerResourceRecord -ZoneName "+Zone+" -Name "+Record+" -RRType "+type+" -Force"
                powershell(command)
                Remove_DNS_Record_Window.destroy()
            def DNS_Setup_Exit():
                Remove_DNS_Record_Window.destroy()
            Remove_DNS_Record_Window=tk.Toplevel(Foward_Lookup_Zone_Window)
            Remove_DNS_Record_Window.title("Remove DNS Record") 
            Remove_DNS_Record_Window.geometry("340x200")
            ZoneNamelabel = tk.Label(Remove_DNS_Record_Window, text='ScopeID:')
            ZoneNamelabel.grid(row=0, column=0)
            ZoneNameentry = tk.Entry(Remove_DNS_Record_Window)
            ZoneNameentry.grid(row=0, column=1)
            RecordNamelabel = tk.Label(Remove_DNS_Record_Window, text='RecordName:')
            RecordNamelabel.grid(row=1, column=0)
            RecordNameentry = tk.Entry(Remove_DNS_Record_Window)
            RecordNameentry.grid(row=1, column=1)
            Set_Record_Type_label=tk.Label(Remove_DNS_Record_Window,text="Type")
            Set_Record_Type_label.grid(row=2,column=0)
            Set_Record_Type=ttk.Combobox(Remove_DNS_Record_Window,values=["A","AAAA","CName"])
            Set_Record_Type.grid(row=2,column=1)
            Exit=ttk.Button(Remove_DNS_Record_Window, text="Exit", command=DNS_Setup_Exit, style='Red.TButton')
            Exit.grid(row=6,column=0,padx=20)
            read_input=ttk.Button(Remove_DNS_Record_Window, text="Finish", command=DNS_Finish_Button, style='Green.TButton')
            read_input.grid(row=6,column=1)            
        Foward_Lookup_Zone_Window=tk.Toplevel(DNS_Setup_Window)
        Foward_Lookup_Zone_Window.title("Foward Lookup Zone")
        Foward_Lookup_Zone_Window.geometry("320x200")
        Add_Primary_Zone_Button=ttk.Button(Foward_Lookup_Zone_Window,text="Add Primary Zone",command=Add_Primary_Button_Click, style='Custom.TButton')
        Add_Primary_Zone_Button.pack()
        Add_DNS_Record_Button=ttk.Button(Foward_Lookup_Zone_Window,text="Add DNS Record",command=Add_DNS_Record_Click, style='Custom.TButton')
        Add_DNS_Record_Button.pack()
        Remove_DNS_Zone_Button=ttk.Button(Foward_Lookup_Zone_Window,text="Remove DNS Zone",command=Remove_DNS_Zone_Click, style='Custom.TButton')
        Remove_DNS_Zone_Button.pack()
        Remove_DNS_Record_Button=ttk.Button(Foward_Lookup_Zone_Window,text="Remove DNS Recoed",command=Remove_DNS_Record_Click, style='Custom.TButton')
        Remove_DNS_Record_Button.pack()       
            #----<DNS Record>----
        
        #-----</Foward lookup zone>-----

        #-----<Reverse lookup zone>-----
    def Reverse_Lookup_Zone_Click():
        Reverse_Lookup_Zone_Window=tk.Toplevel(DNS_Setup_Window)
        Reverse_Lookup_Zone_Window.title("Reverse Lookup Zone")  
        Reverse_Lookup_Zone_Window.geometry("320x200")

        def Add_Zone_Button_Click():
            def Add_Reverse_Zone_input_Click():
                Add_Reverse_Zone_input_Start=threading.Thread(target=Add_Reverse_Zone_input_thread)
                Add_Reverse_Zone_input_Start.start()
                Add_Reverse_Zone_input.config(text="Please Wait")
            def Add_Reverse_Zone_input_thread():
                NetworkID=NetworkID_Entry.get()
                tmp=NetworkID.split(".")
                zonefile=""
                for i in range(3):
                    zonefile+=tmp[2-i]
                    zonefile+="."
                NetworkID=NetworkID+"/24"
                zonefile+="in-addr.arpa.dns"
                command="Add-DnsServerPrimaryZone -NetworkID "+NetworkID+" -ZoneFile "+zonefile
                powershell(command)
                Add_Zone_Window.destroy()
            def Exit_Window():
                Add_Zone_Window.destroy()
            Add_Zone_Window=tk.Toplevel(Reverse_Lookup_Zone_Window)
            Add_Zone_Window.title("Add Zone") 
            Add_Zone_Window.geometry("320x200")
            NetworkID_Label=tk.Label(Add_Zone_Window,text="NetworkID:")
            NetworkID_Label.grid(row=0,column=0)
            NetworkID_Entry=tk.Entry(Add_Zone_Window)
            NetworkID_Entry.grid(row=0,column=1)
            Exit=ttk.Button(Add_Zone_Window,text="Exit",command=Exit_Window, style='Red.TButton')
            Exit.grid(row=1,column=0,padx=20)
            Add_Reverse_Zone_input=ttk.Button(Add_Zone_Window,text="Finish",command=Add_Reverse_Zone_input_Click, style='Green.TButton')
            Add_Reverse_Zone_input.grid(row=1,column=1)

        def Remove_Zone_Button_Click():

            def Remove_Reverse_Zone_input_Click():
                Remove_Reverse_Zone_input_Start=threading.Thread(target=Remove_Reverse_Zone_input_thread)
                Remove_Reverse_Zone_input_Start.start()
                Add_Reverse_Zone_input.config(text="Please Wait")
            def Remove_Reverse_Zone_input_thread():
                NetworkID=NetworkID_Entry.get()
                tmp=NetworkID.split(".")
                ID=""
                for i in range(3):
                    ID+=tmp[2-i]
                    ID+="."
                ID+="in-addr.arpa"
                command="Remove-DnsServerZone "+ID+" -Force"
                powershell(command)
                Remove_Zone_Window.destroy()
            def Exit_Window():
                Remove_Zone_Window.destroy()
            Remove_Zone_Window=tk.Toplevel(Reverse_Lookup_Zone_Window)
            Remove_Zone_Window.title("Remove Zone") 
            Remove_Zone_Window.geometry("320x200")
            NetworkID_Label=tk.Label(Remove_Zone_Window,text="NetworkID:")
            NetworkID_Label.grid(row=0,column=0)
            NetworkID_Entry=tk.Entry(Remove_Zone_Window)
            NetworkID_Entry.grid(row=0,column=1)
            Exit=ttk.Button(Remove_Zone_Window,text="Exit",command=Exit_Window, style='Red.TButton')
            Exit.grid(row=1,column=0,padx=20)
            Add_Reverse_Zone_input=ttk.Button(Remove_Zone_Window,text="Finish",command=Remove_Reverse_Zone_input_Click, style='Green.TButton')
            Add_Reverse_Zone_input.grid(row=1,column=1)
            
        def Add_PTR_Record_Click():
            def Add_PTR_Record_input_Click():
                Add_PTR_Record_input_Start=threading.Thread(target=Add_PTR_Record_input_thread)
                Add_PTR_Record_input_Start.start()
                Add_PTR_Record_input.config(text="Please Wait")
            def Add_PTR_Record_input_thread():
                Name=name_Entry.get()
                ZoneName=ZoneName_Entry.get()
                PTRDomainName=PTRDomainName_Entry.get()
                tmp=ZoneName.split(".")
                ID=""
                for i in range(3):
                    ID+=tmp[2-i]
                    ID+="."
                ID+="in-addr.arpa"
                command="Add-DnsServerResourceRecordPtr -Name "+Name+" -ZoneName "+ID+" -PtrDomainName "+PTRDomainName
                powershell(command)
                Add_PTR_Record_Window.destroy()
            def Exit_Window():
                Add_PTR_Record_Window.destroy()
            Add_PTR_Record_Window=tk.Toplevel(Reverse_Lookup_Zone_Window)
            Add_PTR_Record_Window.title("Add PTR Record") 
            Add_PTR_Record_Window.geometry("320x200")
            Name_Label=tk.Label(Add_PTR_Record_Window,text="Name:")
            Name_Label.grid(row=0,column=0)
            name_Entry=tk.Entry(Add_PTR_Record_Window)
            name_Entry.grid(row=0,column=1)
            ZoneName_ID_Label=tk.Label(Add_PTR_Record_Window,text="ZoneName(ID):")
            ZoneName_ID_Label.grid(row=1,column=0)
            ZoneName_Entry=tk.Entry(Add_PTR_Record_Window)
            ZoneName_Entry.grid(row=1,column=1)
            PTRDomainName_Label=tk.Label(Add_PTR_Record_Window,text="PTRDomainName:")
            PTRDomainName_Label.grid(row=2,column=0)
            PTRDomainName_Entry=tk.Entry(Add_PTR_Record_Window)
            PTRDomainName_Entry.grid(row=2,column=1)
            Exit=ttk.Button(Add_PTR_Record_Window,text="Exit",command=Exit_Window, style='Red.TButton')
            Exit.grid(row=3,column=0,padx=20)
            Add_PTR_Record_input=ttk.Button(Add_PTR_Record_Window,text="Finish",command=Add_PTR_Record_input_Click, style='Green.TButton')
            Add_PTR_Record_input.grid(row=3,column=1)
        def Remove_PTR_Record_Click():
            def Remove_PTR_Record_input_Click():
                Remove_PTR_Record_input_Start=threading.Thread(target=Remove_PTR_Record_input_thread)
                Remove_PTR_Record_input_Start.start()
                Remove_PTR_Record_input.config(text="Please Wait")
            def Remove_PTR_Record_input_thread():
                Name=name_Entry.get()
                ZoneName=ZoneName_Entry.get()   
                tmp=ZoneName.split(".")
                ID=""
                for i in range(3):
                    ID+=tmp[2-i]
                    ID+="."
                ID+="in-addr.arpa"
                command="Remove-DnsServerResourceRecord -ZoneName "+ID+" -RRType PTR -Name "+Name+" -Force"
                powershell(command)
                Remove_PTR_Record_Window.destroy()
            def Exit_Window():
                Remove_PTR_Record_Window.destroy()
            Remove_PTR_Record_Window=tk.Toplevel(Reverse_Lookup_Zone_Window)
            Remove_PTR_Record_Window.title("Remove PTR Record") 
            Remove_PTR_Record_Window.geometry("320x200")
            Name_Label=tk.Label(Remove_PTR_Record_Window,text="Name:")
            Name_Label.grid(row=0,column=0)
            name_Entry=tk.Entry(Remove_PTR_Record_Window)
            name_Entry.grid(row=0,column=1)
            ZoneName_Label=tk.Label(Remove_PTR_Record_Window,text="ZoneName(ID):")
            ZoneName_Label.grid(row=1,column=0)
            ZoneName_Entry=tk.Entry(Remove_PTR_Record_Window)
            ZoneName_Entry.grid(row=1,column=1)
            Exit=ttk.Button(Remove_PTR_Record_Window,text="Exit",command=Exit_Window, style='Red.TButton')
            Exit.grid(row=2,column=0,padx=20)
            Remove_PTR_Record_input=ttk.Button(Remove_PTR_Record_Window,text="Finish",command=Remove_PTR_Record_input_Click, style='Green.TButton')
            Remove_PTR_Record_input.grid(row=2,column=1)         
        Add_Zone_Button=ttk.Button(Reverse_Lookup_Zone_Window,text="Add Zone",command=Add_Zone_Button_Click, style='Custom.TButton')
        Add_Zone_Button.pack()
        Remove_Zone_Button=ttk.Button(Reverse_Lookup_Zone_Window,text="Remove Zone",command=Remove_Zone_Button_Click, style='Custom.TButton')
        Remove_Zone_Button.pack()
        Add_PTR_Record_Button=ttk.Button(Reverse_Lookup_Zone_Window,text="Add PTR Record",command=Add_PTR_Record_Click, style='Custom.TButton')
        Add_PTR_Record_Button.pack()
        Remove_PTR_Record_Button=ttk.Button(Reverse_Lookup_Zone_Window,text="Remove PTR Record",command=Remove_PTR_Record_Click, style='Custom.TButton')
        Remove_PTR_Record_Button.pack()
        #-----</Reverse lookup zone>-----

        #----<DNS Fowarder>----
    def Set_Fowarder_Click():
            #----<Set DNS Fowarder>----
        def input_click():
            DNS_install_thread = threading.Thread(target=Setting_Fowarder)
            DNS_install_thread.start()
            Fowarder_input.config(text="Please Wait")
        def Setting_Fowarder():
            Address=AddressEntry.get()
            command="Set-DnsServerForwarder -IPAddress "+Address
            powershell(command)
            Set_Fowarder_Window.destroy()
            #----</Set DNS Fowarder>----
        def Exit_Window():
            Set_Fowarder_Window.destroy()
        Set_Fowarder_Window=tk.Toplevel(DNS_Setup_Window)
        Set_Fowarder_Window.title("Set Fowarder")  
        Set_Fowarder_Window.geometry("320x200")
        Addresslabel=tk.Label(Set_Fowarder_Window,text="IPAddress")
        Addresslabel.grid(row=0,column=0)
        AddressEntry=tk.Entry(Set_Fowarder_Window)
        AddressEntry.grid(row=0,column=1)
        Exit=ttk.Button(Set_Fowarder_Window,text="Exit",command=Exit_Window, style='Red.TButton')
        Exit.grid(row=1,column=0,padx=20)
        Fowarder_input=ttk.Button(Set_Fowarder_Window,text="Finish",command=input_click, style='Green.TButton')
        Fowarder_input.grid(row=1,column=1)
        #----</DNS Fowarder>----

    DNS_Setup_Window = tk.Toplevel(root)
    DNS_Setup_Window.title('DNS Setup') 
    DNS_Setup_Window.geometry("320x200")
    Foward_Lookup_Zone=ttk.Button(DNS_Setup_Window,text="Foward Look Zone Settings",command=Foward_Lookup_Zone_Click, style='Custom.TButton')
    Foward_Lookup_Zone.pack()
    Reverse_Lookup_Zone=ttk.Button(DNS_Setup_Window,text="Reverse Look Zone Settings",command=Reverse_Lookup_Zone_Click, style='Custom.TButton')
    Reverse_Lookup_Zone.pack()
    Set_Fowarder=ttk.Button(DNS_Setup_Window,text="Set Fowarder",command=Set_Fowarder_Click, style='Custom.TButton')
    Set_Fowarder.pack()
        
        
#----</DNS>-----

def iSCSI_target_Uninstall_click():
    iSCSI_Uninstall_thread = threading.Thread(target=Uninstalling_iSCSI)
    iSCSI_Uninstall_thread.start()
    Uninstall_iSCSITarget.config(text='Uninstalling')

def Uninstalling_iSCSI():
    powershell("Uninstall-WindowsFeature -Name FS-iSCSITarget-Server")
    iSCSI_complete_thread = threading.Thread(target=Func_UniSCSI_complete)
    iSCSI_complete_thread.start()


def Func_UniSCSI_complete():
    Uninstall_iSCSITarget.config(text="Finished")  
    time.sleep(3)
    Uninstall_iSCSITarget.config(text="Uninstall iSCSI Feature") 

def iSCSI_target_install_click():
    iSCSI_install_thread = threading.Thread(target=installing_iSCSI)
    iSCSI_install_thread.start()
    Install_iSCSITarget.config(text='Installing')

def installing_iSCSI():
    powershell("Install-WindowsFeature -Name FS-iSCSITarget-Server")
    iSCSI_complete_thread = threading.Thread(target=Func_iSCSI_complete)
    iSCSI_complete_thread.start()


def Func_iSCSI_complete():
    Install_iSCSITarget.config(text="Finished")  
    time.sleep(3)
    Install_iSCSITarget.config(text="Install iSCSI Feature") 


def Setup_iSCSI_Disk_Share_Click():
    iSCSI_Setup_Window=tk.Toplevel(root)
    iSCSI_Setup_Window.title('iSCSI Setup')
    iSCSI_Setup_Window.geometry("320x200")
    def Add_VirtualDisk_Click():
        def Add_VDisk_input_Click():
            Add_VDisk_input_Start=threading.Thread(target=Add_VDisk_input_thread)
            Add_VDisk_input_Start.start()
            Add_VDisk_input.config(text="Please Wait")
        def Add_VDisk_input_thread():
            path=VDisk_PathEntry.get()
            name=VDisk_NameEntry.get()
            disk=path+name
            size=VDisk_SizeEntry.get()
            command="New-IscsiVirtualDisk -Path "+disk+" -size "+size
            powershell(command)
            Add_VirtualDisk_Window.destroy()
        def Exit_Window():
            Add_VirtualDisk_Window.destroy()
        Add_VirtualDisk_Window=tk.Toplevel(iSCSI_Setup_Window)
        Add_VirtualDisk_Window.title("Add Virtual Disk")
        Add_VirtualDisk_Window.geometry("320x200")
        Add_VirtualDisk_Window.attributes('-topmost', 'true')
        VDisk_PathLabel=tk.Label(Add_VirtualDisk_Window,text="VDisk Path")
        VDisk_PathLabel.grid(row=0,column=0)
        VDisk_PathEntry=tk.Entry(Add_VirtualDisk_Window)
        VDisk_PathEntry.grid(row=0,column=1)
        VDisk_NameLabel=tk.Label(Add_VirtualDisk_Window,text="VDisk Name(Ex:DiskName.vhdx)")
        VDisk_NameLabel.grid(row=1,column=0)
        VDisk_NameEntry=tk.Entry(Add_VirtualDisk_Window)
        VDisk_NameEntry.grid(row=1,column=1)
        VDisk_SizeLabel=tk.Label(Add_VirtualDisk_Window,text="VDisk Size(Ex:10GB)")
        VDisk_SizeLabel.grid(row=2,column=0)
        VDisk_SizeEntry=tk.Entry(Add_VirtualDisk_Window)
        VDisk_SizeEntry.grid(row=2,column=1)
        Exit=ttk.Button(Add_VirtualDisk_Window,text="Exit",command=Exit_Window, style='Red.TButton')
        Exit.grid(row=3,column=0,padx=20)
        Add_VDisk_input=ttk.Button(Add_VirtualDisk_Window,text="Finish",command=Add_VDisk_input_Click, style='Green.TButton')
        Add_VDisk_input.grid(row=3,column=1)
    def Share_VirtualDisk_Click():
        def Share_VDisk_input_Click():
            Share_VDisk_input_Start=threading.Thread(target=Share_VDisk_input_thread)
            Share_VDisk_input_Start.start()
            Share_VDisk_input.config(text="Please Wait")
        def Share_VDisk_input_thread():
            user=UsernameEntry.get()
            pword=PasswordEntry.get()
            target=TargetnameEntry.get()
            path=DiskPathEntry.get()
            command0="New-IscsiServerTarget -TargetName "+target+" -InitiatorId \"Iqn:*\""
            powershell(command0)
            command1="Add-IscsiVirtualDiskTargetMapping -TargetName "+target+" -DevicePath "+path
            powershell(command1)
            command2="$User=\""+user+"\";$PWord = ConvertTo-SecureString -String \""+pword+"\" -AsPlainText -Force;$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $User, $PWord;Set-IscsiServerTarget -TargetName "+target+" -EnableChap $True -Chap $Credential"
            powershell(command2)
            Share_VirtualDisk_Window.destroy()
        def Exit_Window():
            Share_VirtualDisk_Window.destroy()
        Share_VirtualDisk_Window=tk.Toplevel(iSCSI_Setup_Window)
        Share_VirtualDisk_Window.title("Share Virtual Disk")
        Share_VirtualDisk_Window.geometry("320x200")
        TargetnameLabel=tk.Label(Share_VirtualDisk_Window,text="Target Name")
        TargetnameLabel.grid(row=0,column=0)
        TargetnameEntry=tk.Entry(Share_VirtualDisk_Window)
        TargetnameEntry.grid(row=0,column=1)
        DiskPathLabel=tk.Label(Share_VirtualDisk_Window,text="Disk Path")
        DiskPathLabel.grid(row=1,column=0)
        DiskPathEntry=tk.Entry(Share_VirtualDisk_Window)
        DiskPathEntry.grid(row=1,column=1)
        UsernameLabel=tk.Label(Share_VirtualDisk_Window,text="User Name")
        UsernameLabel.grid(row=2,column=0)
        UsernameEntry=tk.Entry(Share_VirtualDisk_Window)
        UsernameEntry.grid(row=2,column=1)
        PasswordLabel=tk.Label(Share_VirtualDisk_Window,text="Password")
        PasswordLabel.grid(row=3,column=0)
        PasswordEntry=tk.Entry(Share_VirtualDisk_Window)
        PasswordEntry.grid(row=3,column=1)
        Exit=ttk.Button(Share_VirtualDisk_Window,text="Exit",command=Exit_Window, style='Red.TButton')
        Exit.grid(row=4,column=0,padx=20)
        Share_VDisk_input=ttk.Button(Share_VirtualDisk_Window,text="Finish",command=Share_VDisk_input_Click, style='Green.TButton')
        Share_VDisk_input.grid(row=4,column=1)
    Add_VirtualDisk=ttk.Button(iSCSI_Setup_Window,text="Add VirtualDisk",command=Add_VirtualDisk_Click, style='Custom.TButton')
    Add_VirtualDisk.pack()
    Share_VirtualDisk=ttk.Button(iSCSI_Setup_Window,text="Share VirtualDisk by iSCSI",command=Share_VirtualDisk_Click, style='Custom.TButton')
    Share_VirtualDisk.pack()
def Restart():
    command="shutdown -r -t 0"
    powershell(command)
#----<main>-----
DHCP_Install = ttk.Button(root, text='Install DHCP Feature', command=DHCP_Install_Click, style='Custom.TButton')
DHCP_Install.pack()
DHCP_Uninstall = ttk.Button(root, text='Uninstall DHCP Feature', command=DHCP_Uninstall_Click, style='Custom.TButton')
DHCP_Uninstall.pack()
Setup_DHCP=ttk.Button(root,text="Setup DHCP",command=DHCP_Setup_Click, style='Custom.TButton')
Setup_DHCP.pack()
Remove_DHCP_Scope=ttk.Button(root,text="Remove DHCP Scope",command=Remove_DHCP_Scope_Click, style='Custom.TButton')
Remove_DHCP_Scope.pack()
DNS_Install=ttk.Button(root,text="Install DNS Feature",command=DNS_Install_Click, style='Custom.TButton')
DNS_Install.pack()
DNS_Uninstall=ttk.Button(root,text="Uninstall DNS Feature",command=DNS_Uninstall_Click, style='Custom.TButton')
DNS_Uninstall.pack()
Setup_DNS=ttk.Button(root,text="Setup DNS",command=DNS_Setup_click, style='Custom.TButton')
Setup_DNS.pack()
Install_iSCSITarget=ttk.Button(root,text="Install iSCSI target",command=iSCSI_target_install_click, style='Custom.TButton')
Install_iSCSITarget.pack()
Uninstall_iSCSITarget=ttk.Button(root,text="Unistall iSCSI target",command=iSCSI_target_Uninstall_click, style='Custom.TButton')
Uninstall_iSCSITarget.pack()
Setup_iSCSI_Disk_Share=ttk.Button(root,text="Setup iSCSI Disk Share",command=Setup_iSCSI_Disk_Share_Click, style='Custom.TButton')
Setup_iSCSI_Disk_Share.pack()
Restart_Computer=ttk.Button(root,text="Restart This Computer",command=Restart, style='Custom.TButton')
Restart_Computer.pack()
#----</main>-----
root.mainloop()