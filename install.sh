#!/bin/bash

cwd="$(dirname $0)"

if test $(id -u) -ne 0; then
    >&2 echo "Must be ROOT to install!"
    exit 1
fi

set -x
install -o www-data -g www-data "${cwd}/cgi/n.cgi" /usr/lib/cgi-bin/notify/
install "${cwd}/systemd/notify-me.service" /usr/lib/systemd/system/
systemctl enable notify-me.service
