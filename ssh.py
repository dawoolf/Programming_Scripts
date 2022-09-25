#!/usr/binenv python

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('localhost', username='demo', password='demo123')

stdin, stout, stderr - ssh.exec_command('cat /etc/passwd')

for line in stdout.readlines() :
	print line.strip()

ssh.close()
