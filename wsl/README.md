## Install dependencies on Windows host:

```bash
choco install -y alacritty
```

Install and configure Debian WSL. 


## Install and configure dependencies in WSL:
```bash
sudo apt-get install -y fzf pass dialog nodejs npm
sudo npm install -g @bitwarden/cli
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
