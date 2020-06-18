# dev_nirqa_xtn

import re
import io
import os
from netmiko import ConnectHandler
from netmiko import Netmiko
#instalar para front-> pip install pyfiglet
import pyfiglet

saludo = pyfiglet.figlet_format("Hello!!")
print(saludo)

#-----------------------------------------------------------------------#
#poner ip de los routers a analizar
ip_host = ['10.1.1.1', '10.1.2.2', '10.1.3.3', '10.1.4.4']

#__ref_Omar_____________________________________________________________#

def read_variables(file_input):
    router = {}
    with open(file_input) as f:
        for line in f:
            (k, v) = line.split(':')
            router[k] = v[:-1]
    return router

def get_lldp_neighbors(input_cmd):
    parser = input_cmd.split('\n')
    lldp_neighbors_no_headers = parser[5:len(parser)-2]
    return lldp_neighbors_no_headers

def neighbors_routers( lldp_preformatted ):
    router_neighbors = []
    for line in lldp_preformatted:
        tmp = line.split()
        router_neighbors = router_neighbors + [tmp]
    return router_neighbors

def print_output(dyct_input):
    
    print('-'*80)
    print("{:*^20}{:*^20}{:*^20}{:*^20}".format("Hostname", "Local Interface", "Neighbor", "Neighbor Interface"))
    print('-'*80)
    for k,v in dyct_output.items():
        i=0
        while i <  len(v):
            print("{:^20}{:^20}{:^20}{:^20}".format(k, v[i][1]+' '+v[i][2], v[i][0], v[i][8]+' '+v[i][9]))
            i = i+1 
    print('-'*80)
    return

def get_output(device_id, send_command):
    net_conn = Netmiko(**device_id)
    output = net_conn.send_command(send_command)
    return output

#_______________________________________________________________________#
#poner dentro de ssh1 parametros de conectividad configurado
for ip in ip_host:
    ssh1 = {'device_type':'cisco_ios','host': ip,
            'username': 'kichan','password': 'kichan',}
    
    net_connect = ConnectHandler(**ssh1)

    find_hostname = net_connect.find_prompt()
    
    hostname1 = find_hostname.replace(">","")
    
    hhnn1 = pyfiglet.figlet_format(str(hostname1))
    print('buscando vecinos de: {}'.format(str(hostname1)),hhnn1, sep='\n'+'\n'+8*'-'+'\n')

    output = net_connect.send_command('show cdp n')
    tot = hostname1 + '\n' + output
    file = open('log_cdp.txt','w')
    file.write(tot)
    file.close()
    
    r_i = get_output(ssh1,'show cdp ne')

    dyct_output = {}

    lldp_neighbors1 = get_lldp_neighbors(r_i)

    dyct_output[hostname1] = neighbors_routers(lldp_neighbors1)

    print_output(dyct_output)
