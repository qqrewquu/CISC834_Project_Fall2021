#!/usr/bin/env python

# Usage:
# This script will generate two files(vpnup and vpndown) after executing.
# Do chmod a+x on the two newly created files, and then move them to the 
# openvpn config folder. then add the following two lines to the vpn config file:
#     up vpnup
#     down vpndown
# you might also need 'redirect-gateway' in the config file, if you don't use vpn 
# as the default gateway.

import re
import urllib

VPNUPBASE="""#!/bin/sh
export PATH="/bin:/sbin:/usr/sbin:/usr/bin"

OLDGW=`ip route show | grep '^default' | sed -e 's/default via \\([^ ]*\\).*/\\1/'`

if [ $OLDGW == '' ]; then
    exit 0
fi

if [ ! -e /tmp/openvpn_oldgw ]; then
    echo $OLDGW > /tmp/openvpn_oldgw
fi

"""

VPNDOWNBASE="""#!/bin/sh
export PATH="/bin:/sbin:/usr/sbin:/usr/bin"

OLDGW=`cat /tmp/openvpn_oldgw`

"""

url=r'http://ftp.apnic.net/apnic/dbase/data/country-ipv4.lst'

handler=urllib.urlopen(url)

upfile=open('vpnup','w')
downfile=open('vpndown','w')

upfile.write(VPNUPBASE)
upfile.write('\n')

downfile.write(VPNDOWNBASE)
downfile.write('\n')

for line in handler.readlines():
    if line.find(': cn ') < 0: continue
    r=line.split(':')[1]
    r=r.strip()
    ip,mask=r.split('/')
    ip=ip.split('.')
    while len(ip) < 4:
        ip.append('0')
    
    mask=int(mask)
    
    bm='1'*mask+'0'*(32-mask)
    mask="%d.%d.%d.%d"%(int(bm[0:8],2),int(bm[8:16],2),int(bm[16:24],2),int(bm[24:32],2))

    upfile.write('route add -net %s netmask %s gw $OLDGW\n'%('.'.join(ip),mask))
    downfile.write('route del -net %s netmask %s\n'%('.'.join(ip),mask))

downfile.write('rm /tmp/openvpn_oldgw\n')

upfile.close()
downfile.close()