#!/usr/bin/python3

### THIS SCRIPT ONLY SUPPORTS DOMAINS CREATED BY THE SCRIPT LOCATED AT:
### /etc/scripts/dns_add_zone

# imports
from dnszone import dnszone
import sys

def handle_a(subdomain, ip, domain):
  zone = dnszone.zone_from_file(domain, '/etc/bind/zones/db.mrt.' + domain)
  zone.add_name(subdomain + '.' + domain + '.')
  zone.names[subdomain + '.' +  domain + '.'].records('A', create=True).add(ip)

  zone.save(autoserial=True)

def handle_cname(alias, host_domain):
  domain = '.'.join(host_domain.split('.')[1:-1]) + '.be'

  zone = dnszone.zone_from_file(domain, '/etc/bind/zones/db.mrt.' + domain)
  zone.add_name(alias + '.' + domain + '.')
  zone.names[alias + '.' + domain + '.'].records('CNAME', create=True).add(host_domain + '.')

  zone.save(autoserial=True)

def handle_mx(mx_name, ip, domain):
  zone = dnszone.zone_from_file(domain, '/etc/bind/zones/db.mrt.' + domain)
  zone.names[domain + '.'].records('MX', create=True).add((10, mx_name))

  zone.save(autoserial=True)

# get needed arguments
arguments = sys.argv[1:]

# handle request based on first argument
if arguments[0] == 'A':
  subdomain = str(arguments[1])
  ip = str(arguments[2])
  domain = str(arguments[3])

  handle_a(subdomain, ip, domain)
elif arguments[0] == 'MX':
  mx_name = str(arguments[1])
  ip = str(arguments[2])
  domain = str(arguments[3])

  handle_a(mx_name, ip, domain)
  handle_mx(mx_name, ip, domain)
elif arguments[0] == 'CNAME':
  alias = str(arguments[1])
  host_domain = str(arguments[2])

  handle_cname(alias, host_domain)
else:
  print('Wrong argument provided, accepts: A, MX, CNAME')
  sys.exit(0)
