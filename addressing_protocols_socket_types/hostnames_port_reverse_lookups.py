# To reverse the service port lookup, use getservbyport()

import socket
from urllib.parse import urlunparse

for port in [ 80, 443, 21, 70, 25, 143, 993, 110, 995 ]:
    print (urlunparse(
        (socket.getservbyport(port), 'python.org', '/', '', '', '')
        ))