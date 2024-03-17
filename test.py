            def DNS_Finish_Button():
                Zone=ZoneNameentry.get()
                command="Remove-DnsServerZone -Name "+Zone
                powershell(command)
            def DNS_Setup_Exit():
                Remove_DNS_Record_Window.destroy()
            Remove_DNS_Record_Window=tk.Toplevel(Foward_Lookup_Zone_Window)
            Remove_DNS_Record_Window.geometry("200x200")
            ZoneNamelabel = tk.Label(Remove_DNS_Record_Window, text='ScopeID:')
            ZoneNamelabel.grid(row=0, column=0)
            ZoneNameentry = tk.Entry(Remove_DNS_Record_Window)
            ZoneNameentry.grid(row=0, column=1)
            Exit=ttk.Button(Remove_DNS_Record_Window, text="Exit", command=DNS_Setup_Exit, style='Red.TButton')
            Exit.grid(row=6,column=0,padx=20)
            read_input=ttk.Button(Remove_DNS_Record_Window, text="Finish", command=DNS_Finish_Button, style='Green.TButton')
            read_input.grid(row=6,column=1)  