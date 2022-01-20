ifconfig eth0:10 192.168.0.2 up
arping -c 1 -U -s 192.168.0.2 192.168.0.1
nc -ul 8000