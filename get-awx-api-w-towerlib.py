#!/usr/bin/env python3

import argparse
from getpass import getpass
import requests
import urllib3

from towerlib import Tower
import sys


def example(tower):
    for inventory in tower.inventories:
        print(inventory.name)
    for host in tower.hosts:
        print(host.name)
    for user in tower.users:
        print(user.username)


def main():
    parser = argparse.ArgumentParser(description='Interact with AWX api')
    parser.add_argument('-u', '--username', required=True, type=str,
                        help="AWX user.")
    parser.add_argument('-p', '--password', required=False, type=str,
                        help="AWX user password. Usually don't use this and just use prompt for it")
    parser.add_argument('-H', '--host',nargs='?',
                        default='awx.mktp.io',
                        help='AWX fqdn of host for api https url')
    parser.add_argument('-s', '--ssl-verify', action='store_true', default=False,
                        # dest='ssl_verify',
                        help='Set a switch to true and check ssl verify for https connections.')
    args = parser.parse_args()
    if not args.password:
        args.password = getpass()
    if args.ssl_verify == False:
        urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)

    tower = Tower(args.host, args.username, args.password, secure=True, ssl_verify=args.ssl_verify)


    # Run some example functions
    example(tower)




if __name__ == "__main__":
    main()
