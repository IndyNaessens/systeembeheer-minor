$TTL	1
@	IN	SOA	ns.indy-naessens.sb.uclllabs.be. admin.indy-naessens.sb.uclllabs.be. (
			 111133		; Serial
			    300		; Refresh
			  86400		; Retry
			2419200		; Expire
			  86400 )	; Negative Cache TTL
; Name servers
@       IN      NS      ns.indy-naessens.sb.uclllabs.be.
@       IN      NS      ns1.uclllabs.be.
@       IN      NS      ns2.uclllabs.be.

; A records for name servers
ns	IN	A	193.191.177.148

; A records for apache
@	IN	A	193.191.177.148
www	IN	A	193.191.177.148
www1	IN	A	193.191.177.148
www2	IN	A	193.191.177.148
secure	IN	A	193.191.177.148
supersecure	IN	A	193.191.177.148

; Test A record
test    IN      A       193.191.177.254

; MX records
@	IN	MX	10	mx.indy-naessens.sb.uclllabs.be.

; A records for mx
mx	IN	A	193.191.177.148

; CAA records
@	IN	CAA	0 issue "letsencrypt.org"
@	IN	CAA	0 iodef "mailto:indy.naessens@student.ucll.be"
