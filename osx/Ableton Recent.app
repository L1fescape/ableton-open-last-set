-- source: https://stackoverflow.com/a/3469708
on FileExists(theFile) -- (String) as Boolean
	tell application "System Events"
		if exists file theFile then
			return true
		else
			return false
		end if
	end tell
end FileExists

on run
	set getRecentSetResult to do shell script "/usr/local/bin/python /path/to/get_recent_set.py 2>&1"
	if FileExists(getRecentSetResult) then
		do shell script "open \"" & getRecentSetResult & "\""
		tell application "Ableton Live 11 Suite" to activate
	else
		display dialog "Could not get a recent file:\n" & getRecentSetResult
	end if
end run