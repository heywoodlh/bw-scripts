#!/usr/bin/env bash

if uname -a | grep -iq 'linux'
then
	OS='Linux'
elif uname -a | grep -iq 'darwin'
then
        OS='Mac'
else
        echo "Unsupported platform. Exiting."
        exit 1
fi


if [[ "$OS" == 'Mac' ]]
then
	VAULT_PW="$(osascript -e 'Tell application "System Events" to display dialog "Enter Bitwarden Vault Password:" with hidden answer default answer ""' -e 'text returned of result' 2>/dev/null)"
elif [[ "$OS" == 'Linux' ]]
then
	echo 'Please enter your password: '
	read -s VAULT_PW
fi

BW_SESSION="$(bw unlock "$VAULT_PW" --raw)"

if [[ "$BW_SESSION" == 'Invalid master password.' ]] && [[ "$OS" == 'Mac' ]]
then
	osascript -e 'tell app "System Events" to display dialog "Invalid master password."'
	exit 1
fi

if [[ "$BW_SESSION" == 'Invalid master password.' ]] && [[ "$OS" == 'Linux' ]]
then
	dialog --infobox 'Invalid master password' 5 30
	exit 1
fi

echo "$BW_SESSION" > ~/.bw_session
