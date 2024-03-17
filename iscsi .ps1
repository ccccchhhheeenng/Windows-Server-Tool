Install-WindowsFeature -Name FS-iSCSITarget-Server
New-IscsiVirtualDisk -Path C:\iSCSIVirtualDisks\iscsiDisk2.vhdx -Size 200GB
New-IscsiServerTarget -TargetName "T1"
Add-IscsiVirtualDiskTargetMapping -TargetName "T1" -DevicePath "path"
Set-IscsiServerTarget -TargetName "Test" -InitiatorId "IQN:*"
#chap
$User = "Domain01\User01"
$PWord = ConvertTo-SecureString -String "P@sSwOrd" -AsPlainText -Force#12~16
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $User, $PWord
Set-IscsiServerTarget -TargetName "T1" -EnableChap $True -Chap $Credential