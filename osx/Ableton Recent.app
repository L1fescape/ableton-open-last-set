on run
	set recentFilepath to do shell script "/usr/local/bin/python /path/to/get_recent_set.py 2>&1"
	if recentFilepath is not equal to "" then
		do shell script "open \"" & recentFilepath & "\""
		tell application "Ableton Live 11 Suite" to activate
	else
		display dialog "Python script could not find a recent file"
	end if
end run
