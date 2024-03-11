#power by ccccchhhheeenng
#2024/03/12 01:04
#                                      @+      +@       :#.      +@
#                                      @+      +@       :#.      +@
#                                      @+      +@       :#.      +@
#    -+.    -+=    .+-     +=.   .=+.  @+ ==   +@  +-   :#.:+.   +@  +:     :+.     :+-      +-       ==       +-     :+.
#  :#%@%  -#@@@+  *%@@=  ##@@=  *%@@%  @@#@@#  +@=#@%-  :#=%@%#  +@##@%-   #%@%#   =%@@+   ##@%#:  ###@@#  =#:#@%+   #%@%+#+
#  @*.   :@@- .= +@.    #@*    :@#  :  @#: @@: +@@  +@: :@+  @@  +@@ :@@: %%: +@. =@- .@+ *@= :%=  @%: @@= +@@  =@: .@*  @@#
# =@=    :@=    =@:     #@     @@      @+   @# +@   =@: :@+  %@  +@   =@: @#...@@:%+..:@+ #@...*@  @+   @# +@.  =@: @#    @#
# @#     :@=    =@:    -%:     @@      @+   @# +@   =@: :#.  =@  +@   =@: @@@@@@@:@@@@@@+ #@@@@@@  @+   @# +@   =@: @#    @#
# @#     :@=    =@:    -%=     @@      @+   @# +@   =@: :#.  =@  +@   =@: @%++++=:@#++++- #@+++++  @+   @# +@   =@: @#    @#
# -@=    :@=    :%#     #@     @@-     @+   @# +@   =@: :#.  =@  +@   =@: @#      *%.     #@       @+   @# +@   =@: @@-  *@#
#  @@%%%  +@%%%* *@%%%+ -@%%%- .@@%%%  @+   @# +@   =@: :#.  =@  +@   =@: :@%%%%  =@%%%%+ .@%%%%:  @+   @# +@   =@: :@@%%#@#
#   =@@%   +@@%   -@@%=   @@@=   %@@-  @+   @# +@   =@: :#.  =%  +@   =@:  :@@@.   :%@@*    @@@=   @+   @# +@   =@:  :@@= @#
#                                                                                                                        -@-
#                                                                                                                    ====@#
#                                                                                                                    @@@@=:
#                                                                                                                    ::::
#--------------------
$Scope="192.168.0.0"
$StartRange="192.168.0.100"
$EndRange="192.168.0.150"
$SubnetMask="255.255.255.0"
$ScopeName="DHCP"
$DNS_Address="1.1.1.1"
#config

Install-WindowsFeature -Name 'DHCP' –IncludeManagementTools
#install Feature in server

Add-DhcpServerV4Scope -Name $ScopeName -StartRange $StartRange -EndRange $EndRange -SubnetMask $SubnetMask
#add scope

Set-DhcpServerv4OptionValue -ScopeID $Scope -OptionId 6 -Value $DNS_Address
#DNS Setting (also can use "-Router" to add gateway)

Add-DhcpServerv4ExclusionRange -ScopeId $Scope -StartRange 192.168.0.101 -EndRange 192.168.0.110
#Add exclusive range
