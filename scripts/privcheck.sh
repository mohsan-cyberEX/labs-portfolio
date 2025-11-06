#!/usr/bin/env bash
echo 'Running quick local enum...'
uname -a
id
sudo -l 2>/dev/null || true
echo 'SUID binaries:'
find / -perm -4000 -type f 2>/dev/null | head -n 50
