$TTL	300
@	IN	SOA	ns.indy-naessens.sb.uclllabs.be. admin.indy-naessens.sb.uclllabs.be. (
		     1222220 ;Serial
			    300	;Refresh
			  86400	;Retry
			2419200	;Expire
			  300 );Negative Cache TTL
; Name servers
@       IN      NS      ns.indy-naessens.sb.uclllabs.be.
@       IN      NS      ns1.uclllabs.be.
@       IN      NS      ns2.uclllabs.be.
@	IN	NS	ns.arthur-joppart.sb.uclllabs.be.

; A , AAAA records for name servers
ns	IN	A	193.191.177.148
ns	IN	AAAA	2001:6a8:2880:a077::94
ns.arthur-joppart.sb.uclllabs.be.	IN	A	193.191.177.133

; A , AAAA records for apache
@	IN	A	193.191.177.148
@	IN      AAAA    2001:6a8:2880:a077::94

www	IN	A	193.191.177.148
www	IN      AAAA    2001:6a8:2880:a077::94

www1	IN	A	193.191.177.148
www1	IN      AAAA    2001:6a8:2880:a077::94

www2	IN	A	193.191.177.148
www2	IN      AAAA    2001:6a8:2880:a077::94

secure	IN	A	193.191.177.148
secure	IN      AAAA    2001:6a8:2880:a077::94

supersecure	IN	A	193.191.177.148
supersecure	IN      AAAA    2001:6a8:2880:a077::94

; Test A, AAAA record
test    IN      A       193.191.177.254

; MX records
@	IN	MX	10	mx.indy-naessens.sb.uclllabs.be.

; A, AAAA records for mx
mx	IN	A	193.191.177.148
mx	IN      AAAA    2001:6a8:2880:a077::94

; CAA records
@	IN	CAA	0 issue "letsencrypt.org"
@	IN	CAA	0 iodef "mailto:indy.naessens@student.ucll.be"

; mrt
subzonedahx4x       IN      NS      ns.indy-naessens.sb.uclllabs.be.
