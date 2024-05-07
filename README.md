
<div align="center">  
    <a href="https://github.com/ccccchhhheeenng/Python-GUI--Setup-Windows-Server-with-python/stargazers"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/ccccchhhheeenng/Python-GUI--Setup-Windows-Server-with-python"></a>
    <a href="https://twitter.com/ccccchhhheeenng"><img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/ccccchhhheeenng"></a>
</div>

# Setup-Windows-Server-with-python
- [Downloads](https://github.com/ccccchhhheeenng/Python-GUI--Setup-Windows-Server-with-python/raw/main/Application.exe)


## Releases
### v 1.0.0
release at 2024/04/05

<a href="https://github.com/ccccchhhheeenng/Python-GUI--Setup-Windows-Server-with-python/raw/main/Application.exe">Windows Executeable Download</a>

<a href="https://github.com/ccccchhhheeenng/Python-GUI--Setup-Windows-Server-with-python/raw/main/main.py">Source Code</a>

## How to use
<p style="color: red;font-size: x-large;"> Warning</p>
<p style="color: red;font-size: large;">This app can only run on Windows Server</p>

### Install step:

1.Download the latest releast

2.open it and enjoy the app
### DHCP
<p style="color: red;font-size: medium;">Please Install DHCP Feature Before Setup</p>

Input the config and press Finish to setup
:::spoiler Example
```
StartRange:  192.168.0.100
EndRange:    192.168.0.200
SubnetMask:  255.255.255.0
ScopeName:   DHCP_Scope
DNS Address: 1.1.1.1
Router IP:   192.168.0.1
```


:::

![image](https://hackmd.io/_uploads/B1uzlprM0.png)

### DNS
<p style="color: red;font-size: medium;">Please Install DNS Feature Before Setup</p>

>Foward lookup:
:::spoiler Add Primary Zone
This Function can Add DNS Zone

Example:
```
Zone Name:hello.world
```
![image](https://hackmd.io/_uploads/SyY5MTHfA.png)

:::

:::spoiler Add DNS Record
This Function can Add DNS Record

Suuport Record type:A、AAAA、CNAME

Step:

1.Enter the zone that you want to add DNS Record

![image](https://hackmd.io/_uploads/Sk4drTBzR.png)

2.Enter ther Record Name and IP address

![image](https://hackmd.io/_uploads/B14cSpHzC.png)

Example:
```
1.
Set Zone:    hello.world
Record Type: A
2.
Name:       aaa
IP Address: 127.0.0.1
```

:::

:::spoiler Remove Primary Zone
:::
:::spoiler Remove DNS Record
:::
<br>

>Reverse lookup:

>Set Fowarder:
