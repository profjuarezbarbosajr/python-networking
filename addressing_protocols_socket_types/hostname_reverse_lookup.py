# when address is available...
# www.ibm.com

import socket

hostname, aliases, addresses = socket.gethostbyaddr('23.40.219.62')

print ('Hostname :', hostname)
print ('Aliases  :', aliases)
print ('Addresses:', addresses)