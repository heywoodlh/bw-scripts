#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


^#s::
Run, "C:\Program Files\Alacritty\Alacritty.exe" -e debian.exe run ~/git/bw-scripts/wsl/slab.sh
return

^#2::
Run, "C:\Program Files\Alacritty\Alacritty.exe" -e debian.exe run ~/git/bw-scripts/wsl/2fa.sh
return

^#u::
Run, "C:\Program Files\Alacritty\Alacritty.exe" -e debian.exe run ~/git/bw-scripts/wsl/unlock.sh
return
