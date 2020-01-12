#!/usr/bin/env python3
from systemd import journal
from helpers.rest_provider import RestProvider

class DuckDNS:


    def __init__(self, zone, config):
        self.zone = zone
        self.config = config
        

        '''
        Configure REST Provider with the headers
        '''
        self.rest = RestProvider("https://duckdns.org/update", auth=None, headers=None)



    def worker(self, ip):

        hosts = self.config['hosts'].split(",")
        for host in hosts:

            '''
            Update each host record with the new IP
            '''
            journal.send(f"[ddnsc]: Updating IP address {ip} to DuckDNS record {host}.{self.config.name}")
            self.rest.get(f"/{host}.{self.config.name}/{self.config.get('token')}/{ip}")