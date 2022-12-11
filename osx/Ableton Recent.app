on run
	do shell script "open \"$(/usr/local/bin/python /path/to/get_recent_set.py 2>&1)\""
	tell application "Ableton Live 11 Suite" to activate
end run
