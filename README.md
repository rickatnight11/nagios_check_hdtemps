Nagios check_hdtemps Script
===========================

`check_hdtemps` is a Nagios script, written in Python, for checking hard-drive temperatures in Linux via `smartctl`.  Since `smartctl` requires root to run, this script is intended to be paired with the (included) `hdtemps` bash script, which should be run regularly (perhaps via root cron) and output written to a file that `check_hdtemps` can read.
