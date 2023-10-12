# In addition to an IP address, each socket address includes an integer port number.
# Some of the port numbers are pre-allocated for specific network protocols 
# As an example, communication between email servers using SMTP occurs over port number 25 using TCP
# web clients and servers use port 80 for HTTP, etc
# Port numbers for network services with standardized names can be looked up with getservbyname()

import socket
from urllib.parse import urlparse

for url in [ 'http://www.python.org',
             'https://www.ibm.com',
             'ftp://prep.ai.mit.edu',
             'gopher://gopher.micro.umn.edu',
             'smtp://mail.example.com',
             'imap://mail.example.com',
             'imaps://mail.example.com',
             'pop3://pop.example.com',
             'pop3s://pop.example.com',
             ]:
    parsed_url = urlparse(url)
    port = socket.getservbyname(parsed_url.scheme)
    print ('%6s : %s' % (parsed_url.scheme, port))