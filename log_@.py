from netmiko import ConnectHandler

kich = {'device_type': 'cisco_ios','host':'kichan.com','username': 'kichan', 'password': 'kichan'}  

net_connect = ConnectHandler(**kich)

net_connect.enable()

out = net_connect.send_command('show cdp ne')

print(out)
