import socket

for host in [ 'localhost', 'www.ibm.com' ]:
    print ('%6s : %s' % (host, socket.getfqdn(host)))