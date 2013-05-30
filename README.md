whatIsPort
==========

Python script that describes services on ports or shows ports that run a service

The ports are based on wikipedia TCP and UDP ports list @ http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers

Usage
=====
python whatisport.py <type> <port/descr>

Usable types:
  TCP
  UDP
  ALL

port/descr:
  use a port number 1-65535
  or 
  use service description

EXAMPLES
========
  python whatisport.py TCP FTP
  
  python whatisport.py UDP 123
  
  python whatisport.py ALL NTP
  
  python whatisport.py ALL 25
