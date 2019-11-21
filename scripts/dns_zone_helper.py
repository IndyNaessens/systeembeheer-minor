#!/usr/bin/python3

# imports
from dnszone import dnszone
import sys

def handle_a(subdomain, ip, domain):
  zone = dnszone.zone_from_file(domain, '/etc/bind/zones/db.mrt.' + domain)
  zone.add_name(subdomain + '.' + domain + '.')
  zone.names[subdomain + '.' +  domain + '.'].records('A', create=True).add(ip)

  zone.save(autoserial=True)

# get needed arguments
arguments = sys.argv[1:]

# handle request based on first argument
if arguments[0] == 'A':
  subdomain = arguments[1]
  ip = arguments[2]
  domain = arguments[3]

  handle_a(str(subdomain), str(ip), str(domain))
elif arguments[0] == 'MX':
  print('MX')
elif arguments[0] == 'CNAME':
  print('CNAME')
else:
  print('Wrong argument provided, accepts: A, MX, CNAME')
  sys.exit(0)
