#!/usr/bin/python3

# imports
from dnszone import dnszone
import sys

arguments = sys.argv[1:]

if arguments[0] == 'NS':
  print('NS')
elif arguments[0] == 'A':
  print('A')
elif arguments[0] == 'MX':
  print('MX')
elif arguments[0] == 'CNAME':
  print('CNAME')
else:
  print('Wrong argument provided, accepts: NS, A, MX, CNAME')
  sys.exit(0)

# zone = dnszone.zone_from_file('indy-naessens.sb.uclllabs.be', '/etc/bind/zones/db.indy-naessens.sb.uclllabs.be')

