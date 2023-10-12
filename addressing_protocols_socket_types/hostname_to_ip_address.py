import socket

for host in [ 'www.google.com', 'www.ibm.com', 'www.python.org', 'localhost', 'nosuchdns' ]:
    try:
        print ('%15s : %s' % (host, socket.gethostbyname(host)))
    except socket.error:
        print (socket.error)