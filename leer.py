import os

a = input('carpeta para tu log-->')
os.makedirs(a) #creamos carpeta con nombre var-->a
os.chdir(a) #entramos al directorio creado 
dd = os.getcwd() #guardamos en dd el directorio en el cual estamos

os.system('dir '+dd) #entramos al directorio

#os.system('telnet 172.18.57.61')
#fichero_log = os.path.join(os.getenv('HOME'), 'irwing-gg.log')


os.system('ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -c aes256-cbc ' +input('usuario-->')+'@172.18.57.61 >> log.txt')
os.system(expect = ('Password: '))
os.system(sendline = ('kichan'))


#os.popen()

