import socket

for host in [ 'www.google.com', 'www.ibm.com', 'www.python.org', 'localhost', 'nosuchdns' ]:
    print (host)
    try:
        hostname, aliases, addresses = socket.gethostbyname_ex(host)
        print ('  Hostname:', hostname)
        print ('  Aliases :', aliases)
        print (' Addresses:', addresses)
    except socket.error:
        print (socket.error)
