#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from pywarden.pywarden import version, handle_config, gen_config

from pywarden.cli import gen_secret, create_item, get_items, get_list, create_collection
from pywarden.login import login, sync, status
from pywarden.logger import logger

def arg_parse():
    gen_config.gen_config()

    parser = argparse.ArgumentParser(
        description = 'PyWarden {}'.format(version.pywarden_version()),
        usage       = '%(prog)s [options]', 
        prog        = 'pywarden',
        epilog      = 'To report any bugs or issues, please visit: https://github.com/stefanfluit/PyWarden/issues'
    )

    add_entry_parser = parser.add_argument_group('When adding an entry')
    add_entry_parser.add_argument('--name', '-n', required=False, help='name of the entry')
    add_entry_parser.add_argument('--username', '-u', required=False, help='username of the entry')
    add_entry_parser.add_argument('--password', '-p', required=False, help='password of the entry')
    add_entry_parser.add_argument('--url', '-l', required=False, help='url of the entry')
    add_entry_parser.add_argument('--match', '-m', required=False, help='add this parameter if you want to match the url')
    add_entry_parser.add_argument('--notes', '-t', required=False, help='notes of the entry')
    add_entry_parser.add_argument('--totp', '-tt', required=False, help='add this parameter if you want to add a TOTP')
    add_entry_parser.add_argument('--folder', '-f', required=False, help='folder of the entry')
    add_entry_parser.add_argument('--collection', '-c', required=False, help='collection of the entry')
    add_entry_parser.add_argument('--org-collection', '-o', required=False, help='org-collection of the entry')
    add_entry_parser.add_argument('--access-group', '-a', required=False, help='group that should have access to the org-collection')

    validate_object_parser = parser.add_argument_group('When validating an object')
    validate_object_parser.add_argument('--object-type', required=False, help='Type of object. Can be organization, collection, or item')
    validate_object_parser.add_argument('--object-name', required=False, help='Name of the object')

    list_parser = parser.add_argument_group('When listing an object')
    list_parser.add_argument('--list-type', required=False, help='Type of object. Can be organization, collection, or item')
    
    parser.add_argument('--version', action='store_true', help='show version')
    parser.add_argument('--debug', action='store_true', help='enable debug mode')
    parser.add_argument('--status', action='store_true', help='Show status of PyWarden')
    parser.add_argument('--check-config', action='store_true', help='Check configuration validity')
    parser.add_argument('--gen-password', action='store_true', help='Generate a password')
    parser.add_argument('--gen-config', action='store_true', help='Generate a configuration file')
    parser.add_argument('--add-org-entry', action='store_true', help='Add an entry to your vault')
    parser.add_argument('--add-org-collection', action='store_true', help='Add a collection to your vault')
    parser.add_argument('--check-exists', action='store_true', help='Check if an entry exists in your vault')
    parser.add_argument('--list-org-item', action='store_true', help='List an item from your organization')
    parser.add_argument('--list-item', action='store_true', help='List an item from your personal vault')

    args = parser.parse_args()

    if args.status:
        handle_config.manage_configuration(supress=True)
        x = status.get_status()
        logger.pywarden_logger(Payload=x, Color="green", ErrorExit=False, Exit=0)

    elif args.check_config:
        handle_config.manage_configuration(supress=False, show_path=True)

    elif args.gen_password:
        handle_config.manage_configuration(supress=True)
        print(gen_secret.gen_password(handle_config.BITWARDEN_PASSWORD_LENGTH))

    elif args.gen_config:
        gen_config.gen_config()

    elif args.add_org_entry:
        handle_config.manage_configuration(supress=True)
        login.bw_login()
        sync.bw_sync()
        create_item.bw_create_org_item(args.name, args.username, args.password, args.url, args.notes, args.folder, args.collection, args.org_collection, args.access_group, args.debug, args.match, args.totp)

    elif args.add_org_collection:
        handle_config.manage_configuration(supress=True)
        login.bw_login()
        sync.bw_sync()
        create_collection.ensure_org_collection(args.name, args.access_group, args.debug)

    elif args.check_exists:
        handle_config.manage_configuration(supress=True)
        login.bw_login()
        get_items.check_if_object_exists(args.object_type, args.object_name)

    elif args.list_item:
        handle_config.manage_configuration(supress=True)
        login.bw_login()
        get_list.list_all(args.list_type)

    elif args.version:
        print(version.pywarden_version())

    else:
        parser.print_help()
