#!/usr/bin/env python3
import xml.etree.ElementTree as ET, json, sys

tree = ET.parse(sys.argv[1])
root = tree.getroot()
out = {'hosts':[]}

for host in root.findall('host'):
    h={}
    addr = host.find('address')
    if addr is not None: h['ip']=addr.get('addr')
    out['hosts'].append(h)

print(json.dumps(out, indent=2))
