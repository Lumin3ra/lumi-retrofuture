#!/bin/bash

# Wait a few seconds to ensure Hyprland and necessary services are fully ready
# 3 seconds is often a safe bet for background processes.
sleep 3

# Run the command in the background
tail -f /tmp/wobpipe | wob &