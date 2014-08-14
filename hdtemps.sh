#!/usr/bin/env bash

# Print datetime
date --rfc-3339='seconds'

# Iterate over drives
for i in /dev/sd[a-z]
do
        # Print drive path and temp
        echo $i `/usr/sbin/smartctl -A $i | grep Temperature_Celsius | awk '{print $10}'`
done