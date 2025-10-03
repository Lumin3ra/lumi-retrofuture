#!/bin/bash

# 1. Create the named pipe if it doesn't exist
[ -p /tmp/wobpipe ] || mkfifo /tmp/wobpipe

# 2. Add a delay (essential for race conditions)
sleep 2

# 3. Start the tail/wob process in the background
tail -f /tmp/wobpipe | wob &