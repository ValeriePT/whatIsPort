whatIsPort
==========

Python script that describes services on ports or shows ports that run a service

The ports are based on wikipedia TCP and UDP ports list @ http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers

Usage
=====
python whatisport.py -p \<protocol type\> -s \<search string\>

Usable types:
  TCP
  UDP
  ALL

search string:
  use a port number 1-65535
  or 
  use service description

you can have this help using 'python whatisport.py -h'

EXAMPLES
========
  python whatisport.py -p TCP -s FTP
  
  python whatisport.py -p UDP -s 123
  
  python whatisport.py -p ALL -s NTP
  
  python whatisport.py .p ALL -s 25
