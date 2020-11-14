## Install dependencies on Windows host:

```bash
choco install -y alacritty
```

Install Debian WSL (or figure it out with a different distro). 

## Install and configure dependencies in WSL:

```bash
sudo apt-get install -y fzf jq pass dialog nodejs npm git
sudo npm install -g @bitwarden/cli
```

## Add bwmenu to PATH:

```bash
git clone https://github.com/heywoodlh/bw-scripts /opt/bw-scripts
sudo ln -s /opt/bw-scripts/wsl/bwmenu /usr/local/bin/bwmenu
```

Login to Bitwarden for initial config:

```bash
bw login
```

Requires `pass` to be installed/configured beforehand:

```bash
## Setup a GPG key beforehand with: gpg --full-generate-key
pass init "myemail@example.com"
```

Requires `clip.exe` on Windows host to be in PATH as xclip in WSL: 

```bash
sudo ln -s /mnt/c/Windows/System32/clip.exe /usr/bin/xclip
```

## Recommendations:

I would recommend adding in a scheduled task to clear the clipboard every five minutes.
