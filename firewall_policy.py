#!/usr/bin/python
															
"Project 2 - This creates the firewall policy. "

from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import packets
from pyretic.core import packet


def make_firewall_policy(config):
    # TODO - This is where you need to write the functionality to create the
    # firewall. What is passed in is a list of rules that you must implement.
    
    # feel free to remove the following "print config" line once you no longer need it
    print config # for demonstration purposes only, so you can see the format of the config

    rules = []
    for entry in config:
        # TODO - build the individual rules

        # examples:

        #check for '*' wildcard to avoid crashing the parser.
        if entry['dstport']!='*':
            rule = match(dstport=int(entry['dstport']), ethtype=packet.IPV4, protocol=packet.TCP_PROTO)
        if entry['srcmac']!='*':
            rule = match(srcmac=MAC(entry['srcmac']))
        if entry['srcip']!='*':
            rule = match(srcip=entry['srcip'])
        if entry['dstmac']!='*':
            rule = match(dstmac=MAC(entry['dstmac']))
        if entry['srcport']!='*':
            rule = match(srcport=int(entry['srcport']), ethtype=packet.IPV4, protocol=packet.TCP_PROTO)

        rules.append(rule)
        pass
    
    allowed = ~(union(rules))
    print allowed

    return allowed

