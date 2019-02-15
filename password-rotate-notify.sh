#!/usr/bin/env bash
### Script for sending email with entries that have passwords that should be rotated

PY_SCRIPT_PATH="./password-rotate.py"
RECIPIENT="myemail@gmail.com"

$PY_SCRIPT_PATH --days 90 --session_file ~/.bw_session > /tmp/password-rotate.txt

echo "Attached is a copy of entries in Bitwarden that should be rotated" | mail -s "Password Rotation Scheme" "$RECIPIENT" -a /tmp/password-rotate.txt 

rm /tmp/password-rotate.txt
