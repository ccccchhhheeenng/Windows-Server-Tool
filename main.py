import tkinter as tk
import time
import threading
import subprocess
from tkinter import ttk



#                                                 @+      +@       :#.      +@                                                                         
#                                                 @+      +@       :#.      +@                                                                         
#                                                 @+      +@       :#.      +@                                                                         
#               -+.    -+=    .+-     +=.   .=+.  @+ ==   +@  +-   :#.:+.   +@  +:     :+.     :+-      +-       ==       +-     :+.                   
#             :#%@%  -#@@@+  *%@@=  ##@@=  *%@@%  @@#@@#  +@=#@%-  :#=%@%#  +@##@%-   #%@%#   =%@@+   ##@%#:  ###@@#  =#:#@%+   #%@%+#+                
#             @*.   :@@- .= +@.    #@*    :@#  :  @#: @@: +@@  +@: :@+  @@  +@@ :@@: %%: +@. =@- .@+ *@= :%=  @%: @@= +@@  =@: .@*  @@#                
#            =@=    :@=    =@:     #@     @@      @+   @# +@   =@: :@+  %@  +@   =@: @#...@@:%+..:@+ #@...*@  @+   @# +@.  =@: @#    @#                
#            @#     :@=    =@:    -%:     @@      @+   @# +@   =@: :#.  =@  +@   =@: @@@@@@@:@@@@@@+ #@@@@@@  @+   @# +@   =@: @#    @#                
#            @#     :@=    =@:    -%=     @@      @+   @# +@   =@: :#.  =@  +@   =@: @%++++=:@#++++- #@+++++  @+   @# +@   =@: @#    @#                
#            -@=    :@=    :%#     #@     @@-     @+   @# +@   =@: :#.  =@  +@   =@: @#      *%.     #@       @+   @# +@   =@: @@-  *@#                
#             @@%%%  +@%%%* *@%%%+ -@%%%- .@@%%%  @+   @# +@   =@: :#.  =@  +@   =@: :@%%%%  =@%%%%+ .@%%%%:  @+   @# +@   =@: :@@%%#@#                
#              =@@%   +@@%   -@@%=   @@@=   %@@-  @+   @# +@   =@: :#.  =%  +@   =@:  :@@@.   :%@@*    @@@=   @+   @# +@   =@:  :@@= @#                
#                                                                                                                                   -@-                
#                                                                                                                               ====@#                 
#                                                                                                                               @@@@=:                 
#                                                                                                                               ::::     




root = tk.Tk()
root.title('Windows Server Setup')
root.geometry('400x400')
current_interface = list()
#Style
style = ttk.Style()
style.configure('Custom.TButton', font=('Helvetica', 12), foreground='blue', padding=5)
style.configure('Red.TButton', font=('Helvetica', 12), foreground='red', padding=5)
style.configure('Green.TButton', font=('Helvetica', 12), foreground='green', padding=5)

lock_interface=False

#powershell
def powershell(command):
    global lock_interface
    lock_interface=True
    subprocess.run(["powershell.exe", command])
    lock_interface=False

#-----<Interface>-----
def update_interface():
    if lock_interface==True:
        current_interface.pop()
    else:
        for widget in root.winfo_children():
            widget.destroy()
        if len(current_interface)==0:
            setup_main_interface()
        if "DHCP" in current_interface:
            setup_DHCP_interface()
        if "DNS" in current_interface:
            setup_DNS_interface()
        if "RemoveDHCP" in current_interface:
            Remove_DHCP_Scope_interface()
        if "iSCSI" in current_interface:
            Setup_iSCSI_Disk_Share_interface()
def back():
    current_interface.pop()
    update_interface()
def Restart():
    command="shutdown -r -t 0"
    powershell(command)
#---------------------

def DHCP_Setup_Click():
    current_interface.append("DHCP")
    update_interface()
def DNS_Setup_click():
    current_interface.append("DNS")
    update_interface()
def Remove_DHCP_Scope_Click():
    current_interface.append("RemoveDHCP")
    update_interface()
def Setup_iSCSI_Disk_Share_Click():
    current_interface.append("iSCSI")
    update_interface()
#-----
def Foward_Lookup_Zone_Click():
    current_interface.append("Foward_Lookup_Zone")
    update_interface()
def Reverse_Lookup_Zone_Click():
    current_interface.append("Reverse_Lookup_Zone")
    update_interface()
def Set_Fowarder_Click():
    current_interface.append("Set_Fowarder")
    update_interface()
#-----
def Add_DNS_Primary_Zone_Click():
    current_interface.append("Add_DNS_Primary_Zone")
    update_interface()
def Add_DNS_Primary_Record_Click():
    current_interface.append("Add_DNS_Primary_Record")
    update_interface()
def Remove_DNS_Primary_Zone_Click():
    current_interface.append("Remove_DNS_Primary_Zone")
    update_interface()
def Remove_DNS_Primary_Record_Click():
    current_interface.append("Remove_DNS_Primary_Record")
    update_interface()
    
def Add_DNS_Reverse_Zone_Click():
    current_interface.append("Add_DNS_Reverse_Zone")
    update_interface()
def Remove_DNS_Reverse_Zone_Click():
    current_interface.append("Remove_DNS_Reverse_Zone")
    update_interface()
def Add_DNS_PTR_Record_Click():
    current_interface.append("Add_DNS_PTR_Record")
    update_interface()
def Remove_DNS_PTR_Record_Click():
    current_interface.append("Remove_DNS_PTR_Record")
    update_interface()

def Add_VirtualDisk_Click():
    current_interface.append("Add_VirtualDisk")
    update_interface()
def Share_VirtualDisk_Click():
    current_interface.append("Share_VirtualDisk")
    update_interface()

#-----

#-----</Interface>-----

#-----</Main Interface>-----
def setup_main_interface():

#-------<Install tools>-----

    #-----<DHCP_Install>-----
    def DHCP_Install_Click():
        DHCP_install_thread = threading.Thread(target=installing_DHCP)
        DHCP_install_thread.start()
        DHCP_Install.config(text='Installing')

    def installing_DHCP():
        powershell("Install-WindowsFeature -Name 'DHCP' –IncludeManagementTools")
        DHCP_complete_thread = threading.Thread(target=Func_DHCP_complete)
        DHCP_complete_thread.start()
        DHCP_Install.config(text="Finished") 

    def Func_DHCP_complete():
        
        time.sleep(3)
        try:
            DHCP_Install.config(text="Install DHCP Feature")  
        except:
            pass
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
        try:
            DHCP_Uninstall.config(text="Uninstall DHCP Feature")  
        except:
            pass
    #-----</DHCP_Uninstall>-----
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

 
#-------</Install tools>-----

    #-----<Main Window Buttons>-----
    DHCP_Install = ttk.Button(root, text='Install DHCP Feature', command=DHCP_Install_Click, style='Custom.TButton')
    DHCP_Install.pack()
    DHCP_Uninstall = ttk.Button(root, text='Uninstall DHCP Feature', command=DHCP_Uninstall_Click, style='Custom.TButton')
    DHCP_Uninstall.pack()
    Setup_DHCP = ttk.Button(root, text="Setup DHCP", command=DHCP_Setup_Click, style='Custom.TButton')
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
    Restart_Computer=ttk.Button(root,text="Restart This Computer",command=Restart, style='Red.TButton')
    Restart_Computer.pack()
    #-----</Main Window Buttons>-----
#-----</Main Interface>-----

#-----<DHCP Interface>-----
def setup_DHCP_interface():
    def DHCP_Finish_Button():
        DHCP_Setup_thread = threading.Thread(target=DHCP_Finish_Button_Run)
        DHCP_Setup_thread.start()
        read_input.config(text="Please Wait")
        
    #<Get user input data>
    def DHCP_Finish_Button_Run():
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
        back()      
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
    Back = ttk.Button(root, text="Back", command=back, style='Red.TButton')
    Back.grid(row=6, column=0, padx=20)
    read_input=ttk.Button(root, text="Finish", command=DHCP_Finish_Button, style='Green.TButton')
    read_input.grid(row=6,column=1)
#-----</DHCP Interface>-----


def Remove_DHCP_Scope_interface():
    def DHCP_Finish_Button():
        DHCP_Setup_Thread=threading.Thread(target=DHCP_Finish_Button_Run)
        read_input.config(text="Please Wait")
        DHCP_Setup_Thread.start()
    def DHCP_Finish_Button_Run():
        ScopeID=ScopeIDentry.get()
        command="Remove-DhcpServerv4Scope -ScopeId "+ScopeID
        powershell(command)
        back()

    ScopeIDlabel = tk.Label(root, text='ScopeID:')
    ScopeIDlabel.grid(row=0, column=0)
    ScopeIDentry = tk.Entry(root)
    ScopeIDentry.grid(row=0, column=1)
    Back=ttk.Button(root, text="Back", command=back, style='Red.TButton')
    Back.grid(row=6,column=0,padx=20)
    read_input=ttk.Button(root, text="Finish", command=DHCP_Finish_Button, style='Green.TButton')
    read_input.grid(row=6,column=1) 
def setup_DNS_interface():
    if "Foward_Lookup_Zone" in current_interface:
        if "Add_DNS_Primary_Zone" in current_interface:
            def Add_Primary_Zone_Click():
                DNS_install_thread = threading.Thread(target=Adding_Zone)
                DNS_install_thread.start()
                Add_Primart_Zone_input.config(text="Please Wait")
            def Adding_Zone():
                ZoneName=ZoneNameEntry.get()
                ZoneFile=ZoneName+".dns"
                command="Add-DnsServerPrimaryZone -Name "+ZoneName+" -ZoneFile "+ZoneFile
                powershell(command)
                back()
            ZoneNamelabel=tk.Label(root,text="Zone Name")
            ZoneNamelabel.grid(row=0,column=0)
            ZoneNameEntry=tk.Entry(root)
            ZoneNameEntry.grid(row=0,column=1)
            Back=ttk.Button(root,text="Back",command=back, style='Red.TButton')
            Back.grid(row=1,column=0,padx=20)
            Add_Primart_Zone_input=ttk.Button(root,text="Finish",command=Add_Primary_Zone_Click, style='Green.TButton')
            Add_Primart_Zone_input.grid(row=1,column=1)
        elif "Add_DNS_Primary_Record" in current_interface:
            def DNS_Record_input_Click():
                tmp=Set_Record_Type.get()
                for widget in root.winfo_children():
                    widget.destroy()
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
                        update_interface()
                    Name_Label=tk.Label(root,text="Name:")
                    Name_Label.grid(row=0,column=0)
                    Name_Entry=tk.Entry(root)
                    Name_Entry.grid(row=0,column=1)
                    IPv4Address_Label=tk.Label(root,text="IPv4Address:")
                    IPv4Address_Label.grid(row=1,column=0)
                    IPv4Address_Entry=tk.Entry(root)
                    IPv4Address_Entry.grid(row=1,column=1)
                    Back=ttk.Button(root,text="Back",command=update_interface, style='Red.TButton')
                    Back.grid(row=2,column=0,padx=20)
                    A_input=ttk.Button(root,text="Finish",command=A_input_Click, style='Green.TButton')
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
                        update_interface()
                    Name_Label=tk.Label(root,text="Name:")
                    Name_Label.grid(row=0,column=0)
                    Name_Entry=tk.Entry(root)
                    Name_Entry.grid(row=0,column=1)
                    IPv6Address_Label=tk.Label(root,text="IPv6Address:")
                    IPv6Address_Label.grid(row=1,column=0)
                    IPv6Address_Entry=tk.Entry(root)
                    IPv6Address_Entry.grid(row=1,column=1)
                    Back=ttk.Button(root,text="Back",command=update_interface, style='Red.TButton')
                    Back.grid(row=2,column=0,padx=20)
                    AAAA_input=ttk.Button(root,text="Finish",command=AAAA_input_Click, style='Green.TButton')
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
                        update_interface()
                    Name_Label=tk.Label(root,text="Name:")
                    Name_Label.grid(row=0,column=0)
                    Name_Entry=tk.Entry(root)
                    Name_Entry.grid(row=0,column=1)
                    HostNameAlias_Label=tk.Label(root,text="HostNameAlias:")
                    HostNameAlias_Label.grid(row=1,column=0)
                    HostNameAlias_Entry=tk.Entry(root)
                    HostNameAlias_Entry.grid(row=1,column=1)
                    Back=ttk.Button(root,text="Back",command=update_interface, style='Red.TButton')
                    Back.grid(row=2,column=0,padx=20)
                    CName_input=ttk.Button(root,text="Finish",command=CName_input_Click, style='Green.TButton')
                    CName_input.grid(row=2,column=1)
            Set_Zone_Label=tk.Label(root,text="Set Zone:")
            Set_Zone_Label.grid(row=0,column=0,)
            Set_Zone_Entry=tk.Entry(root)
            Set_Zone_Entry.grid(row=0,column=1)
            #---<!!!!!!!需合併column!!!!!>---
            Set_Record_Type_Label = ttk.Label(root, text="Record Type:")
            Set_Record_Type_Label.grid(row=1, column=0)
            Set_Record_Type=ttk.Combobox(root,values=["A","AAAA","CName"])
            Set_Record_Type.grid(row=1, column=1)
            Back=ttk.Button(root,text="Back",command=back, style='Red.TButton')
            Back.grid(row=2,column=0,padx=20)
            DNS_Record_input=ttk.Button(root,text="Next",command=DNS_Record_input_Click, style='Green.TButton')
            DNS_Record_input.grid(row=2,column=1)
        elif "Remove_DNS_Primary_Zone" in current_interface:
            def DNS_Finish_Button():
                DNS_Remove_thread=threading.Thread(target=Remove_Start)
                DNS_Remove_thread.start()
                read_input.config(text="Please Wait")
            def Remove_Start():
                Zone=ZoneNameentry.get()
                command="Remove-DnsServerZone -Name "+Zone+" -Force"
                powershell(command)
                back()               
            ZoneNamelabel = tk.Label(root, text='ZoneName:')
            ZoneNamelabel.grid(row=0, column=0)
            ZoneNameentry = tk.Entry(root)
            ZoneNameentry.grid(row=0, column=1)
            Back=ttk.Button(root, text="Back", command=back, style='Red.TButton')
            Back.grid(row=6,column=0,padx=20)
            read_input=ttk.Button(root, text="Finish", command=DNS_Finish_Button, style='Green.TButton')
            read_input.grid(row=6,column=1)  
        elif "Remove_DNS_Primary_Record" in current_interface:
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
                back()
            ZoneNamelabel = tk.Label(root, text='ScopeID:')
            ZoneNamelabel.grid(row=0, column=0)
            ZoneNameentry = tk.Entry(root)
            ZoneNameentry.grid(row=0, column=1)
            RecordNamelabel = tk.Label(root, text='RecordName:')
            RecordNamelabel.grid(row=1, column=0)
            RecordNameentry = tk.Entry(root)
            RecordNameentry.grid(row=1, column=1)
            Set_Record_Type_label=tk.Label(root,text="Type")
            Set_Record_Type_label.grid(row=2,column=0)
            Set_Record_Type=ttk.Combobox(root,values=["A","AAAA","CName"])
            Set_Record_Type.grid(row=2,column=1)
            Back=ttk.Button(root, text="Back", command=back, style='Red.TButton')
            Back.grid(row=6,column=0,padx=20)
            read_input=ttk.Button(root, text="Finish", command=DNS_Finish_Button, style='Green.TButton')
            read_input.grid(row=6,column=1)    
        else:
            Add_Primary_Zone_Button=ttk.Button(root,text="Add Primary Zone",command=Add_DNS_Primary_Zone_Click, style='Custom.TButton')
            Add_Primary_Zone_Button.pack()           
            Add_DNS_Record_Button=ttk.Button(root,text="Add DNS Record",command=Add_DNS_Primary_Record_Click, style='Custom.TButton')
            Add_DNS_Record_Button.pack()
            Remove_DNS_Zone_Button=ttk.Button(root,text="Remove DNS Zone",command=Remove_DNS_Primary_Zone_Click, style='Custom.TButton')
            Remove_DNS_Zone_Button.pack()
            Remove_DNS_Record_Button=ttk.Button(root,text="Remove DNS Recoed",command=Remove_DNS_Primary_Record_Click, style='Custom.TButton')
            Remove_DNS_Record_Button.pack()
            Back=ttk.Button(root,text="Back",command=back, style='Red.TButton')
            Back.pack() 
    elif "Reverse_Lookup_Zone" in current_interface:
        if "Add_DNS_Reverse_Zone" in current_interface:
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
                back()
            NetworkID_Label=tk.Label(root,text="NetworkID:")
            NetworkID_Label.grid(row=0,column=0)
            NetworkID_Entry=tk.Entry(root)
            NetworkID_Entry.grid(row=0,column=1)
            Exit=ttk.Button(root,text="Exit",command=back, style='Red.TButton')
            Exit.grid(row=1,column=0,padx=20)
            Add_Reverse_Zone_input=ttk.Button(root,text="Finish",command=Add_Reverse_Zone_input_Click, style='Green.TButton')
            Add_Reverse_Zone_input.grid(row=1,column=1)
        elif "Remove_DNS_Reverse_Zone" in current_interface:
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
                back()
            NetworkID_Label=tk.Label(root,text="NetworkID:")
            NetworkID_Label.grid(row=0,column=0)
            NetworkID_Entry=tk.Entry(root)
            NetworkID_Entry.grid(row=0,column=1)
            Exit=ttk.Button(root,text="Exit",command=back, style='Red.TButton')
            Exit.grid(row=1,column=0,padx=20)
            Add_Reverse_Zone_input=ttk.Button(root,text="Finish",command=Remove_Reverse_Zone_input_Click, style='Green.TButton')
            Add_Reverse_Zone_input.grid(row=1,column=1)
        elif "Add_DNS_PTR_Record" in current_interface:
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
                back()
            Name_Label=tk.Label(root,text="Name:")
            Name_Label.grid(row=0,column=0)
            name_Entry=tk.Entry(root)
            name_Entry.grid(row=0,column=1)
            ZoneName_ID_Label=tk.Label(root,text="ZoneName(ID):")
            ZoneName_ID_Label.grid(row=1,column=0)
            ZoneName_Entry=tk.Entry(root)
            ZoneName_Entry.grid(row=1,column=1)
            PTRDomainName_Label=tk.Label(root,text="PTRDomainName:")
            PTRDomainName_Label.grid(row=2,column=0)
            PTRDomainName_Entry=tk.Entry(root)
            PTRDomainName_Entry.grid(row=2,column=1)
            Exit=ttk.Button(root,text="Exit",command=back, style='Red.TButton')
            Exit.grid(row=3,column=0,padx=20)
            Add_PTR_Record_input=ttk.Button(root,text="Finish",command=Add_PTR_Record_input_Click, style='Green.TButton')
            Add_PTR_Record_input.grid(row=3,column=1)
        elif "Remove_DNS_PTR_Record" in current_interface:
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
                back()
            Name_Label=tk.Label(root,text="Name:")
            Name_Label.grid(row=0,column=0)
            name_Entry=tk.Entry(root)
            name_Entry.grid(row=0,column=1)
            ZoneName_Label=tk.Label(root,text="ZoneName(ID):")
            ZoneName_Label.grid(row=1,column=0)
            ZoneName_Entry=tk.Entry(root)
            ZoneName_Entry.grid(row=1,column=1)
            Exit=ttk.Button(root,text="Exit",command=back, style='Red.TButton')
            Exit.grid(row=2,column=0,padx=20)
            Remove_PTR_Record_input=ttk.Button(root,text="Finish",command=Remove_PTR_Record_input_Click, style='Green.TButton')
            Remove_PTR_Record_input.grid(row=2,column=1)
        else:
            Add_Zone_Button=ttk.Button(root,text="Add Zone",command=Add_DNS_Reverse_Zone_Click, style='Custom.TButton')
            Add_Zone_Button.pack()
            Remove_Zone_Button=ttk.Button(root,text="Remove Zone",command=Remove_DNS_Reverse_Zone_Click, style='Custom.TButton')
            Remove_Zone_Button.pack()
            Add_PTR_Record_Button=ttk.Button(root,text="Add PTR Record",command=Add_DNS_PTR_Record_Click, style='Custom.TButton')
            Add_PTR_Record_Button.pack()
            Remove_PTR_Record_Button=ttk.Button(root,text="Remove PTR Record",command=Remove_DNS_PTR_Record_Click, style='Custom.TButton')
            Remove_PTR_Record_Button.pack()
            Back=ttk.Button(root,text="Back",command=back, style='Red.TButton')
            Back.pack()
    elif "Set_Fowarder" in current_interface:
        def input_click():
            DNS_install_thread = threading.Thread(target=Setting_Fowarder)
            DNS_install_thread.start()
            Fowarder_input.config(text="Please Wait")
        def Setting_Fowarder():
            Address=AddressEntry.get()
            command="Set-DnsServerForwarder -IPAddress "+Address
            powershell(command)
            back()
        Addresslabel=tk.Label(root,text="IPAddress")
        Addresslabel.grid(row=0,column=0)
        AddressEntry=tk.Entry(root)
        AddressEntry.grid(row=0,column=1)
        Back=ttk.Button(root,text="Back",command=back, style='Red.TButton')
        Back.grid(row=1,column=0,padx=20)
        Fowarder_input=ttk.Button(root,text="Finish",command=input_click, style='Green.TButton')
        Fowarder_input.grid(row=1,column=1)
    else:
        Foward_Lookup_Zone=ttk.Button(root,text="Foward Look Zone Settings",command=Foward_Lookup_Zone_Click, style='Custom.TButton')
        Foward_Lookup_Zone.pack()
        Reverse_Lookup_Zone=ttk.Button(root,text="Reverse Look Zone Settings",command=Reverse_Lookup_Zone_Click, style='Custom.TButton')
        Reverse_Lookup_Zone.pack()
        Set_Fowarder=ttk.Button(root,text="Set Fowarder",command=Set_Fowarder_Click, style='Custom.TButton')
        Set_Fowarder.pack()
        Back=ttk.Button(root,text="Back",command=back, style='Red.TButton')
        Back.pack() 

def Setup_iSCSI_Disk_Share_interface():

    if "Add_VirtualDisk" in current_interface:
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
            back()
        VDisk_PathLabel=tk.Label(root,text="VDisk Path")
        VDisk_PathLabel.grid(row=0,column=0)
        VDisk_PathEntry=tk.Entry(root)
        VDisk_PathEntry.grid(row=0,column=1)
        VDisk_NameLabel=tk.Label(root,text="VDisk Name(Ex:DiskName.vhdx)")
        VDisk_NameLabel.grid(row=1,column=0)
        VDisk_NameEntry=tk.Entry(root)
        VDisk_NameEntry.grid(row=1,column=1)
        VDisk_SizeLabel=tk.Label(root,text="VDisk Size(Ex:10GB)")
        VDisk_SizeLabel.grid(row=2,column=0)
        VDisk_SizeEntry=tk.Entry(root)
        VDisk_SizeEntry.grid(row=2,column=1)
        Exit=ttk.Button(root,text="Exit",command=back, style='Red.TButton')
        Exit.grid(row=3,column=0,padx=20)
        Add_VDisk_input=ttk.Button(root,text="Finish",command=Add_VDisk_input_Click, style='Green.TButton')
        Add_VDisk_input.grid(row=3,column=1)
    elif "Share_VirtualDisk" in current_interface:
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
            command2="$User11=\""+user+"\";$PWord = ConvertTo-SecureString -String \""+pword+"\" -AsPlainText -Force;$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $User, $PWord;Set-IscsiServerTarget -TargetName "+target+" -EnableChap $True -Chap $Credential"
            powershell(command2)
            back()
        TargetnameLabel=tk.Label(root,text="Target Name")
        TargetnameLabel.grid(row=0,column=0)
        TargetnameEntry=tk.Entry(root)
        TargetnameEntry.grid(row=0,column=1)
        DiskPathLabel=tk.Label(root,text="Disk Path")
        DiskPathLabel.grid(row=1,column=0)
        DiskPathEntry=tk.Entry(root)
        DiskPathEntry.grid(row=1,column=1)
        UsernameLabel=tk.Label(root,text="User Name")
        UsernameLabel.grid(row=2,column=0)
        UsernameEntry=tk.Entry(root)
        UsernameEntry.grid(row=2,column=1)
        PasswordLabel=tk.Label(root,text="Password")
        PasswordLabel.grid(row=3,column=0)
        PasswordEntry=tk.Entry(root)
        PasswordEntry.grid(row=3,column=1)
        Exit=ttk.Button(root,text="Exit",command=back, style='Red.TButton')
        Exit.grid(row=4,column=0,padx=20)
        Share_VDisk_input=ttk.Button(root,text="Finish",command=Share_VDisk_input_Click, style='Green.TButton')
        Share_VDisk_input.grid(row=4,column=1)
    else:
        Add_VirtualDisk_Button=ttk.Button(root,text="Add VirtualDisk",command=Add_VirtualDisk_Click, style='Custom.TButton')
        Add_VirtualDisk_Button.pack()
        Share_VirtualDisk=ttk.Button(root,text="Share VirtualDisk by iSCSI",command=Share_VirtualDisk_Click, style='Custom.TButton')
        Share_VirtualDisk.pack()
        Back=ttk.Button(root,text="Back",command=back, style='Red.TButton')
        Back.pack() 

setup_main_interface()
root.mainloop()

#                               .__    .__    .__    .__                   
#  ____  ____  ____  ____  ____ |  |__ |  |__ |  |__ |  |__   ____   ____    ____   ____   ____    ____  
#_/ ___\/ ___\/ ___\/ ___\/ ___\|  |  \|  |  \|  |  \|  |  \_/ __ \_/ __ \ _/ __ \ /    \ /    \  / ___\ 
#\  \__\  \__\  \__\  \__\  \___|   Y  \   Y  \   Y  \   Y  \  ___/\  ___/ \  ___/|   |  \   |  \/ /_/  >
# \___  >___  >___  >___  >___  >___|  /___|  /___|  /___|  /\___  >\___  > \___  >___|  /___|  /\___  / 
#                                                                                                _____/  