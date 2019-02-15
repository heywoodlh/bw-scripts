#!/usr/bin/env python3
### Script that uses Bitwarden's CLI to check if passwords are more than X days old
import argparse
import sys, os, subprocess
import pathlib
import json
import getpass
import datetime
import pyjq
from datetime import datetime, timedelta



default_session_file = str(pathlib.Path.home()) + '/.bw_session'
default_days = int(90)

parser = argparse.ArgumentParser(description="Tool to maintain password rotation in Bitwarden")

parser.add_argument('--password', help='Bitwarden vault password')
parser.add_argument('--session_file', help='Bitwarden session file', metavar='FILE', default=default_session_file)
parser.add_argument('--days', help='Number of days to alert on', metavar='INT', default=default_days)

args = parser.parse_args()




def check_session_file(session_file):
    if not os.path.isfile(session_file):
        bw_password = getpass.getpass('Enter vault password: ')
        try:
            bw_session = subprocess.check_output('bw unlock ' + bw_password + ' --raw', shell=True)
        except:
            print('Invalid Master Password. Please try again.')
            bw_password = getpass.getpass('Enter vault password: ')
            bw_session = subprocess.check_output('bw unlock ' + bw_password + ' --raw', shell=True)
        bw_session = bw_session.decode('utf-8')
        file = open(session_file, 'w')
        file.write(str(bw_session))
        file.close()



def get_dates(days, using_session_file, session_file):
    if using_session_file == 'True':
        with open(session_file, 'r') as content_file:
            session = content_file.read()
        bw_items = subprocess.check_output('bw list items --session ' + session, shell=True)
        bw_items = json.loads(bw_items)
        bw_ids = pyjq.all('.[].id', bw_items)
        for id in bw_ids:
            name_filter = str(".[] | select(.id=="'"' + str(id) + '"'") | .name")
            date_filter = str(".[] | select(.id=="'"' + str(id) + '"'") | .revisionDate")
            id_json_name = pyjq.all(name_filter, bw_items)
            id_json_date = pyjq.all(date_filter, bw_items)
            id_json_name = ''.join(id_json_name)
            id_json_date = ''.join(id_json_date)
            id_json_date = id_json_date.split('T', 1)[0]
            id_json_datetime = datetime.strptime(str(id_json_date), '%Y-%m-%d')
            time_since_revision = datetime.now() - id_json_datetime
            days = int(time_since_revision.days)
            if days >= 90:
                print('Name: ' + str(id_json_name))
                print('Last Revision: ' + str(id_json_date))
                print('Days Since Last Revision: ' +  str(days))

def main():
    if not args.password:
        check_session_file(args.session_file)
        using_session_file = 'True'
        get_dates(args.days, using_session_file, args.session_file)
    else:
        using_session_file = 'False'
        get_dates(args.days, using_session_file, args.session_file)
        


if __name__ == '__main__':
    main()
