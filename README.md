### MacOS Installation:

bw: `brew install bitwarden-cli`

choose: `brew install choose-gui`

jq: `brew install jq`


`sudo chown -R "$USER":"$USER" /opt`

`mkdir -p /opt/slab`

`curl 'https://gist.githubusercontent.com/heywoodlh/4de84b2b55efc681e78e904132e3774e/raw/ea99a9173bf4bcd213d20971f2da4c92be154494/slab.sh' -o /opt/slab/slab.sh`

`chmod +x /opt/slab/slab.sh`



### Linux Installation:

BW CLI install: 

`sudo snap install bw`

Dependency installation (Debian/Ubuntu):

`sudo apt-get install xclip rofi jq zenity`

`sudo chown -R "$USER":"$USER" /opt`

`mkdir -p /opt/slab`

`curl 'https://gist.githubusercontent.com/heywoodlh/4de84b2b55efc681e78e904132e3774e/raw/ea99a9173bf4bcd213d20971f2da4c92be154494/slab.sh' -o /opt/slab/slab.sh`

`chmod +x /opt/slab/slab.sh`



### Usage:

`slab.sh` will only return items in the vault with a corresponding URI of `sudolikeaboss://`. So any entry you'd like to have returned by `slab` will need to have that URI. Also, `slab.sh` doesn't intelligently work with names so if an entry returns multiple values it will not work. I recommend naming each item in your vault that you'd like to have returned by `slab.sh` a really unique name (I.E. `Google Personal Account -- SLAB`) so that `slab.sh` doesn't return multiple values.

`slab.sh` reads `~/.bw_session` for it's session ID. Therefore, login this way:

`bw login --raw > ~/.bw_session`


Once logged in, `slab.sh` should be suitable for use. Either create a keyboard shortcut to `/opt/slab/slab.sh` or invoke `/opt/slab/slab.sh` from the CLI.