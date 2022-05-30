#!/bin/sh

kill -9 $(cat /var/run/notify-me) >/dev/null 2>&1
