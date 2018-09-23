### Script descriptions:

`slab.sh` provides sudo-like-a-boss functionality ([original-repo](https://github.com/ravenac95/sudolikeaboss) -- watch the GIF in the README)

`2fa.sh` provides a graphical front-end to your 2FA TOTP keys stored in Bitwarden


### MacOS Installation:

Install the dependencies:

bw: `brew install bitwarden-cli choose jq`


Download bw-scripts:

`sudo chown -R "$USER":"$USER" /opt`

`git clone https://github.com/heywoodlh/bw-scripts /opt/bw-scripts`



### Linux Installation:

Install the dependencies (Debian/Ubuntu): 

`sudo snap install bw`:

`sudo apt-get install xclip rofi jq zenity`


Download bw-scripts:

`sudo chown -R "$USER":"$USER" /opt`

`git clone https://github.com/heywoodlh/bw-scripts /opt/bw-scripts`



### Usage:

`slab.sh` will only return items in the vault with a corresponding URI of `sudolikeaboss://`. So any entry you'd like to have returned by `slab` will need to have that URI. Also, `slab.sh` doesn't intelligently work with names so if an entry returns multiple values it will not work. I recommend naming each item in your vault that you'd like to have returned by `slab.sh` a really unique name (I.E. `Google Personal Account -- SLAB`) so that `slab.sh` doesn't return multiple values.

All of these scripts read `~/.bw_session` for it's session ID. Therefore, login this way:

`bw login --raw > ~/.bw_session`


Once logged in, `slab.sh` or `2fa.sh` should be suitable for use. Either create a keyboard shortcut the scripts in `/opt/bw-scripts` or invoke the scripts from the CLI.
